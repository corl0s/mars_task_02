#!/usr/bin/env python
import rospy
import random
from geometry_msgs.msg import Pose

def publisher():
    pub = rospy.Publisher('pose', Pose, queue_size=1)
    rospy.init_node('sensor_node', anonymous=True)
    rate = rospy.Rate(2) # Hz
    while not rospy.is_shutdown():
        p = Pose()
        p.position.x = random.random(100)
        p.position.y = random.random(100)
        p.position.z = 0
        # Make sure the quaternion is valid and normalized
        p.orientation.x = 0.0
        p.orientation.y = 0.0
        p.orientation.z = 0.0
        p.orientation.w = 1.0
        pub.publish(p)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy:
        pass