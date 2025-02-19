from tkinter import*
from tkinter.scrolledtext import*
from Cipher import*
#current cipher is rotn by 7
root=Tk()
c=Canvas(root,width=800,height=600)
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
def encrypt():
    plain=textbox_plain.get(1.0,"end-1c")
    cipher=cipher.encrypt_rotn(plain,7)
    textbox_cipher.delete(1.0,"end")
    textbox_cipher.insert(1.0,cipher)
def decrypt():
    cipher=textbox_cipher.get(1.0,"end-1c")
    plain=cipher.decrypt_rotn(cipher,8)
    textbox_plain.delete(1.0,"end")
    textbox_plain.insert(1.0,plain)
frame1=Frame(root)
frame1.grid(row=1,column=1)
button_encrypt=Button(frame1,text="Encrypt >>",command=encrypt)
button_decrypt=Button(frame1,text="<< Decrypt",command=decrypt)
button_encrypt.grid(row=0,column=0,padx=10,pady=10)
button_decrypt.grid(row=1,column=0,padx=10,pady=10)
