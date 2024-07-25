import Board from '../board.js';
import GameError from '../error.js';
import Player from '../player.js';

class TicTacToe {
    constructor(player1, player2) {
        this.board = new Board(3, 3);
        this.players = [player1, player2];
        this.current_player = 0;
        this.winner = null;
        this.game_over = false;
        this.turns = 0;
    }

    getWinner() {
        return this.winner;
    }

    switchPlayer() {
        this.current_player = this.current_player == 0 ? 1 : 0;
    }

    makeMove(row, column) {
        if (this.game_over) {
            return new GameError('Game over', 2);
        }

       if (this.board.setCell(row, column, this.current_player) instanceof Error) {
            return new GameError('Invalid move', 1);
        }

        this.checkWinner();


        if (this.winner !== null) {
            this.game_over = true;
            return true;
        }

        this.turns++;
        if (this.turns == 9) {
            this.game_over = true;
            return true;
        }

        this.switchPlayer();

        return true;
    }

    checkWinner() {
        const grid = this.board.grid;
        const rows = this.board.rows;
        const columns = this.board.columns;

        // Check rows
        for (let row = 0; row < rows; row++) {
            if (grid[row].every(cell => cell === this.current_player)) {
                this.winner = this.current_player;
                return;
            }
        }

        // Check columns
        for (let col = 0; col < columns; col++) {
            if (grid.every(row => row[col] === this.current_player)) {
                this.winner = this.current_player;
                return;
            }
        }

        // Check diagonals
        if (grid.every((row, index) => row[index] === this.current_player)) {
            this.winner = this.current_player;
            return;
        }

        if (grid.every((row, index) => row[columns - index - 1] === this.current_player)) {
            this.winner = this.current_player;
            return;
        }
    }
}

export default TicTacToe;