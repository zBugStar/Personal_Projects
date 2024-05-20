import pgzrun
import random

from pgzero.animation import animate

FONT_COLOR = (255, 255, 255)
WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
CENTER = CENTER_X, CENTER_Y
FINAL_LEVEL = 10
START_SPEED = 11
COLORS = ["green", "blue", "yellow"]

game_over = False
game_complete = False
current_level = 1
gems = []
animations = []


def display_message(heading_text, sub_heading_text):
    screen.draw.text(heading_text, fontsize=60, center=CENTER, color=FONT_COLOR)
    screen.draw.text(sub_heading_text,
                     fontsize=30,
                     center=(CENTER_X, CENTER_Y + 30),
                     color=FONT_COLOR)


def draw():
    screen.clear()
    screen.blit("space_a", (0, 0))
    if game_over:
        display_message("GAME OVER", "Try again")
    elif game_complete:
        display_message("YOU WON!", "Well done")
    else:
        for gem in gems:
            gem.draw()


def update():
    global gems
    if len(gems) == 0:
        gems = make_gems(current_level)


def make_gems(number_of_extra_gems):
    colors_to_create = get_colors_to_create(number_of_extra_gems)
    new_gems = create_gems(colors_to_create)
    layout_gems(new_gems)
    animate_gems(new_gems)
    return new_gems


def get_colors_to_create(number_of_extra_gems):
    colors_to_create = ["red"]
    for i in range(0, number_of_extra_gems):
        random_color = random.choice(COLORS)
        colors_to_create.append(random_color)
    return colors_to_create


def create_gems(colors_to_create):
    new_gems = []
    for color in colors_to_create:
        gem = Actor(color + "-gem")
        new_gems.append(gem)
    return new_gems


def layout_gems(gems_to_layout):
    number_of_gaps = len(gems_to_layout) + 1
    gap_size = WIDTH / number_of_gaps
    random.shuffle(gems_to_layout)
    for index, gem in enumerate(gems_to_layout):
        new_x_pos = (index + 1) * gap_size
        gem.x = new_x_pos


def animate_gems(gems_to_animate):
    for gem in gems_to_animate:
        duration = START_SPEED - current_level
        gem.anchor = ("center", "bottom")
        animation = animate(gem, duration=duration, on_finished=handle_game_over, y=HEIGHT)
        animations.append(animation)


def handle_game_over():
    global game_over
    game_over = True


def on_mouse_down(pos):
    global gems, current_level
    for gem in gems:
        if gem.collidepoint(pos):
            if "red" in gem.image:
                red_gem_click()
            else:
                handle_game_over()


def red_gem_click():
    global current_level, gems, animations, game_complete
    stop_animations(animations)
    if current_level == FINAL_LEVEL:
        game_complete = True
    else:
        current_level = current_level + 1
        gems = []
        animations = []


def stop_animations(animations_to_stop):
    for animation in animations_to_stop:
        if animation.running:
            animation.stop()


pgzrun.go()
