# WaaS | NoobMaster + NoobHacker

- Description: Writing as a Service!
- chall.py:/attachments/chall.py


# Write-up

You can write one line in any file (there are some restrictions though). It is using subprocess.run() to read the `fake_flag.txt`. All python modules are stored at a specific place! We can find this by building our own docker and looking into it. The docker currently being used has subprocess at `/usr/local/lib/python3.11/subprocess.py`! We can overwrite this with a simple `run = lambda arg1,capture_output: exec("import os;os.system('sh')")` To call a shell. Note: We need `capture_output` otherwise the function will not be called correctly, since the server provides `capture_output=True` while calling the function. We have our shell!

# Flag: n00bz{0v3rwr1t1ng_py7h0n3_m0dul3s?!!!}
