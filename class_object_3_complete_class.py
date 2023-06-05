#3.create class student with private name,roll no
class student:
    def __init__(self,_name,_rollno):
        self._name = _name
        self._rollno = _rollno
    def get_name(self):
        return self._name
    def set_name(self,name):
         self._name = name
    def get_rollno(self):
        return self._rollno
    def set_rollno(self,rollno):
        self._rollno = rollno
obj = student("sai", 11712558)
print(f"the name of the student is {obj.get_name()}")
print(f"the rollno of the student is{obj.get_rollno()}") 