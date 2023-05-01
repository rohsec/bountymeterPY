import json
import sys
import os
from pathlib import Path
from datetime import datetime
from progress.bar import ShadyBar


#########################################################
#                   Constants                           #
#########################################################
bred='\033[1;31m'
bblue='\033[1;34m'
bgreen='\033[1;32m'
yellow='\033[0;33m'
red='\033[0;31m'
blue='\033[0;34m'
green='\033[0;32m'
reset='\033[0m'
home_path=Path.home()
file_path=os.path.join(home_path,'.bountymeter_py')


#########################################################
#                   Logo Function                      #
#########################################################
def logo():
    print(f"""{bred}    __                      __                       __           
   / /_  ____  __  ______  / /___  ______ ___  ___  / /____  _____
  / __ \/ __ \/ / / / __ \/ __/ / / / __ `__ \/ _ \/ __/ _ \/ ___/
 / /_/ / /_/ / /_/ / / / / /_/ /_/ / / / / / /  __/ /_/  __/ /    
/_.___/\____/\__,_/_/ /_/\__/\__, /_/ /_/ /_/\___/\__/\___/_/     
                            /____/{reset}{green} Developed by : {blue}@hackinsec              """)
    print(f"{yellow}=========== A utility tool for Bug Hunters ==========\n{reset}")


#########################################################
#                   Usage Function                      #
#########################################################
def usage():
    logo()
    print("[*] To initalize bountymeter\n\tbm init bounty_target username\n\n[*] Add new bounty amount to specified month\n\tbm add month_name bounty_amount\n\n[*] Remove specified bounty_amount from specidief month\n\tbm sub month_name bounty_amount\n\tMonths Format : [ January, February, March...]<First letter needs to be Capital>\n\n[*] Display an Interactive Stats Card\n\tbm stats")


#########################################################
#                   Init_check Function                 #
#########################################################
def init_check():
    if(not os.path.exists(file_path)):
        usage()
        exit()

#########################################################
#                   File Opener Function                #
#########################################################
def file_opener():
    with open(f'{file_path}/bm.json', 'r') as f:
        resp=json.load(f)
    return resp

#########################################################
#                   Init Function                       #
#########################################################
def initt(username,target):
    print(f"{blue}[{green} + {blue}]{bblue} Intitalizing...(✓){reset}")
    dump_data='{"target": '+target+', "total": 0, "username": "'+username+'", "progress": 0, "months": [{"name": "January", "value": 0}, {"name": "February", "value": 0}, {"name": "March", "value": 0}, {"name": "April", "value": 0}, {"name": "May", "value": 0}, {"name": "June", "value": 0}, {"name": "July", "value": 0}, {"name": "August", "value": 0}, {"name": "September", "value": 0}, {"name": "October", "value": 0}, {"name": "November", "value": 0}, {"name": "December", "value": 0}]}'
    if(not os.path.exists(file_path)):
        os.mkdir(file_path)
    print(f"\n{blue}[{green} + {blue}]{bblue} Setting up config file...(✓){reset}")
    with open(f'{file_path}/bm.json', 'w') as f:
        f.write(dump_data)
    f.close()
    print(f"\n{blue}[{green} + {blue}]{bblue} BountyMeter set up successfully...(✓){reset}")
        
    
#########################################################
#                   Total Function                      #
#########################################################
def total():
    resp=file_opener()
    print(f"💰{bblue} Total Bounty: {bgreen}${resp['total']}{reset}")

#########################################################
#                   File Update Function                #
#########################################################
def update_file(resp):
    # resp=file_opener()
    resp['progress']=(int(resp['total'])/int(resp['target']))*100
    with open(f'{file_path}/bm.json', 'w') as f2:
        json.dump(resp, f2)
    f2.close()

#########################################################
#                   Highest Bounty Function             #
#########################################################
def high():
    resp=file_opener()
    x=0
    for i in resp['months']:
        if(i['value']>x):
            high_val=i['value']
            high_mon=i['name']
            x=i['value']
    return high_val,high_mon

#########################################################
#                   Current Month Function              #
#########################################################
def this_month():
    currentMonth = datetime.now().strftime('%B')
    resp=file_opener()
    for i in resp['months']:
        if(currentMonth==i['name']):
            this_mon=i['value']
    return this_mon
    # print(currentMonth)

#########################################################
#                   Monthly Function                    #
#########################################################
def monthly(month_val):
    resp=file_opener()
    for i in resp['months']:
        if(month_val==i['name']):
            this_mon=i['value']
            print(f"💰 {bblue}Bounty earned in {yellow}{month_val} : {bgreen}${this_mon}{reset}")

#########################################################
#                   ADD Function                        #
#########################################################
def add(month_inp,b_amnt):
    init_check()
    resp=file_opener()
    resp['total']=0
    for i in resp["months"]:
        if(month_inp == i['name']):
            i['value']=int(i['value'])+int(b_amnt)
        resp['total']=resp['total']+int(i['value'])
    update_file(resp)
    print(f"{blue}[{green} + {blue}]{bblue} Bounty of {red}${b_amnt}{bblue} added to {yellow}{month_inp} {blue}(✓) {reset}")

#########################################################
#                   SUB Function                        #
#########################################################
def sub(month_inp,b_amnt):
    resp=file_opener()
    resp['total']=0
    for i in resp["months"]:
        if(month_inp == i['name']):
            i['value']=int(i['value'])-int(b_amnt)
        # print(resp)s
        resp['total']=resp['total']+int(i['value'])
    update_file(resp)
    print(f"{blue}[{green} + {blue}]{bblue} Bounty of {red}${b_amnt}{bblue} removed from {yellow}{month_inp} {blue}(✓) {reset}")

#########################################################
#                   Stats Card Function                 #
#########################################################
def stats():
    init_check()
    resp=file_opener()
    progress=round(resp['progress'])
    total=f"${resp['total']}"
    target=f"${resp['target']}"
    highest_profit=high()
    this_month_value=this_month()
    username=resp['username']
    print(f"{blue}================= Hola, {red}{username}{reset} 👋 {blue}================={reset}")
    print(f"\n🎯{blue} Target:{green}{target}\t💰{blue} Bounty Earned:{green}{total}\n\n{blue}💵 This Month:{green}${this_month_value}\t💸{blue} Highest Profit:{green}${highest_profit[0]}({highest_profit[1]})\n")
    with ShadyBar(f"{blue}📊 Progress:{green}[{total}/{target}]", max=100) as bar:
        for i in range(progress):
        # Do some work
            bar.next()

#########################################################
#                   Main Function                        #
#########################################################
# def main():
#     if(len(sys.argv)>1):
#         match sys.argv[1]:
#             case "add":
#                 if(len(sys.argv)> 3 and sys.argv[2]!="" and sys.argv[2].isalpha() and sys.argv[3].isnumeric()):
#                     add(sys.argv[2],sys.argv[3])
#                 else:
#                     usage()
#             case "sub":
#                 if(len(sys.argv)> 3 and sys.argv[2]!="" and sys.argv[2].isalpha() and sys.argv[3].isnumeric()):
#                     sub(sys.argv[2],sys.argv[3])
#                 else:
#                     usage() 
#             case "init":
#                 if(len(sys.argv)>3 and sys.argv[2]!="" and sys.argv[2].isalnum() and sys.argv[3].isnumeric()):
#                     initt(sys.argv[2],sys.argv[3])
#                 else:
#                     usage() 
#             case "total":
#                 total()
#             case "monthly":
#                 if(len(sys.argv)> 2 and sys.argv[2]!="" and sys.argv[2].isalpha()):
#                     monthly(sys.argv[2])
#                 else:
#                     usage()
#             case "stats":
#                 stats() 
#             case default:
#                 usage()
#     else:
#         usage()

## The match case is only supported in python version 3.10 and above therefore moving to if else statement for now

def main():
    if(len(sys.argv)> 3 and sys.argv[1]=="add" and sys.argv[2]!="" and sys.argv[2].isalpha() and sys.argv[3].isnumeric()):
        add(sys.argv[2],sys.argv[3])
    elif(len(sys.argv)> 3 and sys.argv[1]=="sub" and sys.argv[2]!="" and sys.argv[2].isalpha() and sys.argv[3].isnumeric()):
        sub(sys.argv[2],sys.argv[3])
    elif(len(sys.argv)>3 and sys.argv[1]=="init" and sys.argv[2]!="" and sys.argv[2].isalnum() and sys.argv[3].isnumeric()):
        initt(sys.argv[2],sys.argv[3])
    elif(len(sys.argv)>1 and sys.argv[1]!="" and sys.argv[1]=="total"):
        total()
    elif(len(sys.argv)> 2 and sys.argv[1]=="monthly" and sys.argv[2]!="" and sys.argv[2].isalpha()):
        monthly(sys.argv[2])
    elif(len(sys.argv)>1 and sys.argv[1]!="" and sys.argv[1]=="stats"):
        stats() 
    else:
        usage()


#########################################################
#                   Script Start                        #
#########################################################
# Not needed as of now as we are moving to pypi
# if __name__ == "__main__":
#     main()