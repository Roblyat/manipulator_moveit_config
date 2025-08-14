from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from moveit_configs_utils import MoveItConfigsBuilder
import os

def generate_launch_description():
    moveit_config = (
        MoveItConfigsBuilder("ur_manipulator", package_name="ur_manipulator_moveit_config")
        .to_moveit_configs()
    )

    controllers_yaml = os.path.join(
        get_package_share_directory("ur_manipulator_moveit_config"),
        "config",
        "moveit_controller.yaml",           # or "moveit_controller.yaml" if you prefer
    )

    move_group = Node(
        package="moveit_ros_move_group",
        executable="move_group",
        output="screen",
        parameters=[
            moveit_config.to_dict(),   # Load URDF/SRDF/OMPL/…
            controllers_yaml,          # <- Load MoveIt controller mapping
        ],
    )
    return LaunchDescription([move_group])
