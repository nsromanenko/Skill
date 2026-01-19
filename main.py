from __future__ import annotations

from typing import List, Optional, Tuple


WIN_LINES: Tuple[Tuple[int, int, int], ...] = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)


def render(board: List[str]) -> str:
    def cell(i: int) -> str:
        return board[i] if board[i] != " " else str(i + 1)

    return (
        "\n"
        "-------------\n"
        f"| {cell(0)} | {cell(1)} | {cell(2)} |\n"
        "-------------\n"
        f"| {cell(3)} | {cell(4)} | {cell(5)} |\n"
        "-------------\n"
        f"| {cell(6)} | {cell(7)} | {cell(8)} |\n"
        "-------------\n"
    )


def winner(board: List[str]) -> Optional[str]:
    for a, b, c in WIN_LINES:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None


def board_full(board: List[str]) -> bool:
    return all(x != " " for x in board)


def parse_move(text: str) -> Optional[int]:
    text = text.strip()
    if not text.isdigit():
        return None
    n = int(text)
    if 1 <= n <= 9:
        return n - 1
    return None


def choose_player(turn: int) -> str:
    return "X" if turn % 2 == 0 else "O"


def main() -> None:
    board = [" "] * 9
    turn = 0

    print("Крестики-нолики 3x3")
    print("Ход: введите номер клетки 1..9 (как на поле).")

    while True:
        current = choose_player(turn)
        print(render(board))
        move_raw = input(f"Ход игрока {current}: ")

        idx = parse_move(move_raw)
        if idx is None:
            print("Некорректный ввод. Введите число 1..9.")
            continue
        if board[idx] != " ":
            print("Клетка занята. Выберите другую.")
            continue

        board[idx] = current

        w = winner(board)
        if w is not None:
            print(render(board))
            print(f"Победил игрок {w}.")
            return

        if board_full(board):
            print(render(board))
            print("Ничья.")
            return

        turn += 1


if __name__ == "__main__":
    main()
