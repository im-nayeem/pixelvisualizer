# Pixel Plotter - Python Package
# pixelplotter

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

