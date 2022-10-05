from random import random
import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from sensor_msgs.msg import Temperature
import random


class GeneralTemperaturePub(Node):

    def __init__(self):
        super().__init__('GeneralTemperaturePub')
        self.temp_publisher_ = self.create_publisher(Temperature, 'topic/general_temp', 10)
        self.cpu_publisher_ = self.create_publisher(Temperature, 'topic/cpu_temp', 10)
        self.gpu_publisher_ = self.create_publisher(Temperature, 'topic/gpu_temp', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Temperature()
        gpu_msg = Temperature()
        msg.temperature = random.random() + 35.1
        gpu_msg.temperature = random.random() + 50.5
        # msg.gpu_publisher_ = random.random() + 40.5
        # msg.data = 'Hello World: %d' % self.i
        self.temp_publisher_.publish(msg)
        self.cpu_publisher_.publish(msg)
        self.gpu_publisher_.publish(gpu_msg)
        self.get_logger().info('[GeneralTemp] Publishing: "%s"' % msg)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = GeneralTemperaturePub()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
