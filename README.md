## Dropbox Python Backup Script For PostgreSQL

    if '04:' in str(newDate()) and int(datetime.datetime.today().weekday()) == 4:
    # 04 is hour, and weekdays as you choose. - 👋

| Num | En  | Tr |
| -- | ---- | --- |
| 0  | Sun  | Paz |
| 1  | Mon  | Pzt |
| 2  | Tue  | Sal |
| 3  | Wed  | Çar |
| 4  | Thu  | Per |
| 5  | Fri  | Cum |
| 6  | Sat  | Cmt |
  
####logs.txt look like this:

    Backup: 07.01.2022.gz [07.01.2022 04:46]
    Backup: 14.01.2022.gz [14.01.2022 04:46]
    Backup: 21.01.2022.gz [21.01.2022 04:47]
    Backup: 28.01.2022.gz [28.01.2022 04:47]

`$ pm2 start postgresql-backup.py`
