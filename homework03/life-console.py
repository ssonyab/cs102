import curses

from life import GameOfLife
from ui import UI

# pylint: disable=no-member
# pylint: disable=missing-class-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring


class Console(UI):
    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)
        self.rows = len(self.life.curr_generation)
        self.cols = len(self.life.curr_generation[0])

    def draw_borders(self, screen) -> None:
        """ Отобразить рамку. """
        screen.border()

    def draw_grid(self, screen) -> None:
        """ Отобразить состояние клеток. """
        for i in range(1, self.rows - 1):
            for m in range(1, self.cols - 1):
                if self.life.curr_generation[i][m]:
                    bam = "*"
                else:
                    bam = ""
                screen.addch(i, m, bam)

    def run(self) -> None:
        screen = curses.initscr()
        sc = screen.derwin(self.rows, self.cols, 0, 0)
        self.draw_borders(sc)

        try:
            while self.life.is_changing or not self.life.is_max_generations_exceeded:
                self.draw_borders(sc)
                self.draw_grid(sc)
                sc.refresh()
                self.life.step()
        finally:
            curses.endwin()


def main():
    game = GameOfLife(size=(32, 80))
    app = Console(game)
    app.run()


if __name__ == "__main__":
    main()
