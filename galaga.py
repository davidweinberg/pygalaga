import pgzrun
import random

# screen 
WIDTH  = 1200
HEIGHT = 1000

#defining colours for our game
WHITE = (255,255,255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
BLACK = (0, 0, 0)

# galaga ship
ship = Actor('ship')
ship.x = WIDTH//2 # double slash makes int
ship.y = HEIGHT-100
ship.dead = False
ship.countdown = 90

bullets = []
enemies = []
direction = 1
score = 0

# setup enemy array 
for x in range(8):
  for y in range(4):
    enemies.append(Actor('bug'))
    enemies[-1].x = 100 + 90*x
    enemies[-1].y = 80 + 80*y

### functions
def on_key_down(key):
  if ship.dead == False:
    if key == keys.SPACE:
      bullets.append(Actor('bullet'))
      bullets[-1].x = ship.x
      bullets[-1].y = ship.y-50

def draw_score():
  screen.draw.text(str(score),(50, 30), fontname="arcade", fontsize=20)


def update():
  global score
  global direction

  # ship movement using arrow keys (left and right)
  if keyboard.left:
    ship.x -= 5
  elif keyboard.right:
    ship.x += 5 

  for bullet in bullets:
    if bullet.y < -20:
      bullets.remove(bullet)
    else:
      bullet.y -= 10

  moveDown = False

  if len(enemies)>0 and (enemies[-1].x > WIDTH-80 or enemies[0].x < 50):
    moveDown = True
    direction = direction*-1


  for enemy in enemies:
    enemy.x += 5*direction

    if moveDown == True:
      enemy.y += 50

    for bullet in bullets:
      if enemy.colliderect(bullet):
        score += 150
        bullets.remove(bullet)
        enemies.remove(enemy)

    if enemy.colliderect(ship):
      ship.dead = True

  if ship.dead:
    ship.countdown -= 1
  if ship.countdown == 0:
    ship.dead = False
    ship.countdown = 90
    

def draw():
  screen.clear();
  screen.fill(BLACK)

  for bullet in bullets:
    bullet.draw()

  for enemy in enemies:
    enemy.draw()

  if ship.dead == False:
    ship.draw()
  draw_score()


# run the thing!
pgzrun.go()
