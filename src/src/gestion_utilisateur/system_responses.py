import rclpy
from rclpy.node import Node
from std_srvs.srv import SetBool

class SystemResponses(Node):
    def __init__(self):
        super().__init__('system_responses')
        self.client = self.create_client(SetBool, 'find_book')
        self.get_logger().info("System Responses is active.")

    def send_request(self, book_id):
        request = SetBool.Request()
        request.data = book_id
        future = self.client.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        return future.result()

def main(args=None):
    rclpy.init(args=args)
    node = SystemResponses()
    result = node.send_request('001')
    node.get_logger().info(f"Response: {result.success}, Message: {result.message}")
    rclpy.shutdown()

if __name__ == '__main__':
    main()
