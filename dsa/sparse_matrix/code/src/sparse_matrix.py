# sparse_matrix.py

class Node:
    def __init__(self, row, col, value, next=None):
        self.row = row
        self.col = col
        self.value = value
        self.next = next


class SparseMatrix:
    def __init__(self, numRows, numCols):
        self.numRows = numRows
        self.numCols = numCols
        self.head = None

    def setElement(self, row, col, value):
        if row >= self.numRows or col >= self.numCols:
            raise IndexError("Row or Column index out of bounds")

        # Update or insert
        prev = None
        curr = self.head

        while curr:
            if curr.row == row and curr.col == col:
                if value == 0:
                    if prev:
                        prev.next = curr.next
                    else:
                        self.head = curr.next
                    return
                else:
                    curr.value = value
                    return
            elif (curr.row > row) or (curr.row == row and curr.col > col):
                break
            prev = curr
            curr = curr.next

        if value != 0:
            new_node = Node(row, col, value, curr)
            if prev:
                prev.next = new_node
            else:
                self.head = new_node

    def getElement(self, row, col):
        curr = self.head
        while curr:
            if curr.row == row and curr.col == col:
                return curr.value
            curr = curr.next
        return 0

    def getAllElements(self):
        elements = []
        curr = self.head
        while curr:
            elements.append((curr.row, curr.col, curr.value))
            curr = curr.next
        return elements
