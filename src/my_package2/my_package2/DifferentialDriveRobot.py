import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf_transformations import euler_from_quaternion, quaternion_from_euler

class DifferentialDriveRobot(Node):
    def __init__(self):
        super().__init__('differential_drive_robot')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.subscription = self.create_subscription(Odometry, 'odom', self.odom_callback, 10)
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0

    def odom_callback(self, msg):
        orientation_q = msg.pose.pose.orientation
        orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
        (roll, pitch, self.theta) = euler_from_quaternion(orientation_list)
        self.x = msg.pose.pose.position.x
        self.y = msg.pose.pose.position.y

    def move_robot(self, linear_vel, angular_vel):
        msg = Twist()
        msg.linear.x = linear_vel
        msg.angular.z = angular_vel
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    robot = DifferentialDriveRobot()

    try:
        while rclpy.ok():
            rclpy.spin_once(robot)
            robot.move_robot(1.0, 0.5)  # Move with linear velocity 1.0 m/s and angular velocity 0.5 rad/s
    except KeyboardInterrupt:
        pass

    robot.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
