class Board:
    def __init__(self):
        self.board = [['' for _ in range(4)] for _ in range(4)]
        self.current_player = 'X'

    def make_move(self, row, col):
        if self.board[row][col] == '':
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False

    def check_win(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] == row[3] and row[0] != '':
                return row[0]
        # Check columns
        for col in range(4):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] == self.board[3][col] and self.board[0][col] != '':
                return self.board[0][col]
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == self.board[3][3] and self.board[0][0] != '':
            return self.board[0][0]
        if self.board[0][3] == self.board[1][2] == self.board[2][1] == self.board[3][0] and self.board[0][3] != '':
            return self.board[0][3]
        return None

    def check_draw(self):
        return all(cell != '' for row in self.board for cell in row) and self.check_win() is None

    def reset(self):
        self.board = [['' for _ in range(4)] for _ in range(4)]
        self.current_player = 'X'

    def get_board(self):
        return [row[:] for row in self.board]

    def get_win_probabilities(self):
        """Calculate win probabilities for current player and opponent using heuristic approach."""
        if self.check_win() or self.check_draw():
            return {'X': 0.0, 'O': 0.0}

        # Get all possible winning lines
        lines = []
        # Rows
        for row in self.board:
            lines.append(row)
        # Columns
        for col in range(4):
            lines.append([self.board[r][col] for r in range(4)])
        # Diagonals
        lines.append([self.board[i][i] for i in range(4)])
        lines.append([self.board[i][3-i] for i in range(4)])

        current_player = self.current_player
        opponent = 'O' if current_player == 'X' else 'X'

        current_score = 0
        opponent_score = 0
        total_weight = 0

        for line in lines:
            current_count = line.count(current_player)
            opponent_count = line.count(opponent)
            empty_count = line.count('')

            if current_count > 0 and opponent_count == 0:
                # Line controlled by current player
                if current_count == 1:
                    weight = 1
                elif current_count == 2:
                    weight = 3
                elif current_count == 3:
                    weight = 6
                current_score += weight * empty_count
                total_weight += weight * 4  # Max possible for this line

            elif opponent_count > 0 and current_count == 0:
                # Line controlled by opponent
                if opponent_count == 1:
                    weight = 1
                elif opponent_count == 2:
                    weight = 3
                elif opponent_count == 3:
                    weight = 6
                opponent_score += weight * empty_count
                total_weight += weight * 4

            elif current_count == 0 and opponent_count == 0:
                # Open line - both players have equal opportunity
                weight = 1
                current_score += (weight * empty_count) / 2
                opponent_score += (weight * empty_count) / 2
                total_weight += weight * 4

        # Calculate probabilities
        if total_weight == 0:
            return {'X': 0.0, 'O': 0.0}

        current_prob = (current_score / total_weight) * 100
        opponent_prob = (opponent_score / total_weight) * 100

        # Ensure probabilities are reasonable (don't exceed 100% each)
        current_prob = min(current_prob, 100.0)
        opponent_prob = min(opponent_prob, 100.0)

        return {current_player: round(current_prob, 1), opponent: round(opponent_prob, 1)}

    def get_current_player(self):
        return self.current_player