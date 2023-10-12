import pygame 

def starting_screen(screen):
    screen.fill('black')

    text_font = pygame.font.Font('font/123.ttf', 50)

    top_text = text_font.render('Pong game',False,'blue')
    top_text_rect = top_text.get_rect(center = (350, 100))

    bottom_text = text_font.render('Press "Space" to start!',False,'blue')
    bottom_text_rect = bottom_text.get_rect(center = (350, 250))

    screen.blit(top_text, top_text_rect)
    screen.blit(bottom_text, bottom_text_rect)


def bouncing(ball,left_rect, right_rect, tables):

    if ball.rect.bottom >= 400 or ball.rect.top <= 0:
        ball.y_speed *= -1

    collision_tolerance = 10

    collision_spritesv1 = pygame.sprite.spritecollide(ball, tables, False)

    if collision_spritesv1:
        if abs(left_rect.rect.right - ball.rect.left) < collision_tolerance and ball.x_speed < 0:
            ball.x_speed *= -1
        if abs(right_rect.rect.left - ball.rect.right) < collision_tolerance and ball.x_speed > 0:
            ball.x_speed *= -1 

    #collision_spritesv2 = pygame.sprite.spritecollide(ball, right_rect, False)

    """if collision_spritesv2:
        if abs(right_rect.rect.left - ball.rect.right) < collision_tolerance and ball.x_speed > 0:
            ball.x_speed *= -1 """

def test_range(ball):
    if ball.rect.right >= 700 or ball.rect.left <= 0:
        isActive = False
        return isActive
    else:
        isActive = True
        return isActive