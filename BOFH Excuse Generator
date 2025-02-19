from tkinter import*
from random import*
from string import*
root=Tk()
subject=["computer","hard drive","terminal","source code","HTCPCP",
         "shell","bash","mouse","keyboard","mainframe","request",
         "power source","digital wallet"]
verb1=["burnt","toasted","flooded","eaten","munged","garbled",
       "enciphered","erased","deleted","recursively copied","redirected"]
verb2=["burnt","toasted","flooded","eaten","munged","garbled",
       "enciphered","erased","deleted","recursively copied","redirected",
       "missing","indecipherable","overheating",
       "being recursively calculated","stuck in an infinite loop"]
actor=["the BOFH","antigravity.py","the recycle/trash bin",
       "blinkenlights","an overflowing bit bucket","the cat",
       "Russia or China","the color scheme","the Spam Vikings"]
reason=["it does not exist on xkcd.",
        "Yoda hit ^C while fending off seagulls with his Stick.",
        "the BDFL is not so benevolent.",
        "some luser pushed a package onto the unladen swallow, which is now laden and can't fly.",
        "it fell into the bit box.",
        "it was written into a write-only file.",
        "it watched the Spam sketch too many times and now can only output 'spam'.",
        "the defecatory material has collided with the mechanical air impeller.",
        "you're trying to run a Mac app on Windows or vice-versa.",
        "you can't read from dev/null!",
        "it's a TEApot, not a COFFEEpot!",
        "it's a Windows undocumented feature.",
        "Russia or China has hacked it."]
excuse=StringVar()
excuse.set("Click Generate!")
toggle=StringVar()
toggle.set("About")
label1=Label(root,bg="White",fg="Black",font="Consolas 20",
             anchor=CENTER,text="BOFH Excuse Generator")
frame1=Frame(root,width=50,height=50)
label2=Label(root,width=50,height=3,textvariable=excuse,
             font="Consolas 16",bg="Black",fg="White",anchor=NW,
             wraplength=600,justify=LEFT)
def generate():
    #choose one of 2 formats using randint
    format=randint(1,2)
    if format==1:
        #choose one element from each relavant list using randint
        s=subject[randint(0,len(subject)-1)]
        v1=verb1[randint(0,len(verb1)-1)]
        a=actor[randint(1,len(actor)-1)]
        text="The {} was {} by {}.".format(s,v1,a)
    elif format==2:
        s=subject[randint(0,len(subject)-1)]
        v2=verb2[randint(0,len(verb2)-1)]
        r=reason[randint(0,len(reason)-1)]
        text="The {} is {} because {}".format(s,v2,r)
    excuse.set(text)
    root.update()
def display():
    excuse.set("© Sophie Wong")
    about["state"]=DISABLED
    gen["state"]=DISABLED
    back["state"]=NORMAL
def hide():
    excuse.set("Click Generate!")
    back["state"]=DISABLED
    about["state"]=NORMAL
    gen["state"]=NORMAL
gen=Button(frame1,text="Generate New",command=generate,state=NORMAL)
about=Button(frame1,text="About",command=display,state=NORMAL)
back=Button(frame1,text="Go Back",command=hide,state=DISABLED)
label1.pack()
label2.pack()
about.grid(row=0,column=0)
back.grid(row=0,column=1)
gen.grid(row=0,column=2)
frame1.pack()

