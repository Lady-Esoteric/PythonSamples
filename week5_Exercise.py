#Benet Morando, December 6th 2014, High Score 2.0
#there needs to be a function called rate_score() that rates a players score
#so if score < 1000 then the function returns, "Nothing to be proud of"
#if score >= 1000 and less than 10000 then return "not bad"
#if score >= 10000 the function should return "nice"
#the function should be called 3 times once for 50, 5000, and 50000
#each message should print
#include a parameter that is of the function rate_score() with a default of 0
# and add call to rate_score()
print(
    """ Welcome to the score counter! """)
def rate_score(score):
    if score < 1000:
        message = "Nothing to be proud of."
    elif score < 10000:
        message = "Not bad."
    elif score >= 10000:
        message = "Nice!"
    return message

score = input("What is your score?")




input("\n\nPress the enter key to exit.")



        
