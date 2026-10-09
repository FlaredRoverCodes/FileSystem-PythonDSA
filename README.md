# FileSystem-PythonDSA
A lightweight, hierarchical Python implementation of a file management architecture using a Binary Search Tree (BST). Models directories and files as tree nodes, leveraging an in-order traversal algorithm to maintain a naturally alphabetical sorting index without sorting overhead.


- BST Properties Implemented: Automatically branches left for names alphabetically preceding the current directory node, and right for subsequent names.

- Alphabetical Indexing: Lists all active file tracks instantly sorted via In-order Traversal (O(n) time complexity).

- Robust Structural Node Deletion: Correctly preserves relative child balance pointers whether a targeted node has zero, one, or two structural children.
