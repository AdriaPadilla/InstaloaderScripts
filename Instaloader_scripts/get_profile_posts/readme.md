# Instagram Profile Posts to ".xlsx" file

# Download posts from any public Instagram account
### dependencies
```bash
Instaloader (for Instagram data collection)
pandas (for dataframe creation)
openpyxl (for xlsx export)
xlrd (to import xlsx files)
```

### setup

Set the aim accounts in "profile_list" --> main.py (line 11). For example:
```python
profile_list = ["profile_name1", "profile_name2", "etc"]
```

### Run the script:
```
python main.py
```

### **Output**
The script will create:
- New directory for each account
- Json file for each post 
- .xlsx file for each account with data
- .xlsx file with all accounts in the same dataset

#### Citation
*Citation APA Style: Padilla Molina, Adrian (2020). InstaloaderScripts [Software]. Avaliable from: https://github.com/AdriaPadilla/InstaloaderScripts/*
