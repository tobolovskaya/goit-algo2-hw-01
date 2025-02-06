def find_min_max(arr):
    def divide_and_conquer(left, right):
        
        if left == right:
            return arr[left], arr[left]
        
        if right - left == 1:
            if arr[left] < arr[right]:
                return arr[left], arr[right]
            else:
                return arr[right], arr[left]
        
        mid = (left + right) // 2
        min_left, max_left = divide_and_conquer(left, mid)
        min_right, max_right = divide_and_conquer(mid + 1, right)
        
        return min(min_left, min_right), max(max_left, max_right)
    
    if not arr:
        raise ValueError("Масив не може бути порожнім")
    
    return divide_and_conquer(0, len(arr) - 1)

arr = [3, 1, 9, 7, 2, 8, 4, 5, 6]
print(find_min_max(arr))  # (1, 9)
