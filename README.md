# TASK #2 

## How does communication take place in ROS?


The primary mechanism ROS uses to communicate between nodes is by sending named messages called **`topics`**.

Nodes are not aware of who they are communicating with.The idea is that a node that wants to share information will `publish` messages on the appropriate topic or topics; a node that wants to receive information will `subscribe` to the topic or topics that it’s interested in. ROS master makes sure that the publisher and subscriber find each other. 

`Many publishers` and `many subscribers` can also share a single topic. Regardless of which node publishes the message on a particular topic all of the subscribers of the topic have access to the messages.

## What are the different types of node-to-node communication in ROS? Also state two applications of each type.

The node-to-node communication occurs in the following three ways. 

> `Topic and messages`

    Are for continuous data flow. Data might be published and subscribed at any time independent of any senders/receivers. Callbacks receive data once it is available. The publisher decides when data is sent. 

    Applications : turtlesim 1. turtle/cmd_vel
                             2. turtle/pose

> `Services`

    Service calls are bi-directional. One node sends information to another node and waits for a response. Information flows in both directions. Servies only involves one-on-one communication, where each service call is initiated by one node, and the response goes back to that same node.
>
    Client node sends data called request to a server node and waits for a reply. The server having received this request takes some action and sends some data called a response back to the client.


> `Actionlib`

    If the service takes a long time to execute, the user might want the ability to cancel the request during execution or get periodic feedback about how the request is progressing. The actionlib package provides tools to create servers that execute long-running goals that can be preempted. It also provides a client interface in order to send requests to the server. 

## Is there a way to see or generate this architecture of node communication in ROS using a utility or software? If yes, mention it.

This idea is probably easiest to see graphically, and the easiestway to visualize the publishsubscribe relationships between ROS nodes is to use this command:

````rqt_graph````

In this name, the r is for ROS, and the qt refers to the Qt GUI toolkit used to implement the program.

## What are the different sensors and actuators involved in each subsystem of a typical rover?

### `Sensors`

A sensor is a device that detects a physical property in the environment, records and transmits it.

Some of the sensors in a rover are as follows:

> `RAD (Radiation Assessment Detector)`

    RAD measures the type and amount of harmful radiation that reaches the Martian surface from the sun and space sources.

> `DAN (Dynamic Albedo Of Neutrons)`

    Looks for sign for changes in the way neutrons are released from the martian soil that indicates liquid or frozen water exists underground.

> `REMS (Rover Environmental Monitoring Station)`
   
    REMS contains all the weather instruments needed to provide daily and seasonal reprts on meteorological conditions around the rover.

 > `MEDLI (Mars Science Laboratory Entry Descent and Landing Instrument)` 
    
    MEDLI measures the heat and atmospheric changes that occur during the descent, to help determine the effects on different parts of the spacecraft.

### `Actuators`

An actuator is a complex component comprised of a motor and a gearbox.

Some of the actuators in a rover are as follows:

> `Drill System`
    
    To collect rock samples for in depth analysis by instruments inside the rover. The power travels up an auder in the frill for transfer to sample processing mechansims.

> `Collection and Handling for In-situ Rock Analysis (CHIMRA)`
    
    This tool helps in sorting out rock material collected by the rover's drill and 
    scoop.

> `Dust Removal Tool (DRT)`

    Metal-bristle brushing device to remove the dust layer from a rock surface or to clean the rover's observation.
