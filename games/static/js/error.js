class GameError extends Error {
    constructor(message, error_code = 0) {
        super(message);
        this.error_code = error_code;
    }
}

// // Usage example:
// const error = new GameError('Invalid move', 2);

export default GameError;