def quicksort(array):
    if len(array)<2:
        return array
    else:
        pivot=array[0]
        lessPivot=[i for i in array[1:] if i<=pivot]
        BiggerPivot=[i for i in array[1:] if i>pivot]
        return quicksort(lessPivot)+[pivot]+quicksort(BiggerPivot)

print (quicksort([6,4,7,8,2,3]))

print (quicksort(['o','p','u','a','c','b']))
