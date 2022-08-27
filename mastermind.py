from tkinter import*
from random import*
from tkinter import messagebox



def click():
    guessed_code=""
    guessed_dig=""
    dig1=e1.get()
    dig2=e2.get()
    dig3=e3.get()
    dig4=e4.get()
    guessed_code=dig1+dig2+dig3+dig4
    
#if the guessed digit doesn't match with the secret_code,
#the entry box turns RED, indicating the same,
#thus, the user has to guess the same

    if secret_code[0] != guessed_code[0]:
        e1.configure(bg="Red")
        e1.delete(0,'end')
        
    if secret_code[1] != guessed_code[1]:
        e2.configure(bg="Red")
        e2.delete(0,'end')
        
    if secret_code[2] != guessed_code[2]:
        e3.configure(bg="Red")
        e3.delete(0,'end')
        
    if secret_code[3] != guessed_code[3]:
        e4.configure(bg="Red")
        e4.delete(0,'end')
    
#if the digit matches, then the entry box is disabled
#ie. doesn't take input from the user
#thus, the digit is fixed  
    
    if secret_code[0] == guessed_code[0]:
        e1.configure(state='disabled')
        guessed_dig+='0'
        
    if secret_code[1] == guessed_code[1]:
        e2.configure(state='disabled')
        guessed_dig+='1'
        
    if secret_code[2] == guessed_code[2]:
        e3.configure(state='disabled')
        guessed_dig+='2'
        
    if secret_code[3] == guessed_code[3]:
        e4.configure(state='disabled')
        guessed_dig+='3'
    
    
    def climax():
        root.destroy()
    
    def hint(): 
        nonlocal guessed_dig,guessed_code
        secret_code_index="0123"
        flag=0
        hint_options=[]
        def gives_hint(random_dig,random_dig_index):
            nonlocal hint_options, guessed_dig, guessed_code
            hint_dig=StringVar(root, value=random_dig)
            for i in hint_options:
                if i == random_dig_index:
                    if i==0:
                        e1.configure(textvariable=hint_dig,state=DISABLED)
                        guessed_dig+='0'
                        guessed_code+=secret_code[i]
                        
                    if i==1:
                        e2.configure(textvariable=hint_dig,state=DISABLED)
                        guessed_dig+='1'
                        guessed_code+=secret_code[i]
                        
                    if i==2:
                        e3.configure(textvariable=hint_dig,state=DISABLED)
                        guessed_dig+='2'
                        guessed_code+=secret_code[i]
                        
                    if i==3:
                        e4.configure(textvariable=hint_dig,state=DISABLED)
                        guessed_dig+='3'
                        guessed_code+=secret_code[i]
                
            
        if guessed_dig=="":
            random_dig_index1=randint(0,3)
            flag=1
            random_dig1=secret_code[random_dig_index1]
            gives_hint(random_dig1,random_dig_index1)
            
        if flag==0:    
            for i in guessed_dig:
                set1=set(secret_code_index)
                set2=set(guessed_dig)
                set_not_guessed=set()
                set_not_guessed=set1-set2 
                #the index of the digits which aren't guessed correctly are stored in a set
                not_guessed=''.join(set_not_guessed)
                random_dig_index2=int(choice(not_guessed))
            print(random_dig_index2)
            random_dig2=secret_code[random_dig_index2]
            print(secret_code)
            print(random_dig2)
            
            
                
            for i in set_not_guessed:
                hint_options.append(int(i))
            gives_hint(random_dig2,random_dig_index2)
        
    b_try_again =Button(root,text="HINT",command=hint)
    if secret_code!=guessed_code:
        b_try_again.grid(row=4,column=5)
        
    else:       
        messagebox.showinfo("?!","SUCCESS")
        climax()
        
    

root = Tk()
root.geometry("400x200+400+250")
root.title("MASTERMIND")

secret_code=str(randrange(1000,5001))
print(secret_code)
l1=Label(root,text="ENTER").grid(column=1,sticky='w')
e1=Entry(root,width=5,justify='center')
e1.grid(row=2,column=1,padx=5, pady=5)
e1.insert(0,"")

e2=Entry(root,width=5,justify='center')
e2.grid(row=2,column=2,padx=5, pady=5)
e2.insert(0,"")

e3=Entry(root,width=5,justify='center')
e3.grid(row=2,column=3,padx=5, pady=5)
e3.insert(0,"")

e4=Entry(root,width=5,justify='center')
e4.grid(row=2,column=4,padx=5, pady=5)
e4.insert(0,"")
b1=Button(root,text=">",command=click)
b1.grid(row=2,column=5,sticky='w')

root.mainloop()