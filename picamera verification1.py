import  picamera, time
def getpic(name):
    try:
        with picamera.PiCamera() as camera:
            q ="n"
            while q == "n":
                camera.start_preview()
                time.sleep(3)
                camera.capture("{0}.jpeg".format(name))
                camera.stop_preview()
                q = input("is this image okay? (Y/N) ")
        print("your filename is {0}.jpeg".format(name))
        return filename
  except picamera.exc.PicameraMALEError:
        print("there is a problem with the camera, please check it's connected.")
        
        

def getchar():    
    name = input("What is your name?")
    halt = input("What hair colour do they have? (blonde/brown/black/gimger/none)")
    halt = input("Are you wearing a hat?")
    halt = input("Are you Male,Female,or other?")
    halt = input("What colour are your eyes?(green/blue/black/brown/hazel/gray)")
    halt = input("Do you have any facial hair?")
    halt = input(" Are you wearing glasses?")
    getpic(name)

getchar()



 
 
    
          
