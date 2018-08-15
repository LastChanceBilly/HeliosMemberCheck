#!/usr/bin/python3

#Stripe's library used to interact with the main database

import stripe

#csv library to create login databases, as well as RFID code reference databases

#Socket library to get data from the ESP-32

#import sockets

#Import custom library

from HeliosChecker import *

INDEXER_SOURCE = "../html/js/indexer.js"

def create_script(name, status, membership, last_login, current_date, code, src, indexer_file_path):
	status_src = ' '
	if(status >= 0):
		status = '"color: green;",StatusN: "PASS"'
		status_src = '"./img/checkmarkgreen.jpg"'
	else:
		status = '"color: red;",StatusN: "CHECK"'
		status_src = '"./img/xmarkred.jpg"'
	script = 'var container = '+'{'+'userName : "{0}", Title : "{1}", Status : {2}, last_login : "{3}", current_date : "{4}", code :"{5}", src : "{6}", status_src : {7}'.format(name, membership, status, last_login, current_date, code, src, status_src)+'};'
	with open(indexer_file_path, "w") as indexer:
		indexer.write(script)

def main():
	#Initialize HeliosCheck object
	Checker = HeliosCheck("./DB/LTBD.csv", "./DB/RDB.csv")
	#Get the key from the key file
	key = ' '
	try:
		with open("./KeyFile.key", "r") as Key_File:
			key = Key_File.readline()
	except Exception as e:
		print (e)
	try:
		stripe.api_key = key[:len(key) - 1]
		pass
	except Exception as e:
		print (e)
		pass
	#Get customer
	customer = stripe.Customer.retrieve("cus_D0nTkXIS0gUJ9Z")
	Checker.AddLoginTime(customer.email, customer.id)
	#Test example: Display Content on webpage
	create_script(customer.description, customer.account_balance, "Member", Checker.LookForLoginTime("cus_D0nTkXIS0gUJ9Z"), "02/02/05", "cus_D0nTkXIS0gUJ9Z" ,"/msys32/home/lastc/projects/HeliosMemberCheck/backend/DB/imgs/jose.jpg", INDEXER_SOURCE)
if __name__ == "__main__":
	main()
def get_request():
	return 0
