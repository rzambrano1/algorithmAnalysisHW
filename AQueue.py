#!/usr/bin/env python3

import reprlib

class AQueue :
    """
    A queue implementation.
    
    ----------
    Attributes
    ----------
    maxSize : int
        The fixed length of the queue.
    components : list()
        A list of items contained in the queue. The item at index [0] is at the front/head, the last item is at the rear/tail.
    
    -------
    Methods
    -------
    
    >>> a = AQueue(5,'dog','bear','cow','horse','elephant')
    >>> a
    AQueue([maxSize=5],['dog', 'bear', 'cow', 'horse', 'elephant'])

    >>> b = AQueue(10)
    >>> b
    AQueue([maxSize=10],[])

    >>> c = AQueue(10,33,42,'Galaxy','Supercomputer',45,'Arrival')
    >>> c
    AQueue([maxSize=10],[33, 42, 'Galaxy', 'Supercomputer', 45, 'Arrival'])

    Test ``peekFront()`` method:    
    
    >>> a.peekFront()
    'dog'

    >>> b.peekFront()
    The queue is empty

    >>> c.peekFront()
    33
    
    Test ``peekRear()`` method:     
    
    >>> a.peekRear()
    'elephant'

    >>> b.peekRear()
    The queue is empty

    >>> c.peekRear()
    'Arrival'
    
    Test ``isEmpty()`` method:      
    
    >>> a.isEmpty()
    False

    >>> b.isEmpty()
    True
    
    Test ``isFull()`` method:       
    
    >>> a.isFull()
    True

    >>> b.isFull()
    False

    >>> c.isFull()
    False
    
    Test ``size()`` method:
    
    >>> a.size()
    5

    >>> b.size()
    0
    
    Test ``enqueue(item)`` method:
    
    >>> a.enqueue('hippo')
    The queue is full

    >>> b.enqueue('newItem')
    ['newItem']

    >>> c.enqueue('morpheus')
    [33, 42, 'Galaxy', 'Supercomputer', 45, 'Arrival', 'morpheus']
    
    Test ``dequeue()`` method:      
    
    >>> a.dequeue()
    'dog'
    >>> a
    AQueue([maxSize=5],['bear', 'cow', 'horse', 'elephant'])

    >>> b.dequeue()
    'newItem'
    >>> b
    AQueue([maxSize=10],[])
    >>> b.dequeue()
    The queue is empty

    >>> c.dequeue()
    33
    >>> c
    AQueue([maxSize=10],[42, 'Galaxy', 'Supercomputer', 45, 'Arrival', 'morpheus'])
    
    """
    
    def __init__(self,maxSize:int,*args):
        """AQueue class constructor:
        Provide maxSize as and int followed by the elements of the queue.
        To create an empty queue provide maxSize as an int or as a keyword argument."""
        assert type(maxSize) == int, "maxSize has to be an integer"
        assert maxSize >= len(list(args)), "The length of the provided components exceeds the maximum size of the queue"
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
    
    def size(self):         
        """Return the number of items in the queue"""
        return len(self.components)
    
    def isEmpty(self):      
        """Return True if the queue is empty, False otherwise"""
        if len(self.components):
            return False
        return True
        
    def isFull(self):       
        """Return True if there are maxsize items in the queue"""
        if len(self.components) == self.maxSize:
            return True
        return False
    
    def peekFront(self):    
        """Return the item at the front without removing it from the queue"""
        if self.isEmpty():
            print("The queue is empty")
            return None
        return self.components[0]
        
    def peekRear(self):     
        """Return the item at the rear without removing it from the queue"""
        if self.isEmpty():
            print("The queue is empty")
            return None
        return self.components[len(self.components)-1]
    
    def enqueue(self,item):
        """Add item to the rear of the queue if the queue is not full"""
        if self.isFull():
            print("The queue is full")
            return None
        self.components.append(item)
        return self.components
    
    def dequeue(self):      
        """Remove and return an item from the front of the queue. If queue is empty, return None"""
        if self.isEmpty():
            print("The queue is empty")
            return None
        item = self.components.pop(0)
        return item 

if __name__ == "__main__":
    import doctest
    doctest.testmod()