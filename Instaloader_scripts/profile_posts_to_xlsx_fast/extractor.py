def post_to_dict(post):
    data = {}
    data["owner_username"] = post.owner_username
    data["owner_id"] = post.owner_id
    data["post_date"] = post.date_utc
    data["post_caption"] = post.caption
    data["tagged_users"] = post.tagged_users
    data["caption_mentions"] = post.caption_mentions
    data["is_video"] = post.is_video
    data["video_view_count"] = post.video_view_count
    data["video_duration"] = post.video_duration
    data["likes"] = post.likes
    data["comments"] = post.comments
    data["post_url"] = "https://www.instagram.com/p/"+post.shortcode
    data["hashtags_caption"] = post.caption_hashtags

    return data
