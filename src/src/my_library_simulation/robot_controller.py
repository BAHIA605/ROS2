import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class RobotController(Node):
    def __init__(self):
        super().__init__('robot_controller')
        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.publish_velocity)

    def publish_velocity(self):
        msg = Twist()
        msg.linear.x = 0.5  # Déplacer le robot en avant
        msg.angular.z = 0.0  # Pas de rotation
        self.publisher.publish(msg)
        self.get_logger().info('Publishing velocity command: [linear.x: %.2f, angular.z: %.2f]' % (msg.linear.x, msg.angular.z))

def main(args=None):
    rclpy.init(args=args)
    node = RobotController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
