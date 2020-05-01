# Instaloader Auxiliar Scripts

Hi!

Here you'll find some scripts to make your live easier when working with Instaloader. 

- Json files to Excel
- Json files to SQL 
- Capture posts within a hashtag for certain dates **(not working at 01/05/2020)**
- Profile posts to Excel 

Some of them have been created to process json files, other are made to amplify the capabilities of standard extractions, using Instaloader main class to add new fields to the capture.

## hashtag_post_between_dates.py

- **Type:** From Instagram to .xlsx file.

- **Functionality:** Capture all posts within a certain hashtag between dates.

- ***Important:*** *Instaloader does not work with an API in the same way that other applications do. It works like an scraper. To obtain the publications of an old date period within a hashtag, Instaloader have to query all the publications, starting from the most recent one, and go backwards until you reach the starting point of your capture. In other words, Instaloader needs to check the date of all publications and discard those that do not accomplish the date criteria.* ***This script works very slowly. I am currently working to improve performance and enable its use in masive captures. Not recommended for big captures.***

**Dependences**

```python
from datetime import datetime
from itertools import dropwhile, takewhile
import instaloader
import pandas as pd
```

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
- *Post URL Shortcode*
- *Hashtags in caption*

The output file will be a .xlsx, easy to handle. Each element will be in a column. 

## profile_posts_to_xlsx.py 

- **Type:** From Instagram to .xlsx file.

- **Functionality:** Capture all posts from an account and export direct to a ***.xlsx*** file.

- ***Important: Working on performance improvements to make it faster. Not recomended for more than 1000 posts***

**Dependences:**

```python
import instaloader
import pandas as pd
```
**Make it work**

In line 71, you can place a single username or a list of them, separated by comas:

```pytnon
profile_list = ['username_1', 'username_2', 'username_n']
```

**What will you get**

A ***.xlsx*** file with this columns:

+ *owner_username*
+	*owner_id*
+	*post_date*
+	*post_caption*
+	*tagged_users*: users tagged in photo.
+	*caption_mentions*: users mentioned in caption field.
+	*is_video*: True / False.
+	*video_view_count*: If video = true, you'll get the view count.
+	*video_duration*: if video = true, you'll get the duration in seconds.
+	*likes*: nº of like for each post.
+	*comments*: Comments in each post. 
+	*post_url*
+	*hashtags_caption*: Hashtags in text caption. 

## posts_to_xlsx.py

- **Type:** From .json Files to .xlsx file.

- **Functionality:** This scripts allows you to convert json files from an Instaloader profile extraction to a digestible ***.xlsx*** file.

**Dependences:**

```python
import pandas as pd 
import json
import glob
from datetime import datetime
```

You'll need a profile extraction with --no-compress-json

For example:

```
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
