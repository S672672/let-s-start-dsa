#dictioinary-unorder collection of data in key:value pairs
# user = {
#     'name': 'smith',
#     'age' : 22
# }
# print(user)
# print(type(user))

#second method to create a dictionay
# user1 = dict(name = "smith",age=22)
# print(user1)

#access data from dictionary
# user1 = dict(name = "smith",age=22)
# print(user1['name'])

#what type of data dictionary can store
#anything
# user1 = {
#     'name' : 'smith',
#     'age' : 22,
#     "fav_movies" : ['12th fail','jay shree Ram'],
#     'fav_food' : ['alu ko parautha','samosa']
# }
# print(user1['fav_movies'])

#create dictionary inside dictionary
# users = {
#     'user1':{
#         'name' : "smith",
#         'age' : 22,
#     },
#     'user2':{
#         'name' : 'Arpan',
#         'age' : 17
#     }
# }
# print(users['user2']['name'])

#add data to empty dict
# user = {};
# user['name']='smith'
# print(user)

#looping and in keyword in dictionary
# user1 = {
#     'name' : 'smith',
#     'age' : 22,
#     "fav_movies" : ['12th fail','jay shree Ram'],
#     'fav_food' : ['alu ko parautha','samosa']
# }
# if 'names' in user1:
#     print("yes present");
# else:
#     print("not present");

# user1 = {
#     'name' : 'smith',
#     'age' : 22,
#     "fav_movies" : ['12th fail','jay shree Ram'],
#     'fav_food' : ['alu ko parautha','samosa']
# }
# if 'smith' in user1.values():
#     print('present');
# else:
#     print("not presett")

#loops
# user1 = {
#     'name' : 'smith',
#     'age' : 22,
#     "fav_movies" : ['12th fail','jay shree Ram'],
#     'fav_food' : ['alu ko parautha','samosa']
# }
# for i in user1.values():
#     print(i)

#keys method
# user1 = {
#     'name' : 'smith',
#     'age' : 22,
#     "fav_movies" : ['12th fail','jay shree Ram'],
#     'fav_food' : ['alu ko parautha','samosa']
# }
# for i in user1.keys():
#     print(i)

#items method -most importnt while looping
# user1 = {
#     'name' : 'smith',
#     'age' : 22,
#     "fav_movies" : ['12th fail','jay shree Ram'],
#     'fav_food' : ['alu ko parautha','samosa']
# }
# for key,value in user1.items():
#     print(f"{key}:{value}")

#add and delete data from dictionary
user1 = {
    'name' : 'smith',
    'age' : 22,
    "fav_movies" : ['12th fail','jay shree Ram'],
    'fav_food' : ['alu ko parautha','samosa']
}
# user1['study'] = 'btech';
# print(user1)

#pop method
# user1.pop('name');
# print(user1)

#popitem method
# user1.popitem();
# print(user1)

#update()method in dictionary
# user2 = {
#     'name2' : "Arpan",
# }
# user1.update(user2)
# print(user1)
#it will replace the existing key if same name provided