# 2D Projectile Motion Simulator
A modular, object oriented 2D physics simulator in python made to calculate and visualize projectile motion.

## Description
This is an interactive physics simulator that models 2D projectile motion using numerical integration with small time steps.
Users can build a custom obstacle course through command-line prompts by placing vertical walls, ceilings, landing platforms, and targets before launching a projectile with custom initial velocity and launch angle.

## Features

- Object-oriented design
- Configurable projectile parameters
- Numerical simulation using time steps
- Collision detection
- Custom obstacle courses
- Trajectory visualization with Matplotlib

## Planned Features

- Multiple obstacles at once
- Air resistance
- Wind
- Elastic collisions

## Getting Started

### Dependencies

* Python 3.x
* Numpy
* Matplotlib

### Installation

Clone the repository:

```bash
git clone https://github.com/dj0rdjee/Projectile-motion-simulation
cd Projectile-motion-simulation
```

Install dependencies:

```bash
pip install numpy matplotlib
```

### Running

```bash
python projectile_motion.py
```