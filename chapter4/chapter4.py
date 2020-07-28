print("aa")
magicians = ['jack','rose','john']
for magician in magicians:
    print(magician)
    print("\n")


#homework 4-1
pizzas  = ['Durian','Meat','Pinapple']
for pizza in pizzas:
    print(pizza)
    print('I like ' + pizza +' Pizza !\n')
print("I really like Pizza!")

#homework 4-2
#OMIT

#homework 4-3
for digit in range(1,21):
    print(digit)

#homework 4-4
digits = list(range(1,1000001))
#for digit in digits:
#    print(digit)
#annotation above for reducing runtime for the rest tests

#homework 4-5
digits = list(range(1,1000001))

print(min(digits))
print(max(digits))
print(sum(digits))

#homework 4-6
digits = list(range(1,21,2))
for digit in digits:
    print(digit)

#homework 4-7
digits = list(range(3,31,3))
for digit in digits:
    print(digit)

#homework 4-8
digits = [value ** 3 for value in range(1,11)]
for digit in digits:
    print(digit)

#homework 4-9
#REFER TO HOMEWORK 4-8

#homework 4-10
print("The first three items in the list are " + str(digits[0:3]))
print("The first three items in the list are " + str(digits[4:7]))
print("The first three items in the list are " + str(digits[-3:]))

#homework 4-11
friend_pizzas = pizzas[:]
pizzas.append("chocolate")
friend_pizzas.append("lemon")
print("My favorite pizzas are ")
for pizza in pizzas:
    print(pizza)
print("My friend's favorite pizzas are ")
for pizza in friend_pizzas:
    print(pizza)

#homework 4-12
#OMIT REFER TO homework 4-11

#homework 4-13
foods = ('Rice','Noodles','Meat','Soup','Vegan')
for food in foods:
    print(food)
#foods[0] = 'Junk'
foods = ('Fish','Chips','Meat','Soup','Vegan')
for food in foods:
    print(food)

#homework 4-14
#OMIT

#homework 4-15
#OMIT
