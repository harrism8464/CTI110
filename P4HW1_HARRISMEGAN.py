#CTI-110
#P4HW1-Score List
#Megan Harris
#11-8-23

#this program asks for user scores and shows results

student_scores = []

scores = int(input("How many scores would you like to enter?:"))



for num in range (1, scores+1):
    #user enters their scores
    print("Enter score #", num,":", end=" ")

    score= int(input())

    while score < 0 or score > 100:
        print()
        print("INVALID score entered!!!!")
        print("Score should be between 0 and 100")
        print("Enter score #", num, "again:", end=" ")

        
        score= int(input())

    student_scores.append(score)

print("------------------------Results--------------------")

#determine lowest score,average for scores, display grade

print(f'{"Lowest score:" :<25}  {min(student_scores)}')

print(f'{"Modified List:" :25} {student_scores}')

print(f'{"Scores average:" :<25} {sum(student_scores)/len(student_scores):.2f}')


avg=(sum(student_scores)/len(student_scores))

if avg >= 90:
    grade="A"

elif avg >= 80:
    grade="B"

elif avg >= 70:
    grade="C"

elif avg >= 60:
    grade="D"

elif avg >= 50:
    grade="F"


print(f'{"Grade:" :25} {grade}')

print("------------------------------------------------")
