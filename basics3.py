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