from datetime import datetime, date


class Relationships:
    """A class to store the relationships between people"""

    def __init__(self):
        self._children = []
        self._spouse = None
        self._siblings = []
        self._parents = []

    @property
    def siblings(self):
        if self._siblings == []:
            return None
        else:
            return self._siblings
    @siblings.setter
    def siblings(self, sibling):
            self._siblings.append(sibling)

    @property
    def spouse(self):
        return self._spouse
    @spouse.setter
    def spouse(self, spouse):
        self._spouse=  spouse

    @property
    def children(self):
        if self._children == []:
            return None
        else:
            return self._children
    @children.setter
    def children(self, child):
        self._children.append(child)

    @property
    def parents(self):
        if self._parents == []:
            return None
        else:
            return self._parents
    @parents.setter
    def parents(self, parent):
        self._parents = parent

class Person:
    """A generic class to model a human being"""

    def __init__(self, name, dob, rel=None):
        self.name = name
        self.dob = dob
        self.alive = True
        self.relationships = Relationships()

    def getAge(self):
        self.today = date.today()
        return self.today.year - self.dob.year
    
    def getParentNames(self):
        if self.relationships.parents != None:
            self.parents = []
            for parent in self.relationships.parents:
                self.parents.append(parent.name)
            return self.parents
        return None
    
    def getChildrenNames(self):
        if self.relationships.children != None:
            self.children = []
            for child in self.relationships.children:
                self.children.append(child.name)
            return self.children
        return None
    
    def getSpouseNames(self):
        if self.relationships.spouse != None:
            return self.relationships.spouse.name
        return None

    def __str__(self):
        return """
                    Name: {name}
                    Age: {age}
                    Parents: {parents}
                    Children: {children}
                    Spouse: {spouse}
        """.format(name=self.name, age=self.getAge(), parents=self.getParentNames(), children=self.getChildrenNames(), spouse=self.getSpouseNames())




p1 = Person("Daddy Pig", datetime(2001, 9, 11))
p2 = Person("Mummy Pig", datetime(2002, 6, 17))
p3 = Person("Peppa Pig", datetime(2018, 8, 28))

p1.relationships.children = p3
p2.relationships.children = p3
p3.relationships.parents = [p1, p2]

print(p1.getParentNames())
print(p3)


