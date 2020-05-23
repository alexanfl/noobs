import math
import random
from copy import deepcopy
import time
from typing import Tuple
from collections import namedtuple
from dataclasses import dataclass
import multiprocessing
from argparse import ArgumentParser

import numpy as np
from sympy import sqrt, I, simplify
from pathlib import Path


# Representation of path a (lower) and b (upper)
a = np.array([1, 0])
b = np.array([0, 1])

# Normalization constant
N = 1/sqrt(2)

NUM_EXPERIMENTS = int(1e5)

parser = ArgumentParser()

parser = ArgumentParser(
        description="", prog=f"python {__name__}")
parser.add_argument(
        "-n", "--num-procs", 
        default=1,
        type=int, 
        help="number of processes [optional]"
        )
parser.add_argument(
        "-N", "--num_runs", 
        default=1,
        type=int, 
        help="number of runs (per process) [required]"
        )
parser.add_argument(
        "-p", "--print-init", 
        action="store_true",
        help="prints the initial setup of the experiment and exits"
        )
parser.add_argument(
        "--save-to-file", 
        action="store_true",
        help="saves the results to file"
        )
parser.add_argument(
        "-s", "--speed", 
        default=0.5,
        type=float, 
        help="the time it takes for the particle to move one unit"
        )

args = parser.parse_args()
if args.print_init:
    box = Box()
    box.particle = Particle(loc=(box.height - 2, 0), direction=1)
    print(box)
    sys.exit()



def mirror(state):
    """Returns a mirror image of a state vector

    |a) -> i|b)
    |b) -> i|a)
    """
    return np.flip(state)*I


def splitter(state):
    return N*(state + mirror(state))


class OutOfBoundsError(Exception):
    pass


class DetectorAError(Exception):
    pass


class DetectorBError(Exception):
    pass


class ExplosionError(Exception):
    pass


class Particle:
    def __init__(self, loc: Tuple[int, int], direction: int):
        self.loc = loc
        self.direction = direction

    def __str__(self):
        return "•"


class Box:
    def __init__(self):
        self.particle: Particle = None
        self.is_live_bomb = False

        self.height = 14
        self.box_width = 32
        self.board_height = 10
        self.board_width = 20

        self.bomb_loc = (self.height - 2, 10)
        self.mirror1_loc = (self.height - 2, self.box_width - 2)
        self.mirror2_loc = (2, 4)
        self.splitter1_loc = (self.height - 2, 4)
        self.splitter2_loc = (2, self.box_width - 2)
        self.detectorA_loc = (2, self.box_width)
        self.detectorB_loc = (0, self.box_width - 2)

        self.special_fields = {
                self.bomb_loc: self.detect_bomb,
                self.mirror1_loc: self.mirror,
                self.mirror2_loc: self.mirror,
                self.splitter1_loc: self.splitter,
                self.splitter2_loc: self.splitter,
                self.detectorA_loc: self.detectorA,
                self.detectorB_loc: self.detectorB,
                }

 
        self.board = []
        self.board.append(list(f"{' '*(self.box_width - 2)}B  "))
        self.board.append(list(f"{' '*(self.box_width - 2)}¦  "))

        self.board.append(list(f"    /{'-'*(self.box_width - 7)}+-A"))

        for _ in range(self.height - 5):
            self.board.append(list(f"    ¦{' '*(self.box_width - 7)}¦  "))

        self.board.append(list(f"----+{'-'*(self.box_width - 7)}/  "))
        self.board.append(list(f"{' '*self.box_width}"))


    def __str__(self):
        b = deepcopy(self.board)
        b = self.insert_bomb(b)
        b = self.insert_particle(b)
        rows = ["\n"]
        for row in b:
            rows.append("".join(row))
        return "\n".join(rows)


    def insert_bomb(self, board):
        board[self.bomb_loc[0]][self.bomb_loc[1]-1] = "["
        board[self.bomb_loc[0]][self.bomb_loc[1]] = "?"
        board[self.bomb_loc[0]][self.bomb_loc[1]+1] = "]"

        return board

    def insert_explosion(self, board):
        board[self.bomb_loc[0]-1][self.bomb_loc[1]-1] = "\\"
        board[self.bomb_loc[0]+1][self.bomb_loc[1]-1] = "/"
        board[self.bomb_loc[0]-1][self.bomb_loc[1]] = "|"
        board[self.bomb_loc[0]][self.bomb_loc[1]-1] = "-"
        board[self.bomb_loc[0]][self.bomb_loc[1]] = "0"
        board[self.bomb_loc[0]][self.bomb_loc[1]+1] = "-"
        board[self.bomb_loc[0]+1][self.bomb_loc[1]] = "|"
        board[self.bomb_loc[0]-1][self.bomb_loc[1]+1] = "/"
        board[self.bomb_loc[0]+1][self.bomb_loc[1]+1] = "\\"

        return board

    def insert_particle(self, board):
        board[self.particle.loc[0]][self.particle.loc[1]] = str(self.particle)
        return board

    def move_right(self):
        y = self.particle.loc[0]
        x = self.particle.loc[1] + 2
        if x >= self.box_width + 1:
            raise OutOfBoundsError(
                    "Can't move to the right. Reached board width")

        self.particle.loc = (y, x)


    def move_up(self):
        y = self.particle.loc[0] - 1
        x = self.particle.loc[1]
        if y < 0:
            raise OutOfBoundsError(
                    "Can't move up. Reached board height")

        self.particle.loc = (y, x)


    def detect_bomb(self):
        if not self.is_live_bomb:
            self.move_right()
            return
        
        self.explode()

    def explode(self):
        b = deepcopy(self.board)
        b = self.insert_explosion(b)
        for row in b:
            print("".join(row))

        raise ExplosionError

    def mirror(self):
        self.particle.direction = 1 if self.particle.direction == 0 else 0
        loc_list = list(self.particle.loc)
        loc_list[self.particle.direction] += veloc_dict[self.particle.direction]
        self.particle.loc = tuple(loc_list)


    def splitter(self):
        if not self.is_live_bomb and self.particle.loc == self.splitter2_loc:
            self.particle.direction = 1
        else:
            self.particle.direction = random.getrandbits(1)

        loc_list = list(self.particle.loc)
        loc_list[self.particle.direction] += veloc_dict[self.particle.direction]
        self.particle.loc = tuple(loc_list)

    def detectorA(self):
        raise DetectorAError

    def detectorB(self):
        raise DetectorBError


veloc_dict = {1: 2, 0: -1}

@dataclass
class Results:
    num_experiments: int
    detected_in_A: int = 0
    detected_in_B: int = 0
    explosions: int = 0

    def __str__(self):
        return (
                f"Detected in A: {self.detected_in_A/self.num_experiments}\n"
                f"Detected in B: {self.detected_in_B/self.num_experiments}\n"
                f"Bomb exploded: {self.explosions/self.num_experiments}"
                )

outfolder = Path("out")
outfolder.parent.mkdir(exist_ok=True, parents=True) 

def multiprocessing_func(outfile):
    box = Box()
    box.particle = Particle(loc=(box.height - 2, 0), direction=1)
    box.is_live_bomb = random.getrandbits(1) 

    moves = [box.move_up, box.move_right]
    while True:
        # print(box)
        with open(outfile, "w") as fs:
            fs.write(str(box))
        move = box.special_fields.get(
                box.particle.loc, moves[box.particle.direction])
        try:
            move()
        except OutOfBoundsError:
            sys.exit("Particle out of bounds")
        except ExplosionError:
            # print("BOOM!")
            # results.explosions += 1
            break
        except DetectorAError:
            # print(f"Particle detected in A")
            # results.detected_in_A += 1
            break
        except DetectorBError:
            # print(f"Particle detected in B")
            # results.detected_in_B += 1
            break

        # print("Live bomb:", bool(box.is_live_bomb))
        time.sleep(SPEED) 

    # results = Results(1)
    # print(results)


if __name__ == "__main__":
    f1 = outfolder / "tmp1.txt"
    f2 = outfolder / "tmp2.txt"

    fnames = [f2 if i%2 else f1 for i in range(20)]

    pool = multiprocessing.Pool(2)#multiprocessing.cpu_count())
    pool.map(multiprocessing_func, fnames)
    pool.close()


def main():
    print(f"Mirror transform on a:\n\t{a} -> {mirror(a)}\n")
    print(f"Mirror transform on b:\n\t{b} -> {mirror(b)}\n")

    print(f"Splitter transform on a:\n\t{a} -> {splitter(a)}\n")
    print(f"Splitter transform on b:\n\t{b} -> {splitter(b)}\n")

    print("Only upper path open:\n"
          f"\ta -> {simplify(_ := mirror(a))}\n"
          f"\t  -> {simplify(_ := mirror(_))}\n"
          f"\t  -> {simplify(_ := splitter(_))}\n")

    print("Both paths open:\n"
          f"\ta -> {simplify(_ := splitter(a))}\n"
          f"\t  -> {simplify(_ := mirror(_))}\n"
          f"\t  -> {simplify(_ := splitter(_))}\n")


    bomb_exploded = 0
    detected_in_A = 0
    detected_in_B = 0
    for _ in range(NUM_EXPERIMENTS):

        state = a

        has_bomb = random.getrandbits(1)

        dir1 = random.getrandbits(1)
        if dir1 == 0:
            if has_bomb:
                print("BOOM")
                bomb_exploded += 1
                continue

            state = state
            state = mirror(state)

            dir2 = random.getrandbits(1)
            if dir2 == 0:
                detected_in_A += 1
                print("Dectected in A")
            else:
                detected_in_B += 1
                print("Dectected in B")
        else:
            state = mirror(state)
            state = mirror(state)

            dir2 = random.getrandbits(1)
            if has_bomb:
                print("Dectected in A")
                detected_in_A += 1
                continue
            if dir2 == 0:
                detected_in_A += 1
                print("Dectected in A")
            else:
                detected_in_B += 1
                print("Dectected in B")

    print()
    print("Bomb exploded:", bomb_exploded/NUM_EXPERIMENTS)
    print("Detected in A:", detected_in_A/NUM_EXPERIMENTS)
    print("Detected in B (bomb detected):", detected_in_B/NUM_EXPERIMENTS)

