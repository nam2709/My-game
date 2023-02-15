import pygame
import time
from random import randint


pygame.init()


screen = pygame.display.set_mode((680,1500))
Yellow= (238,248,255)
Black = (0,139,139)
Orange=(255,115,0)
Violet = (125,0,225)
LightBlue = (0,125,225)
LightGreen = (80,225,90)
AB= 800
BA= 1000
AG= 1200
AC = 1400
AD = 1600
MN = 500
GAP = 100
CD = 0
ab = 50
ac = 50
cd = 50
de = 50
GH = -100
HG = -100
ef = randint (1500 ,3000)
i = randint (500, 1500)
gh = 5300 - ef
IK = CD + ef + i
ag = randint(500,850)
bg = randint(500,850)
gb = randint(500,850)
bc = randint(500,850)
be = randint(500,850)
OP=0
OP_r = 0
TP_r = 800
TP = 800
score = 0
font = pygame.font.SysFont('sans',50)
a = 5
b = 5
c = 5
d = 5
e = 5
f= 5
g = 5
h = 5
k = 5
l = 5
p = 5
u = 5
z = 5
v = 0
o = 0.5
t = 0.5
m=0
TOTAL = (m + score*200)/2


clock = pygame.time.Clock()
direction = ""
A_image = pygame.image.load("A.jpg")
A_image = pygame.transform.scale(A_image,(720,550))
B_image = pygame.image.load("B.png")
B_image = pygame.transform.scale(B_image,(150,150))
C_image = pygame.image.load("C.png")
C_image = pygame.transform.scale(C_image,(150,150))
D_image = pygame.image.load("D.gif")
D_image = pygame.transform.scale(D_image,(300,450))
 
sound = pygame.mixer.Sound('A.mp3')
sound.set_volume(1.0)


#sound_1 = pygame.mixer.Sound('B.mp3')
#sound_1.set_volume(100.0)


pygame.mixer.Sound.play(sound )




running = True
while True:
	
 clock.tick(60)
 screen.fill(Yellow)
 screen.blit(A_image,(0,430))
 screen.blit(B_image,(108, 1150))
 screen.blit(C_image,(468, 1150))
	
	
 score_txt = font.render("Score : " + str (score) , True ,Black)
 m_txt = font.render(" Meters : " +str (round(m))+" m", True, Black)
 TOTAL_txt = font.render("TOTAL:" + str(round(TOTAL)),True,Black)
 screen.blit(score_txt,(30,120))
 screen.blit(m_txt,(10,60))
 screen.blit(TOTAL_txt,(380, 238))
	
 mn = pygame.draw.rect(screen,LightGreen,(50,MN,ab,ac)) 
	
 op = pygame.draw.rect(screen,LightBlue,(BA ,ag,65,100))
 op_1 = pygame.draw.rect(screen,Orange,(AB ,bg,50,50))
 op_2 = pygame.draw.rect(screen,LightBlue,(AC,bc,100,65))
 op_3 = pygame.draw.rect(screen,Orange,(AD,be,50,50))
 op_5 = pygame.draw.rect(screen,Orange,(AG ,gb,50,50))
 ot = pygame.draw.rect(screen,LightBlue,(GH ,850,50,50))
 ot_r= pygame.draw.rect(screen,LightBlue,(HG ,395,50,330))
 mp = pygame.draw.rect(screen,Violet,(CD ,900,ef,100))
 mr = pygame.draw.rect(screen,Violet,(IK,900,gh,100))
 mv = pygame.draw.rect(screen,Black,(OP,950,800,100))
 mu = pygame.draw.rect(screen,Black,(TP,950,800,100))
 mv_r = pygame.draw.rect(screen,Violet,(OP_r,390,800,50))
 mu_r = pygame.draw.rect(screen,Violet,(TP_r,390,800,50))
	
 pygame.draw.line(screen,Black,(368,1100),(368, 1460))
	
 AB = AB - a
 AG = AG -b
 BA = BA -c
 AC -= d
 AD -= e
	
	
 CD -= f
 GH -= g
 HG -= h
 IK -= k
 MN += v
 OP -= l
 TP -= p
 OP_r -= z
 TP_r -= u
 v += o
 m += t
 TOTAL = (m+ score*150)/2
	
 if CD == -3000:
  CD = 5000
  GH = 5300
  HG = 5300
 if IK == -2500:
  IK = 4200
  GH = 4500
  HG = 4500
 if OP == -800:
  OP = 800
 if TP == -800:
  TP = 800
 if OP_r == -800:
  OP_r = 800
 if TP_r == -800:
  TP_r = 800
	
  
  
 if direction == "move" :
  ab = 50
  ac = 50
 if direction == "punch" :
  ab = ab + 25
 if ab == 125:
  direction = "move"
	
    
 if mn.colliderect(mp):
 # pygame.mixer.Sound.play(sound_1)
  v = 0
  v -= 10
 if mn.colliderect(mr):
  v = 0
  v -= 10
   
 for tube in [op,op_2,ot,ot_r,mv,mu,mv_r,mu_r]:
  if mn.colliderect(tube):
   screen.blit(D_image,(350,480))
   a = 0
   b = 0
   c = 0
   d = 0
   e = 0
   f = 0
   g = 0
   h = 0
   k = 0
   v = 0
   o = 0
   t = 0
   if direction == "punch":
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    k = 0
    v = 0
    o = 0
    t = 0
   
 if mn.colliderect(op_1):
  if ab == 50:
    screen.blit(D_image,(350,480))
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    k = 0
    v = 0
    o = 0
    t = 0
    v = -10
  if 50 < ab <= 130:
   AB = 900
   score += 1
  
	
 if mn.colliderect(op_3):
  if ab == 50:
    screen.blit(D_image,(350,480))
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    k = 0
    v = 0
    o = 0
    t = 0
    v = -10
  if 50 < ab <= 130:
   AD = 1500
   score += 1
  
   
 if mn.colliderect(op_5):
  if ab == 50:
    screen.blit(D_image,(350,480))
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    k = 0
    v = 0
    o = 0
    t = 0
    v = -10
  if 50 < ab <= 130:
   AG = 1800
   score += 1
	
   
   
    
	
 if AB == -450:
   bg = randint(500,850)
   AB = 800
   
 elif BA == -350:
   ag = randint(500,850)
   BA = 1000
     
 elif AG == -380:
   gb = randint(500,850)
   AG = 1200
   
 elif AC == -390:
   bc = randint(500,850)
   AC = 1400
	
 elif AD == -510:
   be = randint(500,850)
   AD = 1600
   
 mouse_x,mouse_y = pygame.mouse.get_pos()
	
 for event in pygame.event.get():
  if event.type == pygame.MOUSEBUTTONDOWN:
   if event.button == 1:
    if (0 < mouse_x < 350) and (950 < mouse_y < 1500):
     direction = "punch"
    
    if (0 < mouse_x < 250) and (0 < mouse_y < 250):
     sound.set_volume(0)
     
    if (0 < mouse_x < 250) and (0 < mouse_y < 250):  
     pygame.mixer.Sound.stop(sound)
     pygame.mixer.Sound.play(sound)
    
    if (380 < mouse_x < 680) and (0 < mouse_y < 250):
     sound.set_volume(1.0)
   
    if (380 < mouse_x < 680) and (950 < mouse_y < 1500):
     v = 0
     v = -10
    
    if (90 < mouse_x < 650) and (300< mouse_y < 920):
     if a == 0:
      AB= 800
      BA= 1000
      AG= 1200
      AC = 1400
      AD = 1600
      MN = 500
      GAP = 100
      CD = 0
      ab = 50
      ac = 50
      cd = 50
      de = 50
      GH = -100
      HG = -100
      ef = randint (1500 ,3000)
      i = randint (500, 1500)
      gh = 5300 - ef
      IK = CD + ef + i
      ag = randint(500,850)
      bg = randint(500,850)
      gb = randint(500,850)
      bc = randint(500,850)
      be = randint(500,850)
      OP=0
      TP = 800
      score = 0
      a = 5
      b = 5
      c = 5
      d = 5
      e = 5
      f= 5
      g = 5
      h = 5 
      k = 5
      l = 5
      p = 5
      v = 0
      o = 0.5
      t = 0.5
      m=0
    
    
  if event.type == pygame.KEYDOWN:
   if event.key == pygame.K_1:
    direction = "punch"
            
   if event.key == pygame.K_SPACE:
    if a == 0:
      AB= 800
      BA= 1000
      AG= 1200
      AC = 1400
      AD = 1600
      MN = 500
      GAP = 100
      CD = 0
      ab = 50
      ac = 50
      cd = 50
      de = 50
      GH = -100
      HG = -100
      ef = randint (1500 ,3000)
      i = randint (500, 1500)
      gh = 5300 - ef
      IK = CD + ef + i
      ag = randint(500,850)
      bg = randint(500,850)
      gb = randint(500,850)
      bc = randint(500,850)
      be = randint(500,850)
      OP=0
      TP = 800
      score = 0
      a = 5
      b = 5
      c = 5
      d = 5
      e = 5
      f= 5
      g = 5
      h = 5 
      k = 5
      l = 5
      p = 5
      v = 0
      o = 0.5
      t = 0.5
      m=0
    
   if event.key == pygame.K_3:
    sound.set_volume(0)
   if event.key == pygame.K_5:
    sound.set_volume(1.0)
   if event.key == pygame.K_8:
    pygame.mixer.Sound.stop(sound)
    pygame.mixer.Sound.play(sound)
    
   if event.key == pygame.K_6:
    v = 0 
    v = -10
  
 pygame.display.flip()
	
pygame.quit()
