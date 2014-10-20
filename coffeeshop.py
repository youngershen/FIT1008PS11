#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author : younger shen
# email  : younger.x.shen@gmail.com

#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author : younger shen
# email  : younger.x.shen@gmail.com

import random

class Event(object):
    def __init__(self , time, label):
        self.time = time
        self.label = label

    def __str__(self):
        return self.label + " at " + str(self.time)  

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
 
class EventPriorityQueue(list, Heap):
 
    @classmethod
    def min_heapify(cls, A, i, heap_size):
        l, r = cls.left(i), cls.right(i)
        if l < heap_size and A[l].time < A[i].time:
            least = l
        else:
            least = i
        if r < heap_size and A[r].time < A[least].time:
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
 
    def decrease_key(self, i, event):
        val = self[i].time
        try:
            assert event.time <= val, "new key is larger than current key"
        except AssertionError as e:
            print("the new key is large than current key\r")
            exit(2)
        
        self[i] = event
        parent = self.parent
        while i > 0 and self[parent(i)].time > self[i].time:
            self[i], self[parent(i)] = self[parent(i)], self[i]
            i = parent(i)
 
    def insert(self, event):
        self.append(Event(float('inf'), "undefine"))
        self.decrease_key(len(self) - 1, event)
    



def create_rand_events(count , label):

    try:
        int(count)
    except ValueError as e:
        print("input error \n")
        exit(3)

    try:
        icount = int(count)
    except ValueError as e:
        print("input must be a inter and a string\r")
        exit(2)

    eventlist = list()
    for i in range(icount):
        if label == 'status':
            index = int(random.random() * 100 % 10)
            rand = 60 * index + 59 

        else:
            index = int(random.random() * 100 % 10)
            rand = 60 * index + int(random.random() * 100 % 60)
        event = Event(rand, label)
        eventlist.append(event)

    return eventlist


def put_events_to_queue(events, equeue):
    for i in events:
        equeue.insert(i)

def convert_time(n):
    
    try:
        time = int(n)
    except ValueError as e:
        print("input wrong parameters\n")
        exit(3)
    return "{min} minutes after 8 am".format(min=n)


def event_manager():
    equeue = EventPriorityQueue()
    events = create_rand_events(200, "arrival")
    sevents = create_rand_events(10, "status")
    put_events_to_queue(events, equeue)
    put_events_to_queue(sevents, equeue)
    
    people_count = 0
    people_dict = dict()
    while len(equeue) > 0:
        event = equeue.extract_min()
        if event.label  == 'arrival':
            print("a customer has arrived and at " + convert_time(event.time) + "\r")
            serving_time = int(random.random() * 10 % 6)
            served_event = Event(event.time + serving_time, "served")
            equeue.insert(served_event)
            people_count += 1
            try:
                people_dict[event.time] += 1
            except KeyError as e:
                people_dict[event.time]  = 1
        elif event.label == 'served':
            print("customer has been served at " + convert_time(event.time) + "\r")
            extra_time = int(random.random() * 100 % 31) + event.time
            leave_event = Event(extra_time, "leaving")
            equeue.insert(leave_event)
        elif event.label == 'leaving':
            print(" a customer has left at " + convert_time(event.time) + "\r")
        elif event.label == 'status':
            print("status " + convert_time(event.time) + "\n")
            print("{count} people are served at last our".format(count = people_count))
            
            if len(people_dict.keys()) > 0:
                pc = people_dict.popitem()[1]
            else:
                pc = 0
            print("the max number of people  are {count} people\n".format(count = pc ))
            people_dict = dict()
            people_count = 0



if __name__ == '__main__':
   
    event2 = Event(20, "eat")
    event3 = Event(30, "dring")
    event1 = Event(10, "arrive")
    equeue = EventPriorityQueue()
    equeue.insert(event1)
    equeue.insert(event2)
    equeue.insert(event3)
    print(equeue.extract_min())

    events = create_rand_events(200, " arrive")
    put_events_to_queue(events, equeue)

    #print(convert_time(320))
    event_manager()
