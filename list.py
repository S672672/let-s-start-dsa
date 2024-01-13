#list - list is the data structure that is the collection of items
#we can store anythig in the lists int,float,string

# numbers = [1,2,3,4];
# print(numbers);

# words = ["smith","bhattarai"];
# print(words);

# mixed = [1,2,3,4,5,"six","seven",2.3,None];
# print(mixed);
# print(mixed[:2]); #slicing is same as index
# mixed[1] = 9;
# print(mixed);
# mixed[1:] = "hundred";
# print(mixed);

#Add data to the list
# fruits = ['apple','banana'];
# # fruits.append('mango'); #adds data to the end of the list
# fruits.insert(1,'mango')
# print(fruits);

#delete data from list
# fruits = ["orange","apple","pear","banana"];
# fruits.pop(2);
# print(fruits)

#using delete operator
# fruits = ["orange","apple","pear","banana"];
# del fruits[2];
# print(fruits)

#using remove method
# fruits = ["orange","apple","pear","banana"];
# fruits.remove("orange")
# print(fruits)

#to add data = append,extend,insert
#to remove data = pop,remove,clear,del

#some more lists method
#if present in list
# fruits = ["orange","apple","pear","banana"];
# if "orange" in fruits:
#     print("orange is present");
# else:
#     print("not present")

#count method
# fruits = ["orange","apple","pear","banana","apple"];
# # print(fruits.count("orange"));
# #sort method
# # fruits.sort();
# print(fruits);
# number = [2,3,6,10,8,9,23,17];
# number.sort();
# print(number)

#is vs equal (list comparision)
# number1 = [1,2,3,4,5];
# number3 = number1.copy()
# number2 = [2,4,6,7,9];
# print(number1 is number3)
#'==' checks if the values are euqal but 'is' checks memory location

#split vs join method --split method converts string to list and join method converts list to string
# info = 'smith 22'.split();
# print(info);

# info = ['smith','22'];
# print(",".join(info));

#looping in List
# fruits = ["orange","apple","pear","banana","apple"];
# # for fruit in fruits:
# #     print(fruit);
# i = 0;
# while i<len(fruits):
#     print(fruits[i]);
#     i+=1;

#list inside list
# matrix = [[1,2],[3,4],[5,6]];
# print(matrix[1]);
# for sublist in matrix:
#     for i in sublist:
#         print(i)
# matrix = [[1,2],[3,4],[5,6]];
# print(matrix[1][1])

#more about lists
#generate list with range function
# lists = list(range(1,11))
# # print(lists)
# # lists.pop(); #pop method
# # print(lists)
# # print(lists.index(3))
# def negative_lists(l):
#     negative = [];
#     for i in l:
#         negative.append(-i);
#     return negative;
# print(negative_lists(lists))

#exercise of list
#define a function which will take list containing numbers as input and return list containing square of every element

# def square_list(lists):
#     square = [];
#     for i in lists:
#         square.append(i**2);
#     return square;
# numbers = list(range(1,10));
# print(square_list(numbers));

# def rev_lists(lists):
#     second = [];
#     for i in range(len(lists)):
#         popped_item = lists.pop();
#         second.append(popped_item)
#     return second;
# first = list(range(1,10));
# print(first)
# print(rev_lists(first))

# def rev_lists(lists):
#     second = [];
#     for i in lists:
#         second.append(i[::-1]);
#     return second;
# name = ['smith','bhattarai'];
# print(rev_lists(name))

# def numbers(lists):
#     odd = []
#     even = [];
#     for i in lists:
#         if(i%2 == 0):
#             even.append(i);
#         else:
#             odd.append(i);
#     output = [odd,even];
#     return output;
# num = [1,2,3,4,5,6,7,8,9,10];
# print(numbers(num))

# def two_lists(lists1,lists2):
#     output = [];
#     for i in lists1:
#         if i in lists2:
#             output.append(i);
#     return output;
# flist = [1,2,3,4,5,6];
# slist = [2,5,9,10,11];
# print(two_lists(flist,slist));