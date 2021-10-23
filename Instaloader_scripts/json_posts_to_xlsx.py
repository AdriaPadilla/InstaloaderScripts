# Basic Libraries
import pandas as pd
import json
import glob
from datetime import datetime

# This is an exemple for pharsing JSON files downloaded with INSTALOADER. 
# You'll need to do a querie similar to:
# Instaloader @username --no-pictures --no-videos --no-metadata --no-compress-json 


global_df = []

def to_xlsx(file):
    info = {}

    with open(file) as f:
        data = json.load(f)
        try:
            info["post_text"] = data["node"]["edge_media_to_caption"]["edges"][0]["node"]["text"]
        except (IndexError, KeyError):
            info["post_text"] = "null"
        try:
            info["account_name"] = data["node"]["owner"]["id"]
        except KeyError:
            info["account_name"] = "null"
        try:
            info["shortcode"] = "https://www.instagram.com/p/"+data["node"]["shortcode"]
        except KeyError:
            info["shortcode"] = 0
        try:
            dt = data["node"]["taken_at_timestamp"]
            info["timestamp"] = datetime.fromtimestamp(dt)
        except KeyError:
            info["timestamp"] = 0
        try:
            info["like_count"] = data["node"]["edge_media_preview_like"]["count"]
        except KeyError:
            info["like_count"] = 0
        try:
            info["comment_count"] = data["node"]["edge_media_to_comment"]["count"]
        except KeyError:
            info["comment_count"] = 0
        try:
            info["video_view_count"] = data["node"]["video_view_count"]
        except (IndexError, KeyError):
            info["video_view_count"] = 0
        try:
            info["comments_disabled"] = data["node"]["comments_disabled"]
        except KeyError:
            info["comments_disabled"] = "null"

        # AFEGITS

        try:
            info["full_name"] = data["node"]["owner"]["full_name"]
        except KeyError:
            info["full_name"] = "null"
        try:
            info["is_professional_account"] = data["node"]["owner"]["is_professional_account"]
        except KeyError:
            info["is_professional_account"] = "null"
        try:
            info["is_business_account"] = data["node"]["owner"]["is_business_account"]
        except KeyError:
            info["is_business_account"] = "null"
        try:
            info["is_verified"] = data["node"]["owner"]["is_verified"]
        except KeyError:
            info["is_verified"] = "null"
        try:
            info["is_video"] = data["node"]["is_video"]
        except KeyError:
            info["is_video"] = "null"
        try:
            info["category_name"] = data["node"]["owner"]["category_name"]
        except KeyError:
            info["category_name"] = "null"

        return info # returning the dict with all data


json_files = glob.glob("/*.json") # Path To JSON FILES
ammount = len(json_files)  # Count nº of files for progress bar

for json_file in json_files:
    print(json_file)
    info = to_xlsx(json_file)  # This is the main function

    df = pd.DataFrame({
        "post_date": info["timestamp"],
        "account_id": info["account_name"],
        "full_name": info["full_name"],
        "text": info["post_text"],
        "post_shortcode":  info["shortcode"],
        "like_count": info["like_count"],
        "comment_count": info["comment_count"],
        "is_video": info["is_video"],
        "video_view_count": info["video_view_count"],
        "comments_policy": info["comments_disabled"],
        "is_professional": info["is_professional_account"],
        "is_business": info["is_business_account"],
        "is_verified": info["is_verified"],
        "person_category": info["category_name"]
    }, index=[1])
    global_df.append(df)

final = pd.concat(global_df)
final.to_csv("filename.csv", index=False) # Your Filename
print("job done!")
