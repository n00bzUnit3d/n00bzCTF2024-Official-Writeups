# The Gang 3 | NoobMaster

- Description: Can you find out where the OG meetup point is? The flag is in the format n00bz{lat,long} with upto 3 decimal places, rounded. Note: Wikipedia can be wrong sometimes ;)

# Write-up

In part 2, you found Twitter with a post. The replies in that post are also by John Doe. He says that in order to join the gang, you need to solve a challenge. That challenge is simple AES-GCM. Decrypting the ciphertext gives a discord invite. Joining the server, you can see chats between the three people. They are planning to meet near a statue near Terminal 2 airport in Bengaluru. They mention things such as "The statue is 110 feet tall" and "The airport is named after the person depicted in the statue". You can see that the airport they are talking about is the `Kempe Gowda international airport`. The person in the status is Kempe Gowda. Doing some Google search + Google Maps magic, you can find the cords!     

# Flag - n00bz{13.199,77.682}
