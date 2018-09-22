from init import *
# Main loop
run = True
while run:
    clock.tick(120)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Exit Control
    if keys[pygame.K_ESCAPE]:
        run = False
    if keys[pygame.QUIT]:
        run = False

    #Controlkeys
    pygame.Surface.fill(window, (0, 0, 0))
    background.be(window)
    home.be(window, keys, mouse, click)
    the_bugman.be(window)
    the_bugman2.be(window)
    the_bugman3.be(window)
    the_bugman4.be(window)


    #Update Display
    pygame.display.update()
