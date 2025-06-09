# 3D Renderer in Python with Pygame

## Description
This project is a simple 3D renderer implemented in Python using Pygame. It features the rendering of 3D objects (cube and pyramid) with rotation capabilities around all axes and around the center of the body. The renderer includes rasterization functionality with adjustable segment counts for performance optimization.

## Features
- Rendering of 3D objects (cube and pyramid)
- Rotation around all axes (X, Y, Z)
- Rotation around the center of the body
- Colorful entities with customizable colors
- Rasterization with adjustable segment counts for FPS optimization
- Backface culling (only visible faces are rendered)

## Installation
### Prerequisites
- Python 3.x
- pip 

### Clone the repo
```bash
   git clone https://github.com/boce1/3d_renderer.git
```

### Pygame Installation
To install Pygame, run the following command in your terminal or command prompt:
```bash
   pip install pygame
```

## Project Structure
3d-renderer/
├── body/ # 3D object definitions


│ ├── init.py


│ ├── cube/ # Cube implementation


│ │ └── init.py


│ └── pyramid/ # Pyramid implementation


│ └── init.py


│


├── math3d/ # 3D math operations


│ ├── init.py


│ ├── projection.py # Projection calculations


│ ├── rotation.py # Rotation transformations


│ └── plane_vector.py # Visibility calculations


│


├── point/ # Point class


│ └── init.py # Point implementation
│


├── triangle/ # Triangle class
│ └── init.py # Rasterization implementation


│
├── constants/ # Render constants
│ └── init.py # Configuration values


│
└── main.py # Main application entry point


## Customization
Color and FOV can be cahanged in the constants/ package

## Screenshot of what the renderer looks like
![screenshot](scr.png)

#### TO DO: make demo video