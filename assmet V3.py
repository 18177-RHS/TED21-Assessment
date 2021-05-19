#imports




#Varbiles

budget = 300
progress = 0
question_db = [
    ["Should we start capturing Co2?",["Yes   -100B","No    +100B"], [-100, 100]],
    ["Which renewable energy(s) should we switch to?",["Wind   -50B", "Solar  -100B", "Hydro  -200B"],[-50, -100, -200]],
    ["What percent should we still use Fossil fuels?",[""],[-100, 100]],
    ["Nuclear energy?",["Zebra","Cat","Dolphin"],[-100, 100]]
    ]

#funtions
def display2(progress, budget):
    print(question_db[progress][0] + "        Budget: %d" %(budget)+"B")
    print("A: "+question_db[progress][1][0])
    print("B: "+question_db[progress][1][1])
    return check(input(">>> "),progress, budget)



def display3(progress, budget):
    print(question_db[progress][0] + "        Budget: %d" %(budget)+"B")
    print("A: "+question_db[progress][1][0])
    print("B: "+question_db[progress][1][1])
    print("C: "+question_db[progress][1][2])
    return check(input(">>> "),progress, budget)    

def display1(progress, budget):
    print(question_db[progress][0] + "        Budget: %d" %(budget)+"B")
    print("" +question_db[progress][1][0])
    return budget  

def check(user_answer, progress, budget):
    if user_answer.upper() == "A":
        budget += question_db[progress][2][0]
    if user_answer.upper() == "B":
        budget += question_db[progress][2][1]
    if user_answer.upper() == "C":
        budget += question_db[progress][2][2]
    return budget




while progress < len(question_db):
    if len(question_db[progress][1]) == 2:
        budget = display2(progress, budget)
        progress += 1
    elif len(question_db[progress][1]) == 3:
        budget = display3(progress, budget)
        progress += 1
    elif len(question_db[progress][1]) == 1:
        budget = display1(progress, budget)
        progress += 1        
    