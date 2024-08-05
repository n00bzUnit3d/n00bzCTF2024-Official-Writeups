# Think outside the box | NoobMaster

- Description: You cannot beat my Tic-Tac-Toe bot! If you do, you get a flag!
thinkoutsidethebox.zip:/attachments/thinkoutsidethebox.zip

# Write-up
There is check that your input cannot be greater than 2, but no check for lower bound (meaning you can give negative)! Overwrite the size variable by giving input: `-1,-4`. Can be found through gdb. This will overwrite the size variable, allowing you to give input greater than 2. What to do now? Give input as `-1,3`. This is the same as `0,0` but the bot will not be able to do any move because the if conditions are not satisfied! Do the same: `0,3` is equal to `1,0` and `1,3` is equal to `2,0`. You win!

# Flag - n00bz{l173r4lly_0u7s1d3_7h3_b0x_L0L}
