#!/usr/bin/env python3

from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
import rclpy
import tkinter as tk

class NavigatorApp:
    def __init__(self):
        self.navigator=BasicNavigator()
        self.tk_button = tk.Tk()
        nav_button = tk.Button(self.tk_button, text='Go Waiter 10', command=self.set_location)
        nav_button.pack()
        self.set_initial_pose()
        

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

    def set_location(self):
        x,y = -0.30,-3.98
        self.go_to_pose(x,y)

    def go_to_pose(self,x,y):
        goal_pose = PoseStamped()
        goal_pose.header.frame_id = 'map'
        goal_pose.header.stamp = self.navigator.get_clock().now().to_msg()
        goal_pose.pose.position.x = x
        goal_pose.pose.position.y = y
        goal_pose.pose.orientation.w = 0.99
        self.navigator.goToPose(goal_pose)

        while not self.navigator.isTaskComplete():
            pass
        result = self.navigator.getResult()
        if result == TaskResult.SUCCEEDED:
            print('Goal succeeded!')
        elif result == TaskResult.CANCELED:
            print('Goal was canceled!')
        elif result == TaskResult.FAILED:
            print('Goal failed!')
        else:
            print('Goal has an invalid return status!')

    def exiting(self):
        self.tk_button.mainloop()
        self.navigator.lifecycleShutdown()





def start_app():
    rclpy.init()
    app = NavigatorApp()
    app.exiting()
    rclpy.shutdown()        