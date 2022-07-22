#!/usr/bin/env python
from distutils.log import warn
from math import sqrt
import rospy
import random
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Twist
from std_msgs.msg import String

pub = rospy.Publisher('twist', Twist, queue_size=1)
t = Twist()
pub1 = rospy.Publisher('chatter', String, queue_size=10)

def callback(data):
    A = random.random(-100,100)
    B = random.random(-100,100)
    C = random.random(-100,100)
    distance = (A*(data.position.x) + B*(data.position.y) + C)/sqrt(A*A + B*B)
    if (distance < 1):
        t.angular.z = 0
        t.linear.x = 0
        warning = "The rover is close to the wall"
        pub1.publish(warning)
    else:
        t.angular.z = random.random(-1,1)
        t.linear.x = random.random(0,1)
    pub.publish(t)
        
def listener():
    rospy.init_node('check_node', anonymous=True)
    rospy.Subscriber("pose", Pose, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()