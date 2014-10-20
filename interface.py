#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author : younger shen
# email  : younger.x.shen@gmail.com

#interface claas
from queue import MinPriorityQueue

class Interface(object):
   
    queue = MinPriorityQueue() 
    
    def __int__(self):
        super(Interface, self).__init__(self)
        

    def run_menu(self):
        while True:
            self.show_welcome()
            cmd = input()
            cmds = self.parse_cmd(cmd)
            
            if cmds[0] == 'append':
                self.queue_handler(cmds, self.queue)
            elif cmds[0] == 'serve':
                self.queue_handler(cmds, self.queue)
            elif cmds[0] == 'print':
                self.queue_handler(cmds, self.queue)
            elif cmds[0] == 'quit':
                print("bye bye beautiful ! \r")
                exit(0)
            else:
                print("wrong command input again\r")

    @staticmethod
    def show_welcome():
        print("please input command\r")


    @staticmethod
    def queue_handler(cmds, queue):
        if cmds[0] == 'append' and len(cmds) == 2:
            try:
                int_value = int(cmds[1])
            except ValueError as e:
                print("your input is not a integer value !\r")
                return
            queue.insert(int_value)

        elif cmds[0] == 'serve' and len(cmds) == 1:
            if len(queue) < 1:
                print("heap empty ! \r")
                return 
            min =  queue.extract_min()
            print("remove the min of heep : %d\r" % min)
        elif cmds[0] == 'print' and len(cmds) ==1:
            print(queue)
            print("\r")
        else:
            print("input error , input again\r")
            return


    @staticmethod
    def parse_cmd(cmds):
        commands = cmds.split(" ")
        return commands 
