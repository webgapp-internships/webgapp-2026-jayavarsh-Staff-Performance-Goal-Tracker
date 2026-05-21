class student:
    def __init__ detail(self,name,marks):
        if marks >=50:
             result="pass"
        else:
             result="fail"
        return name,marks,result
s= student()
print("----------STUDENT MARK DETAILS-----------")
print(s.detail("Jessi",67))
print(s.detail("Arul",74))
print(s.detail("Jeni",90))
print("----------------END------------------")
