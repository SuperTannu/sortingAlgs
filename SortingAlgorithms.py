

#bubble sort

def bubsort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1]=arr[j+1],arr[j]

def selects(arr):
    a=1
    b=0
    for i in range(b,len(arr)):
        for j in range(a,len(arr)):
            if arr[j]<arr[i]:
                arr[i],arr[j]=arr[j],arr[i]
        b+=1
        a+=1




from collections import deque
def dubsel(arr):
    arr2=deque()
    n=len(arr)

    a = 1
    b = 0
    for i in range(b, len(arr)):
        for j in range(a, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
        b += 1
        a += 1

    for k in range(-len(arr),-b):
        for l in range(-len(arr),-a):
            if arr[l]> arr[k]:
                arr[k], arr[l] = arr[l], arr[k]
        b -= 1
        a -= 1



def partition(array,start,stop):
    pivot = start
    for i in range(start+1, stop+1):
        if array[i]<=array[start]:
            pivot+=1
            array[i], array[pivot]=array[pivot],array[i]
    array[pivot],array[start]=array[start],array[pivot]
    return pivot

def quicksort(arr, start=0, stop=None):
    if stop is None:
        stop =len(arr)-1
    def qs(arr,start,stop):
        if start>=stop:
            return
        pivot=partition(arr,start,stop)
        qs(arr, start,pivot-1)
        qs(arr, pivot+1, stop)
    return qs(arr,start,stop)

def mergesort(arr):

    if len(arr)>2:
        div = len(arr) // 2
        before = arr[:div]
        after = arr[div:]

        quicksort(before)
        quicksort(after)

        i=0
        j=0
        k=0

        while i<len(before) and j<len(after):
            if before[i]<=after[j]:
                arr[k]=before[i]
                i+=1
            else:
                arr[k]=after[j]
                j+=1

            k+=1

        while i<len(before):
            arr[k]=before[i]
            i+=1
            k+=1

        while j<len(after):
            arr[k]=after[j]
            j+=1
            k+=1



#a=[7,45,9,2,10,3,1,54,36,21,5,4]

#print(f'original list:{a}')

#bubsort(a)
#print(f'bubble sort:{a}')

#selects(a)
#print(f'select  sort:{a}')

#dubsel(a)
#print(F'double select sort:{a}')

#quicksort(a)
#print(f'quick sort:{a}')

#mergesort(a)
#print(f'merge sort:{a}')