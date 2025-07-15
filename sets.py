# Sets - unordered collection of elements, but don't duplicate
 # (''') 3x single quotes comments out multiple rows of line 
my_set = {1, 2, 3, 4, 5}
print(my_set)

my_set.add(6)
print(my_set)

my_set.remove(3)
print(my_set)


#Operations on Sets
#Union (combines two sets and removes duplicate data)

set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1.union(set2)
print(union_set)

#Intersection (finds common elements in two sets)
inter_set = set1.intersection(set2)
print(inter_set)

#Difference (finds the elements present in one but not the other)
diff_set = set1.difference(set2)
print(diff_set)