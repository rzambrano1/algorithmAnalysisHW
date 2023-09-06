#!/usr/bin/env python3

import reprlib

class AStack():
    """
    A stack implementation.
    
    ----------
    Attributes
    ----------
    maxSize : int
        The fixed length of the stack.
    components : list()
        A list of items contained in the stack. The last item of the list is at the top of the stack.
    
    -------
    Methods
    -------
    
    >>> a = AStack(5,'foo',1,2,3,4)
    >>> a
    AStack([maxSize=5],['foo', 1, 2, 3, 4])
    
    >>> print(a)
    ['foo', 1, 2, 3, 4]
    
    >>> b = AStack(maxSize=10)
    >>> b
    AStack([maxSize=10],[])
    
    Test of ``__len__()`` method:
    
    >>> len(a)
    5
    
    Test of ``__getitem__()`` method:
    
    >>> a[0]
    'foo'
    
    Test ``isEmpty()`` method:
    
    >>> a.isEmpty()
    False
    
    >>> b = AStack(10)
    >>> b.isEmpty()
    True
    
    Test `` isFull()`` method:
    
    >>> a.isFull()
    True
    
    >>> c = AStack(10,99,0.3,False,'foo',1)
    >>> c.isFull()
    False
    
    Test ``peek()`` method:
    
    >>> a.peek()
    4
    
    >>> c.peek()
    1
    
    >>> b.peek()
    The stack is empty
    
    Test ``push(item)`` method:
    
    >>> a.push('pew')
    The stack is full
    
    >>> c.push('pew')
    [99, 0.3, False, 'foo', 1, 'pew']
    
    Test `` pop()`` method:
    
    >>> a = AStack(5,'foo',1,2,3,4)
    >>> a.pop()
    4
    
    >>> b.pop()
    The stack is empty
    
    """
    
    def __init__(self,maxSize:int,*args):
        """AStack class constructor:
        Provide maxSize as and int followed by the elements of the stack.
        To create an empty stack provide maxSize as an int or as a keyword argument.
        The last item provided to the stack will be considered at the top of the stack."""
        assert type(maxSize) == int, "maxSize has to be an integer"
        assert maxSize >= len(list(args)), "The length of the provided components exceeds the maximum size of the stack"
        self.components = list(args)
        self.maxSize = maxSize
        
    def __repr__(self):
        class_name = type(self).__name__
        comp = reprlib.repr(self.components)
        return '{}([maxSize={}],{})'.format(class_name,self.maxSize,self.components)
    
    def __str__(self):
        return str(self.components)
    
    def __len__(self):
        return len(self.components)
    
    def __iter__(self):
        return iter(self.components)
    
    def __getitem__(self,index):
        return self.components[index]
    
    def isEmpty(self):
        """Return True if the stack is empty, False otherwise"""
        if len(self.components):
            return False
        return True
    
    def isFull(self):
        """Return True if there are maxsize items in the stack"""
        if len(self.components) == self.maxSize:
            return True
        return False
    
    def peek(self):
        """Return the item at the top of stack without removing it from the stack"""
        if self.isEmpty():
            print("The stack is empty")
            return None
        return self.components[len(self.components)-1]
        
    def push(self,item):
        """Add item to the top of stack (TOS) if the stack is not full"""
        if self.isFull():
            print("The stack is full")
            return None
        self.components.append(item)
        return self.components
        
    def pop(self):
        """Remove and return an item from the top of stack. If stack is empty, return None"""
        if self.isEmpty():
            print("The stack is empty")
            return None
        item = self.components.pop()
        return item
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()