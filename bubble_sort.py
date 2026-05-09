def bubbleSort(n,elements):
    for i in range(n-2):
        for j in range(n-2-i):
            if elements [j] > elements[j+1]:
                elements[j],elements[j+1]= elements[j+1],elements[j]
return elements 
