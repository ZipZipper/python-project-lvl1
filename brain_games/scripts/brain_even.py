#!/usr/bin/env python
from brain_games.core_logic import start_game
from brain_games.games.brain_even_game import TASK, play_games


def main():
    start_game(TASK, play_games)


if __name__ == '__main__':
    main()