import instaloader
import pandas as pd

def get_profile_posts(username):

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

	for post in profile.get_posts():

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

		print(post.date_utc, post)

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

	df.to_excel(username+".xlsx")

	print(df)

profile_list = ['username_1', 'username_2', 'username_n']

for username in profile_list:
	get_profile_posts(username)
