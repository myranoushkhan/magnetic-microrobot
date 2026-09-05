import math 
import matplotlib.pyplot as plt
import random

def run_trial(start_x,start_y,target_x,target_y,step_size,noise_strength): #start_x: initial x position, start_y: initial y position, target_x: target x position, target_y: target y position, and step_size: the distance to move in each step
    x = start_x #initial x position set to starting x value
    y = start_y #initial y position set to starting y value
    position_x = [start_x] #list to store x positions, starting with inital x value
    position_y = [start_y] #list to store y positions, starting with initial y value
    step_count = 0 #counter to keep track of number of steps taken
    initial_x = (target_x - start_x) #x component of distance vector from start to target
    initial_y = (target_y - start_y) #y component of distance vector from start to target
    initial_distance = (initial_x**2 + initial_y**2) ** 0.5 # initial distance to target  
    distance_list= [initial_distance] #list to store distances to target, starting with initial distance
    iterations = math.ceil(initial_distance / step_size) #calculate number of iterations needed to reach target, round up to nearest whole number

    for step in range(iterations):
        dx = (target_x - x) #x componet of distance vector from current position to target
        dy = (target_y - y)
        distance = (dx**2 + dy**2) ** 0.5  #calculate distance to target using Pythagorean theorem
        if distance < 0.01:
            break
        direction_x = dx/distance #normalize vector to find direction in x
        direction_y = dy/distance #normalize vector to find direction in y

        move_x = direction_x * step_size #calculate movement in x direction
        move_y = direction_y * step_size #calculate movement in y direction

        wobble_x = random.uniform(-noise_strength, noise_strength) #generate random noise in x direction
        wobble_y = random.uniform(-noise_strength, noise_strength) #generate random noise in y direction

        x = x + move_x + wobble_x #new position = current position + amount to move in x direction + noise
        y = y + move_y + wobble_y #new position = current position + amount to move in y direction + noise

        if distance < step_size:
            x = target_x
            y = target_y

        position_x.append(x) #add new x position to list of x positions
        position_y.append(y) #add new y position to list of y positions
        distance_list.append(distance) #add new distance to list of distances
        step_count += 1 #increment step count

    print ("Target reached in", step_count, " steps.")
    plt.plot(position_x, position_y) #path plotting
    plt.xlabel("X Position")
    plt.ylabel("Y Position")
    plt.title("Microrobot Path to Target")
    plt.savefig("path_plot.png") #save the plot as a PNG file
    
    plt.figure() #create a new figure for the distance plot (so both plots dont overlap)
    plt.plot(distance_list) #plot the distance to target over time
    plt.xlabel("Step")
    plt.ylabel("Distance to Target")
    plt.title("Distance to Target Over Time")
    plt.savefig("distance_plot.png") #save the plot as a PNG file
    return position_x, position_y, step_count
