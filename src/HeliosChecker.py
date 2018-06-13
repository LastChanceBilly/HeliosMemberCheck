import csv
from time import gmtime, strftime

class HeliosCheck:
	#Directory where the login time and reference DB are stored
	def __init__(self, LoginTimeDB, ReferenceDB):
		self.LoginTimeDB = LoginTimeDB
		self.ReferenceDB = ReferenceDB
	#To add the login time with the user information
	#Needs the user's email and customer code
	def AddLoginTime(self, email, code):
		#Open the database file
		with open(self.LoginTimeDB, "ab") as DatabaseFILE: 
			#Create write object and write the user's data
			DB_Writer = csv.writer(DatabaseFILE, delimiter=",", quotechar="'", quoting=csv.QUOTE_ALL)
			Data = [strftime("%Y/%m/%d [%H:%M:%S]", gmtime()), code, email]
			DB_Writer.writerow(Data)
	#To add the reference for the RFID code
	#Need RFID code, customer code, Picture directory
	def AddDatabaseReference(self, RFID_code, code, PicDir):
		#Open the database file
		with open(self.ReferenceDB, "ab") as DatabaseFILE:
			#Create write object and write the user's data
			DB_Writer = csv.writer(DatabaseFILE, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)
			Data = [RFID_code, code, PicDir]
			DB_Writer.writerow(Data)
	#Ass the name implies, it'll return the data on the row where the RFID code is stored on
	def LookForRFID(self, RFID_code):
		#Search result variables
		Row = 0
		#Open the database file 
		with open(self.ReferenceDB, "rf") as DatabaseFILE:
			DB_Reader = csv.reader(DatabaseFILE, delimiter=",", quotechar="'")
			for row in DB_Reader:
				if row[0] == RFID_code:
					#RFID code, cus_code, picture_dir
					return Row, row[1], row[2]
				Row += 1
			return 0  
	def LookForLoginTime(self, code):
		Row = 0
		with open(self.LoginTimeDB, "rf") as DatabaseFILE:
			DB_Reader = csv.reader(DatabaseFILE, delimiter=",", quotechar="'")
			result = " " 
			for row in DB_Reader:
				if row[1] == code:
					result = row[0]
		return result
