#!/usr/bin/env python
import rospy
import roslib
from geometry_msgs.msg import PoseArray
from geometry_msgs.msg import Twist
import time
from std_msgs.msg import Empty
import sys, select, termios, tty
from plutodrone.srv import *
from plutodrone.msg import *
from std_msgs.msg import Float64
i = 0
error_sum_x = 0
l_error_x = 0
error_sum_y = 0
l_error_y = 0
n = 1
x_pos = 0
y_pos = 0
error_sum_z = 0
l_error_z = 0

def callback(pos):
 
    x = pos.poses[0].position.x
    y = pos.poses[0].position.y
    z = pos.poses[0].position.z

    print("Marker " + str (i + 1) + ":     " + str (x) + " " + str (y) + " " + str (z))

    pubx = rospy.Publisher('xaxis', Float64, queue_size=8)
    puby = rospy.Publisher('yaxis', Float64, queue_size=8)
    pubz = rospy.Publisher('yaxis', Float64, queue_size=8)    
    pubx.publish(x)
    puby.publish(y)
    pubz.publish(z)

def read():
    # rospy.init_node('listener', anonymous=True)

    rospy.Subscriber ('/whycon/poses', PoseArray, callback)

    # spin() simply keeps python from exiting until this node is destopped
    #rospy.spin ()

if __name__ == '__main__':
	rospy.init_node('drone')
	while not rospy.is_shutdown():
                read()
		rospy.spin()
		sys.exit(1)


