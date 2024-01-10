# def add(a,b):
#     sum = a + b;
#     return sum;
# a = int(input("enter the value of a"));
# b = int(input("enter the value of b"));
# print(add(a,b));

#function practice
# def last_name(name):
#     return name[-1];
# print(last_name("smith"));

# def is_even(number):
#     if(number%2==0):
#         return "even";
#     else:
#         return "odd";
# number = int(input("enter the number"));
# print(is_even(number));

#exercise first function
# def is_greatest(a,b):
#     if(a>b):
#         print("a is greater");
#     else:
#         print("b is greater");
# a = int(input("enter the first number"));
# b = int(input("enter the second number"));
# print(is_greatest(a,b));

#exercise second
# def is_palindrome(word):
#     rev_word = word[::-1];
#     if(rev_word == word):
#         print(f"{word} is palindrome");
#     else:
#         print(f"{word} is not palindrome");
# word = input("enter the word");
# is_palindrome(word);

#fibonacci series
# def fibonacci(number):
#     a = 0;
#     b = 1;
#     if number == 1:
#         print(a);
#     elif number == 2:
#         print(a,b);
#     else:
#         print(a,b, end=" ");
#         for i in range(number-2):
#             c = a + b;
#             a = b;
#             b = c;
#             print(b,end = " ");
# number = int(input("enter the number"));
# fibonacci(number);

# #default parameters 
# def user_info(first_name,last_name,age = 22):
#     print("your first name is ",first_name);
#     print("your last name  is ",last_name);
#     print("you age is ",age);
# first_name = input("enter your first name");
# last_name = input("enter your last name");
# user_info(first_name,last_name);
# #we should make default parameter at the last only

#variable scope
#scope of variable inside and outside the function - the scope of variable is only inside function
x = 10;
def fun1():
    x = 7; #local variable
    return x;
def fun2():
    y = 20;
    print (y);
fun2();
print(x);