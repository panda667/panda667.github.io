from tkinter import* #import statements
from tkinter.scrolledtext import*
import sys
from Cipher import* #change below path to where Cipher.py is located
sys.path.append("panda667.github.io/Cryptography.py")
root=Tk() #window setup
c=Canvas(root,width=800,height=600) #basic structure
label_plain=Label(root,text="Plaintext")
label_cipher=Label(root,text="Ciphertext")
label_plain.grid(row=0,column=0,padx=10,pady=10)
label_cipher.grid(row=0,column=2,padx=10,pady=10)
textbox_plain=ScrolledText(root,width=30,height=10,
                           bg="#ddffdd")
textbox_cipher=ScrolledText(root,width=30,height=10,
                            bg="#ddddff")
textbox_plain.grid(row=1,column=0,padx=10,pady=10)
textbox_cipher.grid(row=1,column=2,padx=10,pady=10)
function="123" #sets starting encryption function
def change_123(): #changes button states and encryption function
    global function
    button_123["state"]=DISABLED
    button_rot3["state"]=NORMAL
    button_rot13["state"]=NORMAL
    button_rotn["state"]=NORMAL
    button_map["state"]=NORMAL
    button_rot_more["state"]=NORMAL
    button_vigenere["state"]=NORMAL
    function="123"
def change_rot3():
    global function
    button_123["state"]=NORMAL
    button_rot3["state"]=DISABLED
    button_rot13["state"]=NORMAL
    button_rotn["state"]=NORMAL
    button_map["state"]=NORMAL
    button_rot_more["state"]=NORMAL
    button_vigenere["state"]=NORMAL
    function="rot3"
def change_rot13():
    global function
    button_123["state"]=NORMAL
    button_rot3["state"]=NORMAL
    button_rot13["state"]=DISABLED
    button_rotn["state"]=NORMAL
    button_map["state"]=NORMAL
    button_rot_more["state"]=NORMAL
    button_vigenere["state"]=NORMAL
    function="rot13"
def change_rotn():
    global function
    button_123["state"]=NORMAL
    button_rot3["state"]=NORMAL
    button_rot13["state"]=NORMAL
    button_rotn["state"]=DISABLED
    button_map["state"]=NORMAL
    button_rot_more["state"]=NORMAL
    button_vigenere["state"]=NORMAL
    function="rotn"
def change_map():
    global function
    button_123["state"]=NORMAL
    button_rot3["state"]=NORMAL
    button_rot13["state"]=NORMAL
    button_rotn["state"]=NORMAL
    button_map["state"]=DISABLED
    button_rot_more["state"]=NORMAL
    button_vigenere["state"]=NORMAL
    function="map"
def change_rot_more():
    global function
    button_123["state"]=NORMAL
    button_rot3["state"]=NORMAL
    button_rot13["state"]=NORMAL
    button_rotn["state"]=NORMAL
    button_map["state"]=NORMAL
    button_rot_more["state"]=DISABLED
    button_vigenere["state"]=NORMAL
    function="rot_more"
def change_vigenere():
    global function
    button_123["state"]=NORMAL
    button_rot3["state"]=NORMAL
    button_rot13["state"]=NORMAL
    button_rotn["state"]=NORMAL
    button_map["state"]=NORMAL
    button_rot_more["state"]=NORMAL
    button_vigenere["state"]=DISABLED
    function="vigenere"
def encrypt(): #encryption function
    global function
    plain=textbox_plain.get(1.0,"end-1c")
    if function=="123":
        cipher=Cipher.encrypt123(plain)
    elif function=="rot3":
        cipher=Cipher.encrypt_rot3(plain)
    elif function=="rot13":
        cipher=Cipher.rot13(plain)
    elif function=="rotn":
        cipher=Cipher.encrypt_rotn(plain,10)
    elif function=="map":
        cipher=Cipher.map_cipher(plain,"e")
    elif function=="rot_more":
        cipher=Cipher.rot_more(plain)
    elif function=="vigenere":
        cipher=Cipher.vigenere(plain,"starburst","e")
    textbox_cipher.delete(1.0,"end")
    textbox_cipher.insert(1.0,cipher)
def decrypt(): #decryption function
    global function
    cipher=textbox_cipher.get(1.0,"end-1c")
    if function=="123":
        plain=Cipher.decrypt123(cipher)
    elif function=="rot3":
        plain=Cipher.decrypt_rot3(cipher)
    elif function=="rot13":
        plain=Cipher.rot13(cipher)
    elif function=="rotn":
        plain=Cipher.decrypt_rotn(cipher,10)
    elif function=="map":
        plain=Cipher.map_cipher(cipher,"d")
    elif function=="rot_more":
        plain=Cipher.rot_more(cipher)
    elif function=="vigenere":
        plain=Cipher.vigenere(cipher,"starburst","d")
    textbox_plain.delete(1.0,"end")
    textbox_plain.insert(1.0,plain)
def clear(): #clears both textboxes
    textbox_plain.delete(1.0,"end")
    textbox_cipher.delete(1.0,"end")
frame1=Frame(root) #middle buttons
frame1.grid(row=1,column=1)
button_encrypt=Button(frame1,text="Encrypt >>",command=encrypt)
button_decrypt=Button(frame1,text="<< Decrypt",command=decrypt)
button_clear=Button(frame1,text="Clear",command=clear)
button_encrypt.grid(row=0,column=0,padx=10,pady=10)
button_decrypt.grid(row=1,column=0,padx=10,pady=10)
button_clear.grid(row=2,column=0,padx=10,pady=10)
frame2=Frame(root) #encryption-change buttons
frame2.grid(row=2,column=0)
change_label=Label(frame2,text="Type of Cipher:")
button_123=Button(frame2,text="123",command=change_123,state=DISABLED)
button_rot3=Button(frame2,text="rot3",command=change_rot3,state=NORMAL)
button_rot13=Button(frame2,text="rot13",command=change_rot13,state=NORMAL)
button_rotn=Button(frame2,text="rotn",command=change_rotn,state=NORMAL)
button_map=Button(frame2,text="map",command=change_map,state=NORMAL)
button_rot_more=Button(frame2,text="rot_more",command=change_rot_more,
                       state=NORMAL)
button_vigenere=Button(frame2,text="vigenere",command=change_vigenere,
                       state=NORMAL)
change_label.grid(row=0,column=0)
button_123.grid(row=0,column=1)
button_rot3.grid(row=0,column=2)
button_rot13.grid(row=0,column=3)
button_rotn.grid(row=0,column=4)
button_map.grid(row=0,column=5)
button_rot_more.grid(row=0,column=6)
button_vigenere.grid(row=0,column=7)
