import mysql.connector
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.font import Font
from PIL import Image,ImageTk
from datetime import datetime
import random
import string

tk=Tk()
tk.geometry("1500x1000")
tk.title("Airline Reservation")
tk.configure(bg="#ffffff")

def Show_table():

    framesh = Frame(tk)
    framesh.grid(row=0,column=0,padx=130,pady=310)

    headersh = ["PNR","Fl_No","Seat_No","Dp_place","Ar_place","Amount","Status","Name","Age","Sex","Address","Ph_No","Date"]
    for i, header in enumerate(headersh):
        header_label = Label(framesh, text=header, font=("times", 18, "bold"),bg="#ced6e0")
        header_label.grid(row=0, column=i, padx=10, pady=10)

    mysql_conn = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="Airline_reservation"
    )

    mycursor = mysql_conn.cursor()
    Fl_date=sptxt.get()
    fld_no=sptxtfld.get()
    shdate_format=datetime.strptime(Fl_date, '%d-%m-%Y').strftime('%Y-%m-%d')
    sql = "select * from passenger_details where Date=%s and Fl_No=%s"

    mycursor.execute(sql,(shdate_format,fld_no))
    myresult = mycursor.fetchall()

    for i, row in enumerate(myresult, start=1):
        for j, item in enumerate(row):
            data_label = Label(framesh, text=item)
            data_label.grid(row=i, column=j, padx=5, pady=5)

    mysql_conn.close()

def Show_passengers():
    global sp_lab, sp_labnew, sptxt, spLabcf, spLabms, sptxtfld, spLabfld, spbtnet1, spbtne4,shw_pg
    def Back7():
        for widget in tk.winfo_children():
            widget.destroy()
        New()

    lab_bkg1.destroy()
    labnew.destroy()
    btnfd.destroy()
    btnpd.destroy()
    btne1.destroy()
    shw_pg=tk
    sp_lab=Label(shw_pg,bg="#badc58")
    sp_lab.place(x=0,y=0,width=1500,height=1000)
    sp_labnew=Label(shw_pg,text="SkyWispher International Airlines",font=('Georgia',40,'bold'),fg="#192a56")
    sp_labnew.place(x=270,y=30)

    sptxt=Entry(shw_pg,width=30,font=('Berlin Sans FB',15),bg="#ffffff")
    sptxt.place(x=330,y=130,width=180,height=38)
    spLabcf=Label(shw_pg,text="Date",font=('Georgia',15),padx=20,pady=5,bg="#ffffff")
    spLabcf.place(x=130,y=130,width=150)

    spLabms=Label(shw_pg,text="* DD-MM-YYYY",font=('Georgia',10),padx=20,pady=5,bg="#badc58")
    spLabms.place(x=530,y=130)

    sptxtfld=Entry(shw_pg,width=30,font=('Berlin Sans FB',15),bg="#ffffff")
    sptxtfld.place(x=330,y=190,width=180,height=38)
    spLabfld=Label(shw_pg,text="Flight No",font=('Georgia',15),padx=20,pady=5,bg="#ffffff")
    spLabfld.place(x=130,y=190,width=150)

    spbtnet1=Button(shw_pg,text="Enter",font=('Georgia',15,'bold'),padx=20,pady=5,bg="#1B1464",fg="#ffffff",command=Show_table)
    spbtnet1.place(x=1100,y=700,width=150)
    spbtne4=Button(shw_pg,text="Back",font=('Georgia',15,'bold'),padx=20,pady=5,bg="#1B1464",fg="#ffffff",command=Back7)
    spbtne4.place(x=1300,y=700,width=150)


def Fl_insertion():
    global Flg_No, Capacity_oc, VSeat, Start_place, Dep_place, Fl_Date

    mysqldb=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="Airline_reservation")

    mycursor=mysqldb.cursor()
    
    Flg_No=txt1.get()
    Aircraft_code=txt2.get()
    Capacity_oc=txt3.get()
    Start_place=txt4.get()
    Dep_place=txt5.get()
    Dep_time=txt6.get()
    Arv_time=txt7.get()
    TotExpense=txt8.get()
    VSeat=txt9.get()
    Fl_Date=txt10.get()
    date_fmt = datetime.strptime(Fl_Date, '%d-%m-%Y').strftime('%Y-%m-%d')

    sql="insert into flight_details (Fl_No,Aircraft,Capacity,St_place,Dp_place,Dp_time,Ar_time,Expense,Vacant_seats,Date) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    data=(Flg_No,Aircraft_code,Capacity_oc,Start_place,Dep_place,Dep_time,Arv_time,TotExpense,VSeat,date_fmt)
    mycursor.execute(sql,data)
    mysqldb.commit()
    print("Data saved")
    txt1.delete(0,END)
    txt2.delete(0,END)
    txt3.delete(0,END)
    txt4.delete(0,END)
    txt5.delete(0,END)
    txt6.delete(0,END)
    txt7.delete(0,END)
    txt8.delete(0,END)
    txt9.delete(0,END)
    txt10.delete(0,END)

    messagebox.showinfo("Skywishper","New Flight Added")

def Fl_Delete():
    mysqld=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="Airline_reservation")
    dele=mysqld.cursor()
    Flg_no=txt1.get()
    
    sql="delete from flight_details where Fl_NO=%s"
    data=(Flg_no,)
    dele.execute(sql,data)
    mysqld.commit()
    print("Data Deleted")
    txt1.delete(0,END)

    messagebox.showinfo("Skywishper","Flight Cancelled")

def Fl_Update():
    mysqldb=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="Airline_reservation")
    upd=mysqldb.cursor()
    Flg_NO=txt1.get()
    Capacity_oc=txt3.get()
    Start_place=txt4.get()
    Dep_place=txt5.get()
    Dep_time=txt6.get()
    Arv_time=txt7.get()
    TotExpense=txt8.get()
    VSeat=txt9.get()
    Fl_Date=txt10.get()
    date_fmt = datetime.strptime(Fl_Date, '%d-%m-%Y').strftime('%Y-%m-%d')

    sql="update flight_details set Capacity=%s,St_place=%s,Dp_place=%s,Dp_time=%s,Ar_time=%s,Expense=%s,Vacant_seats=%s,Date=%s where Fl_No=%s"
    data=(Capacity_oc,Start_place,Dep_place,Dep_time,Arv_time,TotExpense,VSeat,date_fmt,Flg_NO)
    upd.execute(sql,data)
    mysqldb.commit()
    print("Updated")
    txt1.delete(0,END)
    txt2.delete(0,END)
    txt3.delete(0,END)
    txt4.delete(0,END)
    txt5.delete(0,END)
    txt6.delete(0,END)
    txt7.delete(0,END)
    txt8.delete(0,END)
    txt9.delete(0,END)
    txt10.delete(0,END)

    messagebox.showinfo("Skywishper","Updated Successfully")

def clear():
    txt1.delete(0,END)
    txt2.delete(0,END)
    txt3.delete(0,END)
    txt4.delete(0,END)
    txt5.delete(0,END)
    txt6.delete(0,END)
    txt7.delete(0,END)
    txt8.delete(0,END)
    txt9.delete(0,END)
    txt10.delete(0,END)

def Flight_detail(): #Button1 in admin
    global label, Labe, txt1, Lab1, txt2, Lab2, txt3, Lab3, txt4, Lab4, txt5, Lab5, txt6, Lab6, txt7, Lab7, txt8, Lab8, txt9, Lab9, txt10, Lab10

    def Back2():
        label.destroy()
        Labe.destroy()
        txt1.destroy()
        Lab1.destroy()
        txt2.destroy()
        Lab2.destroy()
        txt3.destroy()
        Lab3.destroy()
        txt4.destroy()
        Lab4.destroy()
        txt5.destroy()
        Lab5.destroy()
        txt6.destroy()
        Lab6.destroy()
        txt7.destroy()
        Lab7.destroy()
        txt8.destroy()
        Lab8.destroy()
        flLab.destroy()
        New()

    lab_bkg1.destroy()
    labnew.destroy()
    btnfd.destroy()
    btnpd.destroy()
    btne1.destroy()

    image3=Image.open("C:\\Users\\KAVYA\\OneDrive\\Pictures\\Saved Pictures\\newbg.jpg")
    resize7=image3.resize((1500,1000))
    tk.Fl_img=ImageTk.PhotoImage(resize7)
    label=Label(image=tk.Fl_img)
    label.image=tk.Fl_img
    label.place(x=0,y=0)

    fld=tk
    Labe=Label(fld,text="SkyWispher International Airlines",font=('Georgia',25,'bold'),fg="black",bg="#ffffff")
    Labe.place(x=270,y=30)

    txt1=Entry(fld,width=30,font=('Berlin Sans FB',15),bg="#ffffff")
    txt1.place(x=500,y=120,width=180,height=38)

    Lab1=Label(fld,text="Flight_No",font=('Georgia',15),padx=20,pady=5,bg="#ffffff")
    Lab1.place(x=300,y=120,width=150)

    txt2=Entry(fld,width=30,font=('Berlin Sans FB',15),bg="#ffffff")
    txt2.place(x=500,y=180,width=180,height=38)

    Lab2=Label(fld,text="Airline",font=('Georgia',15),padx=20,pady=5,bg="#ffffff")
    Lab2.place(x=300,y=180,width=150)

    txt3=Entry(fld,width=30,font=('Berlin Sans FB',15),bg="#ffffff")
    txt3.place(x=500,y=240,width=180,height=38)

    Lab3=Label(fld,text="Capacity",font=('Georgia',15),padx=20,pady=5,bg="#ffffff")
    Lab3.place(x=300,y=240,width=150)

    txt4=Entry(fld,width=30,font=('Berlin Sans FB',15),bg="#ffffff")
    txt4.place(x=500,y=300,width=180,height=38)

    Lab4=Label(fld,text="Start_place",font=('Georgia',15),padx=20,pady=5,bg="#ffffff")
    Lab4.place(x=300,y=300,width=150)

    txt5=Entry(fld,width=30,font=('Berlin Sans FB',15),bg="#ffffff")
    txt5.place(x=500,y=360,width=180,height=38)

    Lab5=Label(fld,text="Depature_place",font=('Georgia',15),padx=20,pady=5,bg="#ffffff")
    Lab5.place(x=300,y=360,width=150)

    txt6=Entry(fld,width=30,font=('Berlin Sans FB',15),bg="#ffffff")
    txt6.place(x=500,y=420,width=180,height=38)

    Lab6=Label(fld,text="Depature_time",font=('Georgia',15),padx=20,pady=5,bg="#ffffff")
    Lab6.place(x=300,y=420,width=150)

    txt7=Entry(fld,width=30,font=('Berlin Sans FB',15),bg="#ffffff")
    txt7.place(x=500,y=480,width=180,height=38)

    Lab7=Label(fld,text="Arrival_time",font=('Georgia',15),padx=20,pady=5,bg="#ffffff")
    Lab7.place(x=300,y=480,width=150)

    txt8=Entry(fld,width=30,font=('Berlin Sans FB',15),bg="#ffffff")
    txt8.place(x=500,y=540,width=180,height=38)

    Lab8=Label(fld,text="Expense",font=('Georgia',15),padx=20,pady=5,bg="#ffffff")
    Lab8.place(x=300,y=540,width=150)

    txt9=Entry(fld,width=30,font=('Berlin Sans FB',15),bg="#ffffff")
    txt9.place(x=500,y=600,width=180,height=38)

    Lab9=Label(fld,text="Vacant_seats",font=('Georgia',15),padx=20,pady=5,bg="#ffffff")
    Lab9.place(x=300,y=600,width=150)

    txt10=Entry(fld,width=30,font=('Berlin Sans FB',15),bg="#ffffff")
    txt10.place(x=1300,y=30,width=180,height=38)

    Lab10=Label(fld,text="Date",font=('Georgia',15),padx=20,pady=5,bg="#ffffff")
    Lab10.place(x=1100,y=30,width=150)

    btnet=Button(fld,text="Enter",font=('Georgia',15,'bold'),padx=20,pady=5,bg="#1B1464",fg="#ffffff",command=Fl_insertion)
    btnet.place(x=270,y=680,width=150)

    btncl=Button(fld,text="Clear",font=('Georgia',15,'bold'),padx=20,pady=5,bg="#1B1464",fg="#ffffff",command=clear)
    btncl.place(x=780,y=680,width=150)

    btnd=Button(fld,text="Cancel",font=('Georgia',15,'bold'),padx=20,pady=5,bg="#1B1464",fg="#ffffff",command=Fl_Delete)
    btnd.place(x=440,y=680,width=150)

    btnu=Button(fld,text="Update",font=('Georgia',15,'bold'),padx=20,pady=5,bg="#1B1464",fg="#ffffff",command=Fl_Update)
    btnu.place(x=610,y=680,width=150)

    btne2=Button(fld,text="Back",font=('Georgia',15,'bold'),padx=20,pady=5,bg="#1B1464",fg="#ffffff",command=Back2)
    btne2.place(x=1300,y=700,width=150)

    flLab=Label(fld,text="* DD-MM-YYYY",font=('Georgia',10),padx=20,pady=5,bg="#ffffff")
    flLab.place(x=1300,y=80)

def New():
    global lab_bkg1, labnew, btnfd, btnpd, btne1
    def Back1():
        lab_bkg1.destroy()
        labnew.destroy()
        btnfd.destroy()
        btnpd.destroy()
        btne1.destroy()
        Landing_pg()

    label1.destroy()
    label2.destroy()
    Lab.destroy()
    frame.destroy()
    frame2.destroy()

    label1.destroy()
    label2.destroy()
    Lab.destroy()
    frame.destroy()
    frame2.destroy()
    new=tk
    bkg1=Image.open("C:\\Users\\KAVYA\\OneDrive\\Pictures\\Saved Pictures\\bg11.jpg")
    resize6=bkg1.resize((1500,1000))
    tk.bkg1_img=ImageTk.PhotoImage(resize6)
    lab_bkg1=Label(new,image=tk.bkg1_img)
    lab_bkg1.bkg1=tk.bkg1_img
    lab_bkg1.pack()
    labnew=Label(new,text="SkyWispher International Airlines",font=('Georgia',40,'bold'),fg="#192a56")
    labnew.place(x=270,y=30)
    btnfd=Button(new,text="Flight Details",font=('Georgia',15,'bold'),padx=20,pady=5,fg="#1B1464",command=Flight_detail)#light_details,bg="#48dbfb"
    btnfd.place(x=550,y=200,width=250)
    btnpd=Button(new,text="Passenger Details",font=('Georgia',15,'bold'),padx=20,pady=5,fg="#1B1464",command=Show_passengers)
    btnpd.place(x=550,y=280,width=250)
    btne1=Button(new,text="Landing_page",font=('Georgia',15,'bold'),padx=20,pady=5,fg="white",bg="#1B1464",command=Back1)
    btne1.place(x=1300,y=700,width=170)

def Show_det():
    global txt_gtname
    mysqlgt=mysql.connector.connect(
        host="localhost", user="root", passwd="",database="Airline_reservation")
    gett=mysqlgt.cursor()
    name=txt_gtname.get()
    sql="select PNR from passenger_details where Name=%s"
    data=(name,)
    gett.execute(sql,data)
    gtresult=gett.fetchone()
    if gtresult:
        gtpnr=gtresult[0]
        print("PNR:",gtpnr)
        txt_gtpnr.config(state='normal')
        txt_gtpnr.delete(0, END)  
        txt_gtpnr.insert(END, gtpnr)
        txt_gtpnr.config(state='disabled')

    getd=mysqlgt.cursor()
    sql="select Date from passenger_details where Name=%s"
    getd.execute(sql,data)
    gtdresult=getd.fetchone()
    if gtdresult:
        gtd=gtdresult[0]
        print("Date:",gtd)
        txt_gtdate.config(state='normal')
        txt_gtdate.delete(0, END)  
        txt_gtdate.insert(END, gtd)
        txt_gtdate.config(state='disabled')

    getf=mysqlgt.cursor()
    sql="select Dp_place from passenger_details where Name=%s"
    getf.execute(sql,data)
    gtfresult=getf.fetchone()
    if gtfresult:
        gtf=gtfresult[0]
        print("From:",gtf)
        txt_gtfrom.config(state='normal')
        txt_gtfrom.delete(0, END)  
        txt_gtfrom.insert(END, gtf)
        txt_gtfrom.config(state='disabled')

    getto=mysqlgt.cursor()
    sql="select Ar_place from passenger_details where Name=%s"
    getto.execute(sql,data)
    gttoresult=getto.fetchone()
    if gttoresult:
        gtto=gttoresult[0]
        print("To:",gtto)
        txt_gtto.config(state='normal')
        txt_gtto.delete(0, END)  
        txt_gtto.insert(END, gtto)
        txt_gtto.config(state='disabled')

    gettm=mysqlgt.cursor()
    sql="select Dp_time from flight_details where Fl_No=(SELECT Fl_No FROM passenger_details WHERE Name = %s)"
    gettm.execute(sql,data)
    gttmresult=gettm.fetchone()
    if gttmresult:
        gttm=gttmresult[0]
        print("Time:",gttm)
        txt_gttm.config(state='normal')
        txt_gttm.delete(0, END)  
        txt_gttm.insert(END, gttm)
        txt_gttm.config(state='disabled')

    getfl=mysqlgt.cursor()
    sql="select Fl_NO from passenger_details where Name=%s"
    getfl.execute(sql,data)
    gtflresult=getfl.fetchone()
    if gtflresult:
        gtfl=gtflresult[0]
        print("Fl.No:",gtfl)
        txt_gtfl.config(state='normal')
        txt_gtfl.delete(0, END)  
        txt_gtfl.insert(END, gtfl)
        txt_gtfl.config(state='disabled')

    gets=mysqlgt.cursor()
    sql="select Seat_No from passenger_details where Name=%s"
    gets.execute(sql,data)
    gtsresult=gets.fetchone()
    if gtsresult:
        gts=gtsresult[0]
        print("seat:",gts)
        txt_gts.config(state='normal')
        txt_gts.delete(0, END)  
        txt_gts.insert(END, gts)
        txt_gts.config(state='disabled')

def Get_ticket():
    global txt_gtpnr, txt_gtname, txt_gtfrom, txt_gtto, txt_gtdate, txt_gttm, txt_gtfl, txt_gts
    def Back8():
        for widget in tk.winfo_children():
            widget.destroy()
        New2()    

    lab_bkg.destroy()
    labnew2.destroy()
    btncf.destroy()
    btnbk.destroy()
    btnct.destroy()
    btne2.destroy()
    btngt.destroy()
    gt=tk
    lab_gt=Label(gt,bg="#FF1744")
    lab_gt.place(x=0,y=0,width=1500,height=1000)

    label_gt=Label(gt,text="SkyWispher International Airlines",font=('Georgia',40,'bold'),fg="#1B1464")
    label_gt.place(x=280,y=30)

    framegt=Frame(tk,bg="#FFCC80")
    framegt.place(x=140,y=150,width=1200,height=500)
    gtimage=Image.open("C:\\Users\\KAVYA\\OneDrive\\Pictures\\Saved Pictures\\gt.jpg") 
    resize8=gtimage.resize((1200,500))
    tk.gtimg=ImageTk.PhotoImage(resize8)
    labelgtim=Label(framegt,image=tk.gtimg)
    labelgtim.pack(expand=True)

    Lab_gtbp=Label(framegt,text="🛬 BOARDING PASS",font=('Georgia',20,'bold'),padx=20,pady=5,bg="#01579B",fg="#ffffff")
    Lab_gtbp.place(x=420,y=80,width=350,height=50)

    txt_gtpnr=Entry(framegt,width=30,font=('Berlin Sans FB',15),bg="#FFF3E0",fg="#1B1464")
    txt_gtpnr.place(x=200,y=150,width=150,height=38)
    Lab_gtpnr=Label(framegt,text="Ticket No",font=('Georgia',15,'bold'),padx=20,pady=5,bg="#FFF3E0",fg="#1B1464")
    Lab_gtpnr.place(x=80,y=150,width=100)

    txt_gtname=Entry(framegt,width=30,font=('Berlin Sans FB',15),bg="#FFF3E0",fg="#1B1464")
    txt_gtname.place(x=950,y=150,width=160,height=38)
    Lab_gtname=Label(framegt,text="Name",font=('Georgia',15,'bold'),padx=20,pady=5,bg="#FFF3E0",fg="#1B1464")
    Lab_gtname.place(x=830,y=150,width=100)

    txt_gtfrom=Entry(framegt,width=30,font=('Berlin Sans FB',15),bg="#FFF3E0",fg="#1B1464")
    txt_gtfrom.place(x=200,y=230,width=150,height=38)
    Lab_gtfrom=Label(framegt,text="From",font=('Georgia',15,'bold'),padx=20,pady=5,bg="#FFF3E0",fg="#1B1464")
    Lab_gtfrom.place(x=80,y=230,width=100)

    txt_gtto=Entry(framegt,width=30,font=('Berlin Sans FB',15),bg="#FFF3E0",fg="#1B1464")
    txt_gtto.place(x=590,y=230,width=150,height=38)
    Lab_gtto=Label(framegt,text="To",font=('Georgia',15,'bold'),padx=20,pady=5,bg="#FFF3E0",fg="#1B1464")
    Lab_gtto.place(x=470,y=230,width=100)

    txt_gtdate=Entry(framegt,width=30,font=('Berlin Sans FB',15),bg="#FFF3E0",fg="#1B1464")
    txt_gtdate.place(x=590,y=150,width=150,height=38)
    Lab_gtdate=Label(framegt,text="Date",font=('Georgia',15,'bold'),padx=20,pady=5,bg="#FFF3E0",fg="#1B1464")
    Lab_gtdate.place(x=470,y=150,width=100)

    txt_gttm=Entry(framegt,width=30,font=('Berlin Sans FB',15),bg="#FFF3E0",fg="#1B1464")
    txt_gttm.place(x=200,y=310,width=150,height=38)
    Lab_gttm=Label(framegt,text="Time",font=('Georgia',15,'bold'),padx=20,pady=5,bg="#FFF3E0",fg="#1B1464")
    Lab_gttm.place(x=80,y=310,width=100)

    txt_gtfl=Entry(framegt,width=30,font=('Berlin Sans FB',15),bg="#FFF3E0",fg="#1B1464")
    txt_gtfl.place(x=590,y=310,width=150,height=38)
    Lab_gtfl=Label(framegt,text="Flight",font=('Georgia',15,'bold'),padx=20,pady=5,bg="#FFF3E0",fg="#1B1464")
    Lab_gtfl.place(x=470,y=310,width=100)

    txt_gts=Entry(framegt,width=30,font=('Berlin Sans FB',15),bg="#FFF3E0",fg="#1B1464")
    txt_gts.place(x=950,y=230,width=130,height=38)
    Lab_gts=Label(framegt,text="Seat No",font=('Georgia',15,'bold'),padx=20,pady=5,bg="#FFF3E0",fg="#1B1464")
    Lab_gts.place(x=830,y=230,width=100)
    
    label_no=Label(framegt,text="Gate closes 40 minutes befor depature",font=('times',15),fg="#1B1464",bg="#FFF3E0")
    label_no.place(x=270,y=370)

    btne5=Button(gt,text="Enter name and click",font=('Georgia',15,'bold'),padx=20,pady=5,bg="#ffffff",fg="#1B1464",command=Show_det)
    btne5.place(x=500,y=680)

    btnback=Button(gt,text="Back",font=('Georgia',15,'bold'),padx=20,pady=5,bg="#ffffff",fg="#1B1464",command=Back8)
    btnback.place(x=800,y=680,width=150)


def delete_ticket():#Sub program of Cancel Ticket
    global pnr,pnr_no
    
    mysqlpnr=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="Airline_reservation")
    dele_pnr=mysqlpnr.cursor()
    pnr_no=textpnr.get()
    
    sql="delete from passenger_details where PNR=%s"
    data=(pnr_no,)
    dele_pnr.execute(sql,data)
    mysqlpnr.commit()
    print("Data Deleted")
    textpnr.delete(0,END)

    messagebox.showinfo("Skywishper","Ticket Cancelled")

    inc_vs=mysqlpnr.cursor()
    sql="UPDATE flight_details SET Vacant_seats = Vacant_seats + 1 WHERE Fl_No = (SELECT Fl_No FROM passenger_details WHERE PNR = %s)"
    data=(pnr_no,)
    inc_vs.execute(sql,data)
    print("Vacant Seat incremented")
    mysqlpnr.commit()
    
def Cancel_ticket(): #Cancel Ticket
    global lab_ct, label_ct, btne5, textpnr, Labpnr, btnback
    def Back6():
        lab_ct.destroy()
        label_ct.destroy()
        btne5.destroy()
        textpnr.destroy()
        Labpnr.destroy()
        btnback.destroy()
        New2()

    lab_bkg.destroy()
    labnew2.destroy()
    btncf.destroy()
    btnbk.destroy()
    btnct.destroy()
    btne2.destroy()
    btngt.destroy()
    ct=tk
    #ct.configure(bg="#227093")
    ct_image=Image.open("C:\\Users\\KAVYA\\OneDrive\\Pictures\\Saved Pictures\\bg5.jpeg")
    resize7=ct_image.resize((1500,1000))
    tk.ct_img=ImageTk.PhotoImage(resize7)
    lab_ct=Label(ct,image=tk.ct_img)
    lab_ct.ct_image=tk.ct_img
    lab_ct.pack()

    label_ct=Label(ct,text="SkyWispher International Airlines",font=('Georgia',40,'bold'),fg="#1B1464")
    label_ct.place(x=120,y=30)

    textpnr=Entry(ct,width=30,font=('Berlin Sans FB',15),bg="#ffffff",fg="#1B1464")
    textpnr.place(x=1200,y=300,width=180,height=38)

    Labpnr=Label(ct,text="Enter PNR",font=('Georgia',15),padx=20,pady=5,bg="#ffffff",fg="#1B1464")
    Labpnr.place(x=1000,y=300,width=150)
    
    btne5=Button(ct,text="Enter",font=('Georgia',15,'bold'),padx=20,pady=5,bg="#ffffff",fg="#1B1464",command=delete_ticket)
    btne5.place(x=1000,y=680,width=150)

    btnback=Button(ct,text="Back",font=('Georgia',15,'bold'),padx=20,pady=5,bg="#ffffff",fg="#1B1464",command=Back6)
    btnback.place(x=1200,y=680,width=150)

def rand():
    while True:
        pnr = ''.join(str(random.randint(0, 9)) for _ in range(5))
        mysqlr=mysql.connector.connect(
        host="localhost",user="root",passwd="",database="Airline_reservation")
        rand_pnr=mysqlr.cursor()
        sql="select PNR from passenger_details where Fl_No=%s"
        rand_pnr.execute(sql,(pnr,))
        pnr_result=rand_pnr.fetchone()
        if not pnr_result:
            print("PNR:", pnr)
            text1.config(state='normal')
            text1.delete(0, END)  
            text1.insert(END, pnr)
            text1.config(state='disabled')
            break

def rand_seat():
    global fld
    fld=text2.get()
    date1=text13.get()
    date1_format = datetime.strptime(date1, '%d-%m-%Y').strftime('%Y-%m-%d')
    mysqlrs=mysql.connector.connect(
        host="localhost",user="root",passwd="",database="Airline_reservation")
    random_seat=mysqlrs.cursor()
    sql="select Capacity from flight_details where Fl_No=%s and Date=%s"
    data=(fld,date1_format)
    random_seat.execute(sql,data)
    Sresult=random_seat.fetchone()
    if Sresult:
        cap = Sresult[0]
        existing_seats = set()
        sql_existing_seats = "SELECT Seat_No FROM passenger_details WHERE Fl_No = %s and Date=%s"
        random_seat.execute(sql_existing_seats, data)
        existing_seat_results = random_seat.fetchall()
        for existing_seat in existing_seat_results:
            existing_seats.add(existing_seat[0])
        while True:
            seat = str(random.randint(0, cap))
            if seat not in existing_seats:
                break
        print("Seat:", seat)
        text3.config(state='normal')
        text3.delete(0, END)  
        text3.insert(END, seat)
        text3.config(state='disabled')

    Amt=mysqlrs.cursor()
    sql="select Expense from flight_details where Fl_No=%s and Date=%s"
    data=(fld,date1_format)
    Amt.execute(sql,data)
    Aresult=Amt.fetchone()
    if Aresult:
        amt=Aresult[0]
        print("Amt:", amt)
        text6.config(state='normal')
        text6.delete(0, END)  
        text6.insert(END, amt)
        text6.config(state='disabled')

    Vs=mysqlrs.cursor()
    sql="select Vacant_seats from flight_details where Fl_No=%s and Date=%s"
    data=(fld,date1_format)
    Vs.execute(sql,data)
    Vresult=Vs.fetchone()
    if Vresult:
        vseat=Vresult[0]
        if vseat <= 15:
            print("V_Seat:", "W")
            text7.config(state='normal')
            text7.delete(0, END)  
            text7.insert(END, "W")
            text7.config(state='disabled')
        else:
            print("V_Seat:", "C")
            text7.config(state='normal')
            text7.delete(0, END)  
            text7.insert(END, "C")
            text7.config(state='disabled')

    Uvs=mysqlrs.cursor()
    sql="UPDATE flight_details SET Vacant_seats = Vacant_seats - 1 WHERE Fl_No = %s AND Date = %s"
    data=(fld,date1_format)
    Uvs.execute(sql,data)
    print("Vacant Seat Decremented")
    mysqlrs.commit()

def Pg_det():
    global pnr,fld,seat_no,dp_place,arv_place,name,age,sex,addr,Ph_no,amount,status,date1

    mysqlpg=mysql.connector.connect(
        host="localhost",user="root",passwd="",database="Airline_reservation"
    )
    pgd=mysqlpg.cursor()
    fld=text2.get()
    dp_place=text4.get()
    arv_place=text5.get()
    name=text8.get()
    age=text9.get()
    sex=text10.get()
    addr=text11.get()
    Ph_no=text12.get()
    date1=text13.get()
    date1_format = datetime.strptime(date1, '%d-%m-%Y').strftime('%Y-%m-%d')
    pnr = text1.get()  # Get PNR from text1
    seat_no = text3.get()  # Get Seat_No from text3
    amount = text6.get()  # Get Amount from text6
    status = text7.get()

    sql="insert into passenger_details (PNR,Fl_No,Seat_No,Dp_place,Ar_place,Amount,Status,Name,age,Sex,Address,Ph_No,Date) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    data=(pnr, fld, seat_no, dp_place, arv_place, amount, status, name, age, sex, addr, Ph_no, date1_format)
    pgd.execute(sql,data)
    mysqlpg.commit()
    print("Data saved")
    text1.delete(0,END)
    text2.delete(0,END)
    text3.delete(0,END)
    text4.delete(0,END)
    text5.delete(0,END)
    text6.delete(0,END)
    text7.delete(0,END)
    text8.delete(0,END)
    text9.delete(0,END)
    text10.delete(0,END)
    text11.delete(0,END)
    text12.delete(0,END)
    text13.delete(0,END)
    mysqlpg.close()
    messagebox.showinfo("Skywishper","New Passenger Added")

def Clear():
    text1.delete(0,END)
    text2.delete(0,END)
    text3.delete(0,END)
    text4.delete(0,END)
    text5.delete(0,END)
    text6.delete(0,END)
    text7.delete(0,END)
    text8.delete(0,END)
    text9.delete(0,END)
    text10.delete(0,END)
    text11.delete(0,END)
    text12.delete(0,END)
    text13.delete(0,END)

def Passenger_details():#part of New2
    global lab_pg, btne3, text1, text2, text3, text4, text5, text6, text7, text8, text9, text10, text11, text12, text13, Flg_No, Capacity_oc


    def Back4():
        lab_pg.destroy()
        btne3.destroy()
        text1.destroy()
        text2.destroy()
        text3.destroy()
        text4.destroy()
        text5.destroy()
        text6.destroy()
        text7.destroy()
        text8.destroy()
        text9.destroy()
        text10.destroy()
        text11.destroy()
        text12.destroy()
        text13.destroy()
        New2()

    lab_bkg.destroy()
    labnew2.destroy()
    btncf.destroy()
    btnbk.destroy()
    btnct.destroy()
    btne2.destroy()
    btngt.destroy()
    #pg_det=tk
    pgde=tk
    pg_image=Image.open("C:\\Users\\KAVYA\\OneDrive\\Pictures\\Saved Pictures\\Book_Tickect_Bg1.jpg")
    resize6=pg_image.resize((1500,800))
    tk.pg_img=ImageTk.PhotoImage(resize6)
    lab_pg=Label(pgde,image=tk.pg_img)
    lab_pg.pg_image=tk.pg_img
    lab_pg.pack()
    
    Labe1=Label(pgde,text="SkyWispher International Airlines",font=('Georgia',25,'bold'),fg="black",bg="#ffffff")
    Labe1.place(x=270,y=30)

    text1=Entry(pgde,width=30,font=('Berlin Sans FB',15),bg="#ffffff")
    text1.place(x=500,y=120,width=180,height=38)
    rand()

    La1=Label(pgde,text="PNR",font=('Georgia',15),padx=20,pady=5,bg="#ffffff")
    La1.place(x=300,y=120,width=150)
    
    text2=Entry(pgde,width=30,font=('Berlin Sans FB',15),bg="#ffffff")
    text2.place(x=500,y=180,width=180,height=38)

    La2=Label(pgde,text="Flight_No",font=('Georgia',15),padx=20,pady=5,bg="#ffffff")
    La2.place(x=300,y=180,width=150)

    text3=Entry(pgde,width=30,font=('Berlin Sans FB',15),bg="#ffffff")
    text3.place(x=500,y=240,width=180,height=38)

    btn_seat=Button(pgde,text="Click",font=('Georgia',15,'bold'),padx=20,pady=5,bg="#1B1464",fg="#ffffff",command=rand_seat)
    btn_seat.place(x=750,y=240,width=100,height=35)


    La3=Label(pgde,text="Seat_NO",font=('Georgia',15),padx=20,pady=5,bg="#ffffff")
    La3.place(x=300,y=240,width=150)

    text4=Entry(pgde,width=30,font=('Berlin Sans FB',15),bg="#ffffff")
    text4.place(x=500,y=300,width=180,height=38)

    La4=Label(pgde,text="Start_place",font=('Georgia',15),padx=20,pady=5,bg="#ffffff")
    La4.place(x=300,y=300,width=150)

    text5=Entry(pgde,width=30,font=('Berlin Sans FB',15),bg="#ffffff")
    text5.place(x=500,y=360,width=180,height=38)

    La5=Label(pgde,text="Depature_place",font=('Georgia',15),padx=20,pady=5,bg="#ffffff")
    La5.place(x=300,y=360,width=150)

    text6=Entry(pgde,width=30,font=('Berlin Sans FB',15),bg="#ffffff")
    #text6=Entry(pgde,width=30,font=('Berlin Sans FB',15),bg="#ffffff")
    text6.place(x=500,y=420,width=180,height=38)

    La6=Label(pgde,text="Amount",font=('Georgia',15),padx=20,pady=5,bg="#ffffff")
    La6.place(x=300,y=420,width=150)

    text7=Entry(pgde,width=30,font=('Berlin Sans FB',15),bg="#ffffff")
    #text7=Entry(pgde,width=30,font=('Berlin Sans FB',15),bg="#ffffff")
    text7.place(x=500,y=480,width=180,height=38)

    La7=Label(pgde,text="Status",font=('Georgia',15),padx=20,pady=5,bg="#ffffff")
    La7.place(x=300,y=480,width=150)

    text8=Entry(pgde,width=30,font=('Berlin Sans FB',15),bg="#ffffff")
    text8.place(x=500,y=540,width=180,height=38)

    La8=Label(pgde,text="Name",font=('Georgia',15),padx=20,pady=5,bg="#ffffff")
    La8.place(x=300,y=540,width=150)

    text9=Entry(pgde,width=30,font=('Berlin Sans FB',15),bg="#ffffff")
    text9.place(x=500,y=600,width=180,height=38)

    La9=Label(pgde,text="Age",font=('Georgia',15),padx=20,pady=5,bg="#ffffff")
    La9.place(x=300,y=600,width=150)

    text10=Entry(pgde,width=30,font=('Berlin Sans FB',15),bg="#ffffff")
    text10.place(x=500,y=660,width=180,height=38)

    La10=Label(pgde,text="Sex",font=('Georgia',15),padx=20,pady=5,bg="#ffffff")
    La10.place(x=300,y=660,width=150)

    text11=Entry(pgde,width=30,font=('Berlin Sans FB',15),bg="#ffffff")
    text11.place(x=500,y=720,width=180,height=38)

    La11=Label(pgde,text="Address",font=('Georgia',15),padx=20,pady=5,bg="#ffffff")
    La11.place(x=300,y=720,width=150)

    text12=Entry(pgde,width=30,font=('Berlin Sans FB',15),bg="#ffffff")
    text12.place(x=1000,y=120,width=180,height=38)

    La12=Label(pgde,text="Ph_No",font=('Georgia',15),padx=20,pady=5,bg="#ffffff")
    La12.place(x=800,y=120,width=150)

    text13=Entry(pgde,width=30,font=('Berlin Sans FB',15),bg="#ffffff")
    text13.place(x=1300,y=30,width=180,height=38)

    La13=Label(pgde,text="Date",font=('Georgia',15),padx=20,pady=5,bg="#ffffff")
    La13.place(x=1100,y=30,width=150)

    btnet1=Button(pgde,text="Enter",font=('Georgia',15,'bold'),padx=20,pady=5,bg="#1B1464",fg="#ffffff",command=Pg_det)
    btnet1.place(x=800,y=680,width=150)

    btncl1=Button(pgde,text="Clear",font=('Georgia',15,'bold'),padx=20,pady=5,bg="#1B1464",fg="#ffffff",command=Clear)
    btncl1.place(x=1000,y=680,width=150)

    pdLab=Label(pgde,text="* DD-MM-YYYY",font=('Georgia',10),padx=20,pady=5,bg="#ffffff")
    pdLab.place(x=1300,y=80)


    btne3=Button(pgde,text="Back",font=('Georgia',15,'bold'),padx=20,pady=5,bg="#1B1464",fg="#ffffff",command=Back4)
    btne3.place(x=1200,y=680,width=150)


def Select_flight():#Sub function of Check_flight

    frame3 = Frame(tk)
    frame3.grid(row=0,column=0,padx=130,pady=400)

    headers = ["Fl_No","Aircraft","Capacity","St_place","Dp_place","Dp_time","Ar_time","Expense","Vacant_seats","Date"]
    for i, header in enumerate(headers):
        headers_label = Label(frame3, text=header, font=("times", 18, "bold"),bg="#ced6e0")
        headers_label.grid(row=0, column=i, padx=10, pady=10)

    mysql_connec = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="Airline_reservation"
    )

    mycursors = mysql_connec.cursor()
    Fl_Date=txt.get()
    Start_place=txtst.get()
    Dep_place=txtdp.get()
    date_format=datetime.strptime(Fl_Date, '%d-%m-%Y').strftime('%Y-%m-%d')
    sql="select * from flight_details where Date=%s and St_place=%s and Dp_place=%s"

    mycursors.execute(sql,(date_format,Start_place,Dep_place))
    result = mycursors.fetchall()

    txt.delete(0,END)
    txtst.delete(0,END)
    txtdp.delete(0,END)

    Seat=False
    for i, row in enumerate(result, start=1):
        for j, item in enumerate(row):
            label5 = Label(frame3, text=item,font=("times", 15))
            label5.grid(row=i, column=j, padx=5, pady=5)

        if row[-2]!=0:
            Seat=True
    if not Seat:
        messagebox.showinfo("No Vacant Seats", "Currently fully occupied.")
    if not result:
        messagebox.showerror("No Results", "No flights found for the given route.")
        return
    mysql_connec.close()

def Check_flight():
    global ckf, Cf_labnew, txt, Labcf, txtst, Labst, txtdp, Labdp, btnet1, btne4

    def Back5():
        for widget in tk.winfo_children():
                    widget.destroy()
        New2()

    lab_bkg.destroy()
    labnew2.destroy()
    btncf.destroy()
    btnbk.destroy()
    btnct.destroy()
    btne2.destroy()
    btngt.destroy()
    ckf=tk
    Cf_lab=Label(ckf,bg="#ffb8b8")
    Cf_lab.place(x=0,y=0,width=1500,height=1000)
    Cf_labnew=Label(ckf,text="SkyWispher International Airlines",font=('Georgia',40,'bold'),fg="#192a56")
    Cf_labnew.place(x=270,y=30)

    txt=Entry(ckf,width=30,font=('Berlin Sans FB',15),bg="#ffffff")
    txt.place(x=330,y=130,width=180,height=38)
    Labcf=Label(ckf,text="Date",font=('Georgia',15),padx=20,pady=5,bg="#ffffff")
    Labcf.place(x=130,y=130,width=150)

    Labms=Label(ckf,text="* DD-MM-YYYY",font=('Georgia',10),padx=20,pady=5,bg="#ffb8b8")
    Labms.place(x=530,y=130)

    txtst=Entry(ckf,width=30,font=('Berlin Sans FB',15),bg="#ffffff")
    txtst.place(x=330,y=190,width=180,height=38)
    Labst=Label(ckf,text="From",font=('Georgia',15),padx=20,pady=5,bg="#ffffff")
    Labst.place(x=130,y=190,width=150)

    txtdp=Entry(ckf,width=30,font=('Berlin Sans FB',15),bg="#ffffff")
    txtdp.place(x=330,y=250,width=180,height=38)
    Labdp=Label(ckf,text="To",font=('Georgia',15),padx=20,pady=5,bg="#ffffff")
    Labdp.place(x=130,y=250,width=150)

    btnet1=Button(ckf,text="Enter",font=('Georgia',15,'bold'),padx=20,pady=5,bg="#1B1464",fg="#ffffff",command=Select_flight)
    btnet1.place(x=250,y=310,width=150)
    btne4=Button(ckf,text="Back",font=('Georgia',15,'bold'),padx=20,pady=5,bg="#1B1464",fg="#ffffff",command=Back5)
    btne4.place(x=1300,y=700,width=150)
    Labnt=Label(ckf,text="* Make a note of Flight Number for future use",font=('Georgia',15),padx=20,pady=5,bg="#ffb8b8")
    Labnt.place(x=450,y=700)


def New2():
    global lab_bkg, labnew2, btncf, btnbk, btnct, btne2, btngt
    def Back3():
        lab_bkg.destroy()
        labnew2.destroy()
        btncf.destroy()
        btnbk.destroy()
        btnct.destroy()
        btne2.destroy()
        btngt.destroy()
        Landing_pg()

    label1.destroy()
    label2.destroy()
    Lab.destroy()
    frame.destroy()
    frame2.destroy()
    new2=tk
    try:
        bkg=Image.open("C:\\Users\\KAVYA\\OneDrive\\Pictures\\Saved Pictures\\bg8.jpg")
        resize5=bkg.resize((1500,1000))
        tk.bkg_img=ImageTk.PhotoImage(resize5)
        lab_bkg=Label(new2,image=tk.bkg_img)
        lab_bkg.bkg=tk.bkg_img
        # lab_bkg.place(x=0,y=0)
        lab_bkg.pack()
    except Exception as e:
        print("Error loading background image:", e)

    labnew2=Label(new2,text="SkyWispher International Airlines",font=('Georgia',40,'bold'),fg="#1B1464")
    labnew2.place(x=270,y=30)
    btncf=Button(new2,text="Check Flight",font=('Georgia',15,'bold'),padx=20,pady=5,fg="#1B1464",command=Check_flight)#,bg="#48dbfb"
    btncf.place(x=1000,y=300,width=250)
    btnbk=Button(new2,text="Book Ticket",font=('Georgia',15,'bold'),padx=20,pady=5,fg="#1B1464",command=Passenger_details)#,command=lambda:(Pg_details,Capacity_oc))#lambda:[(rand(),Pg_details)])
    btnbk.place(x=1000,y=370,width=250)
    btnct=Button(new2,text="Cancel Ticket",font=('Georgia',15,'bold'),padx=20,pady=5,fg="#1B1464",command=Cancel_ticket)
    btnct.place(x=1000,y=440,width=250)
    btngt=Button(new2,text="Get Ticket",font=('Georgia',15,'bold'),padx=20,pady=5,fg="#1B1464",command=Get_ticket)
    btngt.place(x=1000,y=510,width=250)
    btne2=Button(new2,text="Landing_page",font=('Georgia',15,'bold'),padx=20,pady=5,fg="white",bg="#1B1464",command=Back3)
    btne2.place(x=1300,y=700,width=170)

#main prg
def Landing_pg():
    global label1, label2, Lab, frame, frame2

    image=Image.open("C:\\Users\\KAVYA\\OneDrive\\Pictures\\Saved Pictures\\bg12.jpg")
    resize1 = image.resize((1500, 1000))
    img=ImageTk.PhotoImage(resize1)
    label1=Label(image=img)
    label1.image=img
    label1.pack()

    image2=Image.open("C:\\Users\\KAVYA\\OneDrive\\Pictures\\Saved Pictures\\airplane_logo6.jpg")
    resize2 = image2.resize((50, 50))
    img2=ImageTk.PhotoImage(resize2)
    label2=Label(image=img2)
    label2.image=img2
    label2.place(x=250,y=20)

    Lab=Label(tk,text="SkyWispher",font=('Georgia',30,'bold'),fg="#1B1464",bg="#ffffff")
    Lab.place(x=10,y=20)

    frame=Frame(tk,highlightbackground="black",highlightthickness=2,bg="#ffffff")
    frame.place(x=420, y=270, width=300, height=300)
    logo=Image.open("C:\\Users\\KAVYA\\OneDrive\\Pictures\\Saved Pictures\\admin icon5.jpg.png") 
    resize3=logo.resize((300,300))
    tk.log=ImageTk.PhotoImage(resize3)
    label3=Label(frame,image=tk.log)
    label3.pack(expand=True)
    #label3.place(x=0,y=0,relwidth=1, relheight=1)
    btnad=Button(frame,text="Admin",font=('Georgia',15,'bold'),padx=20,pady=5,bg="#341f97",fg="white",command=New)
    btnad.place(x=85,y=240)

    frame2=Frame(tk,highlightbackground="black",highlightthickness=2,bg="#ffffff")
    frame2.place(x=820, y=270, width=300, height=300)
    logo2=Image.open("c:\\Users\\KAVYA\\OneDrive\\Pictures\\Screenshots\\user icon3.png")
    resize4=logo2.resize((300,300))
    tk.log2=ImageTk.PhotoImage(resize4)
    label4=Label(frame2,image=tk.log2)
    label4.pack(expand=True)
    #label4.place(x=0,y=0,relwidth=1, relheight=1)
    btnus=Button(frame2,text="User",font=('Georgia',15,'bold'),padx=20,pady=5,bg="#341f97",fg="white",command=New2)
    btnus.place(x=92,y=240)

Landing_pg()

tk.mainloop()