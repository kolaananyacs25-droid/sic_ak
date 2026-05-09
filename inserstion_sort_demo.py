import insertion_sort 
import sys 
numbers = []
for i in range(1,len(sys.argv)):
    numbers.append(float(sys.argv[i]))
print("Numbers before sorting:",numbers)
insertion_sort.insertion_sort(numbers)
print("Numbers after sorting:",numbers)
for i in range(len(numbers)):
    print("%-4d"%(numbers[i]),end="")
