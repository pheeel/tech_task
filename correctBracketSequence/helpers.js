const brackets = require('./constants');

module.exports = {
    /**
     * Checks that two received sequences are located side by side in the original sequence.
     *
     * @param {String} firstSeq - first sequence.
     * @param {String} secondSeq - second sequence.
     * @param {String} originalSeq - original sequence.
     * @returns {boolean} - True if received sequences are located side by side, False otherwise.
     */
    isSequencesIsNear (firstSeq, secondSeq, originalSeq) {
        const preRegex = firstSeq.concat(secondSeq).split('');

        const regex = preRegex.reduce((acc, val) => {
            acc.push('\\');
            acc.push(val);
            return acc;
        }, []).join('');

        return !!originalSeq.match(regex);
    },

    /**
     * Checks that type received brackets are the same.
     *
     * @param {String} openBracket - Open bracket.
     * @param {String} closedBracket - Closed bracket.
     * @returns {boolean} - True if brackets type is the same, False otherwise.
     * @example '{' '}' => True, '[' '}' => False, '(' '(' => False.
     */
    isTypeTheSame (openBracket, closedBracket) {
        return brackets.types[openBracket] === brackets.types[closedBracket];
    },

    /**
     * Get the longest string from the given array.
     * @param {Array} array - Array with strings.
     * @returns {String} - The longest string from an array.
     */
    getLongestString(array) {
        if (!array[0]) return false;
        let max = array[0].length;
        array.map(v => max = Math.max(max, v.length));
        result = array.filter(v => v.length === max);
        return result.pop();
    },
};
