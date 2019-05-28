# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from rcl_interfaces.msg import IntegerRange
from rcl_interfaces.msg import FloatingPointRange
from rcl_interfaces.msg import ParameterDescriptor

import rclpy
from rclpy.node import Node
from rclpy.parameter import Parameter


class ParametersNode(Node):

    def __init__(self):
        super().__init__('parameters_node')
        fp_range = FloatingPointRange(from_value=0.0, to_value=10.0, step=0.5)
        integer_range = IntegerRange(from_value=0, to_value=10, step=2)

        parameters = [
            ('float_parameter', 0.0, ParameterDescriptor(floating_point_range=[fp_range])),
            ('int_parameter', 4, ParameterDescriptor(integer_range=[integer_range])),
            ('str_read_only', 'You cannot edit me', ParameterDescriptor(read_only=True)),
        ]

        self.declare_parameters('', parameters)

def main(args=None):
    rclpy.init(args=args)

    node = ParametersNode()

    float_parameter = node.get_parameter('float_parameter').value
    int_parameter = node.get_parameter('int_parameter').value
    str_parameter = node.get_parameter('str_read_only').value

    node.get_logger().info('Retrieved parameters:\nFloat: {float_parameter}\nInt: {int_parameter}\nstr: {str_parameter}'.format_map(locals()))

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
