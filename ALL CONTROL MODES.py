# -*- coding: utf-8 -*-
# Import required Python libraries
import time
import RPi.GPIO as GPIO
import pylirc

##from nanpy import Arduino
##from nanpy import serial_manager
##from time import sleep

# Use BCM GPIO references
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

### Set Arduino Uno pins as output and input
##Arduino.pinMode(12, Arduino.INPUT)
##Arduino.pinMode(11, Arduino.INPUT)
##Arduino.pinMode(8, Arduino.INPUT)


# Set Rspi LINE FOLLOWER pins as  input
GPIO.setup(14, GPIO.IN)
GPIO.setup(15, GPIO.IN)
GPIO.setup(18, GPIO.IN)

d=0
g=0
M=0

# Define GPIO to use on Pi
TRIG = 27
ECHO = 22

# Set Raspberry Pi pins as output and input
GPIO.setup(TRIG,GPIO.OUT)     # Trig
GPIO.setup(ECHO,GPIO.IN)      # Echo
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)


# Set PWM pins as output or input
GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)

p = GPIO.PWM(2,50)              
p.start(100)

P = GPIO.PWM(3,50)              
P.start(90)   

GPIO.output(9, GPIO.LOW)
GPIO.output(11, GPIO.LOW)
GPIO.output(8, GPIO.LOW)
GPIO.output(7, GPIO.LOW)

s = pylirc.init("myprogram")

GPIO.output(24, GPIO.LOW)          
m = GPIO.PWM(24,50)              
m.start(6.2)
time.sleep(0.5)
m.ChangeDutyCycle(6.2)
time.sleep(1)
m = GPIO.PWM(24,1)


GPIO.output(TRIG, False)                 #Set TRIG as LOW
##Waitng For Sensor To Settle
time.sleep(1)

while True:
	print "SELECT YOUR MODE"
	m = pylirc.nextcode()
	print m
	if (m == ['one']) :
		print "IR MODE is activated with feature of detecting obstacles"
		p = GPIO.PWM(2,50)              
		p.start(100)

		P = GPIO.PWM(3,50)              
		P.start(95)
		
		while True:
			#Obstacle Test
			GPIO.output(TRIG, False)                 #Set TRIG as LOW
			print "Waitng For Sensor To Settle"
			time.sleep(0.1)                            #Delay of 2 seconds

			GPIO.output(TRIG, True)                  #Set TRIG as HIGH
			time.sleep(0.00001)                      #Delay of 0.00001 seconds
			GPIO.output(TRIG, False)                 #Set TRIG as LOW

			while GPIO.input(ECHO)==0:               #Check whether the ECHO is LOW
				pulse_start = time.time()              #Saves the last known time of LOW pulse

			while GPIO.input(ECHO)==1:               #Check whether the ECHO is HIGH
				pulse_end = time.time()                #Saves the last known time of HIGH pulse 

			pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

			distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
			distance = round(distance, 2)
			print "Distance:",distance - 0.5,"cm"

			if distance > 2 and distance < 400:      #Check whether the distance is within range
				print "Distance:",distance - 0.5,"cm"  #Print distance with 0.5 cm calibration
			else:
				print "Out Of Range"                   #display out of range
			#End Test
			
			n = pylirc.nextcode()
			print n

			if (distance<30) :
				GPIO.output(21, GPIO.HIGH)
				GPIO.output(19, GPIO.LOW)
				GPIO.output(16, GPIO.LOW)
				GPIO.output(26, GPIO.LOW)
				GPIO.output(20, GPIO.LOW)
				GPIO.output(25, GPIO.LOW)
				GPIO.output(17, GPIO.HIGH)
				GPIO.output(9, GPIO.LOW)
				GPIO.output(11, GPIO.LOW)
				GPIO.output(8, GPIO.LOW)
				GPIO.output(7, GPIO.LOW)
			else:
				GPIO.output(21, GPIO.LOW)
				GPIO.output(25, GPIO.HIGH)


			if (n == ['up']) :
				GPIO.output(9, GPIO.LOW)
				GPIO.output(11, GPIO.LOW)
				GPIO.output(8, GPIO.LOW)
				GPIO.output(7, GPIO.LOW)
				time.sleep(0.1)
				GPIO.output(9, GPIO.HIGH)
				GPIO.output(11, GPIO.LOW)
				GPIO.output(8, GPIO.HIGH)
				GPIO.output(7, GPIO.LOW)
			      
			if (n == ['down']) :
			      GPIO.output(9, GPIO.LOW)
			      GPIO.output(11, GPIO.LOW)
			      GPIO.output(8, GPIO.LOW)
			      GPIO.output(7, GPIO.LOW)
			      time.sleep(0.1)
			      GPIO.output(9, GPIO.LOW)
			      GPIO.output(11, GPIO.HIGH)
			      GPIO.output(8, GPIO.LOW)
			      GPIO.output(7, GPIO.HIGH)

			if (n == ['left']) :
			      GPIO.output(9, GPIO.LOW)
			      GPIO.output(11, GPIO.LOW)
			      GPIO.output(8, GPIO.LOW)
			      GPIO.output(7, GPIO.LOW)
			      time.sleep(0.1)
			      GPIO.output(9, GPIO.LOW)
			      GPIO.output(11, GPIO.HIGH)
			      GPIO.output(8, GPIO.HIGH)
			      GPIO.output(7, GPIO.LOW)
			      time.sleep(0.54)
			      GPIO.output(11, GPIO.LOW)
			      GPIO.output(8, GPIO.LOW)

			if (n == ['right']) :
			      GPIO.output(9, GPIO.LOW)
			      GPIO.output(11, GPIO.LOW)
			      GPIO.output(8, GPIO.LOW)
			      GPIO.output(7, GPIO.LOW)
			      time.sleep(0.1)
			      GPIO.output(9, GPIO.HIGH)
			      GPIO.output(11, GPIO.LOW)
			      GPIO.output(8, GPIO.LOW)
			      GPIO.output(7, GPIO.HIGH)
			      time.sleep(0.58)
			      GPIO.output(9, GPIO.LOW)
			      GPIO.output(7, GPIO.LOW)

			if (n == ['ok']) :
			      GPIO.output(9, GPIO.LOW)
			      GPIO.output(11, GPIO.LOW)
			      GPIO.output(8, GPIO.LOW)
			      GPIO.output(7, GPIO.LOW)
			      

			if (n == ['l']) :
			      GPIO.output(9, GPIO.LOW)
			      GPIO.output(11, GPIO.LOW)
			      GPIO.output(8, GPIO.LOW)
			      GPIO.output(7, GPIO.LOW)
			      time.sleep(0.1)
			      GPIO.output(9, GPIO.LOW)
			      GPIO.output(11, GPIO.HIGH)
			      GPIO.output(8, GPIO.HIGH)
			      GPIO.output(7, GPIO.LOW)

			if (n == ['r']) :
			      GPIO.output(9, GPIO.LOW)
			      GPIO.output(11, GPIO.LOW)
			      GPIO.output(8, GPIO.LOW)
			      GPIO.output(7, GPIO.LOW)
			      time.sleep(0.1)
			      GPIO.output(9, GPIO.HIGH)
			      GPIO.output(11, GPIO.LOW)
			      GPIO.output(8, GPIO.LOW)
			      GPIO.output(7, GPIO.HIGH)

			if (n == ['volumeup']) :
			      GPIO.output(9, GPIO.LOW)
			      GPIO.output(11, GPIO.LOW)
			      GPIO.output(8, GPIO.LOW)
			      GPIO.output(7, GPIO.LOW)
			      time.sleep(0.1)
			      GPIO.output(9, GPIO.HIGH)
			      GPIO.output(11, GPIO.LOW)
			      GPIO.output(8, GPIO.LOW)
			      GPIO.output(7, GPIO.HIGH)
			      time.sleep(0.1)
			      GPIO.output(9, GPIO.LOW)
			      GPIO.output(7, GPIO.LOW)


			if (n == ['volumedown']) :
			      GPIO.output(9, GPIO.LOW)
			      GPIO.output(11, GPIO.LOW)
			      GPIO.output(8, GPIO.LOW)
			      GPIO.output(7, GPIO.LOW)
			      time.sleep(0.1)
			      GPIO.output(9, GPIO.LOW)
			      GPIO.output(11, GPIO.HIGH)
			      GPIO.output(8, GPIO.HIGH)
			      GPIO.output(7, GPIO.LOW)
			      time.sleep(0.1)
			      GPIO.output(11, GPIO.LOW)
			      GPIO.output(8, GPIO.LOW)



			if (n == ['exit']) :
				GPIO.output(21, GPIO.LOW)
				GPIO.output(25, GPIO.LOW)
				GPIO.output(9, GPIO.LOW)
				GPIO.output(11, GPIO.LOW)
				GPIO.output(8, GPIO.LOW)
				GPIO.output(7, GPIO.LOW)
				break

	if (m == ['two']) :
		print "OBSTACLES AVOIDANCE MODE is activated"
		p = GPIO.PWM(2,50)              
		p.start(100)

		P = GPIO.PWM(3,50)              
		P.start(95)
		
		while True:
			#Obstacle Test
			GPIO.output(TRIG, False)                 #Set TRIG as LOW
			print "Waitng For Sensor To Settle"
			time.sleep(0.1)                            #Delay of 2 seconds

			GPIO.output(TRIG, True)                  #Set TRIG as HIGH
			time.sleep(0.00001)                      #Delay of 0.00001 seconds
			GPIO.output(TRIG, False)                 #Set TRIG as LOW

			while GPIO.input(ECHO)==0:               #Check whether the ECHO is LOW
				pulse_start = time.time()              #Saves the last known time of LOW pulse

			while GPIO.input(ECHO)==1:               #Check whether the ECHO is HIGH
				pulse_end = time.time()                #Saves the last known time of HIGH pulse 

			pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

			distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
			distance = round(distance, 2)
			print "Distance:",distance - 0.5,"cm"

			if distance > 2 and distance < 400:      #Check whether the distance is within range
				print "Distance:",distance - 0.5,"cm"  #Print distance with 0.5 cm calibration
			else:
				print "Out Of Range"                   #display out of range
			#End Test
				
			n = pylirc.nextcode()
			print n

			if (distance>30) :
				GPIO.output(21, GPIO.LOW)
				GPIO.output(19, GPIO.LOW)
				GPIO.output(16, GPIO.LOW)
				GPIO.output(26, GPIO.LOW)
				GPIO.output(20, GPIO.LOW)
				GPIO.output(25, GPIO.HIGH)
				GPIO.output(17, GPIO.HIGH)
				GPIO.output(9, GPIO.HIGH)
				GPIO.output(11, GPIO.LOW)
				GPIO.output(8, GPIO.HIGH)                                          
				GPIO.output(7, GPIO.LOW)

			if (distance<30) :
				    GPIO.output(9, GPIO.LOW)
				    GPIO.output(11, GPIO.LOW)
				    GPIO.output(8, GPIO.LOW)
				    GPIO.output(7, GPIO.LOW)
				    GPIO.output(21, GPIO.HIGH)
				    GPIO.output(25, GPIO.LOW)

				    time.sleep(1)

				    m = GPIO.PWM(24,50)
				    m.start(6.2)
				    time.sleep(0.1)
				    m.ChangeDutyCycle(2.6)                   
				    time.sleep(1)	
				    m = GPIO.PWM(24,1)
							 

				    #Obstacle Test
				    GPIO.output(TRIG, False)                 #Set TRIG as LOW
				    print "Waitng For Sensor To Settle"
				    time.sleep(0.1)                            #Delay of 2 seconds

				    GPIO.output(TRIG, True)                  #Set TRIG as HIGH
				    time.sleep(0.00001)                      #Delay of 0.00001 seconds
				    GPIO.output(TRIG, False)                 #Set TRIG as LOW

				    while GPIO.input(ECHO)==0:               #Check whether the ECHO is LOW
					    pulse_start = time.time()              #Saves the last known time of LOW pulse

				    while GPIO.input(ECHO)==1:               #Check whether the ECHO is HIGH
					    pulse_end = time.time()                #Saves the last known time of HIGH pulse 

				    pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

				    distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
				    distance = round(distance, 2)
				    print "Distance:",distance - 0.5,"cm"

				    if distance > 2 and distance < 400:      #Check whether the distance is within range
					    print "Distance:",distance - 0.5,"cm"  #Print distance with 0.5 cm calibration
				    else:
					    print "Out Of Range"                   #display out of range
				    #End Test

				    if (distance<30) :
					    oright=1
				    else:
					    oright=0

				    print 'oright=',oright

				    m = GPIO.PWM(24,50)              
				    m.start(2.8)
				    time.sleep(0.1)
				    m.ChangeDutyCycle(10.3)                   
				    time.sleep(1)	
				    m = GPIO.PWM(24,1)

				    #Obstacle Test
				    GPIO.output(TRIG, False)                 #Set TRIG as LOW
				    print "Waitng For Sensor To Settle"
				    time.sleep(0.1)                            #Delay of 2 seconds

				    GPIO.output(TRIG, True)                  #Set TRIG as HIGH
				    time.sleep(0.00001)                      #Delay of 0.00001 seconds
				    GPIO.output(TRIG, False)                 #Set TRIG as LOW

				    while GPIO.input(ECHO)==0:               #Check whether the ECHO is LOW
					    pulse_start = time.time()              #Saves the last known time of LOW pulse

				    while GPIO.input(ECHO)==1:               #Check whether the ECHO is HIGH
					    pulse_end = time.time()                #Saves the last known time of HIGH pulse 

				    pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

				    distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
				    distance = round(distance, 2)            #Round to two decimal points

				    if distance > 2 and distance < 400:      #Check whether the distance is within range
					    print "Distance:",distance - 0.5,"cm"  #Print distance with 0.5 cm calibration
				    else:
					    print "Out Of Range"                   #display out of range
				    #End Test
				    
				    if (distance<30) :
					    oleft=1
				    else:
					    oleft=0

				    print 'oleft=',oleft
				    
				    m = GPIO.PWM(24,50)              
				    m.start(10)                             
				    time.sleep(0.1)
				    m.ChangeDutyCycle(6.2)                   
				    time.sleep(1)	
				    m = GPIO.PWM(24,1)
				    
				    if oright==0 :
					    if oleft==1:
						    GPIO.output(9, GPIO.HIGH)
						    GPIO.output(11, GPIO.LOW)
						    GPIO.output(8, GPIO.LOW)
						    GPIO.output(7, GPIO.HIGH)
						    time.sleep(0.58)
						    GPIO.output(9, GPIO.LOW)
						    GPIO.output(11, GPIO.LOW)
						    GPIO.output(8, GPIO.LOW)
						    GPIO.output(7, GPIO.LOW)
						    time.sleep(1)

				    if oleft==0:
					    if oright==1:
						    GPIO.output(9, GPIO.LOW)
						    GPIO.output(11, GPIO.HIGH)
						    GPIO.output(8, GPIO.HIGH)
						    GPIO.output(7, GPIO.LOW)
						    time.sleep(0.54)
						    GPIO.output(9, GPIO.LOW)
						    GPIO.output(11, GPIO.LOW)
						    GPIO.output(8, GPIO.LOW)
						    GPIO.output(7, GPIO.LOW)
						    time.sleep(1)
						    
				    if oright==1:
					    if oleft==1:
						     GPIO.output(9, GPIO.LOW)
						     GPIO.output(11, GPIO.HIGH)
						     GPIO.output(8, GPIO.LOW)
						     GPIO.output(7, GPIO.HIGH)
						     time.sleep(1.5)
						     GPIO.output(9, GPIO.LOW)
						     GPIO.output(11, GPIO.LOW)
						     GPIO.output(8, GPIO.LOW)
						     GPIO.output(7, GPIO.LOW)
						     time.sleep(1)
						     GPIO.output(9, GPIO.HIGH)
						     GPIO.output(11, GPIO.LOW)
						     GPIO.output(8, GPIO.LOW)
						     GPIO.output(7, GPIO.HIGH)
						     time.sleep(1.26)
						     GPIO.output(9, GPIO.LOW)
						     GPIO.output(11, GPIO.LOW)
						     GPIO.output(8, GPIO.LOW)
						     GPIO.output(7, GPIO.LOW)
						     time.sleep(1)
				    
			if (n == ['exit']) :
				GPIO.output(9, GPIO.LOW)
				GPIO.output(11, GPIO.LOW)
				GPIO.output(8, GPIO.LOW)
				GPIO.output(7, GPIO.LOW)
				break


	if (m == ['three']) :
		print "LINE FOLLOWER MODE is activated with feature of detecting obstacles"
		p = GPIO.PWM(2,50)              
		p.start(90)
		P = GPIO.PWM(3,50)              
		P.start(80)
		GPIO.output(TRIG, False)                 #Set TRIG as LOW
		print "Waitng For Sensor To Settle"
		time.sleep(0.1)    
		while True:
##			#Obstacle Test
##			GPIO.output(TRIG, True)                  #Set TRIG as HIGH
##			time.sleep(0.00001)                      #Delay of 0.00001 seconds
##			GPIO.output(TRIG, False)                 #Set TRIG as LOW
##
##			while GPIO.input(ECHO)==0:               #Check whether the ECHO is LOW
##				pulse_start = time.time()              #Saves the last known time of LOW pulse
##
##			while GPIO.input(ECHO)==1:               #Check whether the ECHO is HIGH
##				pulse_end = time.time()                #Saves the last known time of HIGH pulse 
##
##			pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable
##
##			distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
##			distance = round(distance, 2)
##			print "Distance:",distance - 0.5,"cm"
##
##			if distance > 2 and distance < 400:      #Check whether the distance is within range
##				print "Distance:",distance - 0.5,"cm"  #Print distance with 0.5 cm calibration
##			else:
##				print "Out Of Range"                   #display out of range
##			#End Test
##
##
##			if (distance<30) :
##				     print "D<30 STOP"
##				     GPIO.output(9, GPIO.LOW)
##				     GPIO.output(11, GPIO.LOW)
##				     GPIO.output(8, GPIO.LOW)
##				     GPIO.output(7, GPIO.LOW)
##				     GPIO.output(21, GPIO.HIGH)
##				     GPIO.output(25, GPIO.LOW)
##
##			else:
##				GPIO.output(21, GPIO.LOW)
##				GPIO.output(19, GPIO.LOW)
##				GPIO.output(16, GPIO.LOW)
##				GPIO.output(26, GPIO.LOW)
##				GPIO.output(20, GPIO.LOW)
##				GPIO.output(25, GPIO.HIGH)
##				GPIO.output(17, GPIO.HIGH)
				r=GPIO.input(14)
				c=GPIO.input(15)
				l=GPIO.input(18)
				
				m = pylirc.nextcode()
				print m
				if  (m == ['exit']):
					     print "EXIT STOP"
					     GPIO.output(9, GPIO.LOW)
					     GPIO.output(11, GPIO.LOW)
					     GPIO.output(8, GPIO.LOW)
					     GPIO.output(7, GPIO.LOW)
					     break

				if (m == ['up']):
					     GPIO.output(9, GPIO.HIGH)
					     GPIO.output(11, GPIO.LOW)
					     GPIO.output(8, GPIO.HIGH)
					     GPIO.output(7, GPIO.LOW)
					     time.sleep(0.3)
					     GPIO.output(9, GPIO.LOW)
					     GPIO.output(11, GPIO.LOW)
					     GPIO.output(8, GPIO.LOW)
					     GPIO.output(7, GPIO.LOW)
				
				if l==0:
					     g=0
				else:
					     g=1
					     print "g=",g
				   
				if r==0:
					     d=0
				else:     
					     d=1
					     print "d=",d
				   
				if c==1:
					     d=0
					     g=0
					     M=1

				if  (g==1) and (l==1):
				      print "LEFT Black"
				      GPIO.output(9, GPIO.LOW)
				      GPIO.output(11, GPIO.LOW)
				      GPIO.output(8, GPIO.LOW)
				      GPIO.output(7, GPIO.LOW)
				      time.sleep(0.01)                      
				      GPIO.output(9, GPIO.LOW)
				      GPIO.output(11, GPIO.LOW)
				      GPIO.output(8, GPIO.HIGH)
				      GPIO.output(7, GPIO.LOW)
				      time.sleep(0.13)
				      GPIO.output(9, GPIO.LOW)
				      GPIO.output(11, GPIO.LOW)
				      GPIO.output(8, GPIO.LOW)
				      GPIO.output(7, GPIO.LOW)
				      g=1
				      d=0
				      M=0
				      
				if  (c==1):
				      if (l==1):
					      print "LEFT Black"
					      GPIO.output(9, GPIO.LOW)
					      GPIO.output(11, GPIO.LOW)
					      GPIO.output(8, GPIO.LOW)
					      GPIO.output(7, GPIO.LOW)
					      time.sleep(0.01)                      
					      GPIO.output(9, GPIO.LOW)
					      GPIO.output(11, GPIO.LOW)
					      GPIO.output(8, GPIO.HIGH)
					      GPIO.output(7, GPIO.LOW)
					      time.sleep(0.13)
					      GPIO.output(9, GPIO.LOW)
					      GPIO.output(11, GPIO.LOW)
					      GPIO.output(8, GPIO.LOW)
					      GPIO.output(7, GPIO.LOW)
					      g=1
					      d=0
					      M=0

				if (d==1) and (r==1):
				      print "RIGHT Black"
				      GPIO.output(9, GPIO.LOW)
				      GPIO.output(11, GPIO.LOW)
				      GPIO.output(8, GPIO.LOW)
				      GPIO.output(7, GPIO.LOW)
				      time.sleep(0.1)
				      GPIO.output(9, GPIO.HIGH)
				      GPIO.output(11, GPIO.LOW)
				      GPIO.output(8, GPIO.LOW)
				      GPIO.output(7, GPIO.LOW)
				      time.sleep(0.1)
				      GPIO.output(9, GPIO.LOW)
				      GPIO.output(11, GPIO.LOW)
				      GPIO.output(8, GPIO.LOW)
				      GPIO.output(7, GPIO.LOW)
				      d=1
				      g=0
				      M=0
				      
				if (c==1):
				      if (r==1):
					      print "RIGHT Black"
					      GPIO.output(9, GPIO.LOW)
					      GPIO.output(11, GPIO.LOW)
					      GPIO.output(8, GPIO.LOW)
					      GPIO.output(7, GPIO.LOW)
					      time.sleep(0.1)
					      GPIO.output(9, GPIO.HIGH)
					      GPIO.output(11, GPIO.LOW)
					      GPIO.output(8, GPIO.LOW)
					      GPIO.output(7, GPIO.LOW)
					      time.sleep(0.1)
					      GPIO.output(9, GPIO.LOW)
					      GPIO.output(11, GPIO.LOW)
					      GPIO.output(8, GPIO.LOW)
					      GPIO.output(7, GPIO.LOW)
					      d=1
					      g=0
					      M=0

				if (M==1):
				      if (r==0):
					      if (l==0):
						      print "Middel Black"
						      GPIO.output(9, GPIO.HIGH)
						      GPIO.output(11, GPIO.LOW)
						      GPIO.output(8, GPIO.HIGH)
						      GPIO.output(7, GPIO.LOW)                       
					       
					     

				if (c==1):
				      if (r==1):
					      if (l==1):
						      print "ALL BLACK STOP"
						      GPIO.output(9, GPIO.LOW)
						      GPIO.output(11, GPIO.LOW)
						      GPIO.output(8, GPIO.LOW)
						      GPIO.output(7, GPIO.LOW)
						      break

