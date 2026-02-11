# ทิศแนวตรง
straight_dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# ทิศแนวทแยง
diagonal_dirs = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

def evaluate_checkmate(board: str) -> str:

    # แยก string เป็นแต่ละแถวของตาราง
    rows = []
    for line in board.splitlines():
        if line.strip():
            rows.append(line.rstrip())

    # ตารางต้องไม่ว่าง
    if len(rows) == 0:
        return "Error"

    size = len(rows)

    # ต้องเป็นสี่เหลี่ยมจัตุรัส
    for row in rows:
        if len(row) != size:
            return "Error"

    # แปลงเป็น grid 2 มิติ เพราะถ้าเป็น 3D จะกลายเป็นหนัง..?
    grid = []
    for row in rows:
        grid.append(list(row))

    # หา King
    king_row = -1
    king_col = -1
    king_count = 0

    for r in range(size):
        for c in range(size):
            if grid[r][c] == 'K':
                king_row = r
                king_col = c
                king_count += 1

    if king_count != 1:
        return "Error"

    # ใช้ King เป็นตัวไล่ดูในแต่ละทิศว่ามีตัวไหนจะเซ็ทหย่อเรา
    def check_direction(dr, dc, attackers):
        r = king_row + dr
        c = king_col + dc

        while 0 <= r < size and 0 <= c < size:
            piece = grid[r][c]

            # เพราะโจทย์บอกว่ามีแค่ P,R,B,Q,K ที่เซ็ทหย่อ King ได้ ถ้ามีตัวประหลาดอื่น ๆ ก็ข้ามไป
            if piece in {'P', 'R', 'B', 'Q', 'K'}: 
                if piece in attackers:
                    return True
                else:
                    return False

            r += dr
            c += dc

        return False

    # ตรวจ Pawn
    for dc in (-1, 1):
        r = king_row + 1
        c = king_col + dc
        if 0 <= r < size and 0 <= c < size:
            if grid[r][c] == 'P':
                return "Success"

    # แนวตรง Rook กับ Queen
    for dr, dc in straight_dirs:
        if check_direction(dr, dc, {'R', 'Q'}):
            return "Success"

    # แนวทแยง Bishop กับ Queen
    for dr, dc in diagonal_dirs:
        if check_direction(dr, dc, {'B', 'Q'}):
            return "Success"

    return "Fail"

def checkmate(board: str) -> None:
    result = evaluate_checkmate(board)
    print(result)