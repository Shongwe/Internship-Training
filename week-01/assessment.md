# Week 01 Assessment

## 1. Problem Understanding

### FizzBuzz

**Can I explain FizzBuzz in my own words?**

Yes. FizzBuzz requires generating a sequence from 1 to `n`. Numbers divisible by both 3 and 5 are represented as `"FizzBuzz"`, numbers divisible only by 3 as `"Fizz"`, numbers divisible only by 5 as `"Buzz"`, and all other numbers remain as their numeric string representation.

### Palindrome Number

**Can I explain the key insight?**

Yes. A palindrome number reads the same forwards and backwards. The key idea is to compare the original number with its reversed representation, while handling cases such as negative numbers appropriately.

### Two Sum

**Why is a hash table useful?**

A hash table allows previously seen values to be looked up efficiently. For each number, I calculate its complement using:

```text
complement = target - number
```

If the complement has already been seen, the two required indices have been found.

This improves the typical brute-force O(n²) solution to O(n) time with O(n) additional space.

---

## 2. Code Quality

* [x] Followed PEP 8 style guidelines
* [x] Used meaningful variable names
* [x] Added type hints
* [x] Added docstrings to functions
* [x] Added comments where they improve understanding
* [x] Kept solutions focused on the requirements of each problem

### Code Quality Reflection

I focused on keeping the implementations readable and following consistent Python conventions. I also used descriptive names such as `complement`, `visited`, `current`, `prev1`, and `prev2` instead of generic variable names.

---

## 3. Testing

* [x] Tested the provided examples
* [x] Tested edge cases
* [x] Tested duplicate values where applicable
* [x] Tested negative numbers where applicable
* [x] Tested empty inputs where applicable
* [x] Tested single-element inputs where applicable
* [x] Used `pytest` to run the test suite

### Testing Reflection

Writing tests helped identify mistakes in my initial Two Sum implementation. In particular, the tests exposed that my brute-force implementation could use the same index twice and did not correctly process the final element.

This demonstrated the value of testing beyond the basic examples provided by the problem.

---

## 4. Algorithmic Approaches

| Problem            | Approach                   |     Time | Space |
| ------------------ | -------------------------- | -------: | ----: |
| FizzBuzz           | Iteration and conditionals |     O(n) |  O(n) |
| Palindrome Number  | Number/string reversal     |     O(n) |  O(n) |
| Two Sum            | Hash table                 |     O(n) |  O(n) |
| Merge Sorted Array | Two pointers from the end  | O(m + n) |  O(1) |
| Climbing Stairs    | Space-optimized DP         |     O(n) |  O(1) |

---

## 5. End-of-Week Checklist

### Completeness

* [x] All 5 problems are solved
* [x] Each solution has test cases
* [x] Each solution includes a docstring
* [x] Test cases pass

### Code Quality

* [x] PEP 8 style followed
* [x] Variable names are meaningful
* [x] Complex logic has explanatory comments
* [x] No unnecessary magic numbers

### Testing

* [x] Provided examples tested
* [x] Edge cases considered
* [x] Appropriate error/boundary cases tested

### Documentation

* [x] Each solution documents its purpose
* [x] Time complexity considered
* [x] Space complexity considered
* [x] Important assumptions documented

---

## 6. Code Review Self-Assessment

### Correctness

The solutions were tested against the provided examples and additional edge cases. Test failures were used to identify and correct implementation errors.

### Efficiency

I learned to distinguish between solutions that simply work and solutions that satisfy the intended efficiency requirements.

For example:

* Two Sum uses a hash table to achieve O(n) time.
* Merge Sorted Array uses the extra space provided in `nums1` to achieve O(1) auxiliary space.
* Climbing Stairs stores only the previous two results instead of maintaining a complete DP array.

### Style and Clarity

I followed PEP 8 conventions, used type hints and docstrings, and tried to keep variable names descriptive.

### Understanding

I can explain the main approaches used in the solutions and understand why the recommended algorithms are more efficient than their naive alternatives.

---

## 7. Areas for Improvement

One area I would like to improve is recognizing algorithmic patterns more quickly.

I can implement solutions once I understand the required approach, but I want to become faster at identifying patterns such as:

* Hash table lookup
* Two-pointer techniques
* Dynamic programming
* Recursion and memoization

I also want to improve my ability to reason about edge cases before writing the implementation rather than discovering them primarily through failed tests.

---

## 8. Overall Assessment

Week 01 provided a strong foundation in algorithmic problem solving, Python code quality, testing, and complexity analysis.

The biggest lesson was that solving a problem is not only about producing the correct output. The solution should also be understandable, appropriately tested, and efficient according to the constraints of the problem.

**Overall status:** Completed

**Ready for Week 02:** Yes
