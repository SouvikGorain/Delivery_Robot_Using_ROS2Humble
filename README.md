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
--> should have SLAM TOOLBOX
--> should have ROS Nav2 installed
# Implementing the project using Repository
i.  If the above mentioned prerequisites are matched then we are assuming that you are having a fully functional ros2 workspace with you.
ii. Inside your workspace go to src and go to install there , you will find share directory there you should create the project packages as sometimes codes in 1 package need to access others while running so in that case having your project in a shared directory can make your access to these more easier. You may need it while we will be spawning the turtlebot in world environment.
iii. Launch file contains all your launch codes like hotel_waiter.launch.py etc . 
iv. These files will launch your turtlebot in the world environment subsequently in Gazebo and Rviz.
v. Then you need to map 
