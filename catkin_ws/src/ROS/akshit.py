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
from std_msgs.msg import Int16


i = 0
error_sum_x = 0
l_error_x = 0
error_sum_y = 0
l_error_y = 0
flag = 0
flag1 = 1
flag2 = 1
x_pos = 0
y_pos = 0
z_pos = 20
error_sum_z = 0
l_error_z = 0
n = 1
error_y =0
error_z =0


class send_data():

	"""docstring for request_data"""
	def __init__(self):
		rospy.init_node('drone_server')
		self.command_pub = rospy.Publisher('/drone_command', PlutoMsg, queue_size=5)
		#rospy.Subscriber('/input_key', Int16, self.indentify_key )
		rospy.Subscriber ('/whycon/poses', PoseArray, self.callback)

		self.key_value =70
		self.cmd = PlutoMsg()
		self.cmd.rcRoll =1500
		self.cmd.rcPitch = 1500
		self.cmd.rcYaw =1500
		self.cmd.rcThrottle =1000
		self.cmd.rcAUX1 =1500
		self.cmd.rcAUX2 =1500
		self.cmd.rcAUX3 =1500
		self.cmd.rcAUX4 =1000
		self.x =0
		self.y =0
		self.z =0
                self.output_x =0
                self.output_y =0
                self.output_z =0
		self.rate=rospy.Rate(8)
	def callback(self,pos):
    	        kp = 400
    	        kd = 20
   	 	ki = 0.15
		global error_sum_x, l_error_x, error_sum_y, l_error_y, flag, x_pos, flag1, flag2,y_pos , error_sum_z, l_error_z,n,error_y,error_z
		    
		t = time.time ()
		print(str (t))

		self.x = pos.poses[0].position.x
		self.y = pos.poses[0].position.y
		self.z = pos.poses[0].position.z
                print("Marker " + str (i + 1) + ":     " + str (self.x) + " " + str (self.y) + " " + str (self.z))
   	 	# PID for X Coordinate
    		error_x = x_pos - self.x
    		print "error in x"
    		print error_x
    		error_sum_x = error_sum_x + error_x
    		derivative_x = l_error_x - error_x
    		p_gain_x = kp * error_x
    		i_gain_x = ki * (error_sum_x)
    		d_gain_x = kd * (derivative_x)
    		l_error_x = error_x
    		self.output_x = p_gain_x + i_gain_x + d_gain_x

    		# PID for y Coordinate
    		error_y = y_pos - self.y
    		print "error in y"
    		print error_y
    		error_sum_y = error_sum_y + error_y
    		derivative_y = l_error_y - error_y
    		p_gain_y = kp * error_y
    		i_gain_y = ki * error_sum_y
    		d_gain_y = kd * derivative_y
    		l_error_y = error_y
    		self.output_y = p_gain_y + i_gain_y + d_gain_y
    
    		#PID for z Coordinate
    		error_z = z_pos - self.z
    		print "error in z"
    		print error_z
    		error_sum_z = error_sum_z + error_z
    		derivative_z = l_error_z - error_z
    		p_gain_z = kp * error_z
    		i_gain_z = ki * error_sum_z
    		d_gain_z = kd * derivative_z
    		l_error_z = error_z
    		self.output_z = p_gain_z + i_gain_z + d_gain_z


   
    		#print ('last error (x,y):' + str (l_error_x) + " " + str (l_error_y))
    		#print ('output (x,y)' + str (-output_x) + " " + str (-output_y))
    		#print ('derivative (x,y):' + str (derivative_x) + " " + str (derivative_y))
    		#print ('sum(x,y):' + str (error_sum_x) + " " + str (error_sum_y))
    		#print "Flag = " + str(flag)

        


    		#termios.tcsetattr (sys.stdin, termios.TCSADRAIN, settings)

		
		
	def arm(self):
		self.cmd.rcRoll=1500
		self.cmd.rcYaw=1500
		self.cmd.rcPitch =1500
		self.cmd.rcThrottle =1000
		self.cmd.rcAUX4 =1500
		self.command_pub.publish(self.cmd)
		rospy.sleep(.1)
	def disarm(self):
		self.cmd.rcThrottle =1300
		self.cmd.rcAUX4 = 1200
		self.command_pub.publish(self.cmd)
		rospy.sleep(1)
	
	def indentify_key(self, msg):
		self.key_value = msg.data
	def xaxis(self):

		self.cmd.rcPitch =1500-(0.1*self.output_x)
		self.command_pub.publish(self.cmd)
	def backward(self):
		self.cmd.rcPitch =1450
		self.command_pub.publish(self.cmd)
	def yaxis(self):

		self.cmd.rcRoll =1500-(0.1*self.output_y)
		self.command_pub.publish(self.cmd)	
	def right(self):
		self.cmd.rcRoll =1400
		self.command_pub.publish(self.cmd)
	def reset(self):
		self.cmd.rcRoll =1500
		self.cmd.rcThrottle =1500
		self.cmd.rcPitch =1500
		self.cmd.rcYaw = 1500
		self.command_pub.publish(self.cmd)
	def zaxis(self):

		self.cmd.rcThrottle = 1500-(0.1*self.output_z)
		self.command_pub.publish(self.cmd)
	def decrease_height(self):
		self.cmd.rcThrottle =1400
		self.command_pub.publish(self.cmd)

	def control_drone(self):
		global error_y,error_z
		while True:
			
		        if self.key_value == 0:         
				self.disarm()
			if self.key_value == 70:
				self.arm()
			if self.key_value == 10:
				self.forward()
			if self.key_value == 20:
				self.reset()
			if self.key_value == 30:
				self.left()
			if self.key_value == 40:
				self.right()
			if self.key_value == 80:
				self.reset()
			if self.key_value == 50:
				self.increase_height()
			if self.key_value == 60:
				self.decrease_height()
			if self.key_value == 110:
				self.backward()
			self.command_pub.publish(self.cmd)
			global n 
			n = n + 1
			if n > 100:
				self.key_value=0
			if error_y > 0.5:
				self.yaxis()
			if error_z > 1:
				self.zaxis()
		        
if __name__ == '__main__':
	while not rospy.is_shutdown():
		test = send_data()
		test.control_drone()
		rospy.spin()
		sys.exit(1)


