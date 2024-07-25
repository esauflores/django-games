class Board {
    constructor(rows, columns) {
        this.rows = rows;
        this.columns = columns;
        this.grid = this.createGrid();
    }

    createGrid() {
        const grid = [];
        for (let row = 0; row < this.rows; row++) {
            const rowArray = [];
            for (let col = 0; col < this.columns; col++) {
                rowArray.push(null);
            }
            grid.push(rowArray);
        }
        return grid;
    }

    setCell(row, column, value) {
        if (row < 0 || row >= this.rows || column < 0 || column >= this.columns) {
            return Error('Invalid cell coordinates');
        }
        
        this.grid[row][column] = value;

        return value;
    }
}

// Example usage:
// const board = new Board(8, 8);
// console.log(board.getRows()); // 8
// console.log(board.getColumns()); // 8

export default Board;