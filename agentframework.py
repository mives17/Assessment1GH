# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 13:28:49 2019

@author: gy16mei
"""

import random

# create the agent class using __init__ function
class Agent():
    def __init__ (self, environment, agents):
        self.x = random.randint(0,99)
        self.agents = agents
        self.y = random.randint(0,99)
        self.environment = environment
        self.store = 0 
        
# use __str__ to return the self string  
    def __str__(self):
        return str(self.y) + " " + str(self.x)
    
    
    # set the move function
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
    
    # set the eat function (agents will nibble the environment) 
    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
            
    # set the agent to search for close neighbours, and share resources with it
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
            #print("sharing " + str(dist) + " " + str(ave))
            # print to check that share_with_neighbours is working

    #calculate distance using pythagoras
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
            


