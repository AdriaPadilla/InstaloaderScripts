# Download posts from any public Instagram account
### dependencies
```bash
Instaloader (for Instagram data collection)
pandas (for dataframe creation)
openpyxl (for xlsx export)
```

### setup

Set the aim accounts in "profile_list" --> main.py (line 7). For example:
```python
profile_list = ["profile_name1", "profile_name2", "etc"]
```

You can configure data output in query.py

The default config will only output the post data in xlsx file.
```python
        download_pictures=False,
        download_videos=False,
        download_video_thumbnails=False,
        compress_json=False,
        download_geotags=False,
        post_metadata_txt_pattern=None,
        max_connection_attempts=0,
        download_comments=False,
```
¿Want to know more about this configuration? visit https://instaloader.github.io/module/instaloader.html

### Run the script:
```
python main.py
```

### **Output**
The script will create a file named "output.xlsx" with all the data. 

#### Citation
*Citation APA Style: Padilla Molina, Adrian (2020). InstaloaderScripts [Software]. Avaliable from: https://github.com/AdriaPadilla/InstaloaderScripts/*
