# Week 01 Reflection

## Overview

During Week 01 of the training programme, I focused on strengthening my understanding of fundamental algorithms, problem-solving techniques, and writing clean, maintainable Python code.

A major focus was learning how to comply with the organization of the code and the styling recommended.

## Key Topics Covered

### 1. FizzBuzz

I started with the FizzBuzz problem to practise basic Python syntax, loops, conditional statements, functions, type hints, and documentation.

I also focused on following **PEP 8** conventions and writing clear docstrings.

### 2. Two Sum

The Two Sum exercise introduced the difference between a brute-force solution and an optimized solution using a dictionary.

I implemented:

* A brute-force solution using nested loops.
* A dictionary-based solution using complement lookups.

The brute-force approach has **O(n²)** time complexity, while the dictionary approach improves this to **O(n)** time complexity at the cost of **O(n)** additional space.

This exercise helped me understand the importance of considering both time and space complexity when solving algorithmic problems.

### 3. Merge Sorted Array

The Merge Sorted Array exercise introduced the **two-pointer technique** and in-place array manipulation.

The key insight was to work backwards from the end of the arrays so that existing elements in `nums1` are not overwritten before they are processed.

The recommended solution achieves:

* **Time Complexity:** O(m + n)
* **Space Complexity:** O(1)

This helped me better understand how problem constraints can guide the choice of an algorithm.

### 4. Climbing Stairs

The Climbing Stairs exercise introduced **dynamic programming** and the relationship between recursive problems and the Fibonacci sequence.

I learned that the number of ways to reach a step can be calculated using the previous two results:

```text
ways(n) = ways(n - 1) + ways(n - 2)
```

I implemented the space-optimized dynamic programming approach, which has:

* **Time Complexity:** O(n)
* **Space Complexity:** O(1)

## Testing

Throughout the exercises, I created separate test files using `pytest` to verify that the solutions behaved correctly.

I tested:

* Standard inputs
* Edge cases
* Negative numbers
* Duplicate values
* Empty arrays
* Single-element inputs
* Larger inputs
* Cases designed to expose common implementation mistakes

Writing tests helped me identify issues in my initial implementations and understand why the corrections were necessary.

## Key Lessons Learned

The main lessons I took from Week 01 were:

1. **Start with a simple solution and then optimize it.**
2. **Understand the constraints before choosing an algorithm.**
3. **Hash tables can significantly improve lookup performance.**
4. **Two-pointer techniques can solve array problems efficiently.**
5. **Dynamic programming can eliminate repeated calculations.**
6. **Testing is essential for identifying edge cases and implementation errors.**
7. **Clean code matters**, including meaningful variable names, type hints, docstrings, and PEP 8 formatting.
8. **Understanding why an algorithm works is more important than simply memorizing the implementation.**

## Challenges

One of the challenges I encountered was identifying mistakes in the brute-force implementation of Two Sum. My initial implementation allowed the same index to be used twice and did not correctly include the final element of the array.

The test failures made the problem easier to identify because they showed exactly where the implementation did not satisfy the requirements.

This reinforced the importance of using tests not only to confirm that code works, but also to expose incorrect assumptions in the implementation.

## Reflection

Week 01 gave me a stronger foundation in algorithmic problem solving. I became more comfortable breaking problems down into smaller parts, considering complexity, and using tests to validate my solutions.

I also learned that an effective solution is not necessarily the first solution that works. After creating a working approach, it is important to ask whether it can be made more efficient, readable, or maintainable.

Going forward, I want to continue improving my ability to recognize common algorithmic patterns such as **hash tables, two pointers, and dynamic programming**, while maintaining clean coding practices and writing reliable tests.
