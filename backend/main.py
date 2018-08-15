#!/usr/bin/python3
#Thiss code is the first version of Helios Member Check
#Writen by Jose Ricardo Monegro: josetecnom12@hotmail.com

#Stripe's library used to interact with the main database

import stripe

#csv library to create login databases, as well as RFID code reference databases

#Socket library to get data from the ESP-32

#import sockets

#Import custom library

from HeliosChecker import *

INDEXER_SOURCE = "../html/js/indexer.js"

def create_script(name, status, membership, last_login, current_date, code, src, indexer_file_path):
	if(status == "Active"):
		status = '"color: green;"'
	else:
		staus = '"color: red;"'
	script = 'var container = '+'{'+'userName : "{0}", Title : "{1}", Status : {2}, last_login : "{3}", current_date : "{4}", code :"{5}", src : "{6}"'.format(name, membership, status, last_login, current_date, code, src)+'};'
	with open(indexer_file_path, "w") as indexer:
		indexer.write(script)

def main():
	#Initialize HeliosCheck object
	Checker = HeliosCheck("./DB/LTBD.csv", "./DB/RDB.csv")
	#Get the key from the KeyFile
	key = ' '
	try:
		with open("./KeyFile.key", "rf") as Key_File:
			key = Key_File.readline()
	except Exception as e:
		print e
	try:
		stripe.api_key = key[:len(key) - 1]
		pass
	except Exception as e:
		print e
		pass
	#Get customer code
	customer = stripe.Customer.retrieve("cus_D0nTkXIS0gUJ9Z")
	Checker.AddLoginTime(customer.email, "cus_D0nTkXIS0gUJ9Z")
	#Test example: Display Content on webpage
	create_script(customer.description, "Active", "Member", Checker.LookForLoginTime("cus_D0nTkXIS0gUJ9Z"), "02/02/05", "cus_D0nTkXIS0gUJ9Z" ,"Jose.jpg", INDEXER_SOURCE)
if __name__ == "__main__":
	main()
def get_request():
	return 0
