from datetime import datetime
from itertools import dropwhile, takewhile

import instaloader
import pandas as pd

def hashtag_post_between(hashtag):

	L = instaloader.Instaloader( # Main Class info: https://instaloader.github.io/as-module.html#instaloader-main-class
		download_pictures=False,
		download_videos=False, 
		download_video_thumbnails=False,
		compress_json=False, 
		download_geotags=False, 
		post_metadata_txt_pattern=None, 
		max_connection_attempts=0,
		download_comments=False,
		)

	posts = L.get_hashtag_posts(hashtag)

	SINCE = datetime(2019, 12, 19) # Recent Date / format = (yyyy, mm, dd)
	UNTIL = datetime(2019, 9, 1) # Oldest Date /format = (yyyy, mm, dd)
	print("capturing posts from: "+str(SINCE)+" to: "+str(UNTIL))

	owner_username_list = []
	owner_id_list = []
	post_date_list = []
	post_caption_list = []
	tagged_users_list = [] 
	caption_mentions_list = []
	is_video_list = []
	video_view_count_list = []
	video_duration_list = []
	likes_list = []
	comments_list = []
	post_date_list = []
	post_url_list = []
	hashtags_caption_list = []

	for post in takewhile(lambda p: p.date > UNTIL, dropwhile(lambda p: p.date > SINCE, posts)):
	    owner_username_list.append(post.owner_username)
	    owner_id_list.append(post.owner_id)
	    post_date_list.append(post.date_utc)
	    post_caption_list.append(post.caption)
	    tagged_users_list.append(post.tagged_users)
	    caption_mentions_list.append(post.caption_mentions)
	    is_video_list.append(post.is_video)
	    video_view_count_list.append(post.video_view_count)
	    video_duration_list.append(post.video_duration)
	    likes_list.append(post.likes)
	    comments_list.append(post.comments)
	    post_url_list.append(post.shortcode)
	    hashtags_caption_list.append(post.caption_hashtags)

	    for date, name in zip(post_date_list, owner_username_list):
	    	print(date, name)

	df = pd.DataFrame({
		"owner_username": owner_username_list,
		"owner_id": owner_id_list,
		"post_date": post_date_list,
		"likes": likes_list,
		"comments": comments_list,
		"post_caption": post_caption_list,
		"hashtags_caption": hashtags_caption_list,
		"tagged_users": tagged_users_list,
		"caption_mentions": caption_mentions_list,
		"is_video": is_video_list,
		"video_view_count": video_view_count_list,
		"video_duration": video_duration_list,
		"post_shortcode": post_url_list,
		})

	df.to_excel(hashtag+".xlsx")

	print(df)

hashtag_list = ['hastag_1', 'hashtag_2', 'hastahag_n'] # You can use a single hashtag, or iterate the function over a list. Hashtags without "hash" simbol (#)

for hashtag in hashtag_list:
	hashtag_post_between(hashtag)
