import sys
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class MinimalClientAsync(Node):
    def __init__(self):
        super().__init__("minmal_client_async")
        self.cli=self.create_client(AddTwoInts, '/add_two_ints')
        while not self.cli.wait_for_service(1):
            self.get_logger().info('waiting for server to be up.')

    def send_request(self, a, b):
        req=AddTwoInts.Request()
        req.a=a
        req.b=b

        self.future=self.cli.call_async(req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()

def main():
    rclpy.init()

    minimal_client = MinimalClientAsync()
    response = minimal_client.send_request(int(sys.argv[1]), int(sys.argv[2]))
    minimal_client.get_logger().info(
        'Result of add_two_ints: for %d + %d = %d' %
        (int(sys.argv[1]), int(sys.argv[2]), response.sum))

    minimal_client.destroy_node()
    rclpy.shutdown()



if __name__ == '__main__':
    main()