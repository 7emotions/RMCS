from launch import LaunchDescription
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution


def generate_launch_description():
    ld = LaunchDescription()

    ld.add_action(
        Node(
            package="rmcs_executor",
            executable="node",
            parameters=[
                PathJoinSubstitution(
                    [FindPackageShare("rmcs_bringup"), "config", "omni.yaml"]
                )
            ],
        )
    )

    return ld
