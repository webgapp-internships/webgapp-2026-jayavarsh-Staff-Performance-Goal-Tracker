#class student:
   # def __init__(self, name):
       # self.name = name
    #def show (self):
       # print(self.name)
#s1=student("jaya")
#s1.show()

class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks= marks
    def show (self):
        print(self.name , self.marks)
s1=student("Jessi",67)
s2=student("Arul",87)
s3=student("Jeni",90)
s1.show()
s2.show()
s3.show()

