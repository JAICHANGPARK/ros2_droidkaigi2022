#!/usr/bin/env python3

from launch import LaunchDescription
from launch_ros.actions import Node

pkg_name = "ros2_droidkaigi2022"


def generate_launch_description():
    return LaunchDescription([
        Node(
            package="ros2_droidkaigi2022",
            executable="droidkaigi22",
            name="droidkaigi22",
            output="screen",
            emulate_tty=True,
        ),
        Node(
            package="ros2_droidkaigi2022",
            executable="general_temperature_pub",
            name="general_temperature_pub",
            output="screen",
            emulate_tty=True,
        ),
        Node(
            package="ros2_droidkaigi2022",
            executable="general_battery_pub",
            name="general_battery_pub",
            output="screen",
            emulate_tty=True,
        ),
        Node(
            package="ros2_droidkaigi2022",
            executable="subscriber_member_function",
            name="subscriber_member_function",
            output="screen",
            emulate_tty=True,
        ),
       
    ])