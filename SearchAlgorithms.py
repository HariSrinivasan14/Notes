


#################### Binary Search ####################
def binarySearch(arr, num, minIndex=-1, maxIndex=-1):
    middleIndex = 0
    if maxIndex == -1 and minIndex == -1: # first Call
        middleIndex = (len(arr) - 1) // 2
        minIndex = 0
    elif not maxIndex >= minIndex:
        return -1 # could not find the element
    else:
        middleIndex = minIndex + (maxIndex - minIndex) // 2
 
    if arr[middleIndex] == num:
        return middleIndex
    elif num > arr[middleIndex]: # search in the right subarray
        return binarySearch(arr, num, middleIndex + 1, len(arr) - 1)
    else: # search in the left subarray
        return binarySearch(arr, num, minIndex, middleIndex - 1)  

def main():
    num = 15
    arr = [1,2 ,3, 4, 15]
    result = binarySearch(arr, num)  
    print(result)
    return

main()