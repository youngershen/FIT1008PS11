#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author : younger shen
# email  : younger.x.shen@gmail.com


from queue import MinPriorityQueue
from interface import Interface
from coffeeshop import EventPriorityQueue
from coffeeshop import Event
from coffeeshop import event_manager 
from coffeeshop import convert_time
from coffeeshop import create_rand_events

def test_task_1_invaild_queue_insert():
    pqueue = MinPriorityQueue()
    pqueue.insert("test")

def test_task_1_vaild_queue_insert():
    pqueue = MinPriorityQueue()
    pqueue.insert(10)
    pqueue.insert("10")

def test_task_2_vaild_event_covert_time():
    convert_time(10)

def test_task_2_invalid_event_covert_time():
    convert_time("test")

def test_task_2_vaild_create_rand_events():
    create_rand_events(10, "sfsd")

def test_task_2_invalid_create_rand_events():
    create_rand_events("sdsf","sdf")

def test_cases():
    #other of the case please test in the cli
    #test_task_1_vaild_queue_insert()
    #test_task_1_invaild_queue_insert()
    #test_task_2_vaild_event_covert_time()
    #test_task_2_invalid_event_covert_time()
    #test_task_2_vaild_create_rand_events()
    #test_task_2_invalid_create_rand_events()
    pass


def main():
    #test_cases()
    #this is task 1
    Interface().run_menu()
    #this is task 2 do not run at same time
    #event_manager()


if __name__ == '__main__':
    main()
