from asciimatics.effects import Stars, Print
from asciimatics.particles import RingFirework, SerpentFirework, StarFirework, \
    PalmFirework
from asciimatics.renderers import SpeechBubble, FigletText, Rainbow, Fire
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError
from random import randint, choice
import sys


def demo(screen):
    scenes = []
    effects = [
        Stars(screen, screen.width),
        Print(screen,
              SpeechBubble("Press space to see it again"),
              y=screen.height - 3,
              start_frame=300)]
    effects.append(Print(screen,
                     Rainbow(screen, FigletText("3",font = 'roman')),
                     screen.height // 2 ,
                     speed=0.5,
                     start_frame=0,
                     clear = True,
                     stop_frame = 30,
                     ))
    effects.append(Print(screen,
                     Rainbow(screen, FigletText("2",font = 'roman')),
                     screen.height // 2 ,
                     speed=0.5,
                     start_frame=35,
                     clear = True,
                     stop_frame = 70,
                     ))
    effects.append(Print(screen,
                     Rainbow(screen, FigletText("1",font = 'roman')),
                     screen.height // 2 ,
                     speed=0.5,
                     start_frame=75,
                     clear = True,
                     stop_frame = 100,
                     ))
    
    for _ in range(70):
        fireworks = [
            (PalmFirework, 25, 30),
            (PalmFirework, 25, 30),
            (StarFirework, 20, 35),
            (StarFirework, 25, 35),
            (StarFirework, 20, 35),
            (RingFirework, 30, 30),
            (SerpentFirework, 35, 35),
            (SerpentFirework, 35, 35)
        ]
        firework, start, stop = choice(fireworks)
        effects.append(
            firework(screen,
                     randint(0, screen.width),
                     randint(screen.height // 8, screen.height * 3 // 4),
                     randint(start, stop),
                     start_frame=randint(100, 250)))

    effects.append(Print(screen,
                         Rainbow(screen, FigletText("HAPPY",font = 'roman')),
                         screen.height // 2 - 8,
                         speed=1,
                         start_frame=100))
    effects.append(Print(screen,
                         Rainbow(screen, FigletText("NEW YEAR !",font = 'roman')),
                         screen.height // 2 ,
                         speed=1,
                         start_frame=100))
    effects.append(Print(screen,
                         Rainbow(screen, FigletText("2021", font = 'roman')),
                         screen.height // 2 + 8,
                         speed=1,
                         start_frame=100))
    scenes.append(Scene(effects, -1))

    screen.play(scenes, stop_on_resize=True)


while True:
    try:
        Screen.wrapper(demo)
        sys.exit(0)
    except ResizeScreenError:
        pass