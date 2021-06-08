#imports
import random #for my check nuke funtion to see if it ends the game or not



#Varbiles
chance = 2
co2 = 0
budget = 20
progress = 0
#This is a list of my question plus it has improtant info attached to them [0]"The question", [1]"Input options", [2]"Cost", [3]"Co2", [4]"Marker for finding its display funtion"
question_db = [
    ["Should we start capturing Co2?",["Yes   -100B","No    +100B"], [-100, 100], [5, 0], [1,1]],
    ["Which renewable energy(s) should we switch to?",["Wind   -50B", "Solar  -100B", "Hydro  -200B"],[-50, -100, -200], [2, 4, 6], [1,1,1]],
    ["Nuclear energy?",["Yes     -100B","No"],[-100, 100], [15, 0], [1,1,1,1]],
    ["What percent should we still use Fossil fuels?",["Yes     -100B"],[-400, 400], [0, 5], [1,1,1,1,1]],
    ["Which meat alvertive should we swich to",["Insects     -100B", "Vegan     -50B", "Artificial meat     -120B"],[-100, -50, -120], [0, 5], [1,1,1]]
    ] 

#funtions

#A funtion that displays and asks questions with two answers then asks funtion check to check the answers
def display2(progress, budget, co2):
    print(question_db[progress][0] + "        Budget: %d" %(budget)+"B"  + "        Co2: %d" %(co2)+"B")
    print("A: "+question_db[progress][1][0])
    print("B: "+question_db[progress][1][1])
    return check(input(">>> "),progress, budget, co2)


#A funtion that displays and asks questions with three answers then asks funtion check to check the answers
def display3(progress, budget, co2):
    print(question_db[progress][0] + "        Budget: %d" %(budget)+"B" + "        Co2: %d" %(co2)+"B")
    print("A: "+question_db[progress][1][0])
    print("B: "+question_db[progress][1][1])
    print("C: "+question_db[progress][1][2])
    return check(input(">>> "),progress, budget, co2) 

#A funtion that displays and asks questions with two answers and it has a 20% chance that it will end the game if the answers yes 
def displayChance(progress, budget, co2):
    print(question_db[progress][0] + "        Budget: %d" %(budget)+"B" + "        Co2: %d" %(co2)+"B")
    print("A: "+question_db[progress][1][0])
    print("B: "+question_db[progress][1][1])
    return checknuke(input(">>> "),progress, budget, co2) 


          
        
    
#A funtion that displays and asks for a percentage input then uses that to calulate how many point you'll get 
def displayPercent(progress, budget, co2):
    print(question_db[progress][0] + "        Budget: %d" %(budget)+"B" + "        Co2: %d" %(co2)+"B")
    print("" +question_db[progress][1][0])    
    return checkpercent(input(">>> "),progress, budget, co2) 




#checks answers and calutlates budget and co2
def check(user_answer, progress, budget, co2):
    if user_answer.upper() == "A":
        budget += question_db[progress][2][0] 
        co2 += question_db[progress][3][0]
    if user_answer.upper() == "B":
        budget += question_db[progress][2][1]
        co2 += question_db[progress][3][1]
    if user_answer.upper() == "C":
        budget += question_db[progress][2][2]
        co2 += question_db[progress][3][0]
    
    return budget, co2


#If answer yes, it has a 20% chance of you losing the game else just does the same thing as funtion check
def checknuke(user_answer, progress, budget, co2):
    if user_answer.upper() == "A":
        budget += question_db[progress][2][0]
        print(chance)
        if chance == 2:
            print("Boom")
            progress = len(question_db) + 1 #ends the game by adding 1 to the total amount of questions
        else:        
            progress = progress
        
    if user_answer.upper() == "B":
        budget += question_db[progress][2][1]
        
    return progress, budget, co2


#calculates how much bugdet and co2 it needs to add from a percentage value
def checkpercent(user_answer, progress, budget, co2):
        budget += question_db[progress][2][0] * (int(user_answer)/100)
        co2 += question_db[progress][3][0] * (int(user_answer)/100)
        return budget, co2


#main
#checks if all the questions have been displayed and if so it will end the program


print(progress)


#While loop keeps my program running
while progress < len(question_db): #checks if it still has questions to ask
    #finding out what question its on then finds the corrasponding display funtion for that question
    if len(question_db[progress][4]) == 2:
        budget, co2 = display2(progress, budget, co2)
        progress += 1
    elif len(question_db[progress][4]) == 3:
        budget, co2 = display3(progress, budget, co2)
        progress += 1
    elif len(question_db[progress][4]) == 4:
        progress, budget, co2 = displayChance(progress, budget, co2)
        progress += 1        
    elif len(question_db[progress][4]) == 5:
        budget, co2 = displayPercent(progress, budget, co2)
        progress += 1  






#END GAMEE



#if these conditions are true you win the game else you lose
if budget > 0 and co2 > 10:
    print("CONTGRATULATIONS YOUVE WON")
    print("Here are your stats")
    print("Budget: %d"%(budget))
    print("Co2: %d"%(co2))
else:
    print("YOU LOSE LOSER")
    print("Here are your stats")
    print("Budget: %d"%(budget))
    print("Co2: %d"%(co2))    
    
print("""
    
    
    
    
    
    
    
    
    
       
    
""")




