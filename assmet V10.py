#imports
import random



#Varbiles
co2 = 0
budget = 100
progress = 0
budgethave = 1
question_db = [
    ["Should we start capturing Co2?",["Yes   -100B","No    +100B"], [-100, 100], [5, 0], [1,1]],
    ["Which renewable energy(s) should we switch to?",["Wind   -50B", "Solar  -100B", "Hydro  -200B"],[-50, -100, -200], [2, 4, 6], [1,1,1]],
    ["Nuclear energy?",["Yes     -100B","No"],[-100, 100], [15, 0], [1,1,1,1]],
    ["What percent should we still use Fossil fuels?",["Yes     -100B"],[-400, 400], [0, 5], [1,1,1,1,1]],
    ["Which meat alvertive should we swich to",["Insects     -100B", "Vegan     -50B", "Artificial meat     -120B"],[-100, -50, -120], [0, 5], [1,1,1]]
    ]

continue_game = True

#funtions

#A funtion that displays and asks questions with two answers then asks funtion check to check the answers
def display2(progress, budget, co2, budgethave):
    print(question_db[progress][0] + "        Budget: %d" %(budget)+"B"  + "        Co2: %d" %(co2)+"B")
    print("A: "+question_db[progress][1][0])
    print("B: "+question_db[progress][1][1])
    return check(input(">>> "),progress, budget, co2, budgethave)


#A funtion that displays and asks questions with three answers then asks funtion check to check the answers
def display3(progress, budget, co2, budgethave):
    print(question_db[progress][0] + "        Budget: %d" %(budget)+"B" + "        Co2: %d" %(co2)+"B")
    print("A: "+question_db[progress][1][0])
    print("B: "+question_db[progress][1][1])
    print("C: "+question_db[progress][1][2])
    return check(input(">>> "),progress, budget, co2, budgethave) 

#A funtion that displays and asks questions with two answers and it has a 20% chance that it will end the game if the answers yes 
def displayChance(progress, budget, co2):
    print(question_db[progress][0] + "        Budget: %d" %(budget)+"B" + "        Co2: %d" %(co2)+"B")
    print("A: "+question_db[progress][1][0])
    print("B: "+question_db[progress][1][1])
    return checknuke(input(">>> "),progress, budget, co2, ) 


          
        
    
#A funtion that displays and asks for a percentage input then uses that to calulate how many point you'll get 
def displayPercent(progress, budget, co2):
    print(question_db[progress][0] + "        Budget: %d" %(budget)+"B" + "        Co2: %d" %(co2)+"B")
    print("" +question_db[progress][1][0])    
    return checkpercent(input(">>> "),progress, budget, co2) 




#checks answers and returns budget
def check(user_answer, progress, budget, co2, budgethave):
    if user_answer.upper() == "A":
        if question_db[progress][2][0] < 0:
            if budget + question_db[progress][2][0] < 0:
                print("aaaaa")
                print("No mONEy")
                budgethave = 0 
                print(budgethave)
            else:
                print("More than")   
                budget += question_db[progress][2][0]
                co2 += question_db[progress][3][0]                
        else:
            budget += question_db[progress][2][0]
            co2 += question_db[progress][3][0]
    if user_answer.upper() == "B":
        if question_db[progress][2][1] < 0:
            if budget + question_db[progress][2][1] < 0:
                print("No mONEy")
                budgethave = 0 
            else:
                print("More than")   
                budget += question_db[progress][2][1]
                co2 += question_db[progress][3][1]                
        else:
            budget += question_db[progress][2][1]
            co2 += question_db[progress][3][1]        
    if user_answer.upper() == "C":
        if question_db[progress][2][2] < 0:
            if budget + question_db[progress][2][2] < 0:
                print("No mONEy")
                budgethave = 0 
            else:
                print("More than")   
                budget += question_db[progress][2][2]
                co2 += question_db[progress][3][2]                
        else:
            budget += question_db[progress][2][2]
            co2 += question_db[progress][3][2]
    print(budgethave)        
    return budget, co2, progress, budgethave



def checknuke(user_answer, progress, budget, co2):
    if user_answer.upper() == "A":
        budget += question_db[progress][2][0]
        chance = 2
        if chance == 2:
            print("Boom")
            progress = len(question_db) + 1
        else:        
            progress = progress
        
    if user_answer.upper() == "B":
        budget += question_db[progress][2][1]
        
    return progress, budget, co2

def checkpercent(user_answer, progress, budget, co2):
        budget += question_db[progress][2][0] * (int(user_answer)/100)
        co2 += question_db[progress][3][0] * (int(user_answer)/100)
        return budget, co2


#main
#checks if all the questions have been displayed and if so it will end the program


while continue_game == True:
    if budgethave == 0:
        print("IF BUDGETHAVE Progress = %d" %(progress))
        budgethave = 1
        while progress < len(question_db):
            print(progress)   
            if len(question_db[progress][4]) == 2:
                progress, budget, co2, budgethave = display2(progress, budget, co2, budgethave)
            elif len(question_db[progress][4]) == 3:
                progress, budget, co2, budgethave = display3(progress, budget, co2, budgethave)
            elif len(question_db[progress][4]) == 4:
                progress, budget, co2 = displayChance(progress, budget, co2)      
            elif len(question_db[progress][4]) == 5:
                budget, co2 = displayPercent(progress, budget, co2)  

    
    
    
    
    if budgethave == 1:   
        while progress < len(question_db):
            print(progress)
            print(len(question_db[progress][4]))
            if len(question_db[progress][4]) == 2:
                progress, budget, co2, budgethave = display2(progress, budget, co2, budgethave)
                progress += 1
            elif len(question_db[progress][4]) == 3:
                progress, budget, co2, budgethave = display3(progress, budget, co2, budgethave)
                progress += 1
            elif len(question_db[progress][4]) == 4:
                progress, budget, co2 = displayChance(progress, budget, co2)
                progress += 1        
            elif len(question_db[progress][4]) == 5:
                budget, co2 = displayPercent(progress, budget, co2)
                progress += 1  