#!/usr/bin/env python3
"""Simple Rock-Paper-Scissors command-line game.

Usage:
  python rps.py            # best-of-3 by default
  python rps.py --best-of 5

Controls: type r/p/s or rock/paper/scissors. Type q to quit.
"""
import random
import argparse

CHOICES = {"r": "rock", "p": "paper", "s": "scissors"}


def decide(player: str, comp: str) -> str:
    if player == comp:
        return "tie"
    wins = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
    return "win" if wins[player] == comp else "lose"


def normalize(inp: str) -> str | None:
    if not inp:
        return None
    inp = inp.strip().lower()
    if inp in ("q", "quit", "exit"):
        return "quit"
    if inp in CHOICES:
        return CHOICES[inp]
    if inp in CHOICES.values():
        return inp
    return None


def play_round() -> tuple[str, str, str]:
    while True:
        raw = input("Your move (r/p/s or rock/paper/scissors, q to quit): ")
        player = normalize(raw)
        if player == "quit":
            return ("quit", "", "")
        if player is None:
            print("Invalid input. Try 'r', 'p', 's', or full names.")
            continue
        comp = random.choice(list(CHOICES.values()))
        result = decide(player, comp)
        return (player, comp, result)


def main():
    parser = argparse.ArgumentParser(description="Rock-Paper-Scissors")
    parser.add_argument("--best-of", "-b", type=int, default=3,
                        help="Play best-of-N (odd integer), default 3")
    args = parser.parse_args()
    n = args.best_of
    if n <= 0 or n % 2 == 0:
        print("--best-of must be a positive odd integer. Using 3.")
        n = 3
    needed = n // 2 + 1

    print(f"Playing best-of-{n}. First to {needed} wins. Good luck!")
    p_score = 0
    c_score = 0
    round_no = 0
    while p_score < needed and c_score < needed:
        round_no += 1
        player, comp, result = play_round()
        if player == "quit":
            print("Quitting. Final score: You {} - {} Computer".format(p_score, c_score))
            return
        print(f"You: {player}  Computer: {comp}")
        if result == "tie":
            print("Result: Tie\n")
        elif result == "win":
            p_score += 1
            print("Result: You win this round!\n")
        else:
            c_score += 1
            print("Result: Computer wins this round.\n")
        print(f"Score -> You: {p_score}  Computer: {c_score}\n")

    if p_score > c_score:
        print(f"You won the match {p_score} to {c_score}. Well played!")
    else:
        print(f"Computer won the match {c_score} to {p_score}. Better luck next time!")


if __name__ == "__main__":
    main()
