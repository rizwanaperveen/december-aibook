---
sidebar_position: 2
---

# ROS 2 Basics: Robotic Nervous System

## Introduction to ROS 2

ROS 2 (Robot Operating System 2) is a flexible framework for writing robot software. It's a collection of tools, libraries, and conventions that aim to simplify the task of creating complex and robust robot behavior across a wide variety of robot platforms.

## Core Concepts

### Nodes

A node is a process that performs computation. ROS 2 is designed to be modular, with each node running independently and communicating with other components via messages. Nodes are the fundamental building blocks of a ROS 2 system.

### Topics and Messages

Topics are named buses over which nodes exchange messages. Messages are the data packets sent from publishers to subscribers over topics. This publisher-subscriber communication pattern allows for asynchronous communication between nodes.

### Services

Services provide a request/reply communication pattern. Unlike topics which are asynchronous, services are synchronous and block until a response is received. Services are useful for operations that require a specific response.

## Creating Your First ROS 2 Node

Let's create a simple ROS 2 node using Python:

```python
import rclpy
from rclpy.node import Node

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = MinimalPublisher()
    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

## ROS 2 with AI Agents

ROS 2 can be integrated with AI agents through the rclpy library, allowing for sophisticated control and decision-making capabilities. This bridge between traditional robotics and AI enables more intelligent robot behavior.

### Agent-to-ROS Bridge

The agent-to-ROS bridge allows AI agents to interact with ROS 2 nodes seamlessly. This integration enables agents to:

- Subscribe to sensor data from ROS nodes
- Publish commands to robot actuators
- Call services for specific robot operations
- Maintain state information across the robot system

## URDF for Humanoid Robots

URDF (Unified Robot Description Format) is an XML format for representing a robot model. For humanoid robots, URDF describes:

- Kinematic chains
- Physical properties (mass, inertia)
- Visual and collision models
- Joint limits and types

Example URDF snippet for a humanoid robot:

```xml
<robot name="humanoid_robot">
  <link name="base_link">
    <visual>
      <geometry>
        <box size="0.2 0.2 0.2"/>
      </geometry>
    </visual>
  </link>

  <joint name="base_to_torso" type="fixed">
    <parent link="base_link"/>
    <child link="torso"/>
  </joint>

  <link name="torso">
    <visual>
      <geometry>
        <box size="0.3 0.1 0.5"/>
      </geometry>
    </visual>
  </link>
</robot>
```

## Best Practices

1. **Modular Design**: Keep nodes focused on single responsibilities
2. **Robust Communication**: Implement proper error handling for message passing
3. **Resource Management**: Properly clean up resources when nodes are destroyed
4. **Testing**: Use ROS 2 testing frameworks to validate node behavior
5. **Documentation**: Maintain clear interfaces and communication patterns