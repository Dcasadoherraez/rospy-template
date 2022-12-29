#!/usr/bin/env python

import rospy
from std_msgs.msg import String

class Publisher:
    def __init__(self, name: str) -> None:
        rospy.init_node(name, anonymous=True)
        self.publisher = rospy.Publisher('chatter', String, queue_size=10)
        self.rate = rospy.Rate(10) # 10hz
    
    def pub(self):
        while not rospy.is_shutdown():
            hello_str = "hello world %s" % rospy.get_time()
            rospy.loginfo(hello_str)
            self.publisher.publish(hello_str)
            self.rate.sleep()
    
if __name__ == '__main__':
    pub_node = Publisher(name='talker')
    try:
        pub_node.pub()
    except rospy.ROSInterruptException:
        pass