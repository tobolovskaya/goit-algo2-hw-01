### Explanation of the Algorithm:
- **Divide**: The array is split into two parts until only one or two elements remain.
- **Conquer**: The minimum and maximum elements are found recursively in each subpart.
- **Combine**: The results from the two subarrays are merged by taking the smallest of the found minimums and the largest of the found maximums.

### 📝 Acceptance Criteria:
✅ The function accepts an array of numbers of any length.  
✅ A recursive approach is used.  
✅ The function returns a tuple of values (minimum, maximum).  
✅ Time complexity is **O(n)** since each element is examined exactly once.

This implementation ensures efficiency even for large input arrays. 🚀