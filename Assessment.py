# variables
question_db = [
    ["What day is it today?",["Tue","Wed","Thurs"],"Thurs"],
    ["What's my favourite colour?",["Red", "Blue", "Pink"],"Blue"],
    ["What is the first letter of the alphabet?",["B","C","A"],"A"],
    ["What's my favourite animal",["Zebra","Cat","Dolphin"],"Dolphin"]
    ]

quiz_progress = 0 # where we are at in the quiz

# functions
def display_question(quiz_progress):
    '''display_question() displays questions
    @param quiz_progress: int
    @returns: boolean
    #throws: IndexError - out of range
    '''
   
    print(question_db[quiz_progress][0])
    print("A: "+question_db[quiz_progress][1][0])
    print("B: "+question_db[quiz_progress][1][1])
    print("C: "+question_db[quiz_progress][1][2])
    # get answer from user
    check_correct(input(">>> "),quiz_progress)

def check_correct(user_answer,quiz_progress):
    if user_answer.upper() == "A":
        if question_db[quiz_progress][1][0] == question_db[quiz_progress][2]:
            print("Correct")
        else:
            print("Incorrect")
           
    elif user_answer.upper() == "B":
        if question_db[quiz_progress][1][1] == question_db[quiz_progress][2]:
            print("Correct")
        else:
            print("Incorrect")
           
    elif user_answer.upper() == "C":
        if question_db[quiz_progress][1][2] == question_db[quiz_progress][2]:
            print("Correct")
        else:
            print("Incorrect")
           
    else:
        print("That wasn't A, B, or C")


# main routine
while quiz_progress < len(question_db):
    display_question(quiz_progress)
    quiz_progress += 1
   
print("Thanks for playing!")

