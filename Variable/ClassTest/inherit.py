class Parent:        # 定义父类
   parentAttr = 100
   def __init__(self):
      self.name = 'father'
      print("调用父类构造函数", self.name)

   def parentMethod(self):
      print('调用父类方法')

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print("父类属性 :", Parent.parentAttr)

class Child(Parent): # 定义子类
   def __init__(self):                                # 父类构造函数不会自动调用，需要自己显式调用
      self.name = 'child'
      print("调用子类构造方法", self.name)

   def childMethod(self):
      print('调用子类方法 child method')

c = Child()          # 实例化子类
c.childMethod()      # 调用子类的方法
c.parentMethod()     # 调用父类方法
c.setAttr(200)       # 再次调用父类的方法
c.getAttr()          # 再次调用父类的方法