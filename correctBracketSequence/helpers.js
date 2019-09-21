const brackets = require('./constants');

module.exports = {
    /**
     * Checks if type of received brackets are the same.
     *
     * @param {String} openBracket - Open bracket.
     * @param {String} closedBracket - Closed bracket.
     * @returns {boolean} - True if brackets type is the same, False otherwise.
     * @example '{' '}' => True, '[' '}' => False, '(' '(' => False.
     */
    isTypeTheSame (openBracket, closedBracket) {
        return brackets.types[openBracket] === closedBracket || brackets.types[closedBracket] === openBracket;
    },

    /**
     * Get the longest string from the given array.
     * @param {Array} array - Array with strings.
     * @returns {String} - The longest string from an array.
     */
    getLongestString (array) {
        if (!array[0]) return false;
        return array.reduce((a, b) => a.length > b.length ? a : b, '');
    },

    /**
     * Returns indexes of given array of stack items.
     *
     * @param {Array} stack - Array of stack items.
     * @returns {Array} - Array of indexes.
     */
    getIndexOfStackItem (stack) {
        const result = [];
        for (let i of stack) {
            result.push(i[1]);
        }
        return result;
    },

    /**
     * Splits the string by indexes. Characters at the indexes are removed.
     *
     * @param {String} string - The original string.
     * @param {Array} indexes - Array with indexes which need to delete from original string.
     * @returns {Array} - Array of strings.
     */
    splitStringByIndexes (string, indexes) {
        let splits = string;
        for (let i = 0; i < indexes.length; i++) {
            splits = splits.substring(0, indexes[i]) + ' ' + splits.substring(indexes[i]+1);
        }
        return  splits.split(' ').filter(el => el !== '');
    },
};
