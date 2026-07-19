#have each ysws program be either web, software or hardware, and you can increase your skil level through doing projects and other things (books, school, studying), which increases both the speed of completion and quality of apps.
#every week, a new trending topic will show up, and if you cater to it, you get higher levels of popularity.
#points is equal to quality*popularity
#points can be spent on upgrades (esp32 devboards, pinecil, other stem things)
#end score is multiplied by diff to calculate final score
#chores take time, and if not done, you run the risk of getting devices confiscated, making you unable to work on projects
#if you work after bedtime, you  run the risk of getting caught and then getting devices confiscated
#incomplete homework results in afterschool detention, reducing time by 1 hour.
#each ysws lasts 2 seasons.
#
import random
import os
import time
import copy

mochoho=0
choho=0
chores=0
book=0
balance=5
hours=12
sp=5
hard=1
soft=1
web=1
motivation=100
diffmod=0
projects={"Red":{"name":"Red","type":"Software","progress":0.2,"hour":1,"score":0}}
done={}
#format is name, type, progress, program
pgrm=[]
date={"season":1,"week":1,"day":1,"semester":1}
days={1:"Sunday",2:"Monday",3:"Tuesday",4:"Wednesday",5:"Thursday",6:"Friday",7:"Saturday"}
seas={1:"Summer",2:"Autumn",3:"Winter",4:"Spring"}
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def init():
    print("Initiating...")
    time.sleep(1)
    print("Loading functions...")
    time.sleep(1)
    print("Starting application...")
    time.sleep(2)
    main()

def main():
    global diffmod
    cls()
    print("Welcome to YSWSS!")
    print("You Ship We Ship simulator: Inception...")
    time.sleep(1)
    print("Select your difficulty:")
    print("Dropout: No academic responsibility, no chores or curfew, all time can be spent working on projects. [a]")
    input("Press enter to continue...")
    print("F student: Very little academic responsibility, chores are few and far between, curfew set to 11. [b]")
    input("Press enter to continue...")
    print("Average Academic: Medium levels of academic responsibility, chores are occasional, curfew set to 10. [c]")
    input("Press enter to continue...")
    print("A+ student: Chores and homework daily on weekdays, curfew set to 9 PM. [d]")
    input("Press enter to continue...")
    print("Future Doctor: Daily chores and heavy homework load, given a weekly independent study quota, reducing time available for projects. Recommended only for experienced players. [e]")
    diff = input("Select difficulty: ")
    while diff not in ["[a]","[b]","[c]","[d]","[e]"]:
        print("Invalid name!")
        diff = input("Select difficulty: ")
    while diff not in ["[a]","[b]","[c]","[d]","[e]"]:
        if diff=="[a]":
            diffmod=0.5
            print("You have selected: Dropout.")
        elif diff=="[b]":
            diffmod=0.75
            print("You have selected: F student")
        elif diff=="[c]":
            diffmod=1
            print("You have selected: Average academic")
        elif diff=="[d]":
            diffmod=1.5
            print("You have selected: A+ student")
        elif diff=="[e]":
            diffmod=2
            print("You have selected: Future Doctor.")
            time.sleep(1)
            print("Prepare for suffering...")
            time.sleep(1)
    name=input("Please enter name: ")
    input("Game Start!")
    sim()

def sim():
    print("""
      ;   :   ;
   .   \_,!,_/   ,
    `.,'     `.,'
     /         \
~ -- :         : -- ~
     \         /
    ,'`._   _.'`.
   '   / `!` \   `
      ;   :   ;  
""")
    print("""
 ____  _   _ __  __ __  __ _____ ____  
/ ___|| | | |  \/  |  \/  | ____|  _ \ 
\___ \| | | | |\/| | |\/| |  _| | |_) |
 ___) | |_| | |  | | |  | | |___|  _ < 
|____/ \___/|_|  |_|_|  |_|_____|_| \_\ """)
    input("As the school year begins, you wish that the events of the past will be wiped off the board, and you'll be given a blank slate to grow. (Press any key to continue)")
    input("You've recently discovered a new program that allows teens like you to code projects, and be rewarded for it.")
    input("As would be expected, your goal is to, by the end of the year, earn as many points as possible for bragging rights.")
    central()

def central():
    cls()
    print("Week " + str(date["week"]) + ", " + days[date["day"]] + " of " + seas[date["season"]])
    print(f"You have {hours} hours left in the day, and {chores} chores to do by next week.")
    menu=input("What do you do? Check Stats [a], Work on Skills [b], Manage Projects [c], Manage day tasks [d], Skip day [e], End game early [f]")
    if menu=="[a]":
        stats()
    elif menu =="[b]":
        workout()
    elif menu=="[c]":
        proman()
    elif menu=="[d]":
        work()
    elif menu=="[e]":
        advance() 
    elif menu=="[f]":
        gameend() 
    else:
        print("Invalid option!")
        central()         

def stats():
    print(f"Software development: {soft}")
    print(f"Web design: {web}")
    print(f"Hardware design: {hard}")
    input("Press enter to continue...")
    central()

def workout():
    global hours
    global soft
    global web
    global hard
    global book
    print("With your current resources, you can look up resources online (1 hour, minimal levelling) [a], or go to a library and study (3 hours, medium amount of levelling) [b]")    
    study=input("How would you like to work on your skills?")
    if study=="[a]" and hours>=1:
        tree=input("Study what? Software [a], Web design [b], Hardware [c]")
        if tree=="[a]":
            eff=random.random()
            if eff>0.95:
                soft+=10
                print("You read reference manuals and documentation pages, and you learn a whole new branch of software development! +10 in software")
            elif eff>0.8:
                soft+=5
                print("You watch a few independent videos, and now have an almost complete comprehension of what you already know. +5 in Software")
            elif eff>0.7:
                soft+=3
                print("You watch a youtube tutorial to learn new features of your language. +3 in Software")
            elif eff>0.5:
                soft+=1
                print("You read a medium article. +1 in Software")
            elif eff<0.5:
                print("You learned nothing, 2 minutes in, you decided to doomscroll on your phone.")
        if tree=="[b]":
            eff=random.random()
            if eff>0.95:
                web+=10
                print("You read the entirety of the W3 course! +10 in web")
            elif eff>0.8:
                web+=5
                print("You watched a video on the architecture of HTML, and now have a greater understanding of front-end architecture. +5 in Web")
            elif eff>0.7:
                web+=3
                print("You watched a youtube tutorial and followed each step. +3 in Web")
            elif eff>0.5:
                web+=1
                print("You read an article, and covered a gap in your knowledge. +1 in Web")
            elif eff<0.5:
                print("You learned nothing, the words came in through one ear and out the other.")
        if tree=="[c]":
            eff=random.random()
            if eff>0.95:
                hard+=10
                print("You watched an excerpt from the public Harvard design lecture, and learned optimal trace placement! +10 in Hardware")
            elif eff>0.8:
                hard+=5
                print("You followed a tutorial and learned the functions of every component. +5 in Hardware")
            elif eff>0.7:
                hard+=3
                print("You learned how to use design software. +3 in Hardware")
            elif eff>0.5:
                hard+=1
                print("You followed a tutorial and made a blinking led circuit. +1 in Hardware")
            elif eff<0.5:
                print("You couldn't get Kicad to run, and failed to learn anything.")
        hours-=1
    elif study=="[b]" and hours>=3:
        tree=input("Study what? Software [a], Web Design [b], Hardware [c]")
        eff=random.random()  
        if eff>0.9:
            if tree=="[a]":
                soft+=20
                print("You managed to read the entirety of the works written by the leading expert in your field! +20 in Software")
            elif tree=="[b]":
                web+=20
                print(f"You managed to read the entirety of 'The Amateur's Guide to Web Design in 15 easy 500 page tutorials;. +20 in Web Design") 
            elif tree=="[c]":
                hard+=20
                print("You're in luck! The heads of the worlds most succesful tech startups are here to give a talk! You take down as many notes as you can, and learn alot about design. +20 in Hardware")
        elif eff>0.7:
            if tree=="[a]":
                soft+=15
                print("You read through a full, university level textbook. +15 in Software")
            elif tree=="[b]":
                web+=15
                print("You completed Web Design for Dummies. +15 in Web Design")
            elif tree=="[c]":
                hard+=15
                print("You read through 'On Soldering', a PhD thesis on efficient soldering techniques. +15 in Hardware")
        elif eff>0.5:
            if tree=="[a]":
                soft+=13
                print("You read a couple chapters of Enterprise Software Development. +13 in Software")
            elif tree=="[b]":
                web+=13
                print("You read an instructional book about Web Design targeted at beginners, though it's still informative. +13 in Web Design")
            elif tree=="[c]":
                hard+=13
                print("You skim through 'Solder Boy: A rapper's guide to hardware', and learned a thing or two. +13 in Hardware.")
        elif eff>0.3:
            if tree=="[a]":
                soft+=10
                print("You pick up a free brochure on software architecture. +10 Software Development.")
            elif tree=="[b]":
                web+=10
                print("You find an annotated analysis of sample websites submitted for tech company interviews, and improve your sense of style. +10 Web Design")
            elif tree=="[c]":
                hard+=10
                print("You read a book about ergonomic design. +10 Hardware Design")
        elif eff>0.1:
            if tree=="[a]":
                soft+=5
                print("You found a free brochure at the circulation desk about coding. +5 software design.")
            elif tree=="[b]":
                web+=5
                print("You discovered that the library is running an 'Internet for Seniors' workshop, and you learn how to cater to the tech illiterate. +5 Web design")
            elif tree=="[c]":
                hard+=5
                print("You find that a noticeably big print was left unattended, and was in fact, the printed version of a video on soldering. +5 Hardware")
        hours-=3
    else:
       print("Invalid option! Check hours and spelling")

    central()   

def proman():
    global projects
    print("Here are your current projects: ")
    if not projects:
        print("No current Projects.")
    else:
        for x in projects.values():
            print(x["name"])
    proac=input("What would you like to do? View projects [a], Create projects [b], Work on Projects [c]")
    if proac=="[a]":
        viewpro()
    if proac=="[b]":
        procreate()
    if proac=="[c]":
        prowo()
    central()

def viewpro():
    global projects
    print("Current projects: ")
    if not projects:
        print("No current Projects.")
    else:
        for x in projects.values():
            print(x["name"])
        vpro=input("Please enter the name of the project which you would like to view (case sensitive): ")
        if vpro in projects:
            input(f"Project name: {projects[vpro]["name"]}, which is a {projects[vpro]["type"]}-based project, which you spent {projects[vpro]["hour"]} hour/s on. It is currently {projects[vpro]["progress"]*100}% complete. (Press enter to continue)")
        else:
            print("Invalid entry!")
            viewpro()

def procreate():
    global pgrm
    global projects
    selcat=input("Select type of program: Software [a], Web [b], or Hardware [c]")
    if selcat=="[a]":
        curcat="Software"
    if selcat=="[b]":
        curcat="Web"
    if selcat=="[c]":
        curcat="Hardware"
    selname=input("Enter name of project: ")
    projects[f"{selname}"]={"name":f"{selname}","type":f"{curcat}","progress":0,"score":0,"hour":0}
    input(f"Project created. Name: {projects[selname]['name']}, Type: {projects[selname]['type']}")
    central() 

def prowo():
    global projects
    global hours
    global done
    woho=0
    print("Current projects: ")
    if not projects:
        print("No current Projects.")
        central()
    else:
        for x in projects.values():
            print(x["name"])
    selprowo=input("Enter the name of the project which you would like to work on.")
    if selprowo not in projects:
        print("This project does not exist!")
        prowo()
    else:
        print(f"{projects[selprowo]["name"]} is currently {projects[selprowo]["progress"]*100}% complete.")
        selwoho=int(input("Enter number of hours you would like to spend working on this project. "))
        if selwoho>hours:
            print("Not enough time in the day!")
            central()
        else:
            hours-=selwoho
            projects[selprowo]["hour"]+=selwoho
            selwoprog=selwoho*random.uniform(0.1,0.2)
            projects[selprowo]["progress"]+=selwoprog
            while selwoho>woho:
                print("Working...")
                time.sleep(1)
                woho+=1
            if projects[selprowo]["progress"]>=1:
                if selwoprog>1:
                    selwoprog=1
                print(f"You spent {selwoho} hours on {selprowo}. You made {selwoprog*100:.2f}% progress, and the project is now complete.")
                if projects[selprowo]["type"]=="Software":
                    mod=soft/100
                elif projects[selprowo]["type"]=="Hardware":
                    mod=hard/100
                elif projects[selprowo]["type"]=="Web":
                    mod=web/100
                projects[selprowo]["score"]+=projects[selprowo]["hour"]+projects[selprowo]["hour"]*mod
                print("You earnt...")
                time.sleep(1)
                print(".")
                time.sleep(1)
                print(".")
                time.sleep(1)
                input(f"{projects[selprowo]["score"]} points!")
                done[selprowo] = projects[selprowo].copy()
                projects.remove(selprowo)
            else:
                input(f"You spent {selwoho} hours on {selprowo}. You completed {selwoprog*100:.2f}% of the project. It is now {projects[selprowo]["progress"]*100:.2f}% complete.")
        central()

def work():
    global choho
    global hours
    curwochoho=0
    print(f"Currently you have {choho} hours of chores and homework to do.")
    if choho==0:
        print("You have finished all of you required chores and homework for the week.")
        central()
    wochoho=int(input("How long would you like to work on chores and homework today?"))
    if wochoho>hours:
        print("Not enough time in the day!")
        work()
    choho-=wochoho
    while curwochoho<=wochoho:
        print("Working...")
        time.sleep(1)
        curwochoho+=1
    if choho==0:
        print("You have finished all of the chores and homework for this week!")
    else:
        print(f"You worked on your weekly chores and homework for {wochoho} hours. You now have {choho} hours of homework left, due next week.")
    hours-=choho
    central()

def advance():
    global date
    global choho
    global mochoho
    global hours
    date["day"]+=1
    if date["day"]>7:
        date["day"]=1
        date["week"]+=1
        if date["week"]>10:
            date["week"]=1
            date["season"]+=1
            if date["season"]==3:
                date["semester"]+=1
                if date["semester"]>2:
                    gameend()
    print(f"You advanced the day. It is now {seas[date["season"]]}, Week {date["week"]}, {days[date["day"]]}, Semester {date['semester']}.")
    if date["day"]>1 and date["day"]<7:
        hours=10
    else:
        hours=16
    if diffmod==0.5:
        if date["day"]==1:
            if choho>0:
                input(f"You have not completed this week's homework or chores. This year, you have {mochoho} hours of overdue homework. This will be reflected by score deductions at the end of the game.")
            mochoho+=choho
            choho=0
            hours=16            
        if date["day"]==2:
            choho+=1
            print("It is Monday, the only day which you are given homework. You have, in total, 1 hour of homework, due Sunday.")
            hours=9
    if diffmod==0.75:
        if date["day"]==1:
            if choho>0:
                input(f"You have not completed this week's homework or chores. This year, you have {mochoho} hours of overdue homework. This will be reflected by score deductions at the end of the game.")
            mochoho+=choho
            choho=0    
        if date["day"]==3:
            choho+=2
            print("This Tuesday, you have been given one hour of homework and one hour of chores. All homework and chores are due by the end of Sunday.")
        if date["day"]==5:
            choho+=2
            print("This Thursday, you have been given one hour of homework, and one hour of chores. All homework and chores are due at the end of Sunday.")
    if diffmod==1:
        if date["day"]==1:
                if choho>0:
                    input(f"You have not completed this week's homework or chores. This year, you have {mochoho} hours of overdue homework. This will be reflected by score deductions at the end of the game.")
                    mochoho+=choho
                    choho=0
        if date["day"]==2:
            choho+=2
            print("This Monday, you have been given one hour of homework and one hour of chores. All homework and chores are due by the end of Sunday.")
        if date["day"]==4:
            choho+=2
            print("This Wednesday, you have been given one hour of homework and one hour of chores. All homework and chores are due by the end of Sunday.")
        if date["day"]==6:
            choho+=2
            print("This Friday, you have been given one hour of homework and one hour of chores. All homework and chores are due by the end of Sunday.")
    if diffmod==1.5:
        if date["day"]==1:
            if choho>0:
                input(f"You have not completed this week's homework or chores. This year, you have {mochoho} hours of overdue homework. This will be reflected by score deductions at the end of the game.")
        elif date["day"]<7:
            choho+=2
            print(f"Today is {days[date["day"]]}. As usual, you have one hour of homework, and one hour of chores, due next Sunday.")
    if diffmod==2:
        if date["day"]==1:
            if choho>0:
                input(f"You have not completed this week's homework or chores. This year, you have {mochoho} hours of overdue homework. This will be reflected by score deductions at the end of the game.")
                mochoho+=choho
                choho=0
            print("Your destiny as a future doctor means that you have been given a quota of 6 extra hours of studying ahead of schedule.")
            choho+=6
        else:
            choho+=2
    input("Enter to continue...")
    central()        

def gameend():
    global projects
    global done
    global mochoho
    global diffmod
    print("Depending on your options, you've either reached the end of the year, or quit early.")
    input(f"In total, you've made {len(projects)} projects, and spent {sum(project["hour"] for project in projects.values())} hours working on projects.")
    input(f"The projects you made are: ")
    for x in done.values():
        print(f"{x["name"]}, which you spent {x["hour"]} hours on, and earned {x["score"]} points for.")
        time.sleep(0.5)
    input("Press enter to continue")
    input(f"You have missed {mochoho} hours of homework or chores, and spent {sum(project["hours"] for project in done.values())} hours working on projects.")
    input(f"Press enter to reveal the sum of project scores")
    prescore=sum(project["score"] for project in done.values())
    print(prescore)
    input("Enter to continue.")
    print("Subtracting missing hours of chores and homework...")
    time.sleep(1)
    print(f"{prescore}-{mochoho}x10...")
    time.sleep(1)
    subscore=prescore-mochoho*10
    print(subscore)
    print(f"Multiplied by difficulty modifier of {diffmod}...")
    time.sleep(1)
    input("Enter to reveal final score...")
    print(round(subscore*diffmod))
    time.sleep(1)
    input("And that's the game! We hope you enjoyed it!")
init()