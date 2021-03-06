import sys
import pygame
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboar import ScroreBoard
from button import Button


def run_game():
    # initialization
    pygame.init()
    ai_settings = Settings()
    # initializing settings

    # screen = pygame.display.set_mode((600, 600))
    # screen old

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    # name
    pygame.display.set_caption("Alien Invasion")
    # Создание кнопки
    play_button = Button(ai_settings, screen, "Play")

    # Создание экземпляра GameStats и ScoreBoard
    stats = GameStats(ai_settings)
    sb = ScroreBoard(ai_settings, screen, stats)
    # Creating ship
    ship = Ship(ai_settings, screen)
    bullets = Group()

    # Alien Group
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # bg_color = (230,230,230)
    # old color

    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
        if stats.game_active:

            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, 
								aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship,
                         aliens,  bullets, play_button)


run_game()
