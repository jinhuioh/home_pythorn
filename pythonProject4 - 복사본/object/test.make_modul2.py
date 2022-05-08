print(ord('밥'))
# print(ord('반찬'))

#오버로딩
class Sample1():
    def add(self, x, y):
        return x + y
    def add(self,x,y,z):
        return x + y + z
a = Sample1()

#오버라이딩
class sample2():
    def get_value(self):
        return self.value

class ChildSample():
    def get_value(self):
        return self.value * 10
