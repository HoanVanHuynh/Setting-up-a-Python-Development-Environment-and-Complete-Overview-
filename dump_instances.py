import yaml
class Hero:
    def __init__(self, name, hp, sp):
        self.name = name
        self.hp = hp 
        self.sp = sp 

    def __repr__(self):
        return "̀%s(name=%r, hp=%r, sp=%r)" % (self.__class__.__name__, self.name, self.hp, self.sp)
hero = Hero('hoan', hp=1, sp=2)        
print("print with repr: ", hero)
hero2 = yaml.dump(Hero("Galain Ysseleg", hp=-3, sp=2))

print("print with dump: ", hero2)