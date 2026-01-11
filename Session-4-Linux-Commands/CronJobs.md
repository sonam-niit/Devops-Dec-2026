# Seeting up a cron JOb

- in terminal
- crontab -e
- it will open nano editor
- comment the first line for cron job which is generating log after every minute.

- * * * * * echo "Hello Job 1" >> /home/sonam/job1.log

- ctrl+o (save) + enter (with given filename) + ctrl+x (exit)

- once its saved your cron job started executing

- you can check -- cat /home/sonam/job1/log after sometime 
- so you can see the logs updated after every minute

- to stop again crontab -e
- comment the line and save

**Writing multiple Jobs**
```bash
# Every Minutes
* * * * * echo "Job 1 Running" >> /home/sonam/job1.log

# Every 5 Minutes
*/5 * * * * echo "Job 2 Running" >> /home/sonam/job2.log

# EveryDay at 5 AM
0 5 * * * /home/sonam/backup.sh

# Every Monday at 2 PM
0 14 * * 1 /home/sonam/report.sh

# run on Alternative Weekdays
0 9 * * 1,3,5 /home/sonam/script.sh

0 */2 * * * /home/sonam/script.sh # run after every 2 hours

```