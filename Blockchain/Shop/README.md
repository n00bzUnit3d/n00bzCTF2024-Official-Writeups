# Shop | NoobMaster

- Description: Welcome to the Shop! Just buy the flag for 1337 ETH! Too bad you only have 9 ETH...

Shop.sol: attachments/Shop.sol



# Write-up
This contract is vulnreable to a re-entracy attack. A re-entrancy attack is when you call a function while already being in the middle of a function. We are going to write another contract and utilize the fallback function. A fallback function is a function that gets called whenever your contract receives plain ETH. We can exploit this because the refund function first transfers us ETH and then marks it as refunded: `bought[item] -= quantity`. We need to write a contract to solve this challenge (it is not possible to do it with a contract since we have to use the fallback function).

Steps to solve:

1) Buy a rubber duck and refund it
2) When you refund it, you recieve ETH
3) Your contract's fallback funtion will be called. Make sure the fallback function calls refund again. This causes the server to be stuck in a loop. We keep one refunding it without it getting marked as refunded. We drain the entire Shop!
4) Buy the real flag!

Exploit contract is at `solve/Exploit.sol` and deployment script is at `solve/Exploit.sol`

Note: Due to timeout issues on the remote (cause you are taking a LOT of ether, only 5 at a time, you will need to split into multiple transactions.)

So, what I did was:
1) Steal 600 ETH
2) Steal 600 ETH
3) Steal 200 ETH
4) Buy the flag

A total of 4 transactions!

# Flag - n00bz{5h0uld_h4v3_sub7r4ct3d_f1r5t}
