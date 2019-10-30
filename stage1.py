from pico2d import *
import game_framework
# import Items
WEIGH = 1280
HEIGHT = 1024
open_canvas(WEIGH, HEIGHT)
stage1 = load_image('stageone.jpg')
daath = load_image('daath_animation_sheet.png')
daath_jump = load_image('daath_jump_animation.png')


def handle_events():
    global running
    global dir
    global stance_flag
    global jump_stance_flag
    global y_dir
    global jump_count
    global y
    global jump_flag
    global story_flag1
    global story_flag2
    global story_flag3

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
                jump_flag = 1
                if stance_flag == 0:
                    jump_stance_flag = 0
                elif stance_flag == 1:
                    jump_stance_flag = 1
                if event.key == SDLK_LEFT:
                    jump_stance_flag = 1
                elif event.key == SDLK_RIGHT:
                    jump_stance_flag = 0
                if jump_count <= 0:
                    y_dir = 2
                    jump_count += 1
                elif jump_count >= 2:
                    while y == 275:
                        y_dir = 0
                        y -= 2
                        if y == 275:
                            y_dir += 1
                if y == 275:
                    jump_flag = 0
                    jump_count = 0
                    y_dir = 2

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
jump_frame = 0
running = True
dir = 0
stance_flag = 3
y_dir = 0
jump_count = 0
jump_flag = 0
jump_stance_flag = 1

while running:
    clear_canvas()
    jump_frame += 1
    stage1.draw(WEIGH / 2, HEIGHT / 2)
    if jump_flag == 0 and y <= 275:
        frame = (frame + 1) % 8
        daath.clip_draw(frame*100, stance_flag*100, 100, 100, x, y)
    elif jump_flag == 1 or y > 275:
        jump_frame = jump_frame + 1
        if jump_frame >= 9:
            daath_jump.clip_draw(900, jump_stance_flag*100, 100, 100, x, y)
        else:
            daath_jump.clip_draw(jump_frame*100, jump_stance_flag*100, 100, 100, x, y)
        delay(0.001)

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
    delay(0.045)

    #if story_flag1:
    #    change_state()
    #    pass




