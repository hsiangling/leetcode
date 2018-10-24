class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.MyStack = []
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.MyStack.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.MyStack.pop()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.MyStack[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        """
        if len(self.MyStack) == 0:
            return True 
        else:
            return False
        """
        return len(self.MyStack) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()