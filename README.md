# Pixel Plotter - Python Package

`pixelvisualizer` is a Python package for visualizing and plotting pixels while implementing different line or circle drawing algorithms in computer graphics.

## Dependency
First install `pygame` to use this package:
```bash
pip install pygame
```

## Installation
You can install `pixelvisualizer` via `pip`:

```bash
pip install git+https://github.com/im-nayeem/pixelvisualizer.git
```
Make sure you have pygame installed as well, as it is listed as a dependency.

## To Update Package:
```bash
pip uninstall pixelvisualizer
pip install git+https://github.com/im-nayeem/pixelvisualizer.git
```

## Usage
1. Import pixelplotter module
```python
from pixelvisualizer import pixelplotter
```

2. Create an instance of PixelPlotter class and start by calling start() function
```python
plotter = pixelplotter.PixelPlotter()
plotter.start()
```

3. To plot a pixel call plot_pixel() function
```python
plotter.plot_pixel(4,5)
```

4. After plotting all pixels call function execute()
```python
plotter.execute()
```
Here is the complete code:
```python
from pixelvisualizer import pixelplotter
plotter = pixelplotter.PixelPlotter()
plotter.start()
plotter.plot_pixel(4,5)
plotter.execute()
```

## Example: Bresenham's Line Drawing Algorithm
```python
from pixelvisualizer import pixelplotter

def bresenhamsLineDrawing(plotter, x1, y1, x2, y2):
    x = x1
    y = y1
    dx = x2 - x1
    dy = y2 - y1
    m = dy/dx
    
    if(m < 1):
        c1 = 2 * dy
        c2 = 2 * (dy - dx)
        p = c1 - dy
    else:
        c1 = 2 * dx
        c2 = 2 * (dx - dy)
        p = c1 - dy

    while(x <= x2):
        plotter.plot_pixel(x, y)
        if(m < 1):
            if(p < 0):
                p = p + c1
                x = x + 1
                y = y
            else:
                p = p + c2
                x = x + 1
                y = y + 1
        else:
            if(p < 0):
                p = p + c1
                x = x 
                y = y + 1
            else:
                p = p + c2
                x = x + 1
                y = y + 1

plotter = pixelplotter.PixelPlotter()
plotter.start()
bresenhamsLineDrawing(plotter, 0, 0, 5, 7)
plotter.execute()
```
**Output:**
![image](https://github.com/im-nayeem/pixelvisualizer/assets/77660934/c28140a0-96f0-46c1-b58f-6d5ac48871e6)

## Example: Bresenham's Circle Drawing Algorithm
```python
from pixelvisualizer import pixelplotter

def drawCircle(plotter, r, h, k):
    d = 3 - 2*r
    x = 0
    y = r

    while(x <= y):
        plotter.plot_pixel(x+h , y+k)
        plotter.plot_pixel(y+h , x+k)
        plotter.plot_pixel(-y+h, x+k)
        plotter.plot_pixel(-x+h, y+k)
        plotter.plot_pixel(-x+h, -y+k)
        plotter.plot_pixel(-y+h, -x+k)
        plotter.plot_pixel(y+h, -x+k)
        plotter.plot_pixel(x+h, -y+k)

        if(d < 0):
            d = d + 4*x + 6
            x = x+1
            y = y
        else:
            d = d + d*(x - y) + 10
            x = x + 1
            y = y - 1
plotter = pixelplotter.PixelPlotter()
plotter.start()
drawCircle(plotter, 7, 10, 10)
plotter.execute()
```
**Output:**
![image](https://github.com/im-nayeem/pixelvisualizer/assets/77660934/a83b4de5-17cb-4f70-9e42-e1c9a6215ead)

