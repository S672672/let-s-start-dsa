#solve the queries which arise just while sitting to know if i can do it or not
# arr = ["apple","banana","mango","grapes"];
# for i in range(0,len(arr)):
#     if(arr[i] == "mango"):
#         arr[i] = "guava"
# print(arr);

# arr = ['apple','banana','mango','guava'];
# a = arr[0];
# b = arr[-1];
# for i in range(0,len(arr)):
#     arr[0] = b;
#     arr[-1] = a;
# print(arr);

# lists = [1,2,56,80,43,23];
# lists.sort();
# print(lists[-1],'is the maximum');

# lists = ['apple','banana','mango','guava'];
# if 'apple' in lists:
#     print(True);
# else:
#     print(False);

# lists = ['apple','banana','mango','guava'];
# lists.clear();
# print(lists);

# lists = ['apple','banana','mango','guava'];
# lists.reverse();
# print(lists);

# def two_sum(nums, target):
#     result = []
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 result.append([i,j])
#     return result;

# numbers = [2, 3, 6, 7,9]
# to_get = 5
# print(two_sum(numbers, to_get))


# for i in "smith":
#     print(i)
# import random
# random_number = random.randint(1,7)
# print(random_number)

# name = input("enter your name: ")
# new_name = name.replace("t","T",1)
# print(new_name)
# # new_name = ""
# # for i in name:
# #     if i !="t":
# #         new_name+=i
# #     else:
# #         new_name += i.upper()
# # print(new_name)

# name = input("enter your name")


# take a list of numbers from 1 to 100
# if even add that element in even_list variable
# if odd add that element in odd_ltist variable
# lists = list(range(1,101));
# odd_list = [];
# even_list = [] ;
# for i in lists:
#     if i % 2 != 0:
#         odd_list.append(i);
#     else:
#         even_list.append(i);
# print(odd_list);
# print(even_list);

# def isEven(number):
#     return number%2==0
# numbers = list(range(1,101))
# even_number = filter(isEven,numbers)
# print(list(even_number))

# even_list = [i for i in range(1,101) if i%2==0]
# print(even_list)

# List of names 
# input
# Sabin,Smith,Raj,Amit, Sandesh, Hhahha
# if name starts with S then at that condition remove that name and at last return
# remaining list of names
# output
# Raj,Amit,Hhahha

names = ["Sabin","Smith","Raj","Amit","Sandesh","Hahaha"];
# for i in range(0,len(names)-1):
#     if names[i].startswith("S"):
#        del names[i]
# print(names)
for i in range(len(names)-1):
    name = names[i];
    if name[0]=="S":
        names.remove(name);
print(names);