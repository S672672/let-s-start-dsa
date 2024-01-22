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
user = {};
user['name']='smith'
print(user)