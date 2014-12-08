import RPi.GPIO as GPIO,time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)

#define dot

def dot():
	GPIO.output(11,True)
	time.sleep(0.5)
	GPIO.output(11,False)
	time.sleep(0.5)
dot()

def dash():
	GPIO.output(11,True)
	time.sleep(2)
	GPIO.output(11,False)
	time.sleep(0.5)
dash()


def morse():
	if name == "A":
		dot()
		dash()
	if name =="B":
		dash()
		dot()
		dot()
		dot()
	if name =="C"
		dash()
		dot()
		dash()
		dot()
	if name=="D"
		dash()
		dot()
		dot()
	if name=="E"
		dot()
	if name=="F"
		dot()
		dot()
		dash()
		dot()
	if name=="G"	
		dash()
		dash()
		dot()
	if name=="H"
		dot()
		dot()
		dot()
		dot()
	if name=="I"
		dot()
		dot()

