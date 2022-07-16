import random,re

def luck(x,p="",w=""):
    luck_st=f"\n******GOOD LUCK******\n"

    if w=="lotto":

        print(luck_st)
        for index,i in enumerate(range(int(x))):
            a=" ".join(sorted(str(i).zfill(2) for i in random.sample(range(1,41),6)))
            if p=="yes":
                print(f"{a} \t   {str(random.randint(1,10)).zfill(2)}")
            else:
                print(f"{a}")
        print(luck_st)


    else:
        
        print(luck_st)
        global sub
        sub=[]
        for index,i in enumerate(range(int(x))):
                a=" ".join(sorted(str(i).zfill(2) for i in random.sample(range(1,41),4)))
                print(a)
                sub.append(a)
        print(luck_st)
        # return sub



def x(which=""):
    
    if which == "":
        
        which=input('do you want lotto or strike ?\n'.upper()).lower()

        if  re.search(r"[strikea]*",which).group() != ""  :
            if re.search(r"[strikea]*",which).group() == "strike":
                which="strike"
            else:
                ask=input("do you mean strike ? yes or no ?\n").lower()
                if ask=="yes":
                    which="strike"
                else:
                    x()


        if  re.search(r"[lto]*",which).group() != ""  :
            if re.search(r"[lto]*",which).group() == "lotto":
                which="lotto"
            else:
                ask_lotto=input("do you mean lotto ? yes or no ? \n".upper()).lower()
                if ask_lotto=="yes":
                    which="lotto"
                else:
                    x()


    if which == "lotto" or which == "strike" :
        lines=input('How many rows do you wish ?\n')
        
        if  lines.isdigit():

            if which=="lotto":
                power=input("Do you wish powerball ? yes or no \n".upper()).lower()
                luck(lines,power,which)

            else:
                luck(lines)

        else:
            print("you must only insert a number\n".upper())
            x(which)    

    else:
        print("you must choose either strike or lotto\n".upper())
        x()    

  
x()

# x="asdsad sadsa ad".split(' ')
# x=",".join(x)     
# print(x)