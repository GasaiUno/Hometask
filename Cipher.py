from tkinter import *
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]
root=Tk()
s2=0
def Cipher():
    global s2
    s2=list(ent.get())
    for i in range(0,len(s2)):
          b=0
          a=0
          while a==0:
               if s2[i]==' ':
                   s2[i]='_'
                   break
               if s2[i]=='z':
                   s2[i]='a'
                   break
               if alphabet[b]==s2[i]:
                    s2[i]=alphabet[b+1]
                    a=1
               else:
                   b+=1
          ext2['text']='Ответ:',s2
def Decipher():
    global s2
    s2=list(ent.get())
    for i in range(0,len(s2)):
          b=25
          a=0
          while a==0:
               if s2[i]==' ':
                   s2[i]='_'
                   break
               if s2[i]=='a':
                   s2[i]='z'
                   break
               if alphabet[b]==s2[i]:
                    s2[i]=alphabet[b-1]
                    break
               else:
                   b-=1                            
    ext2['text']='Ответ:',s2
ext=Label(text="Введите слово для шифрования/дешифрования")
ent=Entry()
ext2=Label(text=s2)
btn1=Button(text='Зашифровать!',command=Cipher)
btn2=Button(text='Расщифровать!',command=Decipher)
ext.pack()
ent.pack()
ext2.pack()
btn1.pack()
btn2.pack()
root.mainloop()
