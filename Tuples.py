#tuple is a data structure that can store any data type like list 
#tuples are immutable
#no append,no insert,no pop,no remove

#methods in tuples
#count
#index
#len
#slicing

# numbers = (1,2,3,4,5)
# print(numbers[:2])

#more about tuples
#looping in tuples

# mixed = (1,2,3,4,5);
# for i in mixed:
#     print(i)

#create tuple with one element(use comma after the element)
# num = (1,)
# print(type (num))

#tuple unpacking
# name = ("smith","Arpan","Narayan","samjhana");
# name1,name2,name3,name4 = name
# print(name1)

#list inside tuplee(we can use any list method in the list of the tuple)
# name = ("smith","Arpan",["Narayan","samjhana"]);
# print(name[2])

#min,max,sum
# mixed = (1,2,3,4,5);
# print(min(mixed))
# print(max(mixed))
# print(sum(mixed))

# info = ("smith",22,"btech",['6th sem','7th sem','8th sem']);
# print(info[3].pop());


def fun(year):
    if year%4 == 0:
        print(f"{year} is a leap year");
    else:
        print(f"{year} is not a leap year")
yr = int(input('Enter the year '));
fun(yr);