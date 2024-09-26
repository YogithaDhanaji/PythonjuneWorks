class employee:

    eid:int

    name:str

    age:int

    gender:str

    department:str


    def set_employee(self,id,name,age,gender,dept):

        self.eid=id

        self.name=name

        self.age=age

        self.gender=gender

        self.department=dept

    def disply_employee(self):

        print(self.age)

# create onjects      



employee_instanse=employee()

employee_instanse.set_employee(123,"yogi","female",23,"python")

employee_instanse.disply_employee()




