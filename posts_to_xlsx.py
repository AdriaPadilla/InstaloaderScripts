import pandas as pd 
import json
import glob
from datetime import datetime

info = {}
def to_xlsx(file):

	with open(file) as f:
		data = json.load(f)
		try:
			info["post_text"] = data["node"]["edge_media_to_caption"]["edges"][0]["node"]["text"]
		except (IndexError, KeyError):
			info["post_text"] = "null"
		try:
			info["account_name"] = data["node"]["owner"]["edge_felix_video_timeline"]["edges"][0]["node"]["owner"]["username"]
		except KeyError:
			info["account_name"] = "null"
		try:
			info["shortcode"] = data["node"]["shortcode"]
		except KeyError:
			info["shortcode"] = "null"
		try:
			dt = data["node"]["taken_at_timestamp"]
			info["timestamp"] = datetime.fromtimestamp(dt)
		except KeyError:
			info["timestamp"] = "null"
		try:
			info["like_count"] = data["node"]["edge_media_preview_like"]["count"] 
		except KeyError:
			info["like_count"] = "null"
		try:
			info["comment_count"] = data["node"]["edge_media_to_comment"]["count"]
		except KeyError: 
			info["comment_count"] = "null"
		try:
			info["video_view_count"] = data["node"]["video_view_count"]
		except (IndexError, KeyError):
			info["video_view_count"] = "null"
		try:
			info["comments_disabled"] = data["node"]["comments_disabled"]
		except KeyError:
			info["comments_disabled"] = "null"
		return info

post_text_list = []
account_name_list = []
shortcode_list = []
timestamp_list = []
like_count_list = []
comment_count_list = []
video_view_count_list = []
comments_disabled_list = []

json_files = glob.glob("your_path_to_json_files/*.json")

for json_file in json_files:
	to_xlsx(json_file)
	print(json_file)

	post_text_list.append(info["post_text"])
	account_name_list.append(info["account_name"])
	shortcode_list.append(info["shortcode"])
	timestamp_list.append(info["timestamp"])
	like_count_list.append(info["like_count"])
	comment_count_list.append(info["comment_count"])
	video_view_count_list.append(info["video_view_count"])
	comments_disabled_list.append(info["comments_disabled"])

df = pd.DataFrame({
	"text":post_text_list,
	"account":account_name_list,
	"shortcode":shortcode_list,
	"timestamp":timestamp_list,
	"like_count":like_count_list,
	"comment_count":comment_count_list,
	"video_view_count":video_view_count_list,
	"comments_disabled":comments_disabled_list,
	})

df.to_excel("your_output_file.xlsx")

print(df)
