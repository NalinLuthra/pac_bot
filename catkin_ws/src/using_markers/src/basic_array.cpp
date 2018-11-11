/*
 * Copyright (c) 2010, Willow Garage, Inc.
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *
 *     * Redistributions of source code must retain the above copyright
 *       notice, this list of conditions and the following disclaimer.
 *     * Redistributions in binary form must reproduce the above copyright
 *       notice, this list of conditions and the following disclaimer in the
 *       documentation and/or other materials provided with the distribution.
 *     * Neither the name of the Willow Garage, Inc. nor the names of its
 *       contributors may be used to endorse or promote products derived from
 *       this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
 * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 */

#include <ros/ros.h>
#include <visualization_msgs/Marker.h>



int main( int argc, char** argv )
{
  ros::init(argc, argv, "basic_shapes");
  ros::NodeHandle n;
  ros::Rate r(1);
  ros::Publisher marker_pub = n.advertise<visualization_msgs::Marker>("basic", 200);

  uint32_t shape = visualization_msgs::Marker::SPHERE;
  int i = 0;
 while (ros::ok())
  {
    visualization_msgs::Marker marker[5];

    while(i<5)
    {
        marker[i].header.frame_id = "/my_frame";
        marker[i].header.stamp = ros::Time();
        marker[i].ns = "basic_shapes" + char(i);
        std::cout << marker[i].ns << std::endl;
        marker[i].id = i;
        marker[i].type = shape;
        marker[i].action = visualization_msgs::Marker::ADD;
        
        marker[i].pose.orientation.x = 0.0;
        marker[i].pose.orientation.y = 0.0;
        marker[i].pose.orientation.z = 0.0;
        marker[i].pose.orientation.w = 1.0;

        marker[i].scale.x = 20.0;
        marker[i].scale.y = 20.0;
        marker[i].scale.z = 20.0;

        marker[i].color.r = 1.0f;
        marker[i].color.g = 0.0f;
        marker[i].color.b = 0.0f;
        marker[i].color.a = 1.0;
        marker[i].lifetime = ros::Duration();

        i++;
    }

    while (marker_pub.getNumSubscribers() < 1)
    {
      if (!ros::ok())
      {
        return 0;
      }
      ROS_WARN_ONCE("Please create a subscriber to the marker");
      sleep(1);
    }

        marker[0].pose.position.x = 71.46;
        marker[0].pose.position.y = 108.56;
        marker[0].pose.position.z = 10;

        marker[1].pose.position.x = 416.24;
        marker[1].pose.position.y = 43.67;
        marker[1].pose.position.z = 10;

        marker[2].pose.position.x = 246.44;
        marker[2].pose.position.y = 377.81;
        marker[2].pose.position.z = 10;

        marker[3].pose.position.x = 387.94;
        marker[3].pose.position.y = 361.81;
        marker[3].pose.position.z = 10;

        marker[4].pose.position.x = 246.88;
        marker[4].pose.position.y = 86.04;
        marker[4].pose.position.z = 10;
        i=0;
    while (i<5)
    {
        marker_pub.publish(marker[i]);
        i++;    
    }
    
    i=0;
    r.sleep();
  }
}

