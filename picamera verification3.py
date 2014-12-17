import  picamera, time
def getpic(name):
    try:
        with picamera.PiCamera() as camera:
            q ="n"
            while q == "n":
                camera.start_preview()      #shows preview of what picture will look like.
                time.sleep(3)
                camera.capture("{0}.jpeg".format(name))
                camera.stop_preview()
                q = input("is this image okay? (Y/N) ")
        print("your filename is {0}.jpeg".format(name)) #saves as yourname.jpeg.
        return filename

    except picamera.exc.PicameraMALError:   #if there's an error with camera gives the following message.
        print("there is a problem with the camera, please check it's connected.")
        
        

def getCharProfile():   #gathers traits for character picture.
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
    characterProfile = [name,hair,hat,gender,eyes,facial,glasses]
    return characterProfile #returns traits
    


def getCharProfile():
    return[name,filename,hair,hat,gender,eyes,facial,glasses]

def saveCharProfile(profileList):
    profile = getCharProfile()
    profileList.append(profile)
    with open("Files.txt",mode = ) as file:
        my_file.write(str(profile))
    with open("profiles.txt",mode = "a") as my_file:
        json.dump(profile,my_file)
    return profile
     

saveCharProfile()


def loadCharProfile():
    try:
        with open("profiles.txt",mode = "wb") as my_files:
            json.dump(profileList,my_file)

    except File10:
        print("No profiles found")
        profile = []
        


