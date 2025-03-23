import random
#9492 displays └
#9474 displays │
#9484 displays ┌
#9488 displays ┐
#9472 displays ─
#9496 displays ┘
#9679 displays ●
#32 displays _ (space)
def display_die(n):
    if n==1:
        print(chr(9484)+(7*chr(9472))+chr(9488))
        print(chr(9474)+(7*chr(32))+chr(9474))
        print(chr(9474)+(3*chr(32))+chr(9679)+(3*chr(32))+chr(9474))
        print(chr(9474)+(7*chr(32))+chr(9474))
        print(chr(9492)+(7*chr(9472))+chr(9496))
    if n==2:
        print(chr(9484)+(7*chr(9472))+chr(9488))
        print(chr(9474)+chr(32)+chr(9679)+(5*chr(32))+chr(9474))
        print(chr(9474)+(7*chr(32))+chr(9474))
        print(chr(9474)+(5*chr(32))+chr(9679)+chr(32)+chr(9474))
        print(chr(9492)+(7*chr(9472))+chr(9496))
    if n==3:
        print(chr(9484)+(7*chr(9472))+chr(9488))
        print(chr(9474)+chr(32)+chr(9679)+(5*chr(32))+chr(9474))
        print(chr(9474)+(3*chr(32))+chr(9679)+(3*chr(32))+chr(9474))
        print(chr(9474)+(5*chr(32))+chr(9679)+chr(32)+chr(9474))
        print(chr(9492)+(7*chr(9472))+chr(9496))
    if n==4:
        print(chr(9484)+(7*chr(9472))+chr(9488))
        print(chr(9474)+chr(32)+chr(9679)+(3*chr(32))+chr(9679)+chr(32)+chr(9474))
        print(chr(9474)+(7*chr(32))+chr(9474))
        print(chr(9474)+chr(32)+chr(9679)+(3*chr(32))+chr(9679)+chr(32)+chr(9474))
        print(chr(9492)+(7*chr(9472))+chr(9496))
    if n==5:
        print(chr(9484)+(7*chr(9472))+chr(9488))
        print(chr(9474)+chr(32)+chr(9679)+(3*chr(32))+chr(9679)+chr(32)+chr(9474))
        print(chr(9474)+(3*chr(32))+chr(9679)+(3*chr(32))+chr(9474))
        print(chr(9474)+chr(32)+chr(9679)+(3*chr(32))+chr(9679)+chr(32)+chr(9474))
        print(chr(9492)+(7*chr(9472))+chr(9496))
    if n==6:
        print(chr(9484)+(7*chr(9472))+chr(9488))
        print(chr(9474)+chr(32)+chr(9679)+(3*chr(32))+chr(9679)+chr(32)+chr(9474))
        print(chr(9474)+chr(32)+chr(9679)+(3*chr(32))+chr(9679)+chr(32)+chr(9474))
        print(chr(9474)+chr(32)+chr(9679)+(3*chr(32))+chr(9679)+chr(32)+chr(9474))
        print(chr(9492)+(7*chr(9472))+chr(9496))
def roll_one_die():
    n=random.randint(1,6)
    display_die(n)
def roll_two_die():
    n1=random.randint(1,6)
    n2=random.randint(1,6)
    display_die(n1)
    display_die(n2)
    n=n1+n2
    print(n)
def roll_many(n,display):
    total=0
    i=0
    while(i<n):
        number=random.randint(1,6)
        if display==True:
            display_die(number)
        total=total+number
        i=i+1
    print(total)
num=int(input("How many dice to roll? "))
d=input("Display dice? (True/False) ")
disp=False
if d=="True":
    disp=True
if d=="False":
    disp=False
roll_many(num,disp)
