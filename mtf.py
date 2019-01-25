
import tkinter as TK

def cbm(event):

    ft.set(mtr.get()*3)



def main():

    root = TK.Tk()

    global mtr,ft

    mtr = TK.IntVar()
    ft = TK.IntVar()

    mtr.set(0)
    ft.set(0)

    m= TK.Scale(root,from_=0,to=100,variable=mtr,tickinterval=10,width=20,length=400,command=cbm)

    m.grid(row=0,column=0)

    f = TK.Scale(root,from_=0,to=300,variable=ft,length=400,width=20,tickinterval=25)
    f.grid(row=0,column=1)


    label1 = TK.Label(root,text='Metre')
    label2 = TK.Label(root,text='Feet')

    label1.grid(row=1,column=0)
    label2.grid(row=1,column=1)

    root.mainloop()


if __name__ == '__main__':
    main()
