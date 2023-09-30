from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
point = load_image('hand_arrow.png')

def handle_events():
    global running
    global x1, y1
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            x1, y1 = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass



running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
x1, y1 = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
i = 0
# hide_cursor()

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    point.draw(x1, y1)

    character.clip_draw(frame * 100, 0, 100, 100, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8

    t = i / 100
    x = (1 - t) * x + t * x1  # 1-t : t의 비율로 x1, x2를 섞는다 (더한다)
    y = (1 - t) * y + t * y1
    i += 1
    delay(0.05)

    if x==x1 and y==y1:
        i=0


close_canvas()




