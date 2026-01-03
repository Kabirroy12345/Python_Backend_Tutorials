#Sets are similar to lists but are unordered and cannot contain duplicates

#1)Basic set
# my_set={1,2,3,4,5,6,1,2,3} #duplicates are removed
# print(my_set)
# print(len(my_set))

#2)Looping over the set
# my_set={1,2,3,4,5,6,1,2}
# for i in my_set:
#     print(i)

#3)Set methods
# my_set={1,2,3,4,5,6,1,2}
# my_set.discard(3)
# print(my_set)
# my_set.add(8)
# print(my_set)
# my_set.update([7,8,9,0,43])
# print(my_set)

#Tuple are ordered but unchangeable(mutable)
# my_tuple=(1,2,3,4,3)
# print(my_tuple)
# my_tuple[1]=6
# print(my_tuple)  #cant access
