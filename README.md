# chipy2017
Computer Vision Simulation for FRC SteamWorks Gear Lift Vision Targets. Included are OpenGL Simulation, Machine Learning Algorithm to map 2D coordinates (picture) into 3D coordinates (real world), and a simulation of the path the robot will take based on the outputs of the Machine Learning algorithm.

## File Content
```/OpenGL/OpenGL Final.ipynb ``` Contains the simulation that writes data to a CSV database so we can train the Neural Network

```/OpenGL/MachineLearningGL.ipynb ``` Loads the generated datasets and trains a Linear Regression and Neural Network. These are then saved to a file so they can be used later. 

```/OpenGL/OpenGL Combined.ipynb ``` Combines the Simulation with the Neural Network and draws a best path to the target.

```/Practice ML/``` Contains practice for the Machine Learning algorithms I've been working on.

## Blog Posts

To understand the purpose and execution of this project please refer to the following blog posts: 

1. [Blog #1](https://medium.com/@adampatni27/chipy-mentorship-pt-1-a9af5bce2eb9)

2. [Blog #2](https://medium.com/@adampatni27/chipy-mentorship-pt-2-d4a828446a9d)

3. [Blog #3](https://medium.com/@adampatni27/chipy-mentorship-pt-3-6ae9a7335b06)
