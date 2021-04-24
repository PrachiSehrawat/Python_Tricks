#1. <<<<<<<<<< MERGE DICTIONARIES >>>>>>>>>>>

# d1 = {"a":1,"b":2}
# d2 = {"c":3,"d":4}
# print(dict(d1, **d2))
# {'a': 1, 'b': 2, 'c': 3, 'd': 4}  will be the output for above code
#
# print(dict(**d1, **d2))
# {'a': 1, 'b': 2, 'c': 3, 'd': 4}  will be the output for above code


#2. <<<<<<<<<<< STRINGS JOINS >>>>>>>>>>

# A = ["Hyy","There","Lets","Learn","Python!"]
# print("_".join(A))
# Hyy_There_Lets_Learn_Python!  will be the output for above code
#
# print(" ".join(A))
# Hyy There Lets Learn Python!  will be the output for above code


#3. <<<<<<<<<< MAX OCCURANCE IN LIST >>>>>>>>>>>

# A = [1,2,2,3,4,5,2,2,6,7,8,2,4]
# print(max(set(A), key = A.count))
# 2    will be the output for above code


# 4. <<<<<<<<<<<< VALUE SWAPPING >>>>>>>>>>>>>

# a, b = 5, 6
# a, b = b, a
# print(a, b)
# 6 5    will be the output for above code

#5. <<<<<<<<<<<< RANGE INTO LIST >>>>>>>>>>>>>>

# A = list(range(1,11))
# print(A)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] will be the output for above code

#6. <<<<<<<<<<<<<<< LIST COMPREHENSION >>>>>>>>>>>>

# sqr = [i**2 for i in range(1,11)]
# print(sqr)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] will be the output for above code


#7. <<<<<<<<< DICTIONARIES COMPREHENSION >>>>>>>>>>>>

# from string import ascii_lowercase
# print({i:j for i, j in enumerate(ascii_lowercase) if i < 6})
# # {0: "a", 1: "b",3: "c",4: "d",5: "e",5: "f",} will be the output for above code
#
# print({j:i for i, j in enumerate(ascii_lowercase) if i < 6})
# # {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6} will be the output for above code
#
# print({i:i for i in range(6)})
# {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5} will be the output for above code


#8. <<<<<<<<<<< ADDING LISTS >>>>>>>>>>>>

# a = [1,2,3,4,5]
# b = [6,7,8,9,10]
# print(a+b)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] will be the output for above code
#
# (a.append(b))
# print(a)
# [1, 2, 3, 4, 5, [6, 7, 8, 9, 10]] will be the output for above code

# a = [1,2,3,4,5]
# b = [6,7,8,9,10]
# print([i+j for i, j in zip(a, b)])
# [7, 9, 11, 13, 15] will be the output for above code

#9. <<<<<<<<<<<< EXTRACTION OF NESTED LISTS >>>>>>>>>>>>

# list = [[1],[2],[3],[4],[5]]
# print(sum(list, []))
# # [1, 2, 3, 4, 5] will be the output for above code

































