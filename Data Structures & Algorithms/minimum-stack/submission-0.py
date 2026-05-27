class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
            self.stack.append(val)
            return
        
        if self.min_stack[-1] > val:
            self.min_stack.append(val)
            self.stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])
            self.stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]
