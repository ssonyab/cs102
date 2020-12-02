import random
import json
from copy import deepcopy

import pathlib
from itertools import product
from typing import List, Optional, Tuple

# pylint: disable=no-member
# pylint: disable=missing-class-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

Cell = Tuple[int, int]
Cells = List[int]
Grid = List[Cells]


class GameOfLife:
    def __init__(
        self,
        size: Tuple[int, int],
        randomize: bool = True,
        max_generations: Optional[float] = float("inf"),
    ) -> None:
        # Размер клеточного поля
        self.rows, self.cols = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.generations = 1

    def create_grid(self, randomize: bool = False) -> Grid:
        if randomize:
            grid = [
                [random.randint(0, 1) for i in range(self.cols)]
                for i in range(self.rows)
            ]
        else:
            grid = [[0] * self.cols for i in range(self.rows)]
        return grid

    def get_neighbours(self, cell: Cell) -> Cells:
        neighb = []
        for i in range(-1, 2):
            for m in range(-1, 2):
                if i == 0 and m == 0:
                    continue
                if 0 <= cell[0] + i < len(self.curr_generation) and 0 <= cell[1] + m < len(
                    self.curr_generation[0]
                ):
                    neighb.append(self.curr_generation[cell[0] + i][cell[1] + m])
        return neighb

    def get_next_generation(self) -> Grid:
        out = deepcopy(self.curr_generation)
        for i in range(len(out)):
            for m in range(len(out)):
                total = sum(self.get_neighbours((i, m)))
                if total == 2 and self.curr_generation[i][m] == 1 or total == 3:
                    out[i][m] = 1
                else:
                    out[i][m] = 0
        return out

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """
        self.prev_generation = deepcopy(self.curr_generation)
        self.curr_generation = self.get_next_generation()
        self.generations += 1

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        return self.generations >= self.max_generations  # type: ignore

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        if self.prev_generation != self.curr_generation:
            return True
        else:
            return False

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        """
        Прочитать состояние клеток из указанного файла.
        """
        with open(filename, "r") as l:
            curr_generation = json.load(l)
        size = len(curr_generation), len(curr_generation[0])
        game = GameOfLife(size=size, randomize=False)
        game.curr_generation = curr_generation
        return game

    def save(self, filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        with open(filename, "w") as l:
            json.dump(self.curr_generation, fp=l)


def main():
    filename = "generation_{}.txt"

    def gen_path(step):
        return pathlib.Path(filename.format(step)).resolve()

    # New game
    game = GameOfLife(size=(48, 64))
    game.step()
    game.save(gen_path(0))

    # Game from save
    game = GameOfLife.from_file(gen_path(0))
    game.step()
    game.save(gen_path(1))


if __name__ == "__main__":
    main()
