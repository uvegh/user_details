class CreateClass:
    def __init__(self):
        self.name=input("Enter your name: ")
        self.email=input ("Enter your email: ")

 
    def saveDetails(self):
        with open( 'userDetails.txt','w',) as userDetails:
            userDetails.write(f"{self.name}, {self.email}")

details= CreateClass()
details.saveDetails()

