# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
loveCount = name1.lower() + name2.lower()
trueCount = name1.lower() + name2.lower()
loveCompatibility = loveCount.count("l") + loveCount.count("o") + loveCount.count("v") + loveCount.count("e") 
trueCompatibility = trueCount.count("t") + trueCount.count("o") + loveCount.count("v") + loveCount.count("e")
combinedCompatibility = int(str(loveCompatibility) + str(trueCompatibility))
if combinedCompatibility < 10 or combinedCompatibility > 90:
  print("Your score is {}, you go together like coke and mentos.".format(combinedCompatibility))
elif 40 <= combinedCompatibility >= 50:
  print("Your score is {}, you are alright together.".format(combinedCompatibility))
else:
  print("Your score is {}".format(combinedCompatibility))
