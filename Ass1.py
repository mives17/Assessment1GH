# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random
import csv
import agentframework
import matplotlib
import tkinter
matplotlib.use('TkAgg')
import matplotlib.pyplot
import matplotlib.animation
import requests
import bs4

# set perameters
num_of_agents = 20
num_of_iterations = 20
neighbourhood = 20
environment = []
agents = []

# set the plot sizes and axes
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# # Make the environment by reading in.txt and using csv reader

filename = 'in.txt'
file = open("in.txt", "r")

with open('in.txt', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist = []
        environment.append(rowlist)
        for value in row:
            rowlist.append(value) 

          
#Display the environment           
#matplotlib.pyplot.imshow(environment)
#matplotlib.pyplot.show()

#GUI 
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs)

# Make the agents
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment, agents))
    print(agents[i])
    
carry_on = True

def update(frame_number):
    
    fig.clear()   # clear the figure each iteration 
    global carry_on

# Loops to move the agents and set interactions with each other and the environment
for j in range(num_of_iterations):
    random.shuffle(agents)
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
            

# set to show agents on the plot
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)


# set a function for the model to carry out multiple iterations
def gen_function(b = [0]):
    a = 0
    global carry_on 
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1        

# add the run function to run the model in a new window
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=10)

    canvas.draw()

root = tkinter.Tk() 
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run, state="normal")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
root.wm_title("Model")

tkinter.mainloop()

#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=10)
#animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)

r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs)