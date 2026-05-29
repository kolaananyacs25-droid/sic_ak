import selection_sort as sel_sort
import sys
numbers = []
for i in range(1, len(sys.argv)):
    numbers.append(float(sys.argv[i]))
print("Numbers before sorting:\n", numbers)

sel_sort.selection_sort(numbers)
print("Numbers after sorting:")
for i in range(len(numbers)):
    print("%-4d" % (numbers[i]), end="")