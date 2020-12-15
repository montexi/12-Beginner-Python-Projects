# String concatentaiton (aka How To Put Strings Together)
# Suppose we want to create a string that says "Subscribe to _____"
#----
# youtuber = "UncleslimeXI" # some string variable

# # A Few Ways To Do This
# #-----
# print("Subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("verb: ")
famous_person = input("Famous Person: ")
madlib = f"Computer programming is so {adj} ! It makes me so excited all the time because \n I love to {verb1}. Stay hydrated & {verb2} like you are {famous_person}!"

print(madlib)