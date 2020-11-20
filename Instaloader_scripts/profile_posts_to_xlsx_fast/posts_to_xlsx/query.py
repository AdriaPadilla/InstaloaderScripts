import instaloader

def request(user):
    print("------> Making request for user: "+user+" wait!")
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
    profile = instaloader.Profile.from_username(L.context, user)
    posts = profile.get_posts()
    return posts
