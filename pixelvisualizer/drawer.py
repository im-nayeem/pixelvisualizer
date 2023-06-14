

# Draw line using bresenham's line drawing algorithm
# @param plotter the pixelvisualizer.pixelplotter.PixelPlotter instance 
def draw_bresenhams_line(plotter, x1, y1, x2, y2):

    x, y = x1, y1

    dx = x2 - x1
    dy = y2 - y1
    
    m = dy / dx

    if(m < 1):
        draw_direct_line(plotter, x1, y1, x2, y2)
        return

    if(m < 1):
        c1 = 2 * dy
        c2 = 2 * (dy - dx)
        p = c1 - dy
    else:
        c1 = 2 * dx
        c2 = 2 * (dx - dy)
        p = c1 - dy

    while(x <= x2):
        plotter.draw_pixel(x , y)
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



# Draw line using bresenham's circle drawing algorithm
def draw_bresenhams_circle(plotter, r, h, k):
    d = 3 - 2 * r
    x = 0
    y = r

    while(x <= y):
        plotter.draw_pixel(x+h , y+k)
        plotter.draw_pixel(y+h , x+k)
        plotter.draw_pixel(-y+h, x+k)
        plotter.draw_pixel(-x+h, y+k)
        plotter.draw_pixel(-x+h, -y+k)
        plotter.draw_pixel(-y+h, -x+k)
        plotter.draw_pixel(y+h, -x+k)
        plotter.draw_pixel(x+h, -y+k)

        if(d < 0):
            d = d + 4*x + 6
            x = x+1
            y = y
        else:
            d = d + d*(x - y) + 10
            x = x + 1
            y = y - 1



# Draw line using direct use of line equation
def draw_direct_line(plotter, x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    if(dx == 0):
        draw_dda_line(plotter, x1, y1, x2, y2)
        return
    
    m = dy/dx
    b = y1 - m*x1

    if(dx < 0):
        x = x2
        y = y2
        xend = x1
    else:
        x = x1
        y = y1
        xend = x2
    
    while(True):
        plotter.draw_pixel(round(x), round(y))
        x = x+1
        y = m * x + b
        if(x > xend):
            break



# Draw Line using DDA algorithm
def draw_dda_line(plotter, x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    steps = max(abs(dx), abs(dy))
    xinc = dx / steps
    yinc = dy / steps
    x = x1
    y = y1

    while(x <= x2):
        plotter.draw_pixel(round(x), round(y))
        x = x + xinc
        y = y + yinc
        
        if(y > y2):
            break;