# Instaloader Auxiliar Scripts

Hi!

Here you'll find some scripts to make your live easier when working with Instaloader. 

Some of them have been created to process json files, other are made to amplify the capabilities of standard extractions, using Instaloader main class to add new fields to the capture.

## hashtag-post-between-dates.py

**Allows you to capture all posts in certain hashtag between dates**

***Requeriments:***
+ pandas
+ instaloader
+ itertools
+ datetime

**Make it work**

You have to modify lines 22 and 23

```python
SINCE = datetime(2019, 12, 19) # Recent Date / format = (yyyy, mm, dd)
UNTIL = datetime(2019, 9, 1) # Oldest Date / format = (yyyy, mm, dd)
```

¿What will you get? 

- *User name*
- *User Id*
- *Post Date*
- *Post caption*
- *Tagged users in the photo*
- *Users mentioned in caption*
- *Is video (true/fale)*
- *Video View Count*
- *Video duration in Seconds*
- *The nº of likes in each post*
- *The nº of comments in each post*
- *Post date*
- *Post URL Shortcode*
- *Hashtags in caption*

The output file will be a .xlsx, easy to handle. Each element will be in a column. 

## posts-to-xlsx.py

**This scripts allows you to convert json files from an Instaloader profile extraction to a digestible .xlsx file.e**

**Requeriments:**
+ pandas
+ json
+ glob
+ datetime

You'll need a profile extraction with --no-compress-json
Here's an example:

```
instaloader "random_account_name" --no-compress-json --no-pictures --no-videos --max-connection-attempts 0
```

*¿Do you need more help with instaloader command options?*<br />
*Please, check this:*<br />
*https://instaloader.github.io/cli-options.html*

¿What will you get?

A **.xlsx** file with:

- *post_text*
- *account_name*
- *shortcode*
- *timestamp*
- *like_count*
- *comment_count*
- *video_view_count (if photo = "null")*
- *comments_disabled (true/false)*
