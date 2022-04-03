import pygame
import time

pygame.init()
size = (1280, 960)
screen = pygame.display.set_mode(size)

bg = pygame.image.load("background.jpg")


def now_time():
    a = time.time()
    s = a % 60
    m = (a / 60) % 60
    return m, s


def rotate(image, angle):
    w = 1280 / 2
    h = 960 / 2
    hh = h
    ww = w
    image_rect = image.get_rect(topleft=(ww - w, hh - h))
    offset_center_to_pivot = pygame.math.Vector2((ww, hh)) - image_rect.center
    rotated_offset = offset_center_to_pivot.rotate(-angle)
    rotated_image_center = (ww - rotated_offset.x, hh - rotated_offset.y)
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)
    screen.blit(rotated_image, rotated_image_rect)


def main():
    clock = pygame.time.Clock()
    fps = 60
    sc = pygame.image.load("sec.png")
    mn = pygame.image.load("mun.png")
    pre_mn, pre_sc = now_time()
    m_ang = - 60 - pre_mn * 6
    s_ang = 60 - pre_sc * 6
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.blit(bg, (0, 0))
        rotate(sc, s_ang)
        rotate(mn, m_ang)
        current_m, current_s = now_time()
        m_ang += (pre_mn - current_m)*6
        s_ang += (pre_sc - current_s)*6
        pre_mn, pre_sc = current_m, current_s
        pygame.display.flip()
        clock.tick(fps)


if __name__ == "__main__":
    main()
