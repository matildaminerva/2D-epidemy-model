import sys
import copy
import math
import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt
from matplotlib import colors
from scipy.optimize import curve_fit

def population(size):
    #########################################################################
    ## Here we form an array called grid, where all the other elements     ##
    ## are zero except one, which is the seed of the epidemia.             ##
    ## The coordinates for this first infected are randomly selected.      ##
    #########################################################################
    side_length = int(round(np.sqrt(size)))  
    grid = np.zeros((side_length,side_length), dtype=int) 
    
    x_coordinate_of_first_infected = random.randint(0, side_length-1) 
    y_coordinate_of_first_infected = random.randint(0, side_length-1) 
    
    grid[x_coordinate_of_first_infected, y_coordinate_of_first_infected]=1 
    
    return grid 



def set_immune(grid, immune_percent): 
    ##########################################################################
    ## Here we set immune elements into the grid, based on the percentage   ##
    ## the user has determined. Coordinates for these are randomly selected.##
    ########################################################################## 
    immune = int(round(len(grid[0])*len(grid[0])*immune_percent)) 
    
    for i in range(immune): 
        while True:  
            
            randx = random.randint(0, len(grid[0])-1)
            randy = random.randint(0, len(grid[0])-1)
        
            if grid[randx, randy] == 0:  
            
                grid[randx, randy] = 3
                    
                break 
                    
            else:  
                
                pass
            
    return grid 


def spreading(currentgrid, Disease):
    
    ###########################################################################
    ## In this function is described the spread of the infection. We go      ##
    ## through whole grid and if it contains number 1 (=ill) we infect the   ##
    ## elements around it based on the contagion rate the user has determined.#
    ## We ignore immune elements but otherwise we infect as many neighbours  ##
    ## of the one ill element as is possible based on the contagion rate.    ##
    ## Because we operate only with 2-d grid, it is only possible to         ##
    ## infect max eight elements in a one time step.  It is randomly selected##
    ## in what coordinates the new infected lie around the one ill element.  ##
    ###########################################################################                      
    
    newgrid = copy.copy(currentgrid) 
    
    last_index = len(currentgrid[0])-1
    
    for i in range(0, len(currentgrid[0])-1): 
        for j in range(0, len(currentgrid[0])-1): 
            
            if currentgrid[i, j] == 1: 
                
                permutation = random.permutation(8) 
                rndmlist = [] 
                
                for n in range (0, disease.contagion_rate): 
                    rndmlist.append(permutation[n]) 
                    
                
                for k in range (0, len(rndmlist)): 
                    
                    rf = random.random() 
                    
      
                    if rndmlist[k] == 0 and newgrid[i, j-i] == 0 and disease.possibility_of_contagion >= rf and j != 0: 
                        newgrid[i, j-1] = 1
                        
                    elif rndmlist[k] == 1 and newgrid[i-1, j+1] == 0 and disease.possibility_of_contagion >= rf and i != 0 and j != last_index:
                        newgrid[i-1, j+1] = 1
                        
                    elif rndmlist[k] == 2 and newgrid[i, j+1] == 0 and disease.possibility_of_contagion >= rf and j !=last_index:
                        newgrid[i, j+1] = 1
                        
                    elif rndmlist[k] == 3 and newgrid[i+1, j+1] == 0 and disease.possibility_of_contagion >= rf and i!=last_index and j!=last_index:
                        newgrid[i+1, j+1] = 1
                        
                    elif rndmlist[k] == 4 and newgrid[i+1, j] == 0 and disease.possibility_of_contagion >= rf and i!=last_index:
                        newgrid[i+1, j] = 1
                        
                    elif rndmlist[k] == 5 and newgrid[i+1, j-1] == 0 and disease.possibility_of_contagion >= rf and j != 0 and i!=last_index:
                        newgrid[i+1, j-1] = 1
                        
                    elif rndmlist[k] == 6 and newgrid[i-1, j] == 0 and disease.possibility_of_contagion >= rf and i != 0:
                        newgrid[i-1, j] = 1
                        
                    elif rndmlist[k] == 7 and newgrid[i-1, j-1] == 0 and disease.possibility_of_contagion >= rf and i !=0 and j !=0:
                        newgrid[i-1, j-1] = 1
                        
                    else:
                        pass
            
                        
    return newgrid 
                    
                    
def show_grid(grid, j, save): 
    ##########################################################################
    ## In this function the grid is plotted. The colour of the element      ##
    ## depends about the number of it. If number is 0 or 3, colour is white ##
    ## and element is either non-infected or immune (but healty anyways). If #
    ## number is 1, element is sick and the colour is orchid and if the     ##
    ## element number is 2, it is dead and the colour is purple.            ##
    ##########################################################################
   
   cmap = colors.ListedColormap(['white', 'orchid', 'purple', 'white'])
   bounds = [0,0.5,1.5,2.5, 3.5]
   norm = colors.BoundaryNorm(bounds, cmap.N)  
   
   plt.imshow(grid, cmap=cmap, norm = norm)
   
   if save:
       plt.savefig('grid_'+str(j)+'.png', bbox_inches='tight')
   
   plt.show()
    
def dying(grid1, grid2): 
    #########################################################################
    ## Here we change those elements that have been enough iterations ill  ##
    ## into dead. Grid2 is this new grid where the ill ones are.           ##
    #########################################################################
    
    for i in range(0, len(grid1[0])): 
        for j in range(0, len(grid1[0])):
            if grid1[i, j] == 1:
                grid2[i, j] =2
                
    return grid2 
    
    
class Disease:
    ########################################################################
    ## This is a class where we define attributes related to the disease. ##
    ########################################################################
    
    def __init__(self, contagion_rate, diseased_time, possibility_of_contagion):
        
        self.contagion_rate = contagion_rate 
        self.possibility_of_contagion = possibility_of_contagion 
        self.diseased_time= diseased_time 
        
    
       
def main(args):
    """
    The main program.
    """   
    

    
contagion_rate = int(input("Enter the value that tells us how many individuals can one ill individual infect in a one time step. Max value is 8!: "))
    
diseased_time = int(input("Enter how many time steps it takes to die after you've gotten ill:" ))
    

possibility_of_contagion = float(input("Enter what is the possibility that the disease is transmitted between two individuals (has to be between 0.0 and 1.0):"))
    
size = int(input("Enter the size of the population:"))
    
time = int(input("Enter how many time steps do we take in whole:" ))
    
immune_percent = float(input("Enter what percentage of the population is immune (has to be between 0.0 and 1.0):"))

save = input("Enter 0 if you want to save pictures and 1 if you don't wish to save them:")
    
if save == 0:
    save = True
elif save == 1:
    save = False
disease = Disease(contagion_rate, diseased_time, possibility_of_contagion)

    ###########################################################################
    ## Here we make a grid that is as large as the size of the population    ##
    ## and we set the immune individuals to the grid. List output is just    ##
    ## a temporary helping list and value x just index value. To list        ##
    ## "healthy" we add the amount of the healthy individuals in the grid    ##
    ## every time step and to the list "sick" the amount of sick and to the  ##
    ## list "dead" the amount of dead. We go through in a for loop as many   ## 
    ## time steps as the user has set and start to spread the disease. We    ##
    ## also plot the picture of the grid every step so that user can see in  ##
    ## the console what does the epidemy look like and if they have selected ##
    ## to save pictures, images of the grid ase also saved. In the ens also  ##
    ## the graph of the amount of healthy, sick and dead individuals as a    ##
    ## function of the time step is shown.                                   ##
    ###########################################################################

currentgrid = population(size) 

currentgrid = set_immune(currentgrid, immune_percent)

output = [] 
x = 0

healthy = [] 
sick = [] 
dead = [] 

for i in range (0, time): 
    nextgrid = spreading(currentgrid, disease)  
    output.append(nextgrid)  
    
    if i >= diseased_time:
        currentgrid = dying(output[x], nextgrid) 
        x += 1 
        
    else: 
         
         currentgrid = copy.copy(nextgrid) 
         
    h = 0 
    s = 0
    d = 0     
    for j in range(len(currentgrid[0])-1): 
        for k in range(len(currentgrid[0])-1):
            if currentgrid[j, k] == 0 or currentgrid[j, k] == 3:
                h += 1
                
            elif currentgrid[j, k] == 1:
                s += 1
                
            else:
                d += 1
                
    healthy.append(h) 
    sick.append(s)
    dead.append(d)
    
    
    show_grid(currentgrid, i, save) 
    
    
    
fig=plt.figure()
fig.show()
ax=fig.add_subplot(111) 


ax.plot(healthy,c='gray',marker="^",ls='--',label='Healthy')
ax.plot(sick,c='orchid',marker=(8,2,0),ls='--',label='Ill')
ax.plot(dead,c='purple',ls='-',label='Dead')

plt.legend(loc=2)
plt.xlabel("Time")
plt.ylabel("Amount of individuals")
plt.draw()
 
    
    
    
if __name__ == "__main__":
    #random.seed()
    main(sys.argv[1:])
