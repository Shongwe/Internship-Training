# Week 2 Reflection

## Overview

This week focused on developing problem-solving skills through array manipulation, bit manipulation, graph traversal, and algorithm optimization. The exercises helped me strengthen my understanding of how to break problems into smaller steps and implement solutions using appropriate data structures and algorithms.

## Exercises Completed

### Pascal's Triangle

I implemented Pascal's Triangle using nested lists. The solution builds each row from the previous row by adding adjacent elements. This exercise improved my understanding of nested data structures, indexing, and referencing previously generated results.

The solution has a time complexity of O(n²) and a space complexity of O(n²) because the complete triangle is stored.

### Rising Temperature

I implemented the Rising Temperature problem using two approaches. The first approach uses nested loops to search for the next warmer temperature and has O(n²) time complexity.

I also implemented the optimized stack-based solution. This solution processes the temperatures from right to left and uses a stack to efficiently identify the next warmer day. Its time complexity is O(n), which helped me understand how choosing an appropriate data structure can significantly improve algorithm performance.

I also created tests for increasing, decreasing, equal, single-day, empty, and general temperature inputs.

### Reverse Bits

I implemented a bit-manipulation solution that reverses all 32 bits of an unsigned integer. The implementation repeatedly extracts the least significant bit using the AND operation and builds the reversed result using bit shifting.

This exercise improved my understanding of bitwise operators such as `&`, `<<`, and `>>`. Since the algorithm always processes exactly 32 bits, its time and space complexity are both O(1).

### Number of 1 Bits

For the Number of 1 Bits problem, I implemented Brian Kernighan's algorithm. The expression `n &= n - 1` removes the rightmost set bit from the number, allowing the algorithm to count the number of `1` bits efficiently.

This exercise helped me understand how bit manipulation can be used to solve problems without converting numbers into strings or iterating through unnecessary bits.

### Next Permutation

I studied the Next Permutation problem, which requires modifying an array in-place to produce the next lexicographically greater permutation. The algorithm finds the rightmost ascending pair, swaps the appropriate elements, and reverses the remaining suffix.

This exercise improved my understanding of in-place array manipulation and the importance of identifying patterns within an ordered sequence.

## Testing

I continued using `pytest` to test my solutions. I created separate test files for the exercises and included both the provided examples and additional edge cases.

The additional test cases included:

- Empty input
- Single-element input
- Increasing sequences
- Decreasing sequences
- Duplicate values
- Boundary cases
- Values containing multiple set bits

Using automated tests helped me verify that my implementations worked correctly beyond the main examples provided in the exercises.

## Key Lessons Learned

The main lessons I learned this week were:

1. **Choosing the right data structure matters.** The stack-based Rising Temperature solution demonstrated how an appropriate data structure can reduce an algorithm from O(n²) to O(n).

2. **Bit manipulation can provide efficient solutions.** Reverse Bits and Number of 1 Bits helped me become more comfortable with bitwise operators and binary representations.

3. **Edge cases are important.** Testing empty inputs, single values, duplicate values, and boundary cases helps identify problems that may not appear in basic examples.

4. **In-place algorithms can reduce memory usage.** Next Permutation demonstrated how an array can be modified without creating additional arrays.

5. **Automated testing improves confidence.** Writing pytest tests alongside the solutions made it easier to verify that changes did not break existing functionality.

## Challenges

The main challenge this week was understanding algorithms that operate at a lower level, particularly bit manipulation and the stack-based approach to Rising Temperature. I initially found the operations such as `n & 1`, `n >>= 1`, and `n &= n - 1` less intuitive than standard arithmetic operations.

Another challenge was managing pytest test discovery. Running pytest from the Week 2 root directory caused tests from different exercises to be collected together, which resulted in an import error from the Path Sum exercise. I learned that individual test files can be executed directly when debugging a specific exercise.

## Improvements for Next Week

For the next stage of the training, I want to improve my ability to recognize common algorithmic patterns before writing code. In particular, I want to become more comfortable identifying when to use techniques such as hash maps, stacks, queues, recursion, and two-pointer approaches.

I will also continue writing tests alongside my implementations rather than treating testing as a separate final step.

## Conclusion

Overall, Week 2 strengthened my algorithmic problem-solving and testing skills. I gained more experience with nested data structures, array manipulation, stacks, graph concepts, and bitwise operations. I also developed a better understanding of how algorithmic complexity affects the efficiency of a solution and why testing edge cases is important when implementing algorithms.