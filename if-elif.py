userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? ")
if userReply == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("here are", copies,"copies.")
else:
    print("Thank you, please come again.")