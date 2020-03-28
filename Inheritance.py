class A:
    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")

class B:
    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")

#Inheriting class A and B
class C(A,B):
    def feature5(self):
        print("Feature 5 working")

class D(A):
    def feature6(self):
        print("Feature 6 working")

class E(D):
    def feature7(self):
        print("Feature 7 working")

#A can access only feature of its own class
a1 = A()
a1.feature1()
a1.feature2()

#B can access only feature of its own class
b1 = B()
b1.feature3()
b1.feature4()

#C can access feature from all  A, B and C
c1 = C()
c1.feature3()
c1.feature1()
c1.feature5()

#D can access only feature from both A and D
d1 = D()
d1.feature1()
d1.feature6()

#E can access features from both A, D and E
e1 = E()
e1.feature1()
e1.feature6()
e1.feature7()