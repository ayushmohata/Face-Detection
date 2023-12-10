import pygame
import cv2
import numpy as np


video = cv2.VideoCapture(0)

facedetect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml ")

pygame.init()  

window = pygame.display.set_mode((1200,700))

pygame.display.set_caption("face detection app")

img = pygame.image.load("bgimg.png").convert()

Start = True
while Start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Start = False
            pygame.quit()

    ret, frame=video.read()
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(frame , 1.3 , 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h) , (50,50,255) ,  2)
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    imgRGB = np.rot90(imgRGB)
    imgRGB = pygame.surfarray.make_surface(imgRGB).convert()

    font = pygame.font.Font(None,50)
    text = font.render("face detection{}:face detected".format(len(faces)),True,(255,255,255))

    window.fill((0,100,100))
    window.blit(img, (0,0))
    window.blit(imgRGB,(280 ,95))
    pygame.draw.rect(window,(144,238,144),(280,50,640,70),border_top_left_radius=10,border_top_right_radius=10)
    pygame.draw.rect(window,(144,238,144),(280,550,640,70),border_bottom_left_radius=10,border_bottom_right_radius=10)
    window.blit(text,(320,50))
    pygame.display.update()
