class AI:
    def choose_column(self, board, me="O", opponent="X"):
        legal = [
            c for c in range(7)
            if board.grid[0][c] == "."
        ]

        if not legal:
            return None

        # 1. Take an immediate winning move if possible.
        for col in legal:
            row = board.drop(col, me)

            if row is not None:
                winning = board.winner(me)
                board.grid[row][col] = "."

                if winning:
                    return col

        # 2. Block the player's immediate winning move if necessary.
        for col in legal:
            row = board.drop(col, opponent)

            if row is not None:
                opponent_wins = board.winner(opponent)
                board.grid[row][col] = "."

                if opponent_wins:
                    return col

        # 3. Otherwise choose the first legal column.
        return legal[0]