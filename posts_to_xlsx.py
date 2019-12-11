import pandas as pd 
import json
import glob
from datetime import datetime, timedelta


def timestamp(file):
	with open(file) as f:
		data = json.load(f)
		post_text = data["node"]["edge_media_to_caption"]["edges"][0]["node"]["text"]
		account_name = data["node"]["owner"]["edge_felix_video_timeline"]["edges"][0]["node"]["owner"]["username"]
		business_category = data["node"]["owner"]["business_category_name"]
		shortcode = data["node"]["shortcode"]
		timestamp = data["node"]["taken_at_timestamp"]
		like_count = data["node"]["edge_media_preview_like"]["count"] 
		comment_count = data["node"]["edge_media_to_comment"]["count"] 
		video_view_count = data["node"]["video_view_count"]

		return post_text, account_name, business_category, shortcode, timestamp, like_count, comment_count, video_view_count,

json_files = glob.glob("your_extraction_folder/*/*.json")

post_text_list = []
account_name_list = []
business_category_name_list = []
shortcode_list = []
timestamp_list = []
like_count_list = []
comment_count_list = []
video_view_count_list = []

for json_file in json_files:
	try:
		function, function2, function3, function4, function5, function7, function8, function9 = timestamp(json_file)
		
		post_text_list.append(function)
		account_name_list.append(function2)
		business_category_name_list.append(function3)
		shortcode_list.append(function4)
		timestamp_list.append(function5)
		like_count_list.append(function7)
		comment_count_list.append(function8)
		video_view_count_list.append(function9)
		
		print(json_file)

	except (KeyError, IndexError):
		pass

norm_date_list = []

for unix_date in timestamp_list:
	date = unix_date
	dt = (datetime.fromtimestamp(date) - timedelta(hours=0)).strftime('%Y-%m-%d %H:%M:%S')
	norm_date_list.append(dt)

df = pd.DataFrame({
	"text":post_text_list,
	"account":account_name_list,
	"business_category":business_category_name_list,
	"shortcode":shortcode_list,
	"timestamp":timestamp_list,
	"like_count":like_count_list,
	"comment_count":comment_count_list,
	"video_view_count":video_view_count_list,
	"norm_date":norm_date_list

	})

df.to_excel("your_output_file.xlsx")

print(df)