import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class RequestManager(Node):
    def __init__(self):
        super().__init__('request_manager')
        self.publisher = self.create_publisher(String, 'book_requests', 10)
        self.timer = self.create_timer(5.0, self.publish_request)
        self.get_logger().info("Request Manager is active.")

    def publish_request(self):
        request = String()
        request.data = "Find book with ID 001"
        self.publisher.publish(request)
        self.get_logger().info(f"Published: {request.data}")

def main(args=None):
    rclpy.init(args=args)
    node = RequestManager()
    rclpy.spin(node)
    rclpy.shutdown()

# Ce bloc permet d'exécuter la fonction main si le fichier est exécuté directement
if __name__ == '__main__':
    main()

