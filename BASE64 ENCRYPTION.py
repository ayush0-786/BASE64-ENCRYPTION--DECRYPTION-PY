
# encryption and decryption using BASE64 algorithm

from tkinter import *
from tkinter import messagebox
import base64

screen=Tk()
screen.geometry("420x420")
screen.title("Encryptor Decryptor")
screen.configure(bg="grey")



def encrypt():
     password=code.get()
     if password=="1234":
         screen1=Toplevel(screen)
         screen1.title("Encrypted Code")
         screen1.geometry("400x250")
         screen1.configure(bg="black")
         
         message=text1.get(1.0,END)
         encode_message=message.encode("ascii")
         base64_bytes=base64.b64encode(encode_message)
         encrypt=base64_bytes.decode("ascii")
         Label(screen1,text="encrypted code :",font="impack 10 bold").place(x=5,y=6)
         text2=Text(screen1,font="30",bd="4",wrap=WORD)
         text2.place(x=2,y=30,width=390,height=180)
         text2.insert(END,encrypt)
     
     elif(password==""):
          messagebox.showerror("error","please enter key")
          
     elif(password!="1234"):
          messagebox.showerror("sorry!"," enter correct key")
       



def decrypt():
     password=code.get()
     if password=="1234":
         screen2=Toplevel(screen)
         screen2.title("Decrypted Code")
         screen2.geometry("400x250")
         screen2.configure(bg="green")
         
         message=text1.get(1.0,END)
         encode_message=message.encode("ascii")
         base64_bytes=base64.b64decode(encode_message)
         encrypt=base64_bytes.decode("ascii")
         Label(screen2,text="Decrypted code :",font="impack 10 bold").place(x=5,y=6)
         text2=Text(screen2,font="30",bd="4",wrap=WORD)
         text2.place(x=2,y=30,width=390,height=180)
         text2.insert(END,encrypt)
     
     elif(password==""):
          messagebox.showerror("error","please enter key")
          
     elif(password!="1234"):
          messagebox.showerror("sorry!"," enter correct key")
          



def reset():
     text1.delete(1.0,END)
     code.set("")
     



Label(screen,text="enter the text for encryption and decryption",font="impack 14 bold").place(x=5,y=6)




text1=Text(screen,font="20")
text1.place(x=5,y=45,width=410,height=120)




Label(screen,text="Enter The Key",font="impack 14 bold").place(x=15,y=180)



code=StringVar ()
Entry(textvariable=code,bd=4,font="20",show="*").place(x=160,y=178)




Button(screen,text="ENCRYPT",font="arial 15 bold",bg="green",fg="white",command=encrypt).place(x=45,y=230,width=150)
Button(screen,text="DECRYPT",font="arial 15 bold",bg="red",fg="white",command=decrypt).place(x=225,y=230,width=150)
Button(screen,text="RESET",font="arial 15 bold",bg="blue",fg="white",command=reset).place(x=125,y=290,width=150)


mainloop()