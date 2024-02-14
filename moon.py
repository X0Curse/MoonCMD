import random
import time
import urllib.request
import urllib.error
import os
import sys
import getpass
import datetime
import socket
import gzip
import ipaddress
import socket
import requests
#from ip2geotools.databases.noncommercial import DbIpCity
#from geopy.distance import distance
import pygame
from googlesearch import search
import platform


# print(platform.system())
# print(platform.release())
print("Checking your OS...")
#print(platform.machine())
if platform.system()!="Windows":
    print("Your system does not use Windows. Exiting...")
    sys.exit()
if platform.system()=="Windows":
    print("Your system use Windows. Continuing...")
    print("Checking your OS version...")
    if platform.release()!="10":# or platform.release()!="11":
        print("Your system does not use Windows 10 or Windows 11.")# Exiting...")
        sys.exit()
    if platform.release()=="10":# or platform.release()=="11":
        print("Your system use Windows 10 or Windows 11. Continuing...")
        print("""\
                            (                                  (                                    
                            )\ )          )    )               )\ )                            )    
                            (()/( (     ( /( ( /(              (()/( (         (     (       ( /(    
                            /(_)))\ )  )\()))\())  (    (      /(_)))(    (   )\   ))\  (   )\())   
                            (_)) (()/( (_))/((_)\   )\   )\ )  (_)) (()\   )\ ((_) /((_) )\ (_))/ _  
                            | _ \ )(_))| |_ | |(_) ((_) _(_/(  | _ \ ((_) ((_)  ! (_))  ((_)| |_ (_) 
                            |  _/| || ||  _|| ' \ / _ \| ' \)) |  _/| '_|/ _ \ | |/ -_)/ _| |  _| _  
                            |_|   \_, | \__||_||_|\___/|_||_|  |_|  |_|  \___/_/ |\___|\__|  \__|(_) 
                                |__/             *                         |__/   *     (          
                                                (  `                        (    (  `    )\ )       
                                                )\))(                       )\   )\))(  (()/(       
                                                ((_)()\   (    (    (      (((_) ((_)()\  /(_))      
                                                (_()((_)  )\   )\   )\ )   )\___ (_()((_)(_))_       
                                                |  \/  | ((_) ((_) _(_/(  ((/ __||  \/  | |   \      
                                                | |\/| |/ _ \/ _ \| ' \))  | (__ | |\/| | | |) |     
                                                |_|  |_|\___/\___/|_||_|    \___||_|  |_| |___/    
              """)
        print("""
                        (                                                                                                                    
                        )\ )                                               )       )                           )                             
                        (()/(          (            (     (  (   (       ( /(    ( /(                        ( /( (            (     (   (    
                        /(_))   (     )\ )   (    ))\    )\))(  )\  (   )\())   )\()) (      (   (    (     )\()))\   (      ))\   ))\  )\   
                        (_))_    )\   (()/(   )\  /((_)  ((_)()\((_) )\ ((_)\   (_))/  )\     )\  )\   )\ ) (_))/((_)  )\ )  /((_) /((_)((_)  
                        |   \  ((_)   )(_)) ((_)(_))(   _(()((_)(_)((_)| |(_)  | |_  ((_)   ((_)((_) _(_/( | |_  (_) _(_/( (_))( (_))  |__ \ 
                        | |) |/ _ \  | || |/ _ \| || |  \ V  V /| |(_-<| ' \   |  _|/ _ \  / _|/ _ \| ' \))|  _| | || ' \))| || |/ -_)   /_/ 
                        |___/ \___/   \_, |\___/ \_,_|   \_/\_/ |_|/__/|_||_|   \__|\___/  \__|\___/|_||_|  \__| |_||_||_|  \_,_|\___|  (_)  
                                    |__/                                                                                                  """)
        print("""
                                                                (               (                     
                                                            __  )\ )        (   )(         (     __   
                                                            / / (()/(        )\ (()\        )\ )  \ \  
                                                            | |   )(_))      ((_) ((_)      _(_/(   | | 
                                                            | |  | || |     / _ \| '_|     | ' \))  | | 
                                                            \_\  \_, |     \___/|_|       |_||_|  /_/  
                                                                |__/                            """)
        i=input("> ")
        if i == "y":
            #current_working_directory=os.path.dirname(os.path.abspath(sys.argv[0])) 
            current_working_directory=os.getcwd()
            #print(current_working_directory)
            code=f"moon@windows.com $ {current_working_directory} >"
            codeinput=input(code)
            while codeinput != "exit":
                if codeinput == "xhelp":
                    print("""\
                                *                                *     (      
                                (  `                        (    (  `    )\ )   
                                )\))(                       )\   )\))(  (()/(   
                                ((_)()\   (    (    (      (((_) ((_)()\  /(_))  
                                (_()((_)  )\   )\   )\ )   )\___ (_()((_)(_))_   
                                |  \/  | ((_) ((_) _(_/(  ((/ __||  \/  | |   \  
                                | |\/| |/ _ \/ _ \| ' \))  | (__ | |\/| | | |) | 
                                |_|  |_|\___/\___/|_||_|    \___||_|  |_| |___/  
                                        """)
                    print("                             Made by user Moon in 2024")
                    print("")
                    print("*Warning: -You can't use the same code twice, if you do, it won't work.")
                    print("          -findip is currently developing, don't use.")
                    print("          -cd command won't work.")
                    print("          -This program is made only for Windows 10 and 11 users.")
                    print("          -This program still have some bugs, use as your own risk.")
                    print("Continue as you want.")
                    print("All Codes:")
                    print("    xhelp                                Print the information.")
                    print("    add                                 Add two numbers.")
                    print("    minus                               Subtract two numbers.")
                    print("    multiply                            Multiply two numbers.")
                    print("    divide                              Divide two numbers.")
                    print("    random                              Print a random number.")
                    print("    getuser                             Print your username.")
                    print("    getinfo                             Get the information of your computer.")
                    print("    pyver                               Print your Python version.")
                    print("    gettime                             Get the current time.")
                    print("    findfile                            Find a file in a directory.")
                    print("    findip                              Find location of an IP address.")
                    print("    xping                                Ping an website.")
                    print("    websearch                           Find location of an IP address.")
                    print("    exit                                Exit the program.")
                    print("AND all of the Windows CMD command.")
                    print("Gmail: nightmoon48658@gmail.com")
                    print("       wlinux.xyz@proton.me")
                    #current_working_directory=os.path.dirname(os.path.abspath(sys.argv[0])) 
                    codeinput=input(code)
                if codeinput == "add":
                    m=input("Input first number: ")
                    n=input("Input second number: ")
                    b=int(m)+int(n)
                    a=print("The anwser is: " + str(b))
                    #current_working_directory=os.path.dirname(os.path.abspath(sys.argv[0]))
                    current_working_directory=os.getcwd() 
                    codeinput=input(code)
                if codeinput == "cd":
                    pathetic=input("Path to change: ")
                    os.chdir(pathetic)
                    #current_working_directory=os.path.dirname(os.path.abspath(sys.argv[0]))
                    current_working_directory=os.getcwd() 
                    codeinput=input(code)
                if codeinput == "minus":
                    m=input("Input first number: ")
                    n=input("Input second number: ")
                    b=int(m)-int(n)
                    a=print("The anwser is: " + str(b))
                    #current_working_directory=os.path.dirname(os.path.abspath(sys.argv[0])) 
                    current_working_directory=os.getcwd() 
                    codeinput=input(code)
                if codeinput == "multiply":
                    m=input("Input first number: ")
                    n=input("Input second number: ")
                    b=int(m)*int(n)
                    a=print("The anwser is: " + str(b))
                    #current_working_directory=os.path.dirname(os.path.abspath(sys.argv[0])) 
                    current_working_directory=os.getcwd() 
                    codeinput=input(code)
                if codeinput == "divide":
                    m=input("Input first number: ")
                    n=input("Input second number: ")
                    b=int(m)/int(n)
                    h=int(b)
                    r=int(m)%int(n)
                    a=print("The anwser is: " + str(h) +", remain: "+str(r))
                    #current_working_directory=os.path.dirname(os.path.abspath(sys.argv[0])) 
                    current_working_directory=os.getcwd() 
                    codeinput=input(code)
                if codeinput == "random":
                    m=input("Please input the minimum number for the program: ")
                    n=input("Please input the maximum number for the program: ")
                    print("Here is the number you want: "+str(random.randint(int(m), int(n))))
                    #current_working_directory=os.path.dirname(os.path.abspath(sys.argv[0])) ()
                    current_working_directory=os.getcwd() 
                    codeinput=input(code)
                if codeinput == "xping":
                    url=input("What website do you want to ping? > ")
                    timetoping=input("What time do you want to ping? > ")
                    first=0
                    error=0
                    while first < int(timetoping):
                        try:
                            conn = urllib.request.urlopen(url)
                        except urllib.error.HTTPError as e:
                        # Email admin / log
                            print(f'HTTPError: {e.code} for {url}')
                            time.sleep(0.5)
                            first=first+1
                            error=error+1
                        except urllib.error.URLError as e:
                        # Email admin / log
                            print(f'URLError: {e.code} for {url}')
                            time.sleep(0.5)
                            first=first+1
                            error=error+1
                        except ValueError as e:
                            print("ValueError: Unknown URL type")
                            time.sleep(0.5)
                            first=first+1
                            error=error+1
                        else:
                        # Website is up
                            print(f'Reply from: {url}')
                            first=first+1
                    print(f'Ping statistics for {url}:')
                    print("    Packets: Sent = "+ timetoping +", Receive = "+str(int(timetoping)-int(error))+", Error = "+str(error))
                    #current_working_directory=os.path.dirname(os.path.abspath(sys.argv[0])) ()
                    current_working_directory=os.getcwd() 
                    codeinput=input(code)
                if codeinput == "getuser":
                    def get_username_os():
                        return os.getenv("USERNAME")
                    username = get_username_os()
                    print(f"Current username: {username}")
                    #current_working_directory=os.path.dirname(os.path.abspath(sys.argv[0])) ()
                    current_working_directory=os.getcwd() 
                    codeinput=input(code)
                if codeinput == "pyver":
                    print("Current version of Python: Python "+sys.version)
                    #current_working_directory=os.path.dirname(os.path.abspath(sys.argv[0])) ()
                    current_working_directory=os.getcwd() 
                    codeinput=input(code)
                if codeinput == "getwinver":
                    print('Platform processor:', platform.processor()) 
                    print('Platform architecture:', platform.architecture()) 
                    print('Machine type:', platform.machine())
                    print("System's network name:", platform.node())
                    print('OS information:', platform.platform()) 
                    print('Operating system:', platform.system())
                    print('System info:', platform.system())
                    print('Python build no. and date:', platform.python_build()) 
                    #current_working_directory=os.path.dirname(os.path.abspath(sys.argv[0])) ()
                    current_working_directory=os.getcwd() 
                    codeinput=input(code)
                if codeinput == "gettime":
                    current_time = datetime.datetime.now()
                    print("Year :", current_time.year)
                    print("Month : ", current_time.month)
                    print("Day : ", current_time.day)
                    print("Hour : ", current_time.hour)
                    print("Minute : ", current_time.minute)
                    print("Second :", current_time.second)
                    print("Microsecond :", current_time.microsecond)
                    #current_working_directory=os.path.dirname(os.path.abspath(sys.argv[0])) ()
                    current_working_directory=os.getcwd() 
                    codeinput=input(code)
                if codeinput == "findfile":
                    name1=input("What is the file name? > ")
                    path=input("Where in the computer do you want to find that file? > ")

        
                    for root, dirs, files in os.walk(path):
                        for name in files:
            
                # As we need to get the provided python file,
                # comparing here like this
                            if name == name1: 
                                print(os.path.abspath(os.path.join(root, name)))
                    #current_working_directory=os.path.dirname(os.path.abspath(sys.argv[0])) ()
                    current_working_directory=os.getcwd() 
                    codeinput=input(code)
                # if codeinput=="findip":
                #     def printDetails(ip):
                #         res = DbIpCity.get(ip, api_key="free")
                #         print(f"IP Address: {res.ip_address}")
                #         print(f"Location: {res.city}, {res.region}, {res.country}")
                #         print(f"Coordinates: (Lat: {res.latitude}, Lng: {res.longitude})")
                #     ip_add = input("Enter IP: ")
                #     printDetails(ip_add)
                #    codeinput=input("moon@windows.com $> ")
                if codeinput=="websearch":
                    query=input("Please insert the query you wanna web search: ")
                    num_results=int(input("Please enter how much web do you want to search: "))
                    for i in search(query, num_results, sleep_interval=2):
                        print("This is "+str(num_results)+ " websites:")
                        print("     "+i)
                    #current_working_directory=os.path.dirname(os.path.abspath(sys.argv[0])) ()
                    current_working_directory=os.getcwd() 
                    codeinput=input(code)
                if codeinput=="/xxx.snake":
                    ask=input("Really?(y or n): ")
                    if ask == "y":
                        pygame.init()
                        
                        white = (255, 255, 255)
                        yellow = (255, 255, 102)
                        black = (0, 0, 0)
                        red = (213, 50, 80)
                        green = (0, 255, 0)
                        blue = (50, 153, 213)
                        
                        dis_width = 1400
                        dis_height = 700
                        
                        dis = pygame.display.set_mode((dis_width, dis_height))
                        pygame.display.set_caption('mooncmd/snake/secret.exe')
                        
                        clock = pygame.time.Clock()
                        
                        snake_block = 10
                        snake_speed = 15
                        
                        font_style = pygame.font.SysFont("bahnschrift", 25)
                        score_font = pygame.font.SysFont("comicsansms", 20)
                        
                        
                        def Your_score(score):
                            value = score_font.render("Your Score: " + str(score), True, yellow)
                            dis.blit(value, [0, 0])
                        
                        
                        
                        def our_snake(snake_block, snake_list):
                            for x in snake_list:
                                pygame.draw.rect(dis, white, [x[0], x[1], snake_block, snake_block])
                        
                        
                        def message(msg, color):
                            mesg = font_style.render(msg, True, color)
                            dis.blit(mesg, [dis_width / 6, dis_height / 3])
                        
                        
                        def gameLoop():
                            game_over = False
                            game_close = False
                        
                            x1 = dis_width / 2
                            y1 = dis_height / 2
                        
                            x1_change = 0
                            y1_change = 0
                        
                            snake_List = []
                            Length_of_snake = 1
                        
                            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                        
                            while not game_over:
                        
                                while game_close == True:
                                    dis.fill(blue)
                                    message("Because that you lose, loser, press P to play again, or you can just press Q to quit.", red)
                                    Your_score(Length_of_snake - 1)
                                    pygame.display.update()
                        
                                    for event in pygame.event.get():
                                        if event.type == pygame.KEYDOWN:
                                            if event.key == pygame.K_q:
                                                game_over = True
                                                game_close = False
                                            if event.key == pygame.K_p:
                                                gameLoop()
                        
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        game_over = True
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_LEFT:
                                            x1_change = -snake_block
                                            y1_change = 0
                                        elif event.key == pygame.K_RIGHT:
                                            x1_change = snake_block
                                            y1_change = 0
                                        elif event.key == pygame.K_UP:
                                            y1_change = -snake_block
                                            x1_change = 0
                                        elif event.key == pygame.K_DOWN:
                                            y1_change = snake_block
                                            x1_change = 0
                        
                                if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                                    game_close = True
                                x1 += x1_change
                                y1 += y1_change
                                dis.fill(blue)
                                pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
                                snake_Head = []
                                snake_Head.append(x1)
                                snake_Head.append(y1)
                                snake_List.append(snake_Head)
                                if len(snake_List) > Length_of_snake:
                                    del snake_List[0]
                        
                                for x in snake_List[:-1]:
                                    if x == snake_Head:
                                        game_close = True
                        
                                our_snake(snake_block, snake_List)
                                Your_score(Length_of_snake - 1)
                        
                                pygame.display.update()
                        
                                if x1 == foodx and y1 == foody:
                                    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                                    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                                    Length_of_snake += 1
                        
                                clock.tick(snake_speed)
                        
                            pygame.quit()
                            quit()          
                        gameLoop()
                        codeinput=input(code)
                    else:
                        print("Oh.")
                        #current_working_directory=os.path.dirname(os.path.abspath(sys.argv[0])) ()
                        current_working_directory=os.getcwd() 
                        codeinput=input(code)

                else:
                    os.system(codeinput)
                    #current_working_directory=os.path.dirname(os.path.abspath(sys.argv[0])) ()
                    current_working_directory=os.getcwd() 
                    codeinput=input(code)
        if i=="n":
            print("Exiting program...")
            time.sleep(0.9)