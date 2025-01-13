import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, LogInfo
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'robot_description',
            default_value='',
            description='URDF description of the robot'
        ),
        LogInfo(
            condition=IfCondition(LaunchConfiguration('robot_description')),
            msg="Loading robot description"
        ),
        Node(
            package='gazebo_ros',
            executable='gzserver',
            name='gazebo',
            output='screen'
        ),
        Node(
            package='gazebo_ros',
            executable='gzclient',
            name='gazebo_gui',
            output='screen'
        ),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': LaunchConfiguration('robot_description')}]
        ),
    ])
