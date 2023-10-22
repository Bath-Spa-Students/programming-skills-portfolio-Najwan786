# You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.

names =["Neymar Jr", "Lionel messi", "Cristiano Ronaldo"]

print("Hello {}, I would like to invite u to a dinner with me.".format(names[0]))
print("Hello {}, I would like to invite u to a dinner with me.".format(names[1]))
print("Hello {}, I would like to invite u to a dinner with me.".format(names[2]))
print(names.remove("Neymar Jr"))
names.append("Dybala")
print("Hello {}, I would like to invite u to a dinner with me.".format(names[0]))
print("Hello {}, I would like to invite u to a dinner with me.".format(names[1]))
print("Hello {}, I would like to invite u to a dinner with me.".format(names[2]))
# Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
print(names.remove("Lionel messi"))
print("Due to some maintenance issue, I can only invite only the two of you")
print("Hello Lionel Messi, I am truly sorry, I had to replace you instead of Cristiano Ronaldo because he is far more better than you.")
# Print a message to each of the two people still on your list, letting them know they’re still invited.
print("Hello {}, I would like you to know that you guys are still invited for a dinner with me.".format(names[0]))
print("Hello {}, I would like you to know that you guys are still invited for a dinner with me.".format(names[1]))

# Deleting the names in the list
del(names[0])
del(names[0])

print(names)
