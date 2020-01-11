# Instaloader Auxiliar Scripts

Hi!

Here you'll find some scripts to make your live easier when working with Instaloader. 

Some of them have been created to process json files, other are made to amplify the capabilities of standard extractions, using Instaloader main class to add new fields to the capture.

## hashtag-post-between-dates.py

**Allows you to capture all posts in certain hashtag between dates**

***Important: This script works very slowly. I am currently working to improve performance and enable its use in masive captures. Not recommended for captures of more than 1000 posts.***

+ pandas
+ instaloader
+ itertools
+ datetime

**Make it work**

Range of dates: You have to modify lines 22 and 23

```python
SINCE = datetime(2019, 12, 19) # Recent Date / format = (yyyy, mm, dd)
UNTIL = datetime(2019, 9, 1) # Oldest Date / format = (yyyy, mm, dd)
```

Where to place the hashtags to capture: In line 79 you can place the hastags to capture. Use single hashtag or a list, separated by comas. No hashtag simbol is needed.

```python
hashtag_list = ['hastag_1', 'hashtag_2', 'hastahag_n']
```

**¿What will you get?**

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

**This scripts allows you to convert json files from an Instaloader profile extraction to a digestible .xlsx file**

**Requeriments:**
+ pandas
+ json
+ glob
+ datetime

You'll need a profile extraction with --no-compress-json

For example:

```python
instaloader "random_account_name" --no-compress-json --no-pictures --no-videos --max-connection-attempts 0
```

Please, modify the line 55 to point the folder where your json are stored:

```python
json_files = glob.glob("your_path_to_json_files/*.json")

```

In line 81 you can rename your output file:

```python
df.to_excel("your_output_file.xlsx")
```

*¿Do you need more help with instaloader command options?*<br />
*Please, check this:*<br />
*https://instaloader.github.io/cli-options.html*

**¿What will you get?**

A ***.xlsx*** file with:

- *post_text*
- *account_name*
- *shortcode*
- *timestamp*
- *like_count*
- *comment_count*
- *video_view_count (if photo = "null")*
- *comments_disabled (true/false)*
