'''
This source demonstrated how to use class
'''

class person:
    ''' person class'''
    population = 0

    def __init__(self, name):
        self.name = name
        print ("initialing name %s" % self.name)
        person.population += 1

    def __del__(self):
        person.population -= 1
        if person.population == 0:
            print ("I am the last one "+self.name)
        else:
            print ("in del -- there are still %d people here", person.population)

    def sayHI(self):
        print ("Hi, I am ", self.name)

    def howMany(self):
        print ("there are still %d people here", person.population)


Eddy=person("eddy")
Eddy.sayHI()
Eddy.howMany()

Fx = person("FX")
Fx.sayHI()
Fx.howMany()

print (" del Eddy")
del Eddy
Fx.sayHI()
Fx.howMany()