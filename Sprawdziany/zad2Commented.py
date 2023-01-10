# This class represents a node in a binary tree
class Node:
    # Constructor method to initialize a new Node object
    def __init__(self, data):
        # The data value stored in the node
        self.data = data
        # A reference to the left child node
        self.left = None
        # A reference to the right child node
        self.right = None


# This function inserts a data value into a binary tree rooted at the given node
def insert(data, root):
    # If the root node is None, create a new Node object with the given data and return it
    if root is None:
        return Node(data)
    # If the data value is greater than the root node's data, insert it into the right subtree
    if root.data < data:
        root.right = insert(data, root.right)
    # Otherwise, insert it into the left subtree
    else:
        root.left = insert(data, root.left)
    # Return the root node
    return root


# This function appends the data values stored in the nodes of a binary tree rooted at the given node to the given
# list in sorted order
def PrintSorted(root, l):
    # If the root node is not None, visit the left child, the root, and then the right child
    if root:
        PrintSorted(root.left, l)
        l.append(root.data)
        PrintSorted(root.right, l)
    # Return the list
    return l


# This function returns the value in the given list that is closest to the target value
def find_closest(target, values):
    # Initialize the closest value and the difference between the target value and the closest value to the first
    # value in the list
    closest = None
    closest_diff = abs(target - values[0])
    # Iterate through the list of values
    for i in range(1, len(values)):
        # Calculate the difference between the target value and the current value
        diff = abs(target - values[i])
        # If the difference is smaller than the current closest difference, update the closest value and the difference
        if diff < closest_diff:
            closest_diff = diff
            closest = values[i]
    # Return the closest value
    return closest


# The main function reads a value and a number of values from the user, stores them in a list, and then constructs a
# binary tree with the values in the list It then prints the value in the tree that is closest to the value entered
# by the user
def main():
    value = int(input())
    n = int(input())
    values = []
    for i in range(n):
        values.append(int(input()))
    # Return the value and the list of values
    return value, values


# If this script is run as the main script, execute the main function
if __name__ == '__main__':
    value, values = main()
    # Create the root node of the binary tree with the first value in the list
    root = Node(values[0])
    # Insert the remaining values into the tree
    for i in range(1, len(values)):
        root = insert(values[i], root)
    # Get the sorted list of values in the tree
