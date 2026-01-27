# Valid Sudoku

You are given a 9 x 9 Sudoku board `board`. A Sudoku board is valid if the following rules are followed:

1. Each row must contain the digits `1-9` without duplicates.
2. Each column must contain the digits `1-9` without duplicates.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits `1-9` without duplicates.

Return `true` if the Sudoku board is valid, otherwise reutrn `false`

Note: A board does not need to be full or be solvable to be valid.

## Example

```python
Input: board =
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

Output: True
```

```python
Input: board =
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

Output: False
# There are two 1's in the top left square
```

## Constraints

- `board.length == 9`
- `board[i].length == 9`
- `board[i][j]` is a digit `1-9` or `'.'`.

# My Solution

Sudoku problems are always a bit tricky for me because you have to not only think about an array as a 2D object, but include the sub-boxes. The key to solving this problem lies in how to map an entry to a sub box. This can be done using floor division `//`. You can take the element at `board[i//3][j//3]` as there are 3 x 3 sub boxes. For numbers `0-2` `i` will map to `0`, `3-5` will map to `1`, and `6-8` will map to `2`. This allows us to check every corresponding sub box accurately. The only thing left to do is to scan each row, column, and square for each `board[i][j]`, and if it is found in any of the three return `False`, otherwise add the value to each of the three. If we ever leave our loop, then we know that no duplicates have been found and can return `True`.

## Code

```python
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                elif ((board[i][j] in rows[i]) or
                (board[i][j] in columns[j]) or
                (board[i][j]in squares[i//3, j//3])):
                    return False
                rows[i].add(board[i][j])
                columns[j].add(board[i][j])
                squares[i//3, j//3].add(board[i][j])
        return True
```

## Time & Space Complexity

This algorithm runs in O(n<sup><small>2</small></sup>)
