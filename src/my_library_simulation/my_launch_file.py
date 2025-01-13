import launch
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, LogInfo
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('robot', default_value='robot1', description='Robot name'),
        LogInfo(
            condition=launch.substitutions.LaunchConfiguration('robot'),
            msg="Starting robot simulation with name: "
        ),
        Node(
            package='my_library_simulation',
            executable='my_simulation_node',
            name='simulation_node',
            output='screen',
            parameters=[{'robot_name': 'robot1'}]
        )
    ])
