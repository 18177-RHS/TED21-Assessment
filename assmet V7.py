#imports
import random



#Varbiles
condition = 0
budget = 300
progress = 0
question_db = [
    ["Should we start capturing Co2?",["Yes   -100B","No    +100B"], [-100, 100], [], [1,1]],
    ["Which renewable energy(s) should we switch to?",["Wind   -50B", "Solar  -100B", "Hydro  -200B"],[-50, -100, -200], [], [1,1,1]],
    ["Nuclear energy?",["Yes     -100B","No"],[-100, 100], [], [1,1,1,1]],
    ["What percent should we still use Fossil fuels?",[""],[-100, 100], [], [1,1,1,1,1]],
    ]

#funtions

#A funtion that displays and asks questions with two answers then asks funtion check to check the answers
def display2(progress, budget):
    print(question_db[progress][0] + "        Budget: %d" %(budget)+"B")
    print("A: "+question_db[progress][1][0])
    print("B: "+question_db[progress][1][1])
    return check(input(">>> "),progress, budget)


#A funtion that displays and asks questions with three answers then asks funtion check to check the answers
def display3(progress, budget):
    print(question_db[progress][0] + "        Budget: %d" %(budget)+"B")
    print("A: "+question_db[progress][1][0])
    print("B: "+question_db[progress][1][1])
    print("C: "+question_db[progress][1][2])
    return check(input(">>> "),progress, budget) 

#A funtion that displays and asks questions with two answers and it has a 20% chance that it will end the game if the answers yes 
def displayChance(progress, budget):
    print(question_db[progress][0] + "        Budget: %d" %(budget)+"B")
    print("" +question_db[progress][1][0])
    chance = random.randint(0, 10)
    if chance < 10:
        print("Boom")
        progress = len(question_db) + 1
        return progress    
    else:
        return check(input(">>> "),progress, budget)   
    
    
#A funtion that displays and asks for a percentage input then uses that to calulate how many point you'll get 
def displayPercent(progress, budget):
    print(question_db[progress][0] + "        Budget: %d" %(budget)+"B")
    print("" +question_db[progress][1][0])    
    user_answer = input(">>> ")




#checks answers and returns budget
def check(user_answer, progress, budget):
    if user_answer.upper() == "A":
        budget += question_db[progress][2][0]
    if user_answer.upper() == "B":
        budget += question_db[progress][2][1]
    if user_answer.upper() == "C":
        budget += question_db[progress][2][2]
    return budget



#checks if all the questions have been displayed and if so it will end the program
while progress < len(question_db):
    if len(question_db[progress][4]) == 2:
        budget = display2(progress, budget)
        progress += 1
    elif len(question_db[progress][4]) == 3:
        budget = display3(progress, budget)
        progress += 1
    elif len(question_db[progress][4]) == 4:
        progress = displayChance(progress, budget)
        progress += 1        
    elif len(question_db[progress][4]) == 5:
        budget = displayPercent(progress, budget)
        progress += 1  


