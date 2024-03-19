#测试播放音频
import os
import time
import pygame
#import YOLO.myframe
#import YOLO.mydetect
pygame.mixer.init()
print("播放音乐1")
track = pygame.mixer.music.load('1.mp3')
#pygame.mixer.music.play()
#time.sleep(1)
#pygame.mixer.music.stop()
A=[['cell phone', '60.21', ["tensor(406., device='cuda:0')", "tensor(186., device='cuda:0')", "tensor(558., device='cuda:0')", "tensor(384., device='cuda:0')"]], ['person', '62.11', ["tensor(96., device='cuda:0')", "tensor(107., device='cuda:0')", "tensor(562., device='cuda:0')", "tensor(480., device='cuda:0')"]]]
Na = [item[0] for item in A]
if 'cell phone' in A:
    print("exist")
print(Na)
print('结束')
#YOLO.myframe.frametest()
