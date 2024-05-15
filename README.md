## Install python3-colcon

To run install python3-colcon-common-extensions, run the following command

```bash
  sudo apt install python3-colcon-common-extensions
```

## Create a workspace

First, create a directory (ros2_ws) to contain our workspace

```bash
  mkdir -p ~/ros2_ws/src
  cd ~/ros2_ws
```
## 
## Source an underlay = ros2_ws

## build

colcon build --symlink-install

```bash
  colcon build --symlink-install
```

## Run tests

To run tests for the packages we just built, run the following:

```bash
  colcon test
```

## Source the environment

When colcon has completed building successfully, the output will be in the install directory.

```bash
  source install/setup.bash
```


## Source ROS 2 environment

Depending on how you installed ROS 2 (from source or binaries), and which platform you’re on, your exact source command will vary:

```bash
  source /opt/ros/humble/setup.bash
```

## Resolve dependencies

From the root of your workspace (ros2_ws), run the following command

```bash
  rosdep install -i --from-path src --rosdistro humble -y
```
If you already have all your dependencies, the console will return:
```bash
  #All required rosdeps installed successfully
```

