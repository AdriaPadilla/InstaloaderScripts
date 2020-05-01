# Basic Libraries
import pandas as pd 
import json
import glob
from datetime import datetime

# Progress var and sleep functions
from tqdm import tqdm
from time import sleep

# MySQL libraries
import pymysql
import sqlalchemy
from sqlalchemy import create_engine

# Starting connections
engine = create_engine("mysql+pymysql://your_db_username:your_pw@localhost/table_name?charset=utf8mb4")

connection = pymysql.connect(host='localhost',
                             user='your_db_username',
                             password='your_pw',
                             db='table_name',
                             charset="utf8mb4")
                             
# VERY IMPORTANT INFO: Charset, collations or any other encoding in DB must be set to utf8mb4 to support emojis!
# More info: https://mathiasbynens.be/notes/mysql-utf8mb4


# Starting Job

info = {}
def to_xlsx(file):

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
			info["shortcode"] = data["node"]["shortcode"]
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
		return info


json_files = glob.glob("coronavirus/#coronavirusespaña/*.json")

ammount = len(json_files) # Count nº of files for progress bar 
message = "Dumping to DB: "

pbar = tqdm(total=ammount, bar_format='{l_bar}{bar:20}{r_bar}{bar:-20b}', desc=message) # Parameters for tqdm progress bar

for json_file in json_files:
	to_xlsx(json_file) # This is the main function

	post_text_list = []
	account_name_list = []
	shortcode_list = []
	timestamp_list = []
	like_count_list = []
	comment_count_list = []
	video_view_count_list = []
	comments_disabled_list = []


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

	df.to_sql('coronavirus', index=False, con=engine, if_exists='append', chunksize=1000) # This save each loop on the DataBase

	pbar.update() # In each loop, progress bar updates

tqdm._instances.pop().close() # This close all tqdm instances and prevent from re-print

print("job done!")
