from datetime import datetime
from email.header import Header
from random import random
import time
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import BatteryState
from std_msgs.msg import Header


class GeneralBatteryPub(Node):

    def __init__(self):
        super().__init__('GeneralBatteryPub')
        self.publisher_ = self.create_publisher(BatteryState, 'topic/battery', 10)
        timer_period = 1.0  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = BatteryState()
        msg.voltage = random() + 97.2
        msg.current = random() + 1.5
        header = Header()
        header.frame_id = str(self.i)
        header.stamp.sec = int(time.time())
        # header.stamp.nanosec = time.time_ns()
        msg.header = header
        self.publisher_.publish(msg)
      
        self.get_logger().info('[General_Battery] Publishing: "%s"' % msg)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)
    try:

        minimal_publisher = GeneralBatteryPub()
        try:
            rclpy.spin(minimal_publisher)
        except KeyboardInterrupt:
            minimal_publisher.get_logger().info("Keyboard Interrupt ")
        finally:
            minimal_publisher.destroy_node()

    finally:
        rclpy.shutdown()


if __name__ == '__main__':
    main()
