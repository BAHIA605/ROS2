import rclpy
from rclpy.node import Node
from std_srvs.srv import SetBool  # Utilisation d'un service pour rechercher un livre

class BookDatabase(Node):
    def __init__(self):
        super().__init__('book_database')
        self.books = {'001': 'Python Programming', '002': 'ROS 2 Basics'}
        self.service = self.create_service(SetBool, 'find_book', self.handle_find_book)
        self.get_logger().info("Book Database Service is running...")

    def handle_find_book(self, request, response):
        book_id = request.data
        if book_id in self.books:
            response.success = True
            response.message = f"Book found: {self.books[book_id]}"
        else:
            response.success = False
            response.message = "Book not found"
        return response

def main(args=None):
    rclpy.init(args=args)
    node = BookDatabase()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
