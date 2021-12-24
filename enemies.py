class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):
        return self.hp > 0


class GiantSpider(Enemy):
    def __init__(self):
        super().__init__(name="Giant Spider", hp=10, damage=2)


class Ogre(Enemy):
    def __init__(self):
        super().__init__(name="Ogre", hp=30, damage=15)


class Dog(Enemy):
    def __init__(self):
        super().__init__(name="Dog", hp=20, damage=10)


class Wolf(Enemy):
    def __init__(self):
        super().__init__(name="Wolf", hp=25, damage=15)


class Goblin(Enemy):
    def __init__(self):
        super().__init__(name="Goblin", hp=28, damage=18)


class Joker(Enemy):
    def __init__(self):
        super().__init__(name="Joker", hp=23, damage=17)

class Bane(Enemy):
    def __init__(self):
        super().__init__(name="Bane", hp=23, damage=17)        
