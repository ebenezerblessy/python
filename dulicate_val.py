def find_duplicates(lst):
    seen = set()
    duplicates = set()

    for x in lst:
        if x in seen:
            duplicates.add(x)
        else:
            seen.add(x)

    return list(duplicates)



print(find_duplicates([1, 2, 3, 3, 7, 9, 7]))

#Remove duplicate element in the ist
my_list = [1,1,2,7,3,4,4,5,5,3,3,5,4,1,6]
print(list(set(my_list)))