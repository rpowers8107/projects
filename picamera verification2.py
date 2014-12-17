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

    except picamera.exc.PicameraMMALError: 
        print("there is a problem with the camera, please check it's connected.")
        
        

def getchar():
    name = ""
    while name == "":
          name = input("What is your name?")
    hair = ""
    while hair =="":
          hair = input("What hair colour do they have? (blonde/brown/black/gimger/none)")
    hat = ""          
    while hat =="":
          hat = input("Are you wearing a hat?")
    gender = ""
    while gender == "":
          gender = input("Are you Male,Female,or other?")
    eyes = ""
    while eyes =="":
          eyes = input("What colour are your eyes?(green/blue/black/brown/hazel/gray)")
    facial = ""
    while facial =="":
          facial = input("Do you have any facial hair?")
    glasses = ""
    while glasses =="":
          glasses = input(" Are you wearing glasses?")
    getpic(name)

getchar()

profileList = [name,hair,hat,gender,eyes,facial,glasses]
    return profileList

def getProfile():
    return[name,filename,hair,eye]

def saveProfile():
    profile = getProfile()
    with open("profiles.txt",mode = "a",encoding="utf-8") as my_file:
        for item in profile:
            my_file.write(item+",")    
        my_file.write("\b\n")

saveProfile()


def loadProfile():
    try:
        with open("profiles.txt",mode = "wb") as my_files:
            json.dump(profileList,my_file)

    except File10:
        print("No profiles found")
        profile = []
        


