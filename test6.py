class test:
    def __init__(self, age, name) :
        self.age = age
        self.name = name


    def display(self):
        return self.age,self.name

    
result = test(30,'Ram')
print(result.display())