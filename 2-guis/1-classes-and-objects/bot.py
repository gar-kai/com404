class Bot:
    def __init__(self, name, age, energy, shieldlevel):
        self.name = name
        self.age= age
        self.energy = energy
        self.shieldlevel = shieldlevel
    
    def display_name (self):
        print("********************************")
        print("*"    +str(self.name)   +  "         *")
        print("********************************")
    
    def display_age(self):
        print("     )  (  )  (")
        print("    (^)(^)(^)(^)")
        print("    _i__i__i__i_")
        print("   (____________)")
        print("   |####|" +str(self.age) +"|####|")
        print("   (____________)")

    def display_energy(self):
        print("Energy: " + "♥" * self.energy)
    
    def display_shieldlevel(self):
        print("shield: " + "♦" * self.shieldlevel)
    
    def display_summary(self):
        print("{} is {} years old and has an energy level of {} and shieldlevel of {}" .format(self.name, self.age, self.energy, self.shieldlevel))

    def __str__(self):
        return self.name+ ":" + str(self.age) + "," + str(self.energy) + str(self.shieldlevel)


Garkai = Bot("Garkai",37,1,3)
Garkai.display_name()
Garkai.display_age()
Garkai.display_energy()
Garkai.display_shieldlevel()

print(Garkai. __str__ ())

