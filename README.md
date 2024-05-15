# 1
## github -- command -line new-brans

## Full Workflow from Start
cd your src/ < overlay you need >
Initialize the Git repository (if not already initialized):

```bash
  git init
```

Stage your changes:

```bash
  git add .
```

Commit your changes:

```bash
  git commit -m "name you needs"
```

Create a new branch (branch_name) and switch to it:

```bash
  git checkout -b (branch_name)
```


Add your remote repository (replace with your actual repository URL):

```bash
  git remote add origin https://github.com/yourusername/yourrepository.git
```


Push the new branch to the remote repository:

```bash
  git push -u origin --
```
# 2
##

## Create a package

Let’s use the workspace you created in the previous tutorial, ros2_ws, for your new package.
Make sure you are in the src folder before running the package creation command.

```bash
  cd ~/name_workspce/src
```

The command syntax for creating a new package in ROS 2 is:

```bash
  ros2 pkg create --build-type ament_cmake --license Apache-2.0 --node-name (my_node) (my_package)
```

For this tutorial, you will use the optional argument --node-name which creates a simple Hello World type executable in the package.
Enter the following command in your terminal:

```bash
going to create a new package
package name: my_package
destination directory: /home/user/ros2_ws/src
package format: 3
version: 0.0.0
description: TODO: Package description
maintainer: ['<name> <email>']
licenses: ['TODO: License declaration']
build type: ament_cmake
dependencies: []
node_name: my_node
creating folder ./my_package
creating ./my_package/package.xml
creating source and include folder
creating folder ./my_package/src
creating folder ./my_package/include/my_package
creating ./my_package/CMakeLists.txt
creating ./my_package/src/my_node.cpp
```

cd 
```bash
colcon build --symlink-install
```
or select package build

```bash
colcon build --packages-select my_package
```

Source the setup file 

```bash
  cd ..
  source install/local_setup.bash
```

#  Add dependencies
Navigate one level back to the ros2_ws/src/cpp_pubsub directory, where the CMakeLists.txt and package.xml files have been created for you.
## package.xml
Open package.xml with your text editor.

Add a new line after the ament_cmake buildtool dependency and paste the following dependencies corresponding to your node’s include statements:
```bash
  <depend>rclcpp</depend>
  <depend>std_msgs</depend>
```

## CMakeLists.txt
Now open the CMakeLists.txt file. Below the existing dependency find_package(ament_cmake REQUIRED), add the lines:
```bash
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
```
After that, add the executable and name it talker so you can run your node using ros2 run:
```bash
add_executable(talker src/publisher_member_function.cpp)
ament_target_dependencies(talker rclcpp std_msgs)
```
Finally, add the install(TARGETS...) section so ros2 run can find your executable:
```bash
 install(TARGETS
  talker ** add <--
  sub ** add <-- 
  DESTINATION lib/${PROJECT_NAME})
```
