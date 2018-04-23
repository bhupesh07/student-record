
from tkinter import*


root=Tk()
root.geometry("1600x8000")
root.title("Students Record")

Tops=Frame(root, width=1600,relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side=LEFT)
lblInfo=Label(Tops,font=('helvetica',50,'bold'),text="STUDENT RECORD",fg="Black",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)

s1=StringVar()           #Declaration of string variable
s2=StringVar()
s3=StringVar()
s4=StringVar()
s5=StringVar()
s6=StringVar()


#====================================Restaraunt Info 1===========================================================


Cutomer_id1= Label(f1, font=('arial', 16, 'bold'),text="Cutomer_id",bd=16,anchor="w")
Cutomer_id1.grid(row=0, column=0)
n1=Entry(f1, font=('arial',16,'bold'),textvariable=s1,bd=10,insertwidth=4,bg="powder blue",justify='right')
n1.grid(row=0,column=1)


Name1= Label(f1, font=('arial', 16, 'bold'),text="Name",bd=16,anchor="w")
Name1.grid(row=1, column=0)
n2=Entry(f1, font=('arial',16,'bold'),textvariable=s2,bd=10,insertwidth=4,bg="powder blue",justify='right')
n2.grid(row=1,column=1)


Address1= Label(f1, font=('arial', 16, 'bold'),text="Address",bd=16,anchor="w")
Address1.grid(row=2, column=0)
n3=Entry(f1, font=('arial',16,'bold'),textvariable=s3,bd=10,insertwidth=4,bg="powder blue",justify='right')
n3.grid(row=2,column=1)

Batch1= Label(f1, font=('arial', 16, 'bold'),text="Contact",bd=16,anchor="w")
Batch1.grid(row=3, column=0)
n4=Entry(f1, font=('arial',16,'bold'),textvariable=s4,bd=10,insertwidth=4,bg="powder blue",justify='right')
n4.grid(row=3,column=1)

Age1= Label(f1, font=('arial', 16, 'bold'),text="Age",bd=16,anchor="w")
Age1.grid(row=4, column=0)
n5=Entry(f1, font=('arial',16,'bold'),bd=10,textvariable=s5,insertwidth=4,bg="powder blue",justify='right')
n5.grid(row=4,column=1)

n6=Entry(f1, font=('arial',16,'bold'),bd=10,textvariable=s6,insertwidth=4,bg="powder blue",justify='right')
n6.grid(row=11,column=2)


def first():                # Function to traverse first record
    global count
    f=open("pandey.txt","r")
    l=f.readlines()
    m=l[0].split()
    s1.set(m[0])
    s2.set(m[1])
    s3.set(m[2])
    s4.set(m[3])
    s5.set(m[4])
    count=1
def last():                        #Function to traverse last record
    global count
    f=open("pandey.txt","r")
    l=f.readlines()
    k=len(l)
    m=l[-1].split()
    s1.set(m[0])
    s2.set(m[1])
    s3.set(m[2])
    s4.set(m[3])
    s5.set(m[4])
    count=k
def addrec():                   #Function to add a new record
    flag=0
    s6.set("")
    f=open("pandey.txt","w+")
    lines=f.readlines()
    f.close()
    print(lines)
    f=open("pandey.txt","a")
    CustomerID=s1.get()
    Name=s2.get()
    Address=s3.get()
    Contact=s4.get()
    Age=s5.get()
    try:

        for i in lines:
            j=i.split()

            if(CustomerID==(j[0])):
                flag=1
                print("*")

    except:
        print("first record")
    if(flag==0):
        if(len(Contact)==10):

            f.writelines(CustomerID.ljust(5)+Name.ljust(20)+Address.ljust(20)+Contact.ljust(20)+Age.ljust(5)+"\n")
            reset()
            s6.set("Stored")

        else:
           s6.set("Incorrect Mobile no")
    else:
        s6.set("Id already exist")
    f.close()

def nextrec():                   # Function to see next  record
    r=""
    s6.set(r)
    global count
    i=0
    f=open("pandey.txt","r")
    try:

        while(i<=count):
            l=f.readline()
            i=i+1

        m=l.split()
        s1.set(m[0])
        s2.set(m[1])
        s3.set(m[2])
        s4.set(m[3])
        s5.set(m[4])
        print(m)
        count=count+1
    except:
        m=""
        s1.set(m)
        s2.set(m)
        s3.set(m)
        s4.set(m)
        s5.set(m)
        
        s6.set("No More Record Found")
        

    f.close()
def prev():                  #Function to see previous record
    r=""
    s6.set(r)
    global count
    i=0
    print(count)
    f=open("pandey.txt","r")
    try:

        while(count-1>i):
            l=f.readline()
            i=i+1
        m=l.split()
        s1.set(m[0])
        s2.set(m[1])
        s3.set(m[2])
        s4.set(m[3])
        s5.set(m[4])
        print(m)
        count=count-1
    except:

        m=""
        s1.set(m)
        s2.set(m)
        s3.set(m)
        s4.set(m)
        s5.set(m)
        s6.set("you cant go back")
        count=0
                                            #Function to delete record
def delrec():                                              
   
    k=[s1.get(),s2.get(),s3.get(),s4.get(),s5.get()]
    
    f=open("pandey.txt","r")
    lines=f.readlines()
    print(lines)
    print(k)
    f.close()
    f=open("pandey.txt","w")
    for i in lines:
        m=i.split()
        print(m)
        if(m!=k):
             f.writelines(m[0].ljust(3)+m[1].ljust(20)+m[2].ljust(20)+m[3].ljust(20)+m[4].ljust(5)+"\n")
             s6.set("Record Deleted")
    f.close()
def search():                                #Function to search record
    k=Cutomer_id.get()

    f=open("pandey.txt","r")
    h=f.readlines()
    for i in h:
        j=i.split()
        if(j[0]==k):
            print("customer found")
            print(j)
            s1.set(j[0])
            s2.set(j[1])
            s3.set(j[2])
            s4.set(j[3])
            s5.set(j[4])

    f.close()
def update():                         #Function to update record
    a1=s1.get()
    a2=s2.get()
    a3=s3.get()
    a4=s4.get()
    a5=s5.get()
    f=open("pandey.txt","r")
    h=f.readlines()
    f.close()
    f=open("pandey.txt","w")
    flag=0
    for i in h:
        j=i.split()
        if(j[0]!=a1):
            f.writelines(j[0].ljust(3)+j[1].ljust(20)+j[2].ljust(20)+j[3].ljust(20)+j[4].ljust(5)+"\n")

        else:
            f.writelines(a1.ljust(3)+a2.ljust(20)+a3.ljust(20)+a4.ljust(20)+a5.ljust(5)+"\n")
            flag=1
            s6.set("record updated")
    if(flag==0):
        s6.set("You cannot update id")



def reset():                        #Function to clear record
    global count
    count=0 
    m=""
    s1.set(m)
    s2.set(m)
    s3.set(m)
    s4.set(m)
    s5.set(m)
    s6.set(m)




#==========================================Buttons==========================================================================================
btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="ADD",command=addrec,bg="powder blue").grid(row=7,column=1)

btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="DELETE",command=delrec,bg="powder blue").grid(row=7,column=2)

btnExit1=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="UPDATE",command=update,bg="powder blue").grid(row=7,column=3)

btnExit2=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="CLEAR",command=reset,bg="powder blue").grid(row=7,column=4)

btnExit3=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="/>",command=first,bg="powder blue").grid(row=8,column=1)

btnExit4=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text=">",command=nextrec,bg="powder blue").grid(row=8,column=2)

btnExit5=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="<",command=prev,bg="powder blue").grid(row=8,column=3)

btnExit6=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="\<",command=last,bg="powder blue").grid(row=8,column=4)

btnExit7=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="SEARCH",command=search,bg="powder blue").grid(row=12,column=2)




'''l1=Label(win,text="CustomerID")        #Declaration of Labels variable
l2=Label(win,text="Cutomer_id")
l3=Label(win,text="Address")
l4=Label(win,text="Mobile No.")
l5=Label(win,text="Bill")
t1=Entry(win,textvariable=Cutomer_id)           #Declaration of Textboxes
t2=Entry(win,textvariable=Name)
t3=Entry(win,textvariable=Address)
t4=Entry(win,textvariable=Contact)
t5=Entry(win,textvariable=Age)


'''


root.mainloop()

