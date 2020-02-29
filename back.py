import sqlite3

def connect():
	conn=sqlite3.connect("hotel.db")
	cur=conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTs hotel (id INTEGER PRIMARY KEY , name TEXT , address TEXT , phone_number INTEGER , no_of_days INTEGER , room_type TEXT , total INTEGER)")
	conn.commit()
	conn.close()

def calculate(no_of_days,room_type):
	if room_type==("normal" or "NORMAL"):
		total=int(no_of_days)*1500
		return total
	elif room_type==("king" or "KING"):
		total=int(no_of_days)*2000
		return total
	elif room_type==("deluxe" or "DELUXE"):
		total=int(no_of_days)*3000
		return total

def insert(name,address,phone_number,no_of_days,room_type,total):
	conn=sqlite3.connect("hotel.db")
	cur=conn.cursor()
	cur.execute("INSERT INTO hotel VALUES (NULL,?,?,?,?,?,?)",(name,address,phone_number,no_of_days,room_type,calculate(no_of_days,room_type)))
	conn.commit()
	conn.close()
	view()

def view():
	conn=sqlite3.connect("hotel.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM hotel")
	row=cur.fetchall()
	conn.close()
	return row

def search(name="",address="",phone_number="",room_type="",no_of_days="",total=""):
	conn=sqlite3.connect("hotel.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM hotel WHERE name=? or address=? or phone_number=? or room_type=? or no_of_days=? or total=?",(name,address,phone_number,room_type,no_of_days,total))
	row=cur.fetchall()
	conn.close()
	return row

def delete(id):
	conn=sqlite3.connect("hotel.db")
	cur=conn.cursor()
	cur.execute("DELETE FROM hotel WHERE id=?",(id,))
	conn.commit()
	conn.close()

def update(id,name,address,phone_number,room_type,no_of_days,total):
	conn=sqlite3.connect("hotel.db")
	cur=conn.cursor()
	cur.execute("UPDATE hotel SET name=? , address=? ,phone_number=? ,room_type=? , no_of_days=? ,total=? WHERE id=?",(name,address,phone_number,room_type,no_of_days,calculate(no_of_days,room_type),id) )
	conn.commit()
	conn.close()



connect()