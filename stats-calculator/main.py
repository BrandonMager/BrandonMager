import array_functions as ar
import hash_functions as hs

lst = [3, 4, 1, 9, 2, 5, 6]

print(ar.get_max(lst))
#prints out 9
print(ar.get_min(lst))
#prints out 1

dic = {"Hi": 21, "Hello": 10, "Greetings": 4, "Hey": 15}
#Hash Table that shows number of people that use welcoming phrase from a sample of 50 people

print(hs.get_max(dic))
#prints out value of 21
