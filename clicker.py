class Hero:
    def __init__(self, damage, money):
        self._damage = damage
        self._money = money
        self._owned_weapons = [0 for _ in range(10)]

    def get_money(self):
        return self._money

    def get_damage(self):
        return self._damage

    def get_owned_weapons(self):
        return self._owned_weapon

    def set_money(self, money_amount):
        self._money = money_amount


    def set_owned_weapons(self, new_owned_weapons):
        self._owned_weapons = new_owned_weapons

    def attack(self, target):
        target.set_health(target.get_health() - self.get_damage())

class Enemy:
    def __init__(self, health, reward):
        self._health = health
        self._reward = reward

    def get_health(self):
        return self._health

    def set_health(self, new_health):
        self._health = new_health

    def die(self, killer):
        killer.set_money(killer.get_money() + self._reward)
        # generate_enemy(current_level)

class Weapon:
    def __init__(self, cost, added_damage, weapon_id):
        self._cost = cost
        self._damage = added_damage
        self._weapon_id = weapon_id

    def get_cost(self):
        return self._cost

    def get_added_damage(self):
        return self._damage

    def get_id(self):
        return self._weapon_id

    def buy(self, owner):
        owner.set_money(owner.get_money() - self.cost)
        weapons = owner.get_owned_weapons
        weapons[self.get_id()] += 1
        owner.set_owned_weapons(weapons)

player = Hero(1, 0)
print(player.get_money())
o = Enemy(10, 5)
o.die(player)
print(player.get_money())
