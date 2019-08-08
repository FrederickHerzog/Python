#Frederick Herzog
#Bubble Sort
import random as r

def bubble_sort_recursive(listt): 
    for i, num in enumerate(listt): 
        try: 
            if listt[i+1] < num: 
                listt[i] = listt[i+1] 
                listt[i+1] = num 
                bubble_sort(listt) 
        except IndexError: 
            pass
    return listt 

def bubble_sort(unsorted_list):
    length = len(unsorted_list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(length):
            if unsorted_list[i] > unsorted_list[i+1]:
                sorted = False
                unsorted_list[i], unsorted_list[i+1] = unsorted_list[i+1], unsorted_list[i]
            
# TEST
my_list = [r.uniform(0,100) for n in range(20)]
print("UNSORTED LIST:\n")
print(my_list)
sortedlist = bubble_sort_recursive(my_list)
print()
print("SORTED LIST:\n")
print(sortedlist)
