# 🧠 Tower of Hanoi – Learning Recursion

This project is a Python implementation of the classic **Tower of Hanoi** problem, created as a personal challenge to understand and practice **recursion**.

## 🎯 Why I Made This

I built this to get hands-on experience with recursion which is a concept that feels confusing. I thought that solving the Tower of Hanoi would be a great way to train my brain to think recursively, and this project helped me finally understand how recursive calls work step-by-step.

## 🗂️ How It Works

The function moves `N` amount of disks from one rod to another, following these rules:
- Only one disk can be moved at a time
- A larger disk can't be placed on top of a smaller one
- A third rod must be used to help transfer the disks

The recursive solution follows this strategy:
1. Move `N-1` disks from source → helper
2. Move disk `N` from source → destination
3. Move the `N-1` disks from helper → destination

## 💡 Minimum Moves Formula

The minimum number of moves to solve Tower of Hanoi is:

2**N - 1

## 🚀 How to Run

1. Clone the repo
2. Run the script:
```bash
python hanoi.py
