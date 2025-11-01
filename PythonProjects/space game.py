
import random
import sys
import math
import pygame
from pygame.locals import *

# -------- CONFIG --------
WIDTH, HEIGHT = 640, 800
FPS = 60
PLAYER_SPEED = 350  # pixels per second
BULLET_SPEED = 700
ENEMY_SPEED_MIN = 80
ENEMY_SPEED_MAX = 180
ENEMY_SPAWN_INTERVAL = 0.8  # seconds
MAX_LIVES = 3

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 50, 50)
GREEN = (80, 200, 120)
YELLOW = (240, 220, 100)
BLUE = (80, 160, 240)

# -------- PYGAME SETUP --------
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter — Simple Pygame Demo")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 28)
big_font = pygame.font.SysFont(None, 64)

# -------- HELPERS / CLASSES --------

def clamp(x, a, b):
    return max(a, min(b, x))


class Player:
    def __init__(self):
        self.w = 40
        self.h = 48
        self.x = WIDTH // 2
        self.y = HEIGHT - 100
        self.speed = PLAYER_SPEED
        self.color = BLUE
        self.cooldown = 0.15  # seconds between shots
        self._cd_timer = 0.0
        self.alive = True

    def rect(self):
        return pygame.Rect(self.x - self.w // 2, self.y - self.h // 2, self.w, self.h)

    def update(self, dt, keys):
        dx = 0
        dy = 0
        if keys[K_LEFT] or keys[K_a]:
            dx -= 1
        if keys[K_RIGHT] or keys[K_d]:
            dx += 1
        if keys[K_UP] or keys[K_w]:
            dy -= 1
        if keys[K_DOWN] or keys[K_s]:
            dy += 1
        if dx != 0 or dy != 0:
            # normalize for diagonal movement
            l = math.hypot(dx, dy)
            dx /= l
            dy /= l
        self.x += dx * self.speed * dt
        self.y += dy * self.speed * dt
        # clamp to screen
        self.x = clamp(self.x, self.w // 2, WIDTH - self.w // 2)
        self.y = clamp(self.y, self.h // 2, HEIGHT - self.h // 2)

        if self._cd_timer > 0:
            self._cd_timer -= dt

    def can_shoot(self):
        return self._cd_timer <= 0

    def shoot(self):
        self._cd_timer = self.cooldown
        return Bullet(self.x, self.y - self.h // 2 - 6)

    def draw(self, surf):
        # draw a simple triangle ship
        p = [(self.x, self.y - self.h // 2),
             (self.x - self.w // 2, self.y + self.h // 2),
             (self.x + self.w // 2, self.y + self.h // 2)]
        pygame.draw.polygon(surf, self.color, p)
        # engine glow
        pygame.draw.circle(surf, YELLOW, (int(self.x), int(self.y + self.h // 2 - 6)), 6)


class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 4
        self.speed = BULLET_SPEED
        self.color = WHITE
        self.alive = True

    def update(self, dt):
        self.y -= self.speed * dt
        if self.y < -10:
            self.alive = False

    def draw(self, surf):
        pygame.draw.circle(surf, self.color, (int(self.x), int(self.y)), self.r)

    def rect(self):
        return pygame.Rect(self.x - self.r, self.y - self.r, self.r * 2, self.r * 2)


class Enemy:
    def __init__(self):
        self.w = random.randint(28, 48)
        self.h = self.w
        self.x = random.randint(self.w // 2, WIDTH - self.w // 2)
        self.y = -self.h
        self.speed = random.uniform(ENEMY_SPEED_MIN, ENEMY_SPEED_MAX)
        self.color = RED
        self.alive = True

    def update(self, dt):
        self.y += self.speed * dt
        if self.y > HEIGHT + 50:
            self.alive = False

    def draw(self, surf):
        pygame.draw.rect(surf, self.color, (int(self.x - self.w // 2), int(self.y - self.h // 2), self.w, self.h), border_radius=6)

    def rect(self):
        return pygame.Rect(self.x - self.w // 2, self.y - self.h // 2, self.w, self.h)


# -------- GAME STATE --------

def new_game():
    return {
        'player': Player(),
        'bullets': [],
        'enemies': [],
        'spawn_timer': 0.0,
        'score': 0,
        'lives': MAX_LIVES,
        'paused': False,
        'game_over': False,
    }

state = new_game()

# -------- MAIN LOOP --------

def draw_hud(surf, score, lives):
    score_s = font.render(f"Score: {score}", True, WHITE)
    lives_s = font.render(f"Lives: {lives}", True, WHITE)
    surf.blit(score_s, (8, 8))
    surf.blit(lives_s, (8, 36))


def show_text_center(surf, text, fontobj, y_offset=0, color=WHITE):
    txt = fontobj.render(text, True, color)
    r = txt.get_rect(center=(WIDTH // 2, HEIGHT // 2 + y_offset))
    surf.blit(txt, r)


def update_game(dt):
    if state['game_over'] or state['paused']:
        return

    p = state['player']
    keys = pygame.key.get_pressed()
    p.update(dt, keys)

    # bullets
    for b in state['bullets']:
        b.update(dt)
    state['bullets'] = [b for b in state['bullets'] if b.alive]

    # enemies
    for e in state['enemies']:
        e.update(dt)
    state['enemies'] = [e for e in state['enemies'] if e.alive]

    # spawn enemies
    state['spawn_timer'] -= dt
    if state['spawn_timer'] <= 0:
        state['spawn_timer'] = ENEMY_SPAWN_INTERVAL
        state['enemies'].append(Enemy())

    # collisions: bullets vs enemies
    for b in state['bullets']:
        for e in state['enemies']:
            if b.alive and e.alive and b.rect().colliderect(e.rect()):
                b.alive = False
                e.alive = False
                state['score'] += 10

    # collisions: player vs enemies
    for e in state['enemies']:
        if e.alive and p.rect().colliderect(e.rect()):
            e.alive = False
            state['lives'] -= 1
            if state['lives'] <= 0:
                state['game_over'] = True


def draw_game(surf):
    surf.fill((12, 12, 20))
    # starfield background (simple moving dots)
    for i in range(40):
        x = (i * 47) % WIDTH
        y = (i * 89 + pygame.time.get_ticks() // 6) % HEIGHT
        s = 1 + (i % 3)
        surf.fill((20, 20, 30), (x, y, s, s))

    # draw entities
    for b in state['bullets']:
        b.draw(surf)
    for e in state['enemies']:
        e.draw(surf)
    state['player'].draw(surf)

    draw_hud(surf, state['score'], state['lives'])

    if state['paused']:
        show_text_center(surf, "PAUSED", big_font, y_offset=-30, color=YELLOW)
        show_text_center(surf, "Press P to resume", font, y_offset=30)
    if state['game_over']:
        show_text_center(surf, "GAME OVER", big_font, y_offset=-30, color=RED)
        show_text_center(surf, f"Score: {state['score']}", font, y_offset=30)
        show_text_center(surf, "Press R to restart or Esc to quit", font, y_offset=70)


def handle_input(event):
    if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
        if event.key == K_p:
            state['paused'] = not state['paused']
        if event.key == K_r:
            # restart
            new = new_game()
            state.update(new)
        if not state['game_over'] and not state['paused']:
            if event.key == K_SPACE or event.key == K_z:
                p = state['player']
                if p.can_shoot():
                    state['bullets'].append(p.shoot())


def main_loop():
    accumulator = 0.0
    while True:
        dt = clock.tick(FPS) / 1000.0
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            handle_input(event)

        # allow holding space to fire (rapid if cooldown allows)
        keys = pygame.key.get_pressed()
        if (keys[K_SPACE] or keys[K_z]) and not state['paused'] and not state['game_over']:
            p = state['player']
            if p.can_shoot():
                state['bullets'].append(p.shoot())

        update_game(dt)
        draw_game(screen)
        pygame.display.flip()


if __name__ == '__main__':
    try:
        main_loop()
    except Exception as e:
        pygame.quit()
        raise
