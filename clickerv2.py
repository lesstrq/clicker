class Hero:
    def name(self):
        d = {value:key for key,value in globals().items()}
        return d[self]
    def __init__(self, damage, money):
        self._damage = damage
        self._money = money
        self._owned_weapons = [0 for _ in range(10)]

    def get_money(self):
        return self._money

    def get_damage(self):
        return self._damage

    def get_owned_weapons(self):
        return self._owned_weapons

    def set_money(self, money_amount):
        self._money = money_amount

    def calculate_damage(self):
        total_damage = 1
        for i in weapon_list:
            total_damage +=  self.get_owned_weapons()[i[2]] * i[1]
        return total_damage

    def set_owned_weapons(self, new_owned_weapons):
        self._owned_weapons = new_owned_weapons

    def attack(self, target):
        target.set_health(target.get_health() - self.calculate_damage())
        print("You attacked enemy and dealt ", self.calculate_damage()," points of damage\n  enemy's hp is ", target.get_health())
        if target.get_health()<=0:
                # target.is_alife=False
                # self._money+=target._reward
                # print("Congratz! Ypu kill",target.name()," and reward ", target._reward)
                target.die(main_hero)
class Enemy:
    is_alife=True
    def __init__(self, health, reward):
        self._health = health
        self._reward = reward

    def get_health(self):
        return self._health

    def set_health(self, new_health):
        self._health = new_health

    def die(self, killer):
        print("Congratz! You killed enemy and got ", self._reward, "\n Your current balance is", killer.get_money() + self._reward)
        killer.set_money(killer.get_money() + self._reward)
        global amount_of_killed
        global maxlevel
        if amount_of_killed == 9:
            maxlevel += 1
            amount_of_killed = 0

        else:
            amount_of_killed += 1
        generate_enemy(current_level)

class Weapon:
    def name(self):
        d = {value:key for key,value in globals().items()}
        return d[self]
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
        owner.set_money(owner.get_money() - self.get_cost())
        weapons = owner.get_owned_weapons()
        weapons[self.get_id()] += 1
        owner.set_owned_weapons(weapons)

def gotolevel(level):
    global current_level
    if level <= maxlevel:
        current_level = level
        generate_enemy(level)
        if current_level == maxlevel:
            global amount_of_killed
            amount_of_killed = 0

def generate_enemy(level):
    if level > 20:
        hp = 10 * global_level_bonus**(level)
        reward = global_level_bonus**(level)
    else:
        values = [[10, 1], [28, 2], [52, 4], [71, 5], [111, 7], [145, 9], [230, 13], [278, 16], [340, 20], [432, 25], [548, 37], [650, 42], [720, 50], [800, 60], [941, 72], [1053, 80], [1100, 85], [1252, 93]]
        table = {key: value for key,value in zip(range(1, len(values) + 1), values)}
        hp = table[level][0]
        reward = table[level][1]
    global current_enemy
    current_enemy = Enemy(hp, reward)
amount_of_killed = 0
global_level_bonus=1.15
main_hero = Hero(1, 0)
current_level = 1
maxlevel = 1
current_enemy = Enemy(10, 1)

weapon_list = [[5, 1, 0],[25, 3, 1],[125, 6, 2]]
first_weapon = Weapon(5, 1, 0)
second_weapon = Weapon(25, 3, 1)
third_weapon = Weapon(125, 6, 2)

while True:
    exec(input())