import pygame
import sys
import pygame_widgets
from pygame_widgets import button
from random import *
import time

pygame.init()
pygame.font.init()
seed(a=None,version=2)
####################   Music   ##############################
pygame.mixer.init()                                                                                                            
Bg_music = 'main.mp3'
pygame.mixer.music.load(Bg_music)
pygame.mixer.Channel(0).play(pygame.mixer.Sound(Bg_music))
pygame.mixer.music.play(loops = -1)
######################################################
###############  Window   #####################
screen = pygame.display.set_mode((1200,800))
pygame.display.set_caption('slots')
clock = pygame.time.Clock()
clock.tick(60)
#############################################
########   Font   ###################
font = pygame.font.SysFont("Times New Roman", 20)
winfont = pygame.font.SysFont("Times New Roman", 40)
######################  item pics    ##################################
Buffalo = pygame.image.load('buffalo.png')
Buffalo_img = pygame.transform.scale(Buffalo, (75,75))
J = pygame.image.load('jj.png')
J_img = pygame.transform.scale(J, (75,75))
K = pygame.image.load('k.png')
K_img = pygame.transform.scale(K, (75,75))
Eagle = pygame.image.load('bald.png')
Eagle_img = pygame.transform.scale(Eagle, (75,75))
A = pygame.image.load('a.png')
A_img = pygame.transform.scale(A, (75,75))
Ten = pygame.image.load('10.png')
Ten_img = pygame.transform.scale(Ten, (75,75))
wolf = pygame.image.load('wolf.png')
wolf_img = pygame.transform.scale(wolf, (75,75))
deer = pygame.image.load('deer.png')
deer_img = pygame.transform.scale(deer, (75,75))
bob = pygame.image.load('bobcat.png')
bob_img = pygame.transform.scale(bob, (75,75))
diamond = pygame.image.load('diamond.png')
diamond_img = pygame.transform.scale(diamond,(75,75))
pnglist = [Buffalo_img, J_img, K_img, Eagle_img, A_img, Ten_img, wolf_img, deer_img, bob_img, diamond_img]

mini_j = pygame.transform.scale(J_img, (30,30))  
mini_k = pygame.transform.scale(K_img,(30,30))
mini_a = pygame.transform.scale(A_img,(30,30))
mini_ten = pygame.transform.scale(Ten_img, (30,30))
mini_wolf = pygame.transform.scale(wolf_img,(30,30))
mini_deer = pygame.transform.scale(deer_img, (30,30))
mini_bob = pygame.transform.scale(bob_img,(30,30))
mini_eagle = pygame.transform.scale(Eagle_img, (30,30))
mini_buff = pygame.transform.scale(Buffalo_img,(30,30))
mini_diamond = pygame.transform.scale(diamond_img, (30,30))
##################   Button Pics/ ETC    #####################################
play = pygame.image.load('play.png')
play_img = pygame.transform.scale(play, (75,75))
Down = pygame.image.load('down.png')
Down_img = pygame.transform.scale(Down, (75,75))
Raise = pygame.image.load('up.png')
Raise_img = pygame.transform.scale(Raise, (75,75))
Low = pygame.image.load('down.png')
Low_img = pygame.transform.scale(Low, (75,75))
win = pygame.image.load('win.png')
win_img = pygame.transform.scale(win,(75,75))
equalss = pygame.image.load('equal.png')
equals_img = pygame.transform.scale(equalss, (15,15))

class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		pos = pygame.mouse.get_pos()
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True
		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False
		surface.blit(self.image, (self.rect.x, self.rect.y))
		return action
	
class Machine():
    def __init__(self,credits, bet, jp, maj, min, Take_in, Pay_out, K, A, ten, wolf, deer, bob, r1, r2, r3, r4, r5, r6, r7, r8, r9):
        self.credits = credits
        self.bet = bet
        self.jp = jp
        self.maj = maj 
        self.min = min
        self.Take_in = Take_in
        self.Pay_out = Pay_out
        self.K = K
        self.A = A
        self.ten = ten
        self.wolf = wolf
        self.deer = deer
        self.bob = bob
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3
        self.r4 = r4
        self.r5 = r5
        self.r6 = r6
        self.r7 = r7
        self.r8 = r8
        self.r9 = r9

    def stats(self):
        creds = font.render('Credits:  $' + str(self.credits), True, (229,230,228))
        screen.blit(creds, (600,10))
        bet = font.render('Bet  $' + str(self.bet), True, (229,230,228))
        screen.blit(bet, (600,30))
        Taken = font.render('Took in:  ' + str(self.Take_in), True, (229,230,228))
        screen.blit(Taken, ((600,50)))
        payed = font.render('Payed out:   ' + str(self.Pay_out), True, (229,230,228))
        screen.blit(payed, (600,70))
        screen.blit(mini_j, (600,100))
        screen.blit(equals_img, (640,100))
        screen.blit(font.render('$' + str(self.bet), True, (230,230,0) ), (670,100))
        screen.blit(mini_k, (600,130))
        screen.blit(equals_img, (640,130))
        screen.blit(font.render('$' + str(self.K), True, (230,230,0) ), (670, 130))
        screen.blit(mini_a, (600,162))
        screen.blit(equals_img, (640,162))
        screen.blit(font.render('$' + str(self.A), True, (230,230,0) ), (670, 162))
        screen.blit(mini_ten, (600,200))
        screen.blit(equals_img, (640,200))
        screen.blit(font.render('$' + str(self.ten), True, (230,230,0) ), (675, 200))
        screen.blit(mini_wolf, (600,240))
        screen.blit(equals_img, (640,240))
        screen.blit(font.render('$' + str(self.wolf), True, (230,230,0) ), (675, 240))
        screen.blit(mini_deer, (600,280))
        screen.blit(equals_img, (640,280))
        screen.blit(font.render('$' + str(self.deer), True, (230,230,0) ), (675, 280))
        screen.blit(mini_bob, (600,335))
        screen.blit(equals_img, (640,335))
        screen.blit(font.render('$' + str(self.bob), True, (230,230,0) ), (675, 335))
        screen.blit(mini_eagle, (600,365))
        screen.blit(equals_img, (640,365))
        screen.blit(font.render('$' + str(self.min), True, (230,230,0) ), (675, 365))
        screen.blit(mini_buff, (600,395))
        screen.blit(equals_img, (640,395))
        screen.blit(font.render('$' + str(self.maj), True, (230,230,0) ), (675, 395))
        screen.blit(mini_diamond, (600,435))
        screen.blit(equals_img, (640,435))
        screen.blit(font.render('$' + str(self.jp), True, (230,230,0) ), (675, 435))


    def spin(self):
        REEL_AREA = pygame.Rect(200, 200, 400,400)

        for x in range (20):
            pygame.draw.rect(screen, (0, 0, 0), REEL_AREA)
            self.r1 = pnglist[randint(0, 9)]
            self.r2 = pnglist[randint(0, 9)]
            self.r3 = pnglist[randint(0, 9)]
            self.r4 = pnglist[randint(0, 9)]
            self.r5 = pnglist[randint(0, 9)]
            self.r6 = pnglist[randint(0, 9)]
            self.r7 = pnglist[randint(0, 9)]
            self.r8 = pnglist[randint(0, 9)]
            self.r9 = pnglist[randint(0, 9)]
            r1_pos = screen.blit(self.r1, (200, 200))
            r2_pos = screen.blit(self.r2, (200, 300))
            r3_pos = screen.blit(self.r3, (200, 400))
            r4_pos = screen.blit(self.r4, (300, 200))
            r5_pos = screen.blit(self.r5, (300, 300))
            r6_pos = screen.blit(self.r6, (300, 400))
            r7_pos = screen.blit(self.r7, (400, 200))
            r8_pos = screen.blit(self.r8, (400, 300))
            r9_pos = screen.blit(self.r9, (400, 400))


            pygame.display.update()
            pygame.time.delay(45)


    def Raise(self):
        if self.bet != self.credits:
            pygame.mixer.music.load('raise_beep.mp3')
            pygame.mixer.music.play()
            self.bet += 1            
            self.K += 3
            self.A  += 5
            self.ten += 10
            self.wolf += 20
            self.deer += 30
            self.bob += 50
            screen.fill((0,0,0))
            slots.stats()
            pygame.mixer.music.load('raise_beep.mp3')
            pygame.mixer.music.play()

    def lower(self):
        if self.bet != 1:
            pygame.mixer.music.load('lower_beep.mp3')
            pygame.mixer.music.play()
            self.bet  -= 1
            self.K -= 3
            self.A  -= 5
            self.ten -= 10
            self.wolf -= 20
            self.deer -= 30
            self.bob -= 50
            screen.fill((0,0,0))
            slots.stats()

    def check_win(self):
        if self.r2 == self.r5 and self.r5 == self.r8:
            print("win")
            pygame.mixer.music.load('win.wav')
            pygame.mixer.music.play()
            screen.blit(win_img, (520, 555))

            if self.r2 == pnglist[0]:
                self.credits += self.maj
                self.Pay_out += self.maj
                self.maj = 1000
                print("maj win")
                screen.blit(winfont.render("$" + str(self.maj), True, (230,230,0)), (620, 555))

            if self.r2 == pnglist[1]:
                self.credits += self.bet
                self.Pay_out += self.bet
                print("win")
                screen.blit(winfont.render("$" + str(self.bet), True, (230,230,0)), (620, 555))
            if self.r2 == pnglist[2]:
                self.credits += self.K
                self.Pay_out += self.K
                print(" win")
                screen.blit(winfont.render("$" + str(self.K), True, (230,230,0)), (620, 555))
            if self.r2 == pnglist[3]:
                self.credits += self.min
                self.Pay_out += self.min
                self.min = 100
                print("min win")
                screen.blit(winfont.render("$" + str(self.min), True, (230,230,0)), (620, 555))
            if self.r2 == pnglist[4]:
                self.credits += self.A
                self.Pay_out += self.A
                print("win")
                screen.blit(winfont.render("$" + str(self.A), True, (230,230,0)), (620, 555))
            if self.r2 == pnglist[5]:
                self.credits += self.ten
                self.Pay_out += self.ten
                print("win")
                screen.blit(winfont.render("$" + str(self.ten), True, (230,230,0)), (620, 555))
            if self.r2 == pnglist[6]:
                self.credits += self.wolf
                self.Pay_out += self.wolf
                print("win")
                screen.blit(winfont.render("$" + str(self.wolf), True, (230,230,0)), (620, 555))
            if self.r2 == pnglist[7]:
                self.credits += self.deer
                self.Pay_out += self.deer
                print("win")
                screen.blit(winfont.render("$" + str(self.deer), True, (230,230,0)), (620, 555))
            if self.r2 == pnglist[8]:
                self.credits += self.bob
                self.Pay_out += self.bob
                print("win")
                screen.blit(winfont.render("$" + str(self.bob), True, (230,230,0)), (620, 555))
            if self.r2 == pnglist[9]:
                self.credits += self.jp
                self.Pay_out += self.jp
                self.jp = 1000
                print("jp win")
                screen.blit(winfont.render("$" + str(self.jp), True, (230,230,0)), (620, 555))



slots = Machine(credits=100, bet=1, jp=1000, maj=500, min=100, Take_in=0, Pay_out=0, K=2, A=5, ten=10, wolf=20, deer=35, bob=50, r1=pnglist[0], r2=pnglist[1], r3=pnglist[2], r4=pnglist[3], r5=pnglist[4], r6=pnglist[5], r7=pnglist[6], r8=pnglist[7], r9=pnglist[8])
play_button = Button(460,555, play_img, 0.5)
raise_button = Button(200,555, Raise_img, 0.5)
lower_button = Button(280,555, Low_img, 0.5)


while slots.credits > 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if play_button.draw(screen):
            slots.credits -= slots.bet
            slots.maj += slots.bet
            slots.min += slots.bet
            slots.jp += slots.bet
            screen.fill((0,0,0))
            slots.stats()
            pygame.time.delay(100)
            slots.spin()
            slots.check_win()
            pygame.time.delay(222)

        if lower_button.draw(screen):
            slots.lower()
            if slots.bet <= 0:
                 slots.bet = 1
            
        
        if raise_button.draw(screen):
             slots.Raise()
             if slots.bet > slots.credits:
                  slots.bet = 1
    pygame.display.update()