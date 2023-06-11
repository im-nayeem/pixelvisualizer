# Pixel Plotter - Python Package

`pixelplotter` is a Python package for visualizing pixels while implementing different line or circle drawing algorithms in computer graphics.

## Features

- Visualize the generated pixels in various line and circle drawing algorithms in computer graphics using `pygame`.
- Simple and easy-to-use API.
## Dependency
First install `pygame` to use this package:
```bash
pip install pygame
```
## Installation

You can install `pixelplotter` via `pip`:

```bash
pip install git+https://github.com/im-nayeem/pixelplotter.git
```
Make sure you have pygame installed as well, as it is listed as a dependency.

## Usage
1. Import pixeldrawer module
```python
from pixelplotter import pixeldrawer
```

2. Create an instance of PixelDrawer class and start by calling start() function
```python
app = pixeldrawer.PixelDrawer()
app.start()
```

3. To plot a pixel call draw_pixel() function
```python
app.draw_pixel(4,5)
```

4. After plotting all pixels call function execute()
```python
app.execute()
```
Here is the complete code:
```python
from pixelplotter import pixeldrawer
app = pixeldrawer.PixelDrawer()
app.start()
app.draw_pixel(4,5)
app.execute()
```

## Example: Bresenham's Line Drawing Algorithm
```python
from pixelplotter import pixeldrawer

def bresenhamsLineDrawing(drawer, x1, y1, x2, y2):
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
        drawer.draw_pixel(x, y)
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

app = pixeldrawer.PixelDrawer()
app.start()
bresenhamsLineDrawing(app, 0, 0, 5, 7)
app.execute()
```
**Output:**
![image](https://github.com/im-nayeem/pixelplotter/assets/77660934/c28140a0-96f0-46c1-b58f-6d5ac48871e6)

## Example: Bresenham's Circle Drawing Algorithm
```python
from pixelplotter import pixeldrawer

def drawCircle(drawer, r, h, k):
    d = 3 - 2*r
    x = 0
    y = r

    while(x <= y):
        drawer.draw_pixel(x+h , y+k)
        drawer.draw_pixel(y+h , x+k)
        drawer.draw_pixel(-y+h, x+k)
        drawer.draw_pixel(-x+h, y+k)
        drawer.draw_pixel(-x+h, -y+k)
        drawer.draw_pixel(-y+h, -x+k)
        drawer.draw_pixel(y+h, -x+k)
        drawer.draw_pixel(x+h, -y+k)

        if(d < 0):
            d = d + 4*x + 6
            x = x+1
            y = y
        else:
            d = d + d*(x - y) + 10
            x = x + 1
            y = y - 1
app = pixeldrawer.PixelDrawer()
app.start()
drawCircle(app, 7, 10, 10)
app.execute()
```
**Output:**
![image](https://github.com/im-nayeem/pixelplotter/assets/77660934/a83b4de5-17cb-4f70-9e42-e1c9a6215ead)

