import sys
import pygame as pg


def fill(surface, color):
    """Fill all pixels of the surface with color, preserve transparency."""
    w, h = surface.get_size()
    r, g, b, _ = color
    for x in range(w):
        for y in range(h):
            a = surface.get_at((x, y))[3]
            surface.set_at((x, y), pg.Color(r, g, b, a))

def colorize(image, newColor):
    """
    Create a "colorized" copy of a surface (replaces RGB values with the given color, preserving the per-pixel alphas of
    original).
    :param image: Surface to create a colorized copy of
    :param newColor: RGB color to use (original alpha values are preserved)
    :return: New colorized Surface instance
    """
    image = image.copy()
    delimiter = image.get_at((10, 0))
    print(delimiter)
    for x in range (image.get_width()):
        for y in range(image.get_height()):
            if(image.get_at((x, y))[:3] != (0, 0, 0) and image.get_at((x, y)) != delimiter):
                # zero out RGB values
                pg.Surface.set_at(image, [x, y], newColor)


    return image

def main():
    screen = pg.display.set_mode((640, 480))
    dt = clock = pg.time.Clock()

    surface = pg.image.load('./fonts/large_font.png')
    surface.set_colorkey((0, 0, 0))
    surface = pg.transform.rotozoom(surface, 0, 2)

    surface = colorize(surface, (0, 255, 0))
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_f:
                    fill(surface, pg.Color(240, 200, 40))
                if event.key == pg.K_g:
                    fill(surface, pg.Color(250, 10, 40))
                if event.key == pg.K_h:
                    fill(surface, pg.Color(40, 240, 120))

        screen.fill(pg.Color('lightskyblue4'))
        pg.draw.rect(screen, pg.Color(40, 50, 50), (210, 210, 50, 90))
        screen.blit(surface, (200, 200))

        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
    sys.exit()