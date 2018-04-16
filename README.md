# journalctl_time_crwaler
A script to crawl working times from journalctl logs. This only works when you sleep/shutdown your pc after work.

> In my case sometimes sleep not work or maybe i forgot to send to sleep, so i get something like 01:40 - 18:00

----

## Example output

```
[fh@cyf ~]$ python get_work_times.py 2018-04-01
09:10 - 16:32 03.04.2018
08:48 - 17:34 04.04.2018
09:02 - 17:27 05.04.2018
08:48 - 17:55 06.04.2018
09:02 - 18:02 09.04.2018
09:19 - 15:39 10.04.2018
08:59 - 18:57 11.04.2018
08:57 - 15:50 12.04.2018
08:59 - 17:42 13.04.2018
```
