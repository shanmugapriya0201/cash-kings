import pgzrun
from random import randint
WIDTH = 600
HEIGHT = 400

hero = Actor('hero')
hero.x = WIDTH / 2
hero.y = HEIGHT
WHITE = (219, 219, 219)
bank_1 = Actor('bank_1')
wall = Actor('wall')
wall.x = 180
wall.y = 250
wall_blue = Actor('wall_blue')
wall_blue.x = 450
wall_blue.y = 250
thief_1 = Actor('thief_1')
thief_1.x = 500
thief_1.y = 250
step_count = 0
score = 0


def draw():
    screen.blit('background', (0,0))
    hero.draw()
    bank_1.draw()
    wall.draw()
    wall_blue.draw()
    thief_1.draw()
    screen.draw.text("score: "+str(score), (500, 10), fontsize=25, color=WHITE)


def update():
    original_x = hero.x
    original_y = hero.y
    move_hero()
    check_hero_boundaries()
    thief_1_action()
    check_thief_1_boundaries()
    hero_wall_collision(original_x, original_y)
    hero_wall_blue_collision(original_x, original_y)
    hero_bank_1_collision(original_x, original_y)
    hero_thief_1_collision()

def move_hero():
    if keyboard.left:
        hero.x -= 5
    if keyboard.right:
        hero.x += 5
        hero.angle = 0
    if keyboard.up:
        hero.y -= 5
        hero.angle = 90
    if keyboard.down:
        hero.y += 5
        hero.angle = 270


def hero_wall_collision(original_x, original_y):
    if hero.colliderect(wall):
        hero.x = original_x
        hero.y = original_y


def hero_wall_blue_collision(original_x, original_y):
    if hero.colliderect(wall_blue):
        hero.x = original_x
        hero.y = original_y


def hero_bank_1_collision(original_x, original_y):
    if hero.colliderect(bank_1):
        hero.x = original_x
        hero.y = original_y


def hero_thief_1_collision():
    global score
    if hero.colliderect(thief_1):
        score += 1



def check_hero_boundaries():
    if hero.right > WIDTH:
        hero.right = WIDTH
    if hero.left < 0:
        hero.left = 0
    if hero.top < 0:
        hero.top = 0
    if hero.bottom > HEIGHT:
        hero.bottom = HEIGHT


def check_thief_1_boundaries():
    if thief_1.right > WIDTH:
        thief_1.right = WIDTH
    if thief_1.left < 0:
        thief_1.left = 0
    if thief_1.top < 0:
        thief_1.top = 0
    if thief_1.bottom > HEIGHT:
        thief_1.bottom = HEIGHT


def thief_1_action():
    global step_count
    choice = randint(0, 1)
    if step_count > 0:
        step_count -= 1
        if thief_1.angle == 0:
            thief_1.x += 5
        if thief_1.angle == 90:
            thief_1.y -= 5
        if thief_1.angle == 180:
            thief_1.x -= 5
        if thief_1.angle == 270:
            thief_1.y += 5
    elif choice == 0:
        step_count = 20
    elif choice == 1:
        thief_1.angle = randint(0, 3) * 90



pgzrun.go()