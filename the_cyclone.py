height = int(input("height? "))
credits = int(input("credits? "))

if height >= 137 and credits >= 10:
    print("Enjoy the ride ")
elif height < 137:
    print("You are not tall enough to ride.")
elif credits < 10:
    print("You don't have enough credits.")
else:
    print("Invalid data.")