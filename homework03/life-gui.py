import pygame  # type: ignore
from life import GameOfLife
from pygame.locals import *  # type: ignore
from ui import UI
import life


class GUI(UI):
    def __init__(self, life: GameOfLife, cell_size: int = 10, speed: int = 10) -> None:
        super().__init__(life)
        self.width = self.life.cols * cell_size
        self.height = self.life.rows * cell_size
        self.cell_size = cell_size

        self.screen = pygame.display.set_mode((self.width, self.height))
        self.speed = speed

    def draw_lines(self) -> None:
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(
                self.screen, pygame.Color("black"), (x, 0), (x, self.height)
            )
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(
                self.screen, pygame.Color("black"), (0, y), (self.width, y)
            )

    def draw_grid(self) -> None:
        for i in range(len(self.life.curr_generation)):
            for m in range(len(self.life.curr_generation[i])):
                if self.life.curr_generation[i][m] == 1:
                    cell_colour = pygame.Color("green")
                else:
                    cell_colour = pygame.Color("white")
                    kvadr = pygame.Rect(
                        m * self.cell_size,
                        i * self.cell_size,
                        self.cell_size,
                        self.cell_size,
                    )
                pygame.draw.rect(self.screen, cell_colour, kvadr)

    def change_state(self, cell: life.Cell) -> None:
        cell_x = cell[0] // self.cell_size
        cell_y = cell[1] // self.cell_size
        if self.life.curr_generation[cell_x][cell_y]:
            self.life.curr_generation[cell_x][cell_y] = 0
        else:
            self.life.curr_generation[cell_x][cell_y] = 1

    def run(self) -> None:
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color("white"))

        running = True
        pause = False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.mousebuttondown:
                    (cell_x, cell_y) = pygame.mouse.get_pos()
                    self.change_state((cell_x, cell_y))
                    self.draw_grid()
                    self.draw_lines()
                    pygame.display.flip()
                    clock.tick(self.speed)
                    continue
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if pause:
                            pause = False
                        else:
                            pause = True
                if pause:
                    continue

                self.draw_grid()
                self.draw_lines()
                self.life.step()

                pygame.display.flip()
                clock.tick(self.speed)
            pygame.quit()


def main():
    game = GameOfLife(size=(48, 64))
    app = GUI(game)
    app.run()


if __name__ == "__main__":
    main()
