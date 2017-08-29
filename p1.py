class Student(object):
    def __init__(self, name="noname", score=0):
        self.name=name
        self.score=score

    def showme(self):
        print ("name =" + self.name)
        print ("score = " + str (self.score))
    



def isoverzero (num):
    if num>0:
        return True
    return False

A = filter (isoverzero, [-1,-2,3,4,-1,-2,-3,-4])
B = map(abs, [1,2,3,4,-1,-2,-3,-4])

for i in A:
    print (i);

for b in B:
    print (b)


stu = Student("Eddy", 98)
stu.showme()

a = map (type, dir (stu))
for i in a:
    print (i)
