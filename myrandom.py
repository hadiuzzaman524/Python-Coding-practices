import random

#print a random number...
print(random.random())

#print int type random number with range
print(random.randint(2,20))

#choose a person with randomly
li=['jaman','habib','rakib']
print(random.choice(li))

# rolled two dice and see the output
class Dice:
    def roll(self):
        self.number1=random.randint(1,6)
        self.number2=random.randint(1,6)

        return self.number1,self.number2

rolled=Dice()

result=rolled.roll()
print(result)