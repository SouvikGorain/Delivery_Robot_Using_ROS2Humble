# Delivery_Robot_Using_ROS2Humble

# Autonomous Driving and Path Planning using Nav2 and SLAM Toolbox
Creating a Delivery Robot based on TurtleBot3 which is named as hotel_waiter. It spawns itself to a particular location and automatically traces it's path back to initial starting point. The destination is being set by user created custom buttons for different coordinates (in this case you can simply say each button represents the table number where the food is to be delivered.)

# Project Workflow
(i) Main robot used in this project is a turtlebot based robot which is quite ideal for travelling through narrow spaces and complex pathways of our custom world while avoiding obstacles in its path. To be noted that here path means the shortest path to destination.

(ii) A custom launch file is created for bring the robot into simulations(i.e gazebo,rviz). SLAM using Gmapping node will be executed for our custom created world containing MAZE.
(iii) In our main droject whose launch file is named as (hotel_waiter) we are using NAV2 stack and simple GUI Tkinter to create buttons for sending robot to different tables.

# Features



# Pre Course Requirements
--> Ubuntu 22.04
--> ROS2 - Humble
