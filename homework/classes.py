class Character:
    def __init__(self, health):
        self.health = health
        
    def hit_damage(self,damage):
        self.health -= damage
        return self.health
    
    def add_health(self,health):
        self.health += health
        return self.health

class Archer(Character):
    def __init__(self,arrow_amount, health):
        super().__init__(health)
        self.number = arrow_amount

    def shoot(self):
        self.number -= 1
        return self.number