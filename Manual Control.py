from djitellopy import Tello
import sys
import pygame
import cv2, math, time

tello = Tello()

class ManualControl:
    # Display Screen to control the drone with keyboard
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,800))
        self.bg_color = ((230,230,230))
        pygame.display.set_caption('Manual Control Drone')

        # Display Control Settings on Manual Control Window Screen
        self.image = pygame.image.load('Droneinstructions.png')
        self.imagerect = self.image.get_rect()

        # Start Running the Drone
    def run_game(self):
        tello.connect()
        tello.takeoff()
        tello.streamon()
        while True:
            self.screen.blit(self.image, self.imagerect)
            pygame.display.update()
            img = tello.get_frame_read().frame
            img = cv2.resize(img, (400, 400))
            cv2.imshow('Omar Drone Baby', img)
            cv2.waitKey(1)
        
            for event in pygame.event.get():
                # if event.type == pygame.QUIT():
                #     sys.exit()
                if event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)

        # Keys used to Manually Control The Drone
    def _check_keydown_events(self,event):
        lr = 10
        fb = 10
        ud = 10
        if event.key == pygame.K_UP:
            tello.send_rc_control(0, fb, 0,0)
        elif event.key == pygame.K_DOWN:
            tello.send_rc_control(0, -fb, 0, 0)
        elif event.key == pygame.K_LEFT:
            tello.send_rc_control(-lr,0, 0, 0)
        elif event.key == pygame.K_RIGHT:
            tello.send_rc_control(lr, 0, 0, 0)
        elif event.key == pygame.K_a:
            tello.rotate_clockwise(30)
        elif event.key == pygame.K_s:
            tello.rotate_counter_clockwise(30)
        elif event.key == pygame.K_1:
            tello.send_rc_control(0, 0, ud, 0)
        elif event.key == pygame.K_2:
            tello.send_rc_control(0, 0, -ud, 0)
        elif event.key == pygame.K_q:
            tello.flip_left()
        elif event.key == pygame.K_w:
            tello.flip_forward()
        elif event.key == pygame.K_r:
            tello.flip_right()
        elif event.key == pygame.K_e:
            tello.flip_back()
        elif event.key == pygame.K_l:
            tello.land()
        elif event.key == pygame.K_t:
            tello.takeoff()

if __name__ == '__main__':
    manual = ManualControl()
    manual.run_game()
