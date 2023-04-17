from tkinter import *
import mysql.connector
import random
import re as reg
from datetime import datetime
from tkinter import messagebox as mbx
datez = datetime.utcnow().strftime('%Y%m%d%H%M%S' )

#********Root Object with Tk class && Window Geometry********
root = Tk()
root.geometry('770x780')
root.resizable(False,False)
#**********Tk Object*******


srchpar=[]

templis=[]

ledgersum=[]

srchbydate=[]

def ledgertotal():
	global ledgersum
	connecting()
	mycursor=mydb.cursor()
	mycursor.execute('USE billing')
	mydb.commit()
	
	mycursor.execute('SHOW TABLES')
	for i in mycursor:
		ic = str(i)[13:-4]
		templis.append(ic)
	mydb.commit()
	for j in templis:
		print(j)
		mycursor.execute('SELECT total FROM {} WHERE particulars="Total" '.format(j))
		for k in mycursor:
			ledgersum.append(list(k))
	ledgersum=sum(ledgersum,[])
	mbx.showinfo('Total Ledger',f'Total Ledger Sum is {sum(ledgersum)} rs')
				
def searchbydate():
	global templis
	dcc=srdt.get()
	connecting()
	mycursor=mydb.cursor()
	mycursor.execute('USE billing')
	mycursor.execute('SHOW TABLES')
	for i in mycursor:
		ic = str(i)[13:-4]
		templis.append(ic)
	for j in templis:
		print(j)
		mycursor.execute('SELECT * FROM {} WHERE dte like "%{}%" '.format(j,dcc))
		for k in mycursor:
			print(k)

def srchdteprompt():
	srchdte=Tk()
	
	global srdt
	
	framedte=Frame(srchdte)
	framedte.grid(row=0,column=0)
	
	Label(framedte,text='Fomat = YYY-MM-DD',font='bold',fg='red',bg='wheat').grid(row=1,column=0)
	
	srdt=Entry(framedte,font='bold')
	srdt.grid(row=2,column=1)
	
	dtbt = Button(framedte,text='Search',font='bold',command=searchbydate)
	dtbt.grid(row=2,column=2)
	
	srchdte.mainloop()	
	
def billshown():
	
	print(type(srchpar[0][2]))
	thebill=Tk()
	
	basefrm=Frame(thebill)
	basefrm.grid(row=0,column=0,sticky='we')
	
	frm=Frame(thebill)
	frm.grid(row=1,column=0,sticky='we')
	
	frm2=Frame(thebill)
	frm2.grid(row=2,column=0,sticky='we')
	
	Label(basefrm,text='Customer Name :: {}'.format(srchpar[(len(srchpar)-1)][5]),font='bold',bg='green').grid(row=0,column=0,sticky='we')
	
	dp=Entry(frm,font='bold',bg='yellow')
	dp.insert(0,'Date')
	dp.grid(row=1,column=1,sticky='we')
	
	idp=Entry(frm,font='bold',bg='yellow')
	idp.insert(0,'Id')
	idp.grid(row=1,column=2,sticky='we')
	
	pp=Entry(frm,font='bold',bg='yellow')
	pp.insert(0,'Particulars')
	pp.grid(row=1,column=3,sticky='we')
	
	qp=Entry(frm,font='bold',bg='yellow')
	qp.insert(0,'Quantity')
	qp.grid(row=1,column=4,sticky='we')
	
	rp=Entry(frm,font='bold',bg='yellow')
	rp.insert(0,'Rupees')
	rp.grid(row=1,column=5,sticky='we')
	
	tp=Entry(frm,font='bold',bg='yellow')
	tp.insert(0,'Total')
	tp.grid(row=1,column=6,sticky='we')
	
	for i in range(len(srchpar)):
		
		billdate=Entry(frm2,font='bold')
		billdate.insert(0,srchpar[i][0])
		billdate.grid(row=2+i,column=1,sticky='we')
		
		enid=Entry(frm2,font='bold')
		enid.insert(0,srchpar[i][1])
		enid.grid(row=2+i,column=2,sticky='we')
		
		billpar=Entry(frm2,font='bold')
		billpar.insert(0,srchpar[i][2])
		billpar.grid(row=2+i,column=3,sticky='we')
		
		billqn=Entry(frm2,font='bold')
		billqn.insert(0,srchpar[i][3])
		billqn.grid(row=2+i,column=4,sticky='we')
		
		billrs=Entry(frm2,font='bold')
		billrs.insert(0,srchpar[i][4])
		billrs.grid(row=2+i,column=5,sticky='we')
		
		billtot=Entry(frm2,font='bold')
		billtot.insert(0,srchpar[i][6])
		billtot.grid(row=len(srchpar)+1,column=6,sticky='we')
		
	thebill.mainloop()
	
	

def showbill():

	scr=srchcus.get()
	scn=srchnum.get()
	concat=scr+scn
	print(concat)
	connecting()
	searchdata(concat)

def searchabill():

	search=Tk()
	search.geometry('350x150')
	
	global srchcus,srchnum
	Label(search,text='Enter Customer Name',font='bold').grid(row=0,column=0)
	
	srchcus=Entry(search,font='bold 20')
	srchcus.grid(row=1,column=0)
	
	Label(search,text='Enter Customer Number',font='bold').grid(row=2,column=0)
	
	srchnum=Entry(search,font='bold 20')
	srchnum.grid(row=3,column=0)
	
	srchbut=Button(search,text='Search',command= showbill)
	srchbut.grid(row=4,column=0)
	
	search.mainloop()
	
	

menubar=Menu(root,bg='grey',fg='white')
menubar.add_command(label='Search-a-Bill',font='bold',command=searchabill)
menubar.add_command(label='Search-by-Date',font='bold',command=srchdteprompt)
menubar.add_command(label='Ledgers-Total',font='bold',command=ledgertotal)
menubar.add_command(label='Exit',font='bold',command=root.quit)

#*********Receipt Window*********

def newwindow():
	
	receipt=Tk()
	receipt.geometry('750x600')
	frame4=Frame(receipt,highlightbackground='black',highlightthickness=2,bg='grey')
	frame4.grid(row=0,column=0,sticky='we')
	
	frame5=Frame(receipt,highlightbackground='black',highlightthickness=2,bg='red')
	frame5.grid(row=1,column=0,sticky='we')
	
	frame6=Frame(receipt,highlightbackground='black',highlightthickness=2,bg='grey')
	frame6.grid(row=2,column=0,sticky='we')
	
	Label(frame4,text='From :',font='bold 15',bg='grey').grid(row=0,column=0,sticky='w')
	Label(frame4,text='ShopNameHere....',font='bold 15',bg='white',fg='black').grid(row=1,column=0,sticky='we')
	Label(frame4,text='Addr :: 44-1 new vasanthnagar hosur-635109 \n krishnagiri district Tamilnadu India',bg='wheat',font='bold 15').grid(row=1,column=4,padx=45,sticky='e')
	
	print(f'label{cr}')
	Label(frame4,text='To : ',font='bold 15',bg='grey').grid(row=2,column=0,sticky='w')
	Label(frame4,text=cr+' '+cn,font='bold 15',bg='lightgreen').grid(row=3,column=0,sticky='we')
	
	sl=Label(frame5,text='Sl',font='bold')
	sl.grid(row=0,column=0,sticky='we')
	
	rpr=Entry(frame5,font='bold')
	rpr.insert(0,'Particulars')
	rpr.grid(row=0,column=1,sticky='we')
	
	rqn=Entry(frame5,font='bold')
	rqn.insert(0,'Quantity')
	rqn.grid(row=0,column=2,sticky='we')
	
	rrs=Entry(frame5,font='bold')
	rrs.insert(0,'Rupees')
	rrs.grid(row=0,column=3,sticky='we')
	
	rtt=Entry(frame5,font='bold')
	rtt.insert(0,'Total')
	rtt.grid(row=0,column=4,sticky='we')
	
	tst=0
	for i in data:
	
		ii=Label(frame6,text=str(i)+'.',font='bold 10',bg='black',fg='white')
		ii.grid(row=i,column=0,sticky='we')
		
		print(f'totals{pardata}')
		print(f'result{pardata.get(i)}')
		ipr=Entry(frame6,font='bold')
		ipr.insert(0,pardata.get(i))
		ipr.grid(row=i,column=1,sticky='we')
		
		iqn=Entry(frame6,font='bold')
		iqn.insert(0,qndata.get(i))
		iqn.grid(row=i,column=2,sticky='we')
		
		irs=Entry(frame6,font='bold')
		irs.insert(0,data.get(i))
		irs.grid(row=i,column=3,sticky='we')
		
		
	itl=Entry(frame6,font='bold')
	itl.insert(0,c)
	itl.grid(row=16,column=4,sticky='we')
		
	
	receipt.mainloop()
	
#********End of Receipt Window*******

#********Frames management section**********

frame=Frame(root,highlightbackground='black',highlightthickness=2,bg='grey')
frame.grid(row=0,column=0,sticky='w')

frame2=Frame(root)
frame2.grid(row=1,column=0,sticky='w')

frame3=Frame(root)
frame3.grid(sticky='w')

#*********End of frames section**************

#label for total button initiated here formally to avoid -not defined- error from clear() function
ttdis=Label()
crt=''
#***************MySqlDataManagementSection*******************

#creates connection to mysql database
def connecting():
	global mydb
	mydb=mysql.connector.connect(host='localhost',user='root',password=None)
	print('connection established')

#query for creating a new database if not exits	
def createdatabase():
	global mycursor
	mycursor=mydb.cursor()
	mycursor.execute('CREATE DATABASE IF NOT EXISTS {}'.format('billing'))
	mydb.commit()

#query to use the database created and create a table for entries
def usedata():
	mycursor=mydb.cursor()
	mycursor.execute('USE {}'.format('billing'))
	mydb.commit()
	print(f'special{crt}')
	mycursor.execute('CREATE TABLE IF NOT EXISTS {} ({} DATETIME,{} INT DEFAULT 0,{} VARCHAR(50) DEFAULT "Total",{} FLOAT DEFAULT 0 ,{} FLOAT DEFAULT 0,{} VARCHAR(60) DEFAULT "nullish",{} FLOAT DEFAULT 0)'.format(crt,'dte','id','particulars','quantity','rupees','customer','total'))
	mydb.commit()

def searchdata(concat):
	mycursor=mydb.cursor()
	mycursor.execute('USE {}'.format('billing'))
	
	if concat:
		try:
			mycursor.execute('SELECT * FROM {}'.format(concat))
			for i in mycursor:
				srchpar.append(i)
			billshown()
		except Exception as e:
			print(e)
			mbx.showinfo('no data','No Such Customer Details Exists')
	else:
		mbx.showinfo('details empty','Provide Customer Name and Number')
	
	
	
#query to insert data
def insertdata(cl,pr,qn,rs,crn,tt):
	print(cl,pr,qn,rs,crn,tt)
	mycursor.execute('insert into {} (dte,id,particulars,quantity,rupees,customer,total) values({},{},"{}",{},{},"{}",{}) '.format(crt,datez,cl,pr,qn,rs,crn,tt))
		
	mydb.commit()
	mydb.close()

#query to delete data
def deleterow(rmrn):
	connecting()
	mycursor=mydb.cursor()
	mycursor.execute('USE {}'.format('billing'))
	mydb.commit()
	print(f'specialrmrn{rmrn}')
	if rmrn:
		mycursor.execute('DELETE FROM {} WHERE id = {}'.format(crt,rmrn))
		mydb.commit()
	print(f'special{cl}')
	if  data :
		pass
	else:
		mycursor.execute('DELETE FROM {} WHERE id="{}"'.format(crt,cl))
		mydb.commit()
		print('Total Row Deleted Successfully')
	print('deleted entry successfully')

#main function carries mysql and above query function as a main function	
def main(cl,pr,qn,rs,crn,tt):
	connecting()
	createdatabase()
	usedata()
	insertdata(cl,pr,qn,rs,crn,tt)
	
#*****************End of MySqlData Section********************

#****************Begin of SourceCodeManagement*******************

#*************Variables storing data section**************** 

#variable acts as a counter in addfield function to add row and columns when clicked 
r=0
#variable kept as ref for variable c
v=0
#variable carries instance total of an entry of all rows
c=0
#variable carries unique id for each row entry as ref to push in mysql database  
cl=0
#variable carries a special id for total to delete from database if necessary
rmrn=0
#variable carries customer name
cr=''

#**************End of variables data section***************


data={}
qndata={}
pardata={}
uniqueids={}

refcref=[]
buttonsref=[]
rupeesref=[]
quantityref=[]
particularsref=[]

	
def clearofclear():
			global refcref, buttonsref,rupeesref,quantityref,particularsref,r,v,c,cl,rmrn,uniqueids,data,qndata,pardata,ttdis
			
			data={}
			qndata={}
			pardata={}
			
			print(f'special{data}')
			print(f'special{qndata}')
			
			r=0
			v=0
			c=0
			rmrn=0

def clearofcleared():	
			uniqueids={}
			
			refcref=[]
			buttonsref=[]
			rupeesref=[]
			quantityref=[]
			particularsref=[]
			
			ttdis.config(text=c)
			cl=0
			Label(frame2,).grid(row=0,column=0)
			addfield.config(state='active')

def clear():
	
	if data or r :
		warnclear=mbx.askokcancel('Confirm','Clear All ?')
		if warnclear:		
			clearofclear()
			
			if buttonsref:
				for i in range(len(buttonsref)):
					refcref[i].destroy()
					buttonsref[i].destroy()
					rupeesref[i].destroy()
					quantityref[i].destroy()
					particularsref[i].destroy()
				
					if uniqueids:
						print(i)
						deleterow(uniqueids.get(i))
			
			clearofcleared()

	else:
		mbx.showinfo('null','Nothing to clear')
		
def addcustomer():
	if data :
		clearofclear()
		if buttonsref:
				for i in range(len(buttonsref)):
					refcref[i].destroy()
					buttonsref[i].destroy()
					rupeesref[i].destroy()
					quantityref[i].destroy()
					particularsref[i].destroy()
		clearofcleared()
	else:
		mbx.showinfo('null','Nothing to Add Already a New Ledger \n \n Add Field and Fill Entries')
			
def remove(rn):
		
	warn=mbx.askokcancel('Confirm','Remove ?')
	print(warn)
	if warn == True:
		global rmrn
		
		rmrn=uniqueids.get(rn)
		
		print(data,'\n',qndata,'\n',pardata)
		print(buttonsref[rn])
		
		refcref[rn].destroy()
		buttonsref[rn].destroy()
		rupeesref[rn].destroy()
		particularsref[rn].destroy()
		quantityref[rn].destroy()
		
		del data[rn]
		del qndata[rn]
		del pardata[rn]
		deleterow(rmrn)
		print(data,"\n",qndata,'\n',pardata)
		
		calculate.config(state='active')

	if  rn <=13:
		addfield.config(state='active')
	
		
def store(l):
	
	global rs,cl,cn,crt,cr
	
	cn=customernum.get()
	cr=customername.get()
	print(f'regex{cr}')
	
	if cr and cn:
		rule=reg.compile('[~!,.?@#$%^&*()_+=|\}{]')
		validate1 = rule.search(cr)
		validate2=rule.search(cn)
		if validate1 or validate2:
			mbx.showwarning('regex error','Customer-Name or Customer-Number Should not contain any Special Characters')
		else:
			cnt=cn.replace(' ','')
			
			if cnt.isdigit() and len(cnt)==10:
			
				crt=(cr.replace(" ",""))+str(cnt)
				
				cl=str(random.randint(10,99))+str(l)
				
				pr = particularsref[l].get()
				rs = rupeesref[l].get()
				qn = quantityref[l].get()
				
				print(type(rs))
					
				if rs.isdigit() and qn.isdigit() :
					qndata.update({l:float(qn)})
					data.update({l:float(rs)})
					
					pardata.update({l:str(pr)})
					uniqueids.update({l:int(cl)})
					
					main(int(cl),pr,qn,rs,crn="***",tt=0)
					buttonsref[l].destroy()
					buttonsref[l]=Button(frame2,text='Remove'+str(l),command=lambda rn=l:remove(rn))
					buttonsref[l].grid(row=l,column=4)

				else:
					mbx.showwarning('Integer Error','Must be a Number and Fields should not be Empty')
			else:
				mbx.showinfo('number','Enter 10 Digit Customer Mobile number')
	else:
		mbx.showinfo('customer','Enter Both Customer Name and Number ')

	
def fields():
	global r,particulars,quantity,rupees,add
	
	refc=Label()
	
	particulars = Entry()
	
	quantity = Entry()
	
	rupees = Entry()
	
	add=Button()
	
	refcref.append(refc)
	particularsref.append(particulars)
	quantityref.append(quantity)
	rupeesref.append(rupees)
	buttonsref.append(add)
	
def references():
	addnewcus.config(state='disabled')
	calculate.config(state='active')
	global r,refc

	if r>=13:
		addfield.config(state='disabled')
	
	fields()
	
	refcref[r]=Label(frame2,text=str(r)+'.',font='bold')
	refcref[r].grid(row=r,column=0)

	particularsref[r]=Entry(frame2,font='bold')
	particularsref[r].grid(row=r,column=1)
	
	quantityref[r]=Entry(frame2,font='bold')
	quantityref[r].insert(0,0)
	quantityref[r].grid(row=r,column=2)
	
	rupeesref[r]=Entry(frame2,font='bold')
	rupeesref[r].insert(0,0)
	rupeesref[r].grid(row=r,column=3)
	
	buttonsref[r]=Button(frame2,text='Add To Entry'+ str(r),command=lambda l=r : store(l))
	buttonsref[r].grid(row=r,column=4)
	r+=1
	

def total():
	
	global cr,c,v,ttdis

	print(f'special{data}')
	print(f'special{qndata}')
	
	if data:
		for i in data:
			c=(data.get(i)*qndata.get(i))+v
			v=c
	
		main(cl=random.randint(10,999),pr='Total',qn=0,rs=0,crn=cr,tt=c)
		print('main',cl)
		calculate.config(state='disabled')
		addnewcus.config(state='active')
		newwindow()
		
	else:
		mbx.showinfo('Null Values','Entries are empty \n >Click Add To Entry<')
		
	
def headers():
	global customername,addfield,calculate,addnewcus,customernum
	
	Label(frame,text='Shop Name Here.... Billing Application',bg='white',font='bold 30').grid(row=1,column=0,columnspan=5,pady=5,sticky='wn')
	
	
	Label(frame,text='Addr :: 44-1 new vasanthnagar hosur-635109 krishnagiri district Tamilnadu',bg='wheat',font='bold 15').grid(row=2,column=0,columnspan=5,pady=10,sticky='n')
	
	
	
	customername=Entry(frame,bg='lightgreen',font='bold')
	customername.insert(0,'Customer name...')
	customername.grid(row=3,column=0,sticky='w')
	
	customernum=Entry(frame,bg='lightgreen',font='bold')
	customernum.insert(0,'Customer number...')
	customernum.grid(row=3,column=1,sticky='w')
	
	addnewcus=Button(frame,text='New Ledger',bg='green',font='bold',command= addcustomer)
	addnewcus.grid(row=3,column=2,sticky='w',padx=50)
		
	prts=Entry(frame,bg='red',font='bold',width=2)
	prts.insert(0,'Particulars')
	prts.grid(row=4,column=0,sticky='wes')
	
	qnty=Entry(frame,bg='red',font='bold')
	qnty.insert(0,'Quantity')
	qnty.grid(row=4,column=1,sticky='wes')
	
	rps=Entry(frame,bg='red',font='bold')
	rps.insert(0,'Rupees')
	rps.grid(row=4,column=2,sticky='wes')
	
	clearall=Button(frame,text='Clear All',bg='red',font='bold',command=clear)
	clearall.grid(row=4,column=3,sticky='wes',padx=15)
	
	addfield=Button(frame3,text='Add Field',bg='yellow',font='bold',command=references)
	addfield.bind('<Return>',references)
	addfield.grid(row=0,column=1,sticky='we')
	
	calculate=Button(frame3,text='Total',bg='green',font='bold',command=total)
	calculate.grid(row=0,column=2,sticky='we')
	
def clock():
	tm = datetime.utcnow()
	tms=tm.strftime("%H:%M:%S")
	tim=Label(frame,text=tms,bg='yellow',font='bold 0 roman',width=2,fg='red')
	tim.grid(row=3,column=3,sticky='wen')
	tim.after(1000,clock)
		
headers() 
clock()

root.config(menu=menubar)
root.mainloop()

#***************End of Billing SourceCode**********************
