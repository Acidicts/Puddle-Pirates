import pygame


class Timer:
    def __init__(self, duration, loop=False, func=None):
        self.start = None
        self.end = duration
        self.active = False

        self.loop = loop

        self.func = func

    def activate(self):
        self.active = True
        self.start = pygame.time.get_ticks()

    def deactivate(self):
        self.active = False
        self.start = None

        if self.loop:
            self.activate()

    def update(self):
        current_time = pygame.time.get_ticks()
        if self.active and current_time - self.start > self.end:
            self.deactivate()

            if self.func is not None:
                self.func()
