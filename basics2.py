#string formatting
# name = input("enter your name");
# age = input("enter your age");
# print(f"hello {name} your age is {age}");

#exercise1
# num1 = int(input("enter the  first number"));
# num2 = int(input("enter the second number"));
# num3 = int(input("enter the third number"));
# avg = (num1 + num2 + num3)/3
# print(f"The average of the numbers {num1} {num2} and {num3} is {avg}");

#string indexing
# name = "smith";
# print(name[1]);
# print(name[-3]);

#string slicing
# name = "smith";
# print(name[2:4]);

#step argument
# name = "smith bhattarai";
# print(name[0:15:2]);
# print(name[0::2]);

#exercise 2
# name = input("enter your name");
# print(name[-1::-1]);

#string method
# name = input("enter your name");
# # print(len(name));
# print(name.upper());
# print(name.lower());
# print(name.title()); #capitalize the title of the element
# print(count());

#exercise3
# name, character = input("enter your name and any character").split(",");
# print(f'hello length of your name is {len(name)} character count is:{name.count(character)}');

#exercise
# name = input("enter your name");
# newName = name.title();
# if(name):
#     if(newName[0] == 'S'):
#         print("king");
#     else:
#         print("queen");
# else:
#     print("naam lekh");

#remove unused spaces 
# lstrip()--removes the space before starting
# rstrip()--removes the space of after ending
#strip()--removes space from both end and starting
#replace("original","new")--replaces old by new
# name = '     sm ith     ';
# lname = 'Bhattarai';
# print(name.lstrip()+lname);
# print(name.rstrip()+lname);
# print(name.strip()+lname);
# print(name.replace(" ","") + lname);

#find method
name = "my is name is smith bhattarai";
print(name.find('is',4))