import instaloader
import pandas as pd
import json
import time
import os
import glob
from datetime import datetime

# Global Variables. Please, define usernames (without @)

profile_list = ["username", "username", "username"]
save_path = "output_folder/"
minutes = 300 # Sleep Time between users. 5 minutes recommend.

def get_profile_posts(username, save_path):
    save_path = save_path+username+"/"
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    L = instaloader.Instaloader(
        download_pictures=False,
        download_videos=False,
        download_video_thumbnails=False,
        compress_json=False,
        download_geotags=False,
        post_metadata_txt_pattern=None,
        max_connection_attempts=0,
        download_comments=False,
        )

    profile = instaloader.Profile.from_username(L.context, username)
    posts = profile.get_posts()
    for post in posts:
        post_sleep = 1 # Sleep 1 seconds between posts
        print("sleeping for: " + str(post_sleep) + " seconds")
        time.sleep(post_sleep)

        data = post.__dict__
        data_node = data["_node"]
        captured_on = time.strftime("%Y-%m-%d")
        file_name = captured_on+"_"+post.shortcode
        with open(os.path.join(save_path, file_name+".json"), "w", encoding='utf-8') as write_file:
            json.dump(data_node, write_file, sort_keys=True, indent=4, ensure_ascii=False)
            print(write_file)


def decode_jsons(username, save_path):

    path_to_files = save_path+username+"/"
    json_files = glob.glob(os.path.join(path_to_files, "*.json"))

    list_of_df = []

    for file in json_files:
        with open(file, encoding="utf-8") as f:
            data = json.load(f)

            list_owner_id = []
            list_post_date = []
            list_likes = []
            list_comments = []
            list_caption = []
            list_of_tagged_users = []
            list_hashtags_in_text = []
            list_is_video = []
            list_post_shortcode = []

            user_id = data["owner"]["id"]
            list_owner_id.append(user_id)

            date = datetime.fromtimestamp(data["taken_at_timestamp"])
            list_post_date.append(date)

            is_video = data["is_video"]
            list_is_video.append(is_video)

            try:
                vid_v_count = data["video_view_count"]
            except KeyError:
                vid_v_count = "FALSE"
                pass

            shortcode = "https://www.instagram.com/p/"+data["shortcode"]
            list_post_shortcode.append(shortcode)

            comments = data["edge_media_to_comment"]["count"]
            list_comments.append(comments)

            try:
                tagged_users = data["edge_media_to_tagged_user"]["edges"]
                list_of_tagged = []
                for user in tagged_users:
                    tagged_user = user["node"]["user"]["username"]
                    list_of_tagged.append(tagged_user)
                list_of_tagged_users.append(list_of_tagged)
            except KeyError:
                list_of_tagged_users.append("False")

            try:
                caption = data["edge_media_to_caption"]["edges"][0]["node"]["text"]
                list_caption.append(caption)
            except IndexError:
                list_caption.append("No Caption")


            hashtags_in_text = [word for word in caption.split() if word.startswith("#")]
            list_hashtags_in_text.append(hashtags_in_text)

            likes = data["edge_media_preview_like"]["count"]
            list_likes.append(likes)

            df = pd.DataFrame({
                "username": username,
                "user_id": list_owner_id,
                "post_date": list_post_date,
                "caption": list_caption,
                "likes": list_likes,
                "comments": list_comments,
                "tagged_users": list_of_tagged_users,
                "hashtags": list_hashtags_in_text,
                "is_video": list_is_video,
                "vid_view_count": vid_v_count,
                "shortcode": list_post_shortcode,
            })
            list_of_df.append(df)

    final_frame = pd.concat(list_of_df)
    final_frame.to_excel(username+".xlsx")

def loop():
    for username in profile_list:

        print("Getting Data for: "+username)
        get_profile_posts(username, save_path) # This will collect all Instagram data

        print("Parsing Data for: " + username)
        decode_jsons(username, save_path) # This will convert Json files to dataframe
        print("Finished: " + username)

        actual_time = time.strftime("%H:%M:%S")
        time_sleep = minutes / 60
        print("sleeping for: " + str(time_sleep) + " minutes at " + actual_time)
        time.sleep(minutes)


def controller():

    # First Step:
    # Download posts, extract data, serialize Json and create a .xlsx file for each user
    loop()

    # Second Step:
    # Read all .xlsx file downloaded in previous step, and create a unique file with all data
    path = os.getcwd()
    files = glob.glob(os.path.join(path, "*.xlsx"))

    list_of_frames = []
    for file in files:
        df = pd.read_excel(file)
        list_of_frames.append(df)
    actual_time = time.strftime("%Y-%m-%d")
    df = pd.concat(list_of_frames)
    df.to_excel("your_dataset-"+actual_time+".xlsx")

controller()
