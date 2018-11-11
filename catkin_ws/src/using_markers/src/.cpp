#include "ros/ros.h"
#include "geometry_msgs/PosseArray.h"
#include "std_msgs/Float64"
#include <iostream>

void chatterCallback(const geometry_msgs::PosseArray msg)
{
	float x = msg->posses[0].position.x;
	float y = msg->posses[0].position.y;

	std::cout << x << " " << y; 
}


int main(int argc, char const **argv)
{
	ros::init(argc, argv, "listener");
	ros::NodeHandle n;
	ros::Subscriber sub = n.subscriber("/whycon/poses")

	return 0;
}