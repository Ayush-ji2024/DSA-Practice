<h1 align="center">🧠 DSA Practice — Striver's A2Z Sheet in C++</h1>

<p align="center">
  <b>Clean, well-documented C++ solutions to Striver's A2Z DSA Sheet,<br/>solved on LeetCode, GeeksforGeeks & takeUforward and pushed here every day.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Language-C++17-00599C?style=for-the-badge&logo=cplusplus&logoColor=white"/>
  <img src="https://img.shields.io/badge/Roadmap-Striver's%20A2Z-FF6B35?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Solved-0%20%2F%20455-brightgreen?style=for-the-badge"/>
  <img src="https://img.shields.io/github/last-commit/Ayush-ji2024/DSA-Practice?style=for-the-badge&color=blueviolet&label=Last%20Solved"/>
</p>

<p align="center">
  <a href="https://leetcode.com/u/Ayush_JI2024/"><img src="https://img.shields.io/badge/LeetCode-Profile-FFA116?style=for-the-badge&logo=leetcode&logoColor=black"/></a>
  <a href="https://github.com/Ayush-ji2024"><img src="https://img.shields.io/badge/GitHub-Ayush--ji2024-181717?style=for-the-badge&logo=github&logoColor=white"/></a>
</p>

---

## 👋 About This Repository

I'm **Ayush Kumar**, a B.Tech CSE student (2023–2027) preparing for **software engineering roles at product-based companies**.
This repository is my public record of working through **Striver's A2Z DSA Sheet** — from the basics to Graphs and Dynamic Programming.

**What you'll find in every solution:**

- ✅ An **accepted** solution (verified on the original platform)
- 🧩 The **approach** explained in my own words
- ⏱️ **Time & space complexity**
- 🔗 A **link** to the original problem

---

## 📈 LeetCode Stats

<p align="center">
  <img src="https://leetcard.jacoblin.cool/Ayush_JI2024?theme=dark&font=Fira%20Code&ext=heatmap" alt="LeetCode Stats"/>
</p>

---

## 📊 Progress Tracker

| Step | Topic | Solved | Total | Status |
|:-:|---|:-:|:-:|:-:|
| 01 | [Learn the Basics](./Step-01-Basics) | 0 | 31 | 🟡 |
| 02 | [Important Sorting Techniques](./Step-02-Sorting) | 0 | 7 | ⚪ |
| 03 | [Arrays (Easy → Medium → Hard)](./Step-03-Arrays) | 0 | 40 | ⚪ |
| 04 | [Binary Search (1D, 2D, Search Space)](./Step-04-Binary-Search) | 0 | 32 | ⚪ |
| 05 | [Strings (Basic & Medium)](./Step-05-Strings) | 0 | 15 | ⚪ |
| 06 | [Linked List](./Step-06-Linked-List) | 0 | 31 | ⚪ |
| 07 | [Recursion (Pattern-wise)](./Step-07-Recursion) | 0 | 25 | ⚪ |
| 08 | [Bit Manipulation](./Step-08-Bit-Manipulation) | 0 | 18 | ⚪ |
| 09 | [Stack & Queues](./Step-09-Stack-Queue) | 0 | 30 | ⚪ |
| 10 | [Sliding Window & Two Pointers](./Step-10-Sliding-Window) | 0 | 12 | ⚪ |
| 11 | [Heaps](./Step-11-Heaps) | 0 | 17 | ⚪ |
| 12 | [Greedy Algorithms](./Step-12-Greedy) | 0 | 16 | ⚪ |
| 13 | [Binary Trees](./Step-13-Binary-Trees) | 0 | 39 | ⚪ |
| 14 | [Binary Search Trees](./Step-14-BST) | 0 | 16 | ⚪ |
| 15 | [Graphs](./Step-15-Graphs) | 0 | 54 | ⚪ |
| 16 | [Dynamic Programming](./Step-16-Dynamic-Programming) | 0 | 56 | ⚪ |
| 17 | [Tries](./Step-17-Tries) | 0 | 7 | ⚪ |
| 18 | [Strings (Hard)](./Step-18-Strings-Hard) | 0 | 9 | ⚪ |
| | **Total** | **0** | **455** | |

> ⚪ Not Started · 🟡 In Progress · 🟢 Completed

---

## 🧩 Patterns I've Mastered

*Ticked when the related step is fully completed.*

- [ ] Hashing & Frequency Counting
- [ ] Two Pointers & Sliding Window
- [ ] Prefix Sum & Kadane's Algorithm
- [ ] Binary Search on Answer
- [ ] Fast & Slow Pointers (Linked List)
- [ ] Recursion & Backtracking
- [ ] Monotonic Stack / Queue
- [ ] Heap / Priority Queue
- [ ] Tree Traversals (DFS / BFS)
- [ ] Graph Algorithms (BFS, DFS, Topo Sort, Dijkstra, DSU, MST)
- [ ] Dynamic Programming (1D, 2D, Subsequences, Strings, Stocks, Partition)
- [ ] Tries

---

## 📁 Repository Structure

## 📁 Folder & File Naming Convention

*Example layout.* Folders follow the sheet's steps; files follow the sheet's order within each step.

```
DSA-Practice/
├── Step-01-Basics/
│   ├── 01_count_digits.cpp
│   └── 02_reverse_a_number.cpp
├── Step-03-Arrays/
│   ├── 01_largest_element.cpp
│   └── ...
├── ...
└── README.md
```

**File naming:** `<number-in-step>_<problem_name>.cpp`

### Solution Template

```cpp
/*
 Problem  : Largest Element in an Array
 Sheet    : Striver A2Z — Step 3, Lec 1 (Easy)
 Platform : GeeksforGeeks
 Link     : <problem link>

 Approach : Traverse the array once and keep track of the maximum seen so far.
 Time     : O(n)
 Space    : O(1)
*/

class Solution {
public:
    int largest(vector<int>& arr) {
        int mx = arr[0];
        for (int x : arr) mx = max(mx, x);
        return mx;
    }
};
```

---

## 🔁 My Workflow

```
Pick next problem from the sheet  ➜  Solve & get "Accepted" on the platform
        ➜  Save the solution here with approach + complexity  ➜  Commit & push
```

1. Understand the problem and try a **brute-force** idea first
2. **Optimise** and reason about time & space complexity
3. Get it **Accepted** on the original platform
4. Document the approach and push it here — **the same day**

---

## 🙏 Acknowledgements

Problem list and order are from **[Striver's A2Z DSA Sheet](https://takeuforward.org/dsa/strivers-a2z-sheet-learn-dsa-a-to-z)** by Raj Vikramaditya (takeUforward).
All solutions and explanations in this repository are my own.

<p align="center">⭐ If this repository helps you, consider giving it a star!</p>