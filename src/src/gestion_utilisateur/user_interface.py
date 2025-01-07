import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class UserInterface(Node):
    def __init__(self):
        super().__init__('user_interface')
        self.subscription = self.create_subscription(String, 'book_requests', self.handle_request, 10)
        self.get_logger().info("User Interface is active.")

    def handle_request(self, msg):
        self.get_logger().info(f"Received request: {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    node = UserInterface()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
