from launch import LaunchDescription
from launch_ros.actions import Node

from launch_ros.substitutions import FindPackageShare
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from random import randint

WORLD_FILE = "drone_world.sdf"

bridge_1=Node(
  package='ros_gz_bridge',
  executable='parameter_bridge',
  arguments=[
    "/X3/cmd_vel@geometry_msgs/msg/Twist@ignition.msgs.Twist"
  ],
  name='cmd_vel_bridge'
)

bridge_2=Node(
  package='ros_gz_bridge',
  executable='parameter_bridge',
  arguments=[
    "/X3/odometry@nav_msgs/msg/Odometry@ignition.msgs.Odometry"
  ],
  name='odometry_bridge'
)

get_up=Node(
        package='drone_patrol',
        executable='get_up',
        name='get_up',
        output='screen'
      )

def generate_launch_description():

  return LaunchDescription(
    [
      IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
          PathJoinSubstitution([
              FindPackageShare('ros_gz_sim'),
              'launch/'
              'gz_sim.launch.py',
          ])
        ]),
        launch_arguments={
          'gz_args' : "./"+WORLD_FILE
        }.items()
      ),
      bridge_1,
      bridge_2,
      get_up
    ]
  )
