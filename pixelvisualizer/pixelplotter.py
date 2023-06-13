import pygame
from pygame.locals import *

class PixelPlotter:

    def __init__(self):
        # Initialize pygame
        pygame.init()

        # Set up the display
        self.width, self.height = 1108, 630
        self.box_size = 14  # Size of each box representing a pixel
        self.margin = 21 # Margin for labels

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("(-o_o-)      Meow /ᐠ｡ꞈ｡ᐟ\ Meow =(^.^)= Pixel Visualizer")

        # Define colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.LABEL_COLOR = (0, 0, 0)  
        self.AXIS_COLOR = (204, 33, 33)



    # Initialize pygame screen
    def start(self):
        # Fill the screen with white color
        self.screen.fill(self.WHITE)

        self._draw_labels()
        self._draw_borders()
        self._draw_axes()


    # Function to plot a pixel
    def plot_pixel(self, x, y, fill=True):
        x1 = (x + self.width // (2 * self.box_size)) * self.box_size
        y1 = (-y + self.height // (2 * self.box_size)) * self.box_size
        pygame.draw.rect(self.screen, self.BLACK, (x1, y1, self.box_size, self.box_size), 1)
        if fill:
            pygame.draw.rect(self.screen, self.BLACK, (x1, y1, self.box_size, self.box_size))
        pygame.display.flip()


    def _draw_labels(self):
        font = pygame.font.Font(None, 14)

        # Draw x-axis labels
        for i in range(-self.width // (2 * self.box_size), self.width // (2 * self.box_size)):
            text = font.render(str(i), True, self.LABEL_COLOR)
            self.screen.blit(text, (i * self.box_size + self.width // 2 - self.box_size // 2, self.height - self.margin // 2))

        # Draw y-axis labels
        for i in range(-self.height // (2 * self.box_size), self.height // (2 * self.box_size)):
            text = font.render(str(-i), True, self.LABEL_COLOR)
            self.screen.blit(text, (self.margin // 2 - self.box_size // 2, i * self.box_size + self.height // 2 - self.box_size // 2))

    def _draw_borders(self):
        # Draw borders for each coordinate
        for x in range(0, self.width, self.box_size):
            pygame.draw.line(self.screen, self.BLACK, (x, 0), (x, self.height))
        for y in range(0, self.height, self.box_size):
            pygame.draw.line(self.screen, self.BLACK, (0, y), (self.width, y))

    def _draw_axes(self):
        # Draw x-axis line
        pygame.draw.line(self.screen, self.AXIS_COLOR, (0, self.height // 2), (self.width, self.height // 2), 2)

        # Draw y-axis line
        pygame.draw.line(self.screen, self.AXIS_COLOR, (self.width // 2, 0), (self.width // 2, self.height), 2)
    

    # Event listener to quit
    def execute(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False


