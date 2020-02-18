# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    a = 0
    b = 0
    
    # arrA and arrB already sorted, compare the first element of each when merging
    for i in range( 0, elements ):
        # all elements in arrA have been merged
        if a >= len(arrA):    
            merged_arr[i] = arrB[b]
            b += 1
        # all elements in arrB have been merged
        elif b >= len(arrB):  
            merged_arr[i] = arrA[a]
            a += 1
        # next element in arrA smaller, so add to final array
        elif arrA[a] < arrB[b]:  
            merged_arr[i] = arrA[a]
            a += 1
        # else, next element in arrB must be smaller, so add it to final array
        else:  
            merged_arr[i] = arrB[b]
            b += 1
    
    return merged_arr
 

# TO-DO: implement the Merge Sort function below USING RECURSION

def merge_sort( arr ):
    # TO-DO
    if len( arr ) > 1:
        left = merge_sort( arr[ 0 : len( arr ) // 2 ] )
        right = merge_sort( arr[ len( arr ) // 2 : ] )
        arr = merge( left, right ) 
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
