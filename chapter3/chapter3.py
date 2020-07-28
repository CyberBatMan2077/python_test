print("aaa")
name = ['Liao','Zhou','Lee']
print(name)
print(name[0].upper())
#homework 3-1
print(name[0])
print(name[1])
print(name[2])

#homework 3-2
print("Hello! " + name[0] + ".")
print("Hello! " + name[1] + ".")
print("Hello! " + name[2] + ".")

#homework 3-3
#OMIT

#homework 3-4
guest = ['Michael Jackson','Taylor Swift','Robinson']
print('Hello, ' + guest[0] + 'would you like to have a dinner with me ?')
print('Hello, ' + guest[1] + 'would you like to have a dinner with me ?')
print('Hello, ' + guest[2] + 'would you like to have a dinner with me ?')
print('Hello, ' + str(guest) + 'would you like to have a dinner with me ?')

#homework 3-5
print(guest[0] + 'is unable to attend')
guest[0] = 'ZhouMengying'
print('Hello, ' + guest[0] + 'would you like to have a dinner with me ?')
print('Hello, ' + guest[1] + 'would you like to have a dinner with me ?')
print('Hello, ' + guest[2] + 'would you like to have a dinner with me ?')

#homework 3-6
print("I've found a bigger table!")
guest.insert(0,'Lee')
guest.insert(2,'Zhao')
guest.append('Jay Chow')
print('Hello, ' + guest[0] + 'would you like to have a dinner with me ?')
print('Hello, ' + guest[1] + 'would you like to have a dinner with me ?')
print('Hello, ' + guest[2] + 'would you like to have a dinner with me ?')
print('Hello, ' + guest[3] + 'would you like to have a dinner with me ?')
print('Hello, ' + guest[4] + 'would you like to have a dinner with me ?')
print('Hello, ' + guest[5] + 'would you like to have a dinner with me ?')

#homework 3-7
print('Sry,you are fooled! I can only invite 2 guests now.')
pop_1 = guest.pop()
print('Sorry ' + pop_1 + ', maybe next time')
pop_1 = guest.pop()
print('Sorry ' + pop_1 + ', maybe next time')
pop_1 = guest.pop()
print('Sorry ' + pop_1 + ', maybe next time')
pop_1 = guest.pop()
print('Sorry ' + pop_1 + ', maybe next time')
print(guest[0] + 'you are still invited')
print(guest[-1] + 'you are still invited')
del guest[0]
del guest[-1]
print(guest)

#homework 3-8
places = ["Xi'an",'Beijing','Liannan','Guangzhou']
print(places)
print(sorted(places))
print(places)
print(sorted(places,reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)

#homework 3-9
print(len(places))

#homework 3-10
#OMIT

#homework 3-11
#print(places[4])
