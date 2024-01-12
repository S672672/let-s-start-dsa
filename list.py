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


