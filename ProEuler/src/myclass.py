class Person:
    """ person class"""
    population = 0

    def __init__(self, name):
        self.name = name
        print ("initialing name %s" % self.name)
        Person.population += 1

    def __del__(self):
        Person.population -= 1
        if Person.population == 0:
            print ("I am the last one "+self.name)
        else:
            print ("in del -- there are still %d people here", person.population)

    def sayhi(self):
        print ("Hi, I am ", self.name)

    def howmany(self):
        print ("there are still %d people here", person.population)