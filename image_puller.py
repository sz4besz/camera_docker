import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_srvs.srv import Trigger

class ImagePuller(Node):
    def __init__(self):
        super().__init__('image_puller_node')


        self.create_subscription(Image, '/camera/camera/color/image_raw', self.camera_callback, 10)
        self.img_pub = self.create_publisher(Image, '/camera_latest', 10)
        self.srv = self.create_service(Trigger, 'get_latest_frame', self.trigger_callback)

        self.latest_msg = None

    def camera_callback(self, msg):
        # Latest image from subscription
        self.latest_msg = msg

    def trigger_callback(self, request, response):
        if self.latest_msg is not None:
            self.img_pub.publish(self.latest_msg)
            response.success = True
            response.message = "Frame published"
        else:
            response.success = False
            response.message = "Latest image is None"

        return response

def main():
    rclpy.init()
    node = ImagePuller()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
