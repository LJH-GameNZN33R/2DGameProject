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
    global y_dir
    global jump_count
    global y

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
            elif event.key == SDLK_UP:
                if jump_count <= 0:
                    y_dir = 1
                    jump_count += 1
                elif jump_count >= 2:
                    while y == 275:
                        y_dir = 0
                        y -= 1
                        if y == 275:
                            y_dir += 1
                if y == 275:
                    jump_count = 0
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
y = 275
frame = 0
running = True
dir = 0
stance_flag = 3
y_dir = 0
jump_count = 0

while running:
    clear_canvas()
    stage1.draw(WEIGH / 2, HEIGHT / 2)
    character.clip_draw(frame*100, stance_flag*100, 100, 100, x, y)
    handle_events()
    update_canvas()
    handle_events()
    x += dir*13
    y += y_dir*6
    frame = (frame + 1) % 8
    if x >= 1280:
        x = 0
    elif x <= 0:
        x = 1280
    if y <= 275:
        y_dir = 0
    elif y >= 350:
        y_dir -= 1
    delay(0.04)


