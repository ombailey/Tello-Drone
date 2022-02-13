from djitellopy import Tello
import sys
import pygame
import cv2, math, time

tello = Tello()

class ManualControl:
    # Display Screen to control the drone with keyboard
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,600))
        self.bg_color = ((230,230,230))
        pygame.display.set_caption('Manual Control Drone')

        # Display Control Settings on Manual Control Window Screen
        self.image = pygame.image.load('Droneinstructions.jpg')
        self.imagerect = self.image.get_rect()

        # Drone Picture Count starts at 0 everytime its started up again. Rename pictures form last flight.
        self.i = 0

        # Start Running the Drone
    def run_game(self):
        tello.connect()
        tello.takeoff()
        tello.streamon()
        while True:
            self.screen.blit(self.image, self.imagerect)
            pygame.display.update()
            self.img = tello.get_frame_read().frame
            self.img = cv2.resize(self.img, (600, 600))
            cv2.imshow('Omar Drone Baby', self.img)
            cv2.waitKey(1)
        
        
            for event in pygame.event.get():
                # if event.type == pygame.QUIT():
                #     sys.exit()
                if event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                # If you are no longer holding the key down the drone will stay in place.
                if event.type == pygame.KEYUP:
                    tello.send_rc_control(0,0,0,0)

        # Keys used to Manually Control The Drone
    def _check_keydown_events(self,event):
        lr = 30
        fb = 40
        ud = 30
        if event.key == pygame.K_UP:
            tello.send_rc_control(0, fb, 0,0)
        elif event.key == pygame.K_DOWN:
            tello.send_rc_control(0, -fb, 0, 0)
        elif event.key == pygame.K_LEFT:
            tello.send_rc_control(-lr,0, 0, 0)
        elif event.key == pygame.K_RIGHT:
            tello.send_rc_control(lr, 0, 0, 0)
        elif event.key == pygame.K_a:
            tello.rotate_clockwise(45)
        elif event.key == pygame.K_s:
            tello.rotate_counter_clockwise(45)
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
        # Code to take pictures when key is pressed. It will take multiple pictures.
        elif event.key == pygame.K_c:
            cv2.imwrite(f'Pictures/dronepic{self.i}.png',self.img)
            self.i += 1
if __name__ == '__main__':
    manual = ManualControl()
    manual.run_game()
