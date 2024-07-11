Benchmarking for ZeroMQ library
=========

To reproduce the tests you can use a native Ubuntu system or you can use a Docker container. In the following instructions, if you have Ubuntu installed natively, ignore directions for using Docker.

## Set up project with Docker

### Create and start a Docker container

```
docker run -it -v <dir_project_absolute_path>:/zeromq_benchmarking/ --name zeromq_project ros:foxy
```

### Install requirements

```
pip install -r requirements.txt
```

### Set up ROS2 workspace

Enter in the root folder of the project called 'zeromq_benchmarking'

```
cd zeromq_benchmarking
```

In the same terminal you can use this doc to set up ROS workspace: [Cheat Sheet RTES Lab Unimore](https://github.com/HiPeRT/F1tenth-RTES/blob/master/Code/ros2/LAB_CHEAT_SHEET.md#cheat-sheet-for-the-lab-exercises-in-ros2)

> Note: workspace directory is 'ros2_ws'

## Testing ROS2
It is necessary one terminal for each node.

### Server node
In the same terminal where you are setting up ROS2 workspace: 

```
ros2 run cpp_echo server
```

### Client node
Open a new terminal inside the container: 

```
docker exec -ti zeromq_project /bin/bash
```

Then:

```
cd zeromq_benchmarking/ros2_ws
```
```
source install/setup.bash
```
```
ros2 run cpp_echo client
```

### Show result graph

Open a new terminal (not inside the container) and execute:

```
cd zeromq_benchmarking/ros2_ws/src/cpp_echo/src
```
```
docker run --rm -v $(pwd):/work remuslazar/gnuplot graph.gnu
```


## Testing ZeroMQ
It is necessary one terminal for each node.

### Server node

```
docker exec -ti zeromq_project /bin/bash
```
```
./zeromq_benchmarking/zeromq/pub-sub/server.py
```

### Client node

```
docker exec -ti zeromq_project /bin/bash
```
```
./zeromq_benchmarking/zeromq/pub-sub/client.py
```

### Show results graph

Open a new terminal (not inside the container) and execute:

```
cd zeromq_benchmarking/zeromq/pub-sub/
```
```
docker run --rm -v $(pwd):/work remuslazar/gnuplot graph.gnu
```