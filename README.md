# chipy2017
Computer Vision Simulation for FRC SteamWorks Gear Lift Vision Targets. Included are OpenGL Simulation, Machine Learning Algorithm to map 2D coordinates (picture) into 3D coordinates (real world), and a simulation of the path the robot will take based on the outputs of the Machine Learning algorithm.

## Blog Posts

To understand the purpose and execution of this project please refer to the following blog posts: 

1. [Blog #1](https://medium.com/@adampatni27/chipy-mentorship-pt-1-a9af5bce2eb9)

2. [Blog #2](https://medium.com/@adampatni27/chipy-mentorship-pt-2-d4a828446a9d)

3. [Blog #3](https://medium.com/@adampatni27/chipy-mentorship-pt-3-6ae9a7335b06)

At the end of my mentorship I gave a brief talk to the Chicago Python Group. [Video](https://www.youtube.com/watch?v=KMurhmSS6pg)

## File Content
```/OpenGL/Simulation.ipynb ``` Contains the simulation that writes data to a CSV database so we can train the Neural Network. Basically puts a series of points that define the target in 3D space. It them simulates a robot moving around and converging upon this target.

```/OpenGL/Train Neural Network.ipynb ``` Loads the generated datasets and trains a Neural Network. These are then saved to a file so they can be used later. 

```/OpenGL/Simulation and Prediction.ipynb ``` Combines the Simulation with the Neural Network and draws a best path to the target. The angle generated is the one in which the robot will travel.

```/Practice ML``` Contains practice for the Machine Learning algorithms I've been working on.

```/Robot``` Contains an implementation of this that may work on our robot.
