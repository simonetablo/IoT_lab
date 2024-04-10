import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from turtlesim.srv import SetPen

class MyTurtle(Node):

    def __init__(self):
        super().__init__('turtle_publisher')
        self.publisher = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.client=self.create_client(SetPen, '/turtle1/set_pen')
        self.timer = self.create_timer(1.0, self.publish_velocity)
        self.velocity = Twist()
        self.direction = 0

    def publish_velocity(self):
        color=SetPen.Request()
        color.width=7
        color.off=0

        if self.direction == 0:
            self.velocity.linear.x = 2.0  
            self.velocity.angular.z = 0.0
            self.direction += 1
            color.r=255
            color.g=0
            color.b=0
        elif self.direction == 1:
            self.velocity.linear.x = 0.0
            self.velocity.angular.z = 1.5617
            self.direction += 1
        elif self.direction == 2:
            self.velocity.linear.x = 2.0
            self.velocity.angular.z = 0.0
            self.direction += 1
            color.r=0
            color.g=255
            color.b=0
        elif self.direction == 3:
            self.velocity.linear.x = 0.0
            self.velocity.angular.z =  1.5617
            self.direction += 1
        elif self.direction == 4:
            self.velocity.linear.x = 2.0 
            self.velocity.angular.z = 0.0
            self.direction += 1
            color.r=0
            color.g=0
            color.b=255
        elif self.direction == 5:
            self.velocity.linear.x = 0.0
            self.velocity.angular.z =  1.5617
            self.direction += 1
        elif self.direction == 6:
            self.velocity.linear.x = 2.0
            self.velocity.angular.z = 0.0
            self.direction += 1
            color.r=255
            color.g=255
            color.b=0
        elif self.direction == 7:
            self.velocity.linear.x = 0.0
            self.velocity.angular.z =  1.5617
            self.direction = 0

        '''
        if self.direction == 0:
            self.velocity.linear.x = 2.0  # move left
            self.velocity.linear.y = 0.0
            self.direction += 1
            color.r=255
            color.g=0
            color.b=0
        elif self.direction == 1:
            self.velocity.linear.x = 0.0
            self.velocity.linear.y = 2.0  # move up
            self.direction += 1
            color.r=0
            color.g=255
            color.b=0
        elif self.direction == 2:
            self.velocity.linear.x = -2.0  # move right
            self.velocity.linear.y = 0.0
            self.direction += 1
            color.r=0
            color.g=0
            color.b=255
        elif self.direction == 3:
            self.velocity.linear.x = 0.0
            self.velocity.linear.y = -2.0 # move down
            self.direction = 0
            color.r=255
            color.g=255
            color.b=0
        '''
        self.publisher.publish(self.velocity)
        self.client.call_async(color)

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MyTurtle()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
