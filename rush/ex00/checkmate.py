STRAIGHT_DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
DIAGONAL_DIRS = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

def evaluate_checkmate(board: str) -> str:
    
    # ----- Parse & Validate -----
    rows = [r.rstrip() for r in board.splitlines() if r.strip()]
    if not rows or any(len(r) != len(rows) for r in rows):
        return "Error"

    n = len(rows)
    grid = [list(r) for r in rows]

    # ----- Validate King -----
    kings = [(r, c) for r in range(n) for c in range(n) if grid[r][c] == 'K']
    if len(kings) != 1:
        return "Error"

    kr, kc = kings[0]

    # ----- Directional Scan -----
    def scan(dr, dc, valid):
        r, c = kr + dr, kc + dc
        while 0 <= r < n and 0 <= c < n:
            piece = grid[r][c]
            if piece in {'P','R','B','Q','K'}:
                return piece in valid
            r += dr
            c += dc
        return False

    # ----- Pawn Check -----
    for dc in (-1, 1):
        r, c = kr + 1, kc + dc
        if 0 <= r < n and 0 <= c < n and grid[r][c] == 'P':
            return "Success"

    # ----- Straight Threats -----
    for dr, dc in STRAIGHT_DIRS:
        if scan(dr, dc, {'R', 'Q'}):
            return "Success"

    # ----- Diagonal Threats -----
    for dr, dc in DIAGONAL_DIRS:
        if scan(dr, dc, {'B', 'Q'}):
            return "Success"

    return "Fail"

def checkmate(board: str) -> None:
    print(evaluate_checkmate(board))