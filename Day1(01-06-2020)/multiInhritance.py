class ClassA:
    def method1():
        return "i am from classA method1"
    def hello1():
        return "i am from classA Hello function"

class ClassB:
    def method2():
        return "i am from ClassB"
    def hello2():
        return "i am from hello2"

class ClassC(ClassA,ClassB):
    def method3():
        return "i am from ClassC"
    def hello3():
        return "i am from hello3"

obj=ClassC
print(obj.method2())
print(obj.method3())
