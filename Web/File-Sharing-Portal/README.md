# File Sharing Portal | NoobMaster + NoobHacker

- Description: Welcome to the file sharing portal! We only support tar files!
- chall.zip:/attachments/chall.zip

# Write-up

You can upload any tar file and it will untar it for you through python. This is vulnreable to some common attacks (known as zip-slip). You can read any file by making a symlink and tarring it. Uploading that tar, and view file. Example: `ln -s /etc/passwd abc.txt` Will make a symlink. Use python to create the tar file. You can read any file like this! But there's a problem, we don't know where the flag is!

## Cronjob

You can see there is a running cronjob, which deletes files in uploads directory every 5 minutes! You can overwrite that cronjob with your own code, RCE!!!! Make a bash script: 
```bash
#!/bin/bash
ls /app/ > /app/ls.txt
```
Make sure you run `chmod 777` on this file to give it execute permission (otherwise the cronjob won't be run)
Now, create another symlink to read `/app/ls.txt`. This will have information for what file your flag is in. Read flag by creating a symlink the same way!

Steps:
1) Over-write the cronjob using `solve/write.py`
2) Wait one minute for the cronjob to run again (this time it's the modified one)
3) Read `/app/ls.txt` using `solve/create_symlink.py`
4) Read `/app/flag_15b726a24e04cc6413cb15b9d91e548948dac073b85c33f82495b10e9efe2c6e.txt` using `solve/read_flag.py`

# Flag - n00bz{n3v3r_7rus71ng_t4r_4g41n!}