// https://leetcode.com/problems/trapping-rain-water/
// Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water
// it can trap after raining.
// Constraints:
//    n == height.length
//    1 <= n <= 2 * 10^4
//    0 <= height[i] <= 10^5


func max(a int, b int) int {
    if a > b {
        return a
    }
    return b
}

//  Time Complexity: O(n)
//  Auxiliary Space: O(1)
func trap(height []int) int {
    out := 0
    i, j := 1, len(height) - 1
    max_i, max_j := height[0], height[j]

    for i <= j {
        max_i = max(max_i, height[i])
        max_j = max(max_j, height[j])

        if max_i < max_j {
            out += max_i - height[i]
            i += 1
        } else {
            out += max_j - height[j]
            j -= 1
        }
    }

    return out
}