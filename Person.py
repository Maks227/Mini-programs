class Person:
    def __init__(self, ловкость, сила, магия, удача, защита, точность, ум, имя):
        self.ловкость = ловкость
        self.сила = сила
        self.магия = магия
        self.удача = удача
        self.защита = защита
        self.точность = точность
        self.ум = ум
        self.имя = имя

    def показать(self):
        print("\t\t[#] %s [#]" % self.имя)
        print("	#===============#")
        print("	| ловкость: %s\t|" % self.ловкость)
        print("	| сила: %s\t\t|" % self.сила)
        print("	| магия: %s\t\t|" % self.магия)
        print("	| удача: %s\t\t|" % self.удача)
        print("	| защита: %s\t\t|" % self.защита)
        print("	| точность: %s\t|" % self.точность)
        print("	| ум: %s\t\t\t|" % self.ум)
        print("	#===============#")
