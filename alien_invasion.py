import pygame 
from pygame.sprite import Group
from settings import Settings 
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf

def run_game():
	#初始化游戏并、设置和屏幕对象
	pygame.init()
	ai_settings=Settings()
	screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption('Alien invasion')
	#创建play按钮
	play_button=Button(ai_settings,screen,"Play")
	stats=GameStats(ai_settings)
	#设置背景色
	bg_color=(230,230,230)
	#创建一艘飞船、一个子弹的编组、一个外星人编组
	ship=Ship(ai_settings,screen)
	bullets=Group()
	aliens=Group()
	#创建外星人群
	gf.create_fleet(ai_settings,screen,ship,aliens)
	#创建存储游戏统计信息的实例，并创建记分牌
	ststs=GameStats(ai_settings)
	sb=Scoreboard(ai_settings,screen,stats)
	
	#开始游戏主循环
	while True:
		#监视键盘是鼠标事件
		gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
			gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
		#每次循环时都重绘屏幕、刷新屏幕
		gf.update_screen(ai_settings,screen, stats,sb,ship,aliens,bullets,play_button)
		
		
run_game()


