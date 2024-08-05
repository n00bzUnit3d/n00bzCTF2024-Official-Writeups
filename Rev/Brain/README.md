# Brain | NoobMaster

- Description: Help! A hacker said that this "language" has a flag but I can't find it!
- bf.txt: attachments/bf.txt

# Write-up

This is the common Brainf*ck esolang. It operates using "cells". `>` is to move to the next cell while `<` is to move to the previous. `[]` are the start and end of a for loop. The loop stops when the cell being decremented reaches 0. This code writes the ASCII value of each character of the flag in a cell but then it sets it to 0 using `[-]`. A `.` can be used to print the character which corresponds to the current number (ASCII). Adding a `.` before each of the `[-]` will print the corressponding ASCII character of the current cell and then make it 0. This way, you can add the `.` before every occurance of `[-]`. An alternate solution is to remove every occurence of `<[-]`. This moves to the previous cell (where the flag character is written) and makes it 0. Removing this will store the character's ASCII value. You can then use a visualiser to look at the values. Example visualiser: https://ashupk.github.io/Brainfuck/brainfuck-visualizer-master/index.html

# Flag - n00bz{1_c4n_c0d3_1n_br41nf*ck!}
