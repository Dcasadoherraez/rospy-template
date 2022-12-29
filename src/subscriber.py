#!/usr/bin/env python
import rospy
from std_msgs.msg import String

class Subscriber:
    def __init__(self, name: str) -> None:
        rospy.init_node(name, anonymous=True)
        rospy.Subscriber("chatter", String, self.callback)

        # spin() simply keeps python from exiting until this node is stopped
        rospy.spin()
        
    def callback(self, data):
        rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)


if __name__ == '__main__':
    sub_node = Subscriber(name='listener')
    