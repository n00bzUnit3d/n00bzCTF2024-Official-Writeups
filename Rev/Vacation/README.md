# Vacation | 0xBlue

- Description: My friend told me they were going on vacation, but they sent me this weird PowerShell script instead of a postcard!
- output.txt: attachments/output.txt
- Script: attachments/run.ps1

# Write-up

This is an entry-level introduction to XOR - since the key(3) and the output is given, the player can find the input(the flag). If you replace the `flag.txt` part in the first line of the script to `output.txt`, it'll xor the output with the key instead, giving you back the original flag.

# Flag - n00bz{from_paris_wth_xor}