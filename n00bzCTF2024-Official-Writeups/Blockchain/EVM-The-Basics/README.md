# EVM - The Basics | NoobMaster

- Description: I have some EVM runtime bytecode, whatever that means. You need to find the value, in hex, that you need to send to make the contract STOP and not self destruct. Wrap the hex in n00bz{}. If the correct answer is 9999, the flag is `n00bz{0x270f}`

- evm.txt:/attachments/evm.txt

# Write-up

As mentioned in the description, this is the runtime bytecode of an EVM (Ethereum Virtual Machine). You can use websites like https://ethervm.io/ and https://ethereum.org/en/developers/docs/evm/opcodes/ to get the list of OPCODES. Once you reverse the opcodes, the instructions will look like:

```
0x0: 5f: PUSH0: [0x0] <- Top of the stack

0x1: 34: CALLVALUE: [0x0,msg.value] <- Top of the stack

0x2: 61 0x1337: PUSH2 0x1337: [0x0,msg.value,0x1337] <- Top of the stack

0x5: 02: MUL: [0x0,0x1337*msg.value] <- Top of the stack

0x6: 65 0x10b6bc7fc259: PUSH6 0xfdc29ff358a3: [0x0,0x1337*msg.value,0xfdc29ff358a3] <- Top of the stack
 
0xd: 14: EQ: [0x0,0x1337*msg.value==0xfdc29ff358a3] <- Top of the stack

0xe: 60 0x12: PUSH1 0x12: [0x0,0x1337*msg.value=0xfdc29ff358a3,0x12] <- Top of the stack

0x10: 57: JUMPI: Jump to 0x12 if 0x1337*msg.value==0xfdc29ff358a3

0x11: ff: SELF DESTRUCT

0x12: 00: STOP (Need to reach here)

```
I have added comments on how the stack looks and what you need to do. As you can see, in order to get the transaction to NOT self destruct, one needs to make sure that `msg.value*0x1337==0xfdc29ff358a3`. Solve the equation, and the correct msg.value, in hex, is `0xd34db33f5`.

# Flag - n00bz{0xd34db33f5}
