# 0x01. Lockboxes

## 📚 Project Overview

This project focuses on determining whether a series of locked boxes can all be opened given a set of keys contained within the boxes themselves. It involves list manipulation, graph traversal logic, and efficient algorithm design.

---

## 🧠 Concepts Covered

To solve this problem efficiently, the following programming and algorithmic concepts were applied:

- **Lists and List Manipulation**: Iterating and dynamically accessing list elements.
- **Graph Theory Basics**: Treating boxes and keys as nodes and edges for traversal.
- **Recursion and DFS (Depth-First Search)**: To explore reachable boxes.
- **Set Operations**: Keeping track of visited boxes.
- **Algorithmic Complexity**: Ensuring time and space efficiency.

---

## 📌 Requirements

- Ubuntu 20.04 LTS
- Python 3.4.3
- Use of `vi`, `vim`, or `emacs` editors
- All files must:
  - Be executable
  - End with a new line
  - Begin with the line: `#!/usr/bin/python3`
  - Follow PEP 8 (version 1.7.x)
  - Be properly documented

---

## 🧪 Function Prototype

```python
def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.
    
    Args:
        boxes (list of list of int): A list where each index represents a box,
                                     and the sublist contains keys to other boxes.
    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """

