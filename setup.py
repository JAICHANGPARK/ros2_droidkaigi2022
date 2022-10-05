from setuptools import setup
import os
from glob import glob

package_name = 'ros2_droidkaigi2022'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
         (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dw',
    maintainer_email='dw@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'droidkaigi22 = ros2_droidkaigi2022.droidkaigi22:main',
            'general_temperature_pub = ros2_droidkaigi2022.general_temperature_pub:main',
            'general_battery_pub = ros2_droidkaigi2022.general_battery_pub:main',
            'subscriber_member_function = ros2_droidkaigi2022.subscriber_member_function:main',
            
        ],
    },
)
