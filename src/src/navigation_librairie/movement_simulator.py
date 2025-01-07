import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose

class MovementSimulator(Node):
    def __init__(self):
        super().__init__('movement_simulator')
        self.publisher = self.create_publisher(Pose, 'robot_position', 10)
        self.timer = self.create_timer(1.0, self.publish_position)
        self.get_logger().info("Movement Simulator is active.")

    def publish_position(self):
        pose = Pose()
        # Simuler une position de robot
        self.publisher.publish(pose)
        self.get_logger().info("Position published")

def main(args=None):
    rclpy.init(args=args)
    node = MovementSimulator()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
