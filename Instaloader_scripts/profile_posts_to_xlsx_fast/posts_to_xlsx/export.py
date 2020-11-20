import pandas as pd

def framer(data):
    print("------> From Dict to Dataframe |  wait!")
    frames_list = []
    for post in data:

        frame = pd.DataFrame({
            "owner_username": post["owner_username"],
            "owner_id": post["owner_id"],
            "post_date": post["post_date"],
            "post_caption": [post["post_caption"]],
            "tagged_users": [post["tagged_users"]],
            "caption_mentions": [post["caption_mentions"]],
            "is_video": post["is_video"],
            "video_view_count": post["video_view_count"],
            "video_duration": post["video_duration"],
            "likes": post["likes"],
            "comments": post["comments"],
            "post_url": post["post_url"],
            "hashtags_caption": [post["hashtags_caption"]],
        })
        frames_list.append(frame)

    final_frame = pd.concat(frames_list, ignore_index=True)
    final_frame.to_excel("output.xlsx")
