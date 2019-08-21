def quick_sort(array, left, right):
    if left >= right:
        return
    low = left
    high = right  # 记录开始和结束的位置。应为后面left、right均会改变。
    key = array[low]
    while left < right:
        while left < right and array[right] > key:
            right -= 1
        array[left] = array[right]                  #将right的值给left，则Rihgt处相当于空了，
        while left < right and array[left] <= key:  #再从前面找比key小的值，填到right处
            left += 1
        array[right] = array[left]                  #将left值给到之前的空right处，则left空了
                                                    #再从后面找大的数填到left
    array[right] = key    #最后right == left，令之等于key即可。
    quick_sort(array, low, left - 1)
    quick_sort(array, left + 1, high)

a = [6,4, 10,3,12, 1,2,11, 5, 9, 13]
quick_sort(a, 0, len(a)-1)
print(a)