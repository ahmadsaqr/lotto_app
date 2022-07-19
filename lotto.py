import random,re
from termcolor import colored


def luck(L,p="",w=""):
    luck_st=colored(f"\n******GOOD LUCK******\n","red")

    if w=="lotto":

        print(luck_st)
        for i in range(int(L)):
            a=" ".join(sorted(str(i).zfill(2) for i in random.sample(range(1,41),6)))
            if p=="yes":
                print(colored(f"{a} \t   {str(random.randint(1,10)).zfill(2)}","cyan"))
            else:
                print(colored(f"{a}","blue"))
        print(luck_st)


    else:
        
        print(luck_st)
        for i in range(int(L)):
                a=" ".join(str(i).zfill(2) for i in random.sample(range(1,41),4))
                print(colored(a,"blue"))
        print(luck_st)



def x(which=""):
    
    if which=="": 
        which=input(colored('do you want lotto or strike ?\n','red').capitalize()).lower()

        if  which != "lotto" and which !="strike"  :
            if re.search(r"[strike]*",which).group() :
                ask=input(colored("do you mean strike ? yes or no ?\n",'red').capitalize()).lower()
                if ask=='yes':
                    which="strike"
                else:
                    x()


            elif re.search(r"[lotto]*",which).group() : 
                ask=input(colored("do you mean lotto ? yes or no ? \n",'red').capitalize()).lower()
                if ask=="yes":
                    which="lotto"
                else:
                    x()
            
            else:
                x()        
        else:
            if which=="lotto":
                which="lotto"                
            
            else:
                which="strike"
                
    else:             
        if which=="lotto":
            which="lotto"                
            
        else:
            which="strike"
    
    lines=input(colored('How many rows do you wish ?\n','red').capitalize())
    
    if  lines.isdigit():
        if which=="lotto":
            power=input(colored("Do you wish powerball ? yes or no \n",'red').capitalize()).lower()
            luck(lines,power,which)
        else:
            luck(lines)
    else:
        print(colored("you must only insert a number\n",'red').capitalize())
        x(which)    

  
x()
