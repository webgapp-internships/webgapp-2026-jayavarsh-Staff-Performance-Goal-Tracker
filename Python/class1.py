
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks= marks

    def is_pass(self):
          if self.marks >=50:
             return "pass"
          else:
             return "fail"

    def show (self):
        print(self.name , self.marks )

s1=student("Jessi",67)
s2=student("Arul",87)
s3=student("Jeni",90)

s1.show()
s2.show()
s3.show()

print("result",s1.is_pass())
print("result",s2.is_pass())
print("result",s3.is_pass())


        
    
        