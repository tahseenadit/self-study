class Child:
    def func1(self):
        ...

class Child:
    def func1(self):
        print("I am from child!")
        print(Child.__bases__)

if __name__ == '__main__':
    child = Child()
    child.func1()