import random,re

def luck(L,p="",w=""):
    luck_st=f"\n******GOOD LUCK******\n"

    if w=="lotto":

        print(luck_st)
        for index,i in enumerate(range(int(L))):
            a=" ".join(sorted(str(i).zfill(2) for i in random.sample(range(1,41),6)))
            if p=="yes":
                print(f"{a} \t   {str(random.randint(1,10)).zfill(2)}")
            else:
                print(f"{a}")
        print(luck_st)


    else:
        
        print(luck_st)
        for index,i in enumerate(range(int(L))):
                a=" ".join(str(i).zfill(2) for i in random.sample(range(1,41),4))
                print(a)
        print(luck_st)



def x(which=""):
    
    if which == "":
        
        which=input('do you want lotto or strike ?\n'.upper()).lower()

        if  re.search(r"[strike]*",which).group() != ""  :
            if re.search(r"[strike]*",which).group() == "strike":
                which="strike"
            else:
                ask=input("do you mean strike ? yes or no ?\n".upper()).lower()
                if ask=='yes':
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
        lines=input('How many rows do you wish ?\n'.upper())
        
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
        x()    
  
x()
