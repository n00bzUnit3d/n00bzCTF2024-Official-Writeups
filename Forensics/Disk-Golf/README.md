# Disk Golf | NoobMaster
- Description: Let's play some disk golf!
disk.img.tar.gz: https://static.n00bzunit3d.xyz/Forensics/Disk-Golf/disk.img.tar.gz

# Write-up

We are provided with a disk dump. First step is to unzip all of it. Afterwards, use the sleuthkit to analyze. Running `fls disk.img` (fls is short for file list) lists all the files. We can see their is a root directory and home directory. Looking at the home directory `fls disk.img 1723` (the 1723 is unique identifier for the directory) shows the directory `johnhackerdoe`, who is a user and this is his home directory. We can read the `flag.txt` through icat: `icat disk.img 262249` (the number is the unique identifier). The file has octal encoded flag, decode it to get the flag!

# Flag - n00bz{7h3_l0ng_4w41t3d_d15k_f0r3ns1c5}
