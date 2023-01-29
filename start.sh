cd /sled_schedule
apt update && pip3 install -r requirements.txt
touch /var/log/cron-1.log
touch /var/log/cron-2.log
cat cron | crontab
service cron start & tail -f /var/log/cron-2.log
