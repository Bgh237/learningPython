class PlayerCharacter:
    membership = True
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def shout(self):
        print (f'my name is {self.name} and I am {self.age} years old')

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)

    @staticmethod
    def adding_things2(cls, num1, num2):
        return num1 + num2

# player1 = PlayerCharacter('Cindy')
# player2 = PlayerCharacter('Tom', 21)

# print(player1.name, player1.age)
# print(player2.name, player2.age)
# print(player1.adding_things(2, 3))
# print(player2.shout())

player3 = PlayerCharacter.adding_things(2,3)
print(player3.age)