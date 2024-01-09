#condtions and loops and operators
#if statement
# age = int(input("what is your age?"));
# if age >= 16:
#     print("you are eligble to vote");
# else:
#     print("you are not eligible");

#pass statement --if we don't want anything after condtion we can use pass to avoid error
# age = 14;
# if(age>10):
#     pass

#exercise 1
# import random;
# guess = int(input("guess the number"));
# result = random.randint(0,100);
# if(guess == result):
#     print("you win!!")
# else:
#     if(guess > (result+10)):
#         print("you are guessing too high");
#     elif(guess < (result+10)):
#         print("you are guessing too low");
# print(f"the result is {result}")

#And and or operator
# name = input("Enter your name");
# age = int(input("enter your age"));
# if(name == "smith" and age == 22): #and(all the condition should be true)
#     print("you are correct");
# else:
#     print("you are wrong")

# name = input("Enter your name");
# age = int(input("enter your age"));
# if(name == "smith" or age == 22): #or(any of the condition should be true)
#     print("you are correct");
# else:
#     print("you are wrong");

#exercise 2
# name = input("enter your name");
# age = int(input("enter your age"));
# name = name.title();
# if(name[0] == 'S' and age==22):
#     print("your name starts with s");
# else:
#     print("bhak bsdk");

#exercise 4
# age = int(input("enter your age"));
# if(age<=3):
#     print("you don't need to give any fare");
# elif(age>=4 or age<=10):
#     print("your ticket fare is 150");
# elif(age<=11 or age<=60):
#     print("your ticket fare is 250");
# else:
#     print("your ticket fare is 200");

#in keyword = checks if it is present in the mentioned var
# name = input("enter your name");
# if 's' in name:
#     print("you are king");
# else:
#     print("ayy gandu");

#checks if empty or not
# name = input("enter your name");
# if name:
#     print(f"your name is {name}");
# else:
#     print("enter your name bsdk");

#loops
# i = 1;
# while i<=10:
#     print("smith Bhattarai");
#     i = i + 1;

#practice of the while loop
# number = int(input("enter any number"));
# i = 1;
# while(i<=10):
#     print(f"{number} * {i} = {number*i}");
#     i = i+1;

#sum of any number using while loop(exercise by harshit sir)
# number = int(input("enter any number"));
# i = 0;
# total = 0;
# while(i<=number):
#     total = total + i;
#     i = i + 1;
# print(total);

#exercise 4
# number = input("enter any number");
# total = 0;
# i = 0;
# while(i<len(number)):
#     total += int(number[i]);
#     i += 1;
# print(total);

#exercise 5:
# name = input("enter your name");
# i = 0;
# while(i<len(name)):
#     print(f'{name[i]} : {name.count(name[i])}');
#     i = i + +1;

#for loop
# number = int(input("enter your name"));
# total = 0;
# for k in range(0,number):
#     total += k;
# print(total);

#exercise for loop
# number = input("enter any digit");
# total = 0;
# for i in range(0,len(number)):
#     total += int(number[i]);
# print(total);

#exercise 2 for loop
# name = input("enter your name");
# var_name = ''
# for i in range(0,len(name)):
#     if name[i] not in var_name:
#         print(f"{name[i]} = {name.count(name[i])}");
#         var_name += name[i];

#Break and continue keyword
# for i in range(1,11):
#     if i == 5:
#         break;
#     print (i)

#continue 
# for i in range(1,10):
#     if i == 5:
#         continue;
#     print(i);

#exercise 6
# import random
# number = int(input("guess any number"));
# answer = random.randint(1,100);
# guess = 1;
# game_over = False;

# while not game_over:
#     if(number == answer):
#         print(f"you win in {guess} times");
#         game_over = True;
#     else:
#         if(number<answer):
#             print("too low");
#             guess += 1;
#             number = int(input("guess again"));
#         else:
#             print("too high");
#             guess += 1;
#             number = int(input("guess again"));

#Dry principle--Don't repeat yourself
# import random
# number = int(input("guess any number"));
# answer = random.randint(1,100);
# guess = 1;
# game_over = False;

# while not game_over:
#     if(number == answer):
#         print(f"you win in {guess} times");
#         game_over = True;
#     else:
#         if(number<answer):
#             print("too low");
#             guess += 1;
#             number = int(input("guess again"));
#         else:
#             print("too high");
#             guess += 1;
#             number = int(input("guess again"));

#step argument
# for i in range(1,10,3): 
#     print(i);

# for i in range(10,0,-1):
#     print(i);

#for loop in string
# name = input("enter your name");
# for i in range(len(name)):
#     print(name[i]);

# number = input("enter any number");
# total = 0;
# for i in number:
#     total += int(i);
# print(total);