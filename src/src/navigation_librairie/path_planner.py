import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from action_msgs.msg import GoalStatus
from example_interfaces.action import Fibonacci  # Vous pouvez remplacer par une action spécifique

class PathPlanner(Node):
    def __init__(self):
        super().__init__('path_planner')
        self._action_server = ActionServer(self, Fibonacci, 'plan_trajectory', self.execute_callback)

    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing plan...')
        # Simuler la planification de trajet (vous pouvez ajouter une logique plus complexe ici)
        feedback_msg = Fibonacci.Feedback()
        feedback_msg.sequence = [1, 1, 2, 3, 5]
        goal_handle.publish_feedback(feedback_msg)
        goal_handle.succeed()
        return GoalStatus.SUCCEEDED

def main(args=None):
    rclpy.init(args=args)
    node = PathPlanner()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

