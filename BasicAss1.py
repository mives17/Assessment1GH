import random
import csv
import matplotlib
import tkinter
matplotlib.use('TkAgg')
import matplotlib.pyplot
import matplotlib.animation 


# set perameters
num_of_agents = 20
num_of_iterations = 20
neighbourhood = 20
agents = []
environment = []

# set plot size and axis
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# Make the environment by reading in.txt and using csv reader
with open('in.txt', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist = []
        environment.append(rowlist)
        for value in row:
            rowlist.append(value) 


# Make the agents and print to verify.
for i in range(num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])
print(agents)

carry_on = True	

def update(frame_number):
    
    global carry_on 
    # figure is not cleared to see agent movement
    
    # make a loop to move the agents
    for i in range(num_of_agents): 
        if random.random() < 0.5:
            agents[i][0]  = (agents[i][0] + 1) % 99 
        else:
            agents[i][0]  = (agents[i][0] - 1) % 99
        
        if random.random() < 0.5:
            agents[i][1]  = (agents[i][1] + 1) % 99 
        else:
            agents[i][1]  = (agents[i][1] - 1) % 99 
      
        
    #set stopping condition for the model and print if met
    if random.random() < 0.1:
        carry_on = False
        print("stopping condition")
    
    
    #project agents on to a plot
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i][0],agents[i][1])
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.imshow(environment)
        #print(agents[i][0],agents[i][1])

		
# set a function for the model to carry out multiple iterations
def gen_function(b = [0]):
    a = 0
    global carry_on 
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1


# set the model to run in a separate window
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
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


#r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
#content = r.text
#soup = bs4.BeautifulSoup(content, 'html.parser')
#td_ys = soup.find_all(attrs={"class" : "y"})
#td_xs = soup.find_all(attrs={"class" : "x"})
#print(td_ys)
#print(td_xs)

