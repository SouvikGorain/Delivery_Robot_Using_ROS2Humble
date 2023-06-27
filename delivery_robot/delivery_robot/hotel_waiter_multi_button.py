#!/usr/bin/env python3

from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
import rclpy
import tkinter as tk
from ament_index_python.packages import get_package_share_directory
import os
import subprocess

class NavigatorApp:
    def __init__(self):
        self.navigator=BasicNavigator()
        self.tk_button = tk.Tk()
        self.create_button('Table 1',  -0.74,    2.66)
        self.create_button('Table 2',   3.89,    2.65)
        self.create_button('Table 3',   3.85,   -4.12)
        self.create_button('Table 4',  -0.40,   -4.06)
        self.beer_path = os.path.join(get_package_share_directory('delivery_robot'),'models','beer','model.sdf')
        self.waiter_active_flag=False
        self.return_from_table=False
        self.set_initial_pose()


    def create_button(self,text,x,y):
        button = tk.Button(self.tk_button, text= text, command=lambda:self.go_to_pose(x,y))
        button.pack()
        

    def set_initial_pose(self):
        initial_pose = PoseStamped()
        initial_pose.header.frame_id = 'map'
        initial_pose.header.stamp = self.navigator.get_clock().now().to_msg()
        initial_pose.pose.position.x = -5.19
        initial_pose.pose.position.y = -1.09
        initial_pose.pose.orientation.z = 0.0
        initial_pose.pose.orientation.w = 0.99
        self.navigator.setInitialPose(initial_pose)
        self.navigator.waitUntilNav2Active()
        self.go_to_pose(-5.20,-3.38)
        self.waiter_active_flag=True
    

    def go_to_pose(self,x,y):
        table_serving = PoseStamped()
        table_serving.header.frame_id = 'map'
        table_serving.header.stamp = self.navigator.get_clock().now().to_msg()
        table_serving.pose.position.x = x
        table_serving.pose.position.y = y
        table_serving.pose.orientation.w = 0.99

        counter_return = PoseStamped()
        counter_return.header.frame_id = 'map'
        counter_return.header.stamp = self.navigator.get_clock().now().to_msg()
        counter_return.pose.position.x = -5.20
        counter_return.pose.position.y = -3.38
        counter_return.pose.orientation.w = 0.99

        if self.waiter_active_flag:
            print("Navigation towards Goal Table")
            goals=[]
            goals.append(table_serving)
            goals.append(counter_return)
            cmd = ['ros2' , 'run' , 'delivery_robot' , 'sdf_spawner' ,self.beer_path,"beer","-5.29","-3.46" ]
            process = subprocess.Popen(cmd)
            process.wait()
            self.navigator.followWaypoints(goals)
            self.return_from_table=True
        else:
            print("Navigation towards Counter")
            self.navigator.goToPose(counter_return)    


        while not self.navigator.isTaskComplete():
            pass
        result = self.navigator.getResult()
        if result == TaskResult.SUCCEEDED:
            print('Goal succeeded!')
        
        else:
            print('Goal Failed')

        if self.return_from_table:
            cmd = ['gz' , 'model' , '-d' , '-m' ,'beer' ]
            process = subprocess.Popen(cmd)
            process.wait()
            self.return_from_table=False


    def exiting(self):
        self.tk_button.mainloop()
        self.navigator.lifecycleShutdown()





def start_app():
    rclpy.init()
    app = NavigatorApp()
    app.exiting()
    rclpy.shutdown()  
