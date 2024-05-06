from launch import LaunchDescription
from launch_ros.actions import Node

from launch_ros.substitutions import FindPackageShare
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution

WORLD_NAME = "vehicle_blue_world"

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
          'gz_args' : "./%s.sdf" % WORLD_NAME
        }.items()
      ),
      Node(
        package="ros_gz_bridge",
        executable="parameter_bridge",
        arguments=[
          "/cmd_vel@geometry_msgs/msg/Twist@ignition.msgs.Twist"
        ]
      ),
      Node(
        package="ros_gz_bridge",
        executable="parameter_bridge",
        arguments=[
          "/world/%s/control@ros_gz_interfaces/srv/ControlWorld" % WORLD_NAME
        ]
      ),
      Node(
        package='square_gazebo',
        executable='vehicle_controller'
      )


    ]
  )


