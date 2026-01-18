from pygame import *
from random import randint

init()
W, H = 1000, 650
FPS = 120
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (63, 211, 255)

window = display.set_mode((W, H))
display.set_caption("Flappy Bird")

clock = time.Clock()

player_size = 80
player = Rect(100, H // 2, player_size, player_size)
player_speed = 7


def generate_pipes(
        count,
        pipe_width=140,
        gap=280,
        min_height=50,
        max_height=440,
        distance=650):
    pipes = []
    start_x = H
    for _ in range(count):
        height = randint(min_height, max_height)
        top_pipe = Rect(start_x, 0, pipe_width, height)
        bottom_pipe = Rect(start_x, height + gap, pipe_width, H - (height + gap))
        pipes.extend([top_pipe, bottom_pipe])
        start_x += distance
    return pipes


pipes = generate_pipes(150)

game = True
lose = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not lose:

        keys = key.get_pressed()
        if keys[K_UP] and player.top > 0:
            player.y -= player_speed
        if keys[K_DOWN] and player.bottom < H:
            player.y += player_speed

        window.fill(BLUE)

        draw.rect(window, YELLOW, player)

        for pipe in pipes:
            pipe.x -= 5
            draw.rect(window, GREEN, pipe)

            if player.colliderect(pipe):
                lose = False

            if pipe.x <= -200:
                pipes.remove(pipe)

    else:

        game = False

    clock.tick(FPS)
    display.update()