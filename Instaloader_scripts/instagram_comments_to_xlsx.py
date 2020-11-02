import pandas as pd
import json
import glob
from datetime import datetime

post_date_list = []
id_list = []
created_at_list = []
text_list = []
verified_list = []
username_list = []
likes_count_list = []

def funcion(file):

    post_date = str(file)
    date = post_date.split('.')[0].split("_")[0]
    print(date)

    with open(file) as f:
        comments = json.load(f)

        for comment in comments:
            post_date = date
            id = str(comment["id"])
            timestamp = comment["created_at"]
            created_at = datetime.fromtimestamp(timestamp)  # convert timestamp to date time

            text = comment["text"]
            verified = comment["owner"]["is_verified"]
            username = comment["owner"]["username"]
            likes = comment["likes_count"]

            post_date_list.append(post_date)
            id_list.append(id)
            created_at_list.append(created_at)
            text_list.append(text)
            verified_list.append(verified)
            username_list.append(username)
            likes_count_list.append(likes)

json_files = glob.glob("jsons/*.json")
for file in json_files:
    funcion(file)

print("create DF")

df = pd.DataFrame({
    "post_date": post_date_list,
    "id": id_list,
    "created_at": created_at_list,
    "text": text_list,
    "verified": verified_list,
    "username": username_list,
    "likes": likes_count_list,
    })
df.to_excel("output.xlsx")
