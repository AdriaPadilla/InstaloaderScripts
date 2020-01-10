# Instaloader Auxiliar Scripts

Hi!

Here you'll find some scripts to make your live easier when working with Instaloader. 

Some of them have been created to process json files, other are made to amplify the capabilities of standard extractions, using Instaloader main class to add new fields to the capture.


# hashtag-post-between-dates.py
<b>Allows you to capture all posts in certain hashtag between dates</b><br />
<b>Requeriments:</b>
+ pandas
+ instaloader
+ itertools
+ datetime

¿What will you get? <br />
<i>
- User name
- User Id
- Post Date
- Post caption
- Tagged users in the photo
- Users mentioned in caption
- Is video (true/fale)
- Video View Count
- Video duration in Seconds
- The nº of likes in each post
- The nº of comments in each post
- Post date
- Post URL Shortcode
- Hashtags in caption
</i>
The output file will be a .xlsx, easy to handle. Each element will be in a column. 

# posts_to_xlsx.py
<b>This scripts allows you to convert json files from an Instaloader profile extraction to a digestible .xlsx file.</b><br />
<b>Requeriments:</b>
+ pandas
+ json
+ glob
+ datetime

You'll need a profile extraction with --no-compress-json
Here's an example:<br />
<b>instaloader "random_account_name" --no-compress-json --no-pictures --no-videos --max-connection-attempts 0</b>

<i>¿Do you need more help with instaloader command options?</i>
Please, check this:<br />
https://instaloader.github.io/cli-options.html

¿What will you get?<br />

A .xlsx file with:
<i>
- post_text
- account_name
- shortcode
- timestamp
- like_count
- comment_count
- video_view_count (if photo = "null")
- comments_disabled (true/false)
</i>

