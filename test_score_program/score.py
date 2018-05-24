#!/usr/bin/env/ python3
print("The Test Score Program")
print()
print("Enter 999 To End Our Program ")
print("==============================")

# my varialbles 
counter = 0
test_score = 0
score_total = 0

while True:
    test_score = int(input("Enter The Test Score: "))
    if test_score >= 0 and test_score <= 100:
        score_total += test_score
        counter += 2
    elif test_score == 999:
        print(" Good Bye Keep In Touch Again")
        break
    else:
        print("The Score Must Be Between 0 To 100")
average = round(score_total / counter)
print("===============================")
print("The Total Score Is:", score_total)
print("The Average Score is:", average)
print()
print("bye")



