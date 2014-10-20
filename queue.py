#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author : younger shen
# email  : younger.x.shen@gmail.com

class Heap(object):

    @classmethod
    def parent(cls, i):
        return int((i - 1) >> 1);
 
    @classmethod
    def left(cls, i):
        return (i << 1) + 1;
 
    @classmethod
    def right(cls, i):
        return (i << 1) + 2;
 
class MinPriorityQueue(list, Heap):
 
    @classmethod
    def min_heapify(cls, A, i, heap_size):
        l, r = cls.left(i), cls.right(i)
        if l < heap_size and A[l] < A[i]:
            least = l
        else:
            least = i
        if r < heap_size and A[r] < A[least]:
            least = r
        if least != i:
            A[i], A[least] = A[least], A[i]
            cls.min_heapify(A, least, heap_size)
 
    def minimum(self):
        return self[0]
 
    def extract_min(self):
        heap_size = len(self)
        assert heap_size > 0, "heap underflow"
        val = self[0]
        tail = heap_size - 1
        self[0] = self[tail]
        self.min_heapify(self, 0, tail)
        self.pop(tail)
        return val
 
    def decrease_key(self, i, key):
        val = self[i]
        try:
            assert key <= val, "new key is larger than current key"
            int_key = int(key)
        except AssertionError as e:
            print("the new key is large than current key\r")
            exit(2)
        except ValueError as e:
            print("input must be a integer number\r")
            exit(3)
        
        self[i] = int_key
        parent = self.parent
        while i > 0 and self[parent(i)] > self[i]:
            self[i], self[parent(i)] = self[parent(i)], self[i]
            i = parent(i)
 
    def insert(self, key):
        
        try:
            int_key  = int(key)

        except ValueError as e:
            print("you must insert a integer number")
            exit(1)
        else:
            self.append(float('inf'))
            self.decrease_key(len(self) - 1, int_key)
    


if __name__ == '__main__':
    import random
 
    keys = range(10)
    random.shuffle(list(keys))
    print(keys)
 
    queue = MinPriorityQueue() 
    for i in keys:
        queue.insert(i)
    print(queue)
 
    print('*' * 30)
 
    for i in range(len(queue)):
        val = i % 3
        if val == 0:
            val = queue.extract_min() 
        elif val == 1:
            val = queue.minimum() 
        else:
            val = queue[1] - 10
            queue.decrease_key(1, val) 
        print(queue, val)
 
    print([queue.extract_min() for i in range(len(queue))])
