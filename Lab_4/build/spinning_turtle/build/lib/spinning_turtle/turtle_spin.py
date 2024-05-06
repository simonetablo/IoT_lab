import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3
from tutorial_interfaces.srv import SpinTurtle


class TurtleSpinService(Node):

    def __init__(self):
        super().__init__('turtle_publisher')
        self.spin_service = self.create_service(SpinTurtle, 'spin', self.spin_callback)
        self.publish_to = self.create_publisher(Twist, '/turtle/cmd_vel', 10)

    def spin_callback(self, msg, response):
        dir = msg.dir
        dir = float(dir)
        
        move_msg = Twist()
        move_msg.linear = Vector3(x=0.0, y= 0.0, z=0.0)
        move_msg.angular = Vector3(x=0.0, y=0.0, z=5.0*dir)

        self.publish_to.publish(move_msg)
        response.res = "Spinning!"

        return response



def main(args=None):
    rclpy.init(args=args)

    spin_service = TurtleSpinService()

    rclpy.spin(spin_service)

    spin_service.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
