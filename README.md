# Ezy ROS Python Package template
Quick and easy! Why go through all the ROS tutorials again when all you wanna do is save time?

Create your workspace, download the template and start developing! This simple template will get you started on any ROS project in Python under 5 minutes! What are you waiting for?

## Usage
Install ROS, and make sure you execute `source /opt/ros/<your version>/setup.bash`. Then create your catkin workspace directory `catkin_ws` and initialize it with `catkin init`.

Inside your workspace create `src` directory where you will put your ROS packages. 

Clone the **rospy-templates** repository to your `src` directory.

Go back to your `catkin_ws` and run the command `catkin build`. 

**Done!** 

Let's summarize all the steps into easy copy & paste commands.

```
source /opt/ros/<your version>/setup.bash

cd ~/

mkdir catkin_ws && cd catkin_ws

catkin init

mkdir src && cd src

git clone https://github.com/Dcasadoherraez/rospy-template.git

cd ..

catkin build
```

## Running the nodes
Make sure you execute roscore in another terminal by running 
```
source /opt/ros/noetic/setup.bash

roscore
```

(*) Then, in your terminal, make sure your current directory is `~/catkin_ws`, and source your workspace by `source devel/setup.bash`. 

You can now run the nodes individually or using the launch file

### Individually
You will need to repeat (*) for two terminals. Then run `rosrun rospy-templates publisher.py` on the first one, and `rosrun rospy-templates subscriber.py` on the second one.

### With the launch file
This one will launch both nodes from the same terminal just by using the command `roslaunch rospy-templates pub_sub.launch`.