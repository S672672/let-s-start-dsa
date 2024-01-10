#list - list is the data structure that is the collection of items
#we can store anythig in the lists int,float,string

# numbers = [1,2,3,4];
# print(numbers);

# words = ["smith","bhattarai"];
# print(words);

mixed = [1,2,3,4,5,"six","seven",2.3,None];
print(mixed);
print(mixed[:2]); #slicing is same as index
mixed[1] = 9;
print(mixed);
mixed[1:] = "hundred";
print(mixed);