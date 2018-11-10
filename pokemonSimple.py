class Pokemon(object):
    HP = ''
    attack = ''
    defense = ''
    special_attack = ''
    special_defense = ''
    speed = ''

    def info(self):
        print("Pokemon: " + self.__class__.__name__)
        print("HP: " + str(self.HP))
        print("Attack: " + str(str(self.attack)))
        print("Defense: " + str(self.defense))
        print("Special attack: " + str(self.special_attack))
        print("Special defense: " + str(self.special_defense))
        print("Speed: " + str(self.speed))

    def simple_fight(self, other):
        if self.HP > 0:
            print("%s stars fighting with %s" % (self.__class__.__name__, other.__class__.__name__))
            print("Now %s has %d HP" % (other.__class__.__name__, other.HP))
            other.HP -= self.attack
            return other.simple_fight(self)
        else:
            print("%s is dead! / %s wins! (%d hp left)" % (self.__class__.__name__, other.__class__.__name__, other.HP))
            return other, self


    def Pokeyball(kind):
        if kind == "Azurill":
            return Azurill()
        if kind == "Slowpoke":
            return Slowpoke()
        if kind == "Happiny":
            return Happiny()
        if kind == "Cyndaquil":
            return Cyndaquil()
        if kind == "Zubat":
            return Zubat()
        if kind == "Clamperl":
            return Clamperl()
        if kind == "Starly":
            return Starly()
        if kind == "Riolu":
            return Riolu()
        if kind == "Venipede":
            return Venipede()
        if kind == "Sandile":
            return Sandile()
        else:
            return None


class Azurill(Pokemon):
    HP = 50
    attack = 20
    defense = 40
    special_attack = 20
    special_defense = 40
    speed = 20


class Slowpoke(Pokemon):
    HP = 90
    attack = 65
    defense = 65
    special_attack = 40
    special_defense = 40
    speed = 15


class Happiny(Pokemon):
    HP = 100
    attack = 5
    defense = 5
    special_attack = 15
    special_defense = 65
    speed = 30


class Cyndaquil(Pokemon):
    HP = 39
    attack = 52
    defense = 43
    special_attack = 60
    special_defense = 50
    speed = 65


class Zubat(Pokemon):
    HP = 40
    attack = 45
    defense = 35
    special_attack = 30
    special_defense = 40
    speed = 55


class Clamperl(Pokemon):
    HP = 35
    attack = 64
    defense = 85
    special_attack = 74
    special_defense = 55
    speed = 32


class Starly(Pokemon):
    HP = 40
    attack = 55
    defense = 30
    special_attack = 30
    special_defense = 30
    speed = 60


class Riolu(Pokemon):
    HP = 40
    attack = 70
    defense = 40
    special_attack = 35
    special_defense = 40
    speed = 60


class Venipede(Pokemon):
    HP = 30
    attack = 45
    defense = 59
    special_attack = 30
    special_defense = 39
    speed = 57


class Sandile(Pokemon):
    HP = 50
    attack = 72
    defense = 35
    special_attack = 35
    special_defense = 35
    speed = 60

# пока я так понимаю фабрику
pok1 = [Pokemon.Pokeyball("Azurill"), Pokemon.Pokeyball("Slowpoke"), Pokemon.Pokeyball("Happiny"), Pokemon.Pokeyball("Cyndaquil"), Pokemon.Pokeyball("Zubat"), Pokemon.Pokeyball("Clamperl"), Pokemon.Pokeyball("Starly"), Pokemon.Pokeyball("Riolu"), Pokemon.Pokeyball("Venipede"), Pokemon.Pokeyball("Sandile")]
from random import randrange
random_index = randrange(0, len(pok1))
print(pok1[random_index].info())

# самая простая атака
fighter1 = pok1[random_index]
fighter2 = pok1[random_index-1]
winner, loser = fighter2.simple_fight(fighter1)