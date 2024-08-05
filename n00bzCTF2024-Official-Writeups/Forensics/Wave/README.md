# Wave | NoobMaster

- Description: The Wave is not audible, perhaps corrupted? Note: Wrap the flag in n00bz{}. There are no spaces in the flag and it is all lowercase.

  chall.wav: /attachments/chall.wav

  # Write-up

  The WAV file header is corrupted. The first four bytes should be changed to "RIFF". Bytes 9 through 15 should be changed to "WAVEfmt" while bytes 37 through 40 should be changed to "data". Once the WAV has been fixed, decode it from morse-code using a website like [this](https://morsecode.world/international/decoder/audio-decoder-adaptive.html)

  # Flag - n00bz{beepbopmorsecode}
