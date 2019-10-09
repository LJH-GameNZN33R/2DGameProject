from pico2d import *
WEIGH = 1280
HEIGHT = 1024
open_canvas(WEIGH, HEIGHT)
stage1 = load_image('stageone.jpg')
character = load_image('animation_sheet.png')


def handle_events():
    global running
    global dir
    global stance_flag

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                stance_flag = 1
                dir += 1
            elif event.key == SDLK_LEFT:
                stance_flag = 0
                dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                stance_flag = 3
                dir -= 1
            elif event.key == SDLK_LEFT:
                stance_flag = 2
                dir += 1


x = 400
frame = 0
running = True
dir = 0
stance_flag = 3

while running:
    clear_canvas()
    stage1.draw(WEIGH / 2, HEIGHT / 2)
    character.clip_draw(frame*100, stance_flag*100, 100, 100, x, 275)
    handle_events()
    update_canvas()
    handle_events()
    x += dir*13
    frame = (frame + 1) % 8
    if x >= 1280:
        x = 1280
        stance_flag = 3
    elif x <= 0:
        x = 0
        stance_flag = 2
    delay(0.04)


