const {isTypeTheSame, getIndexOfStackItem, getLongestString, splitStringByIndexes} = require('./helpers');
const brackets = require('./constants');

/**
 * Checks if the given string contains the substrings of the correct sequence
 * of opening and closing square, round and curly brackets.
 *
 * @param {String} sequence - String of bracket sequence.
 * @returns {Boolean|String} - False if no parenthesis sequences are found,
 *          otherwise the longest parentheses sequence are returned.
 */
const getCorrectBracketSequence = sequence => {
    if (typeof sequence !== "string") return false;
    const bracketList = sequence.split('');
    const dividingIndexes = [];
    const stack = [];

    for (const [index, bracket] of bracketList.entries()) {
        if (brackets.open.includes(bracket)) stack.push([bracket, index]);
        else if (brackets.closed.includes(bracket) && !(stack.length === 0) && isTypeTheSame(stack[stack.length -1][0], bracket)) {
            stack.pop();
        } else dividingIndexes.push(...getIndexOfStackItem(stack), index);
    }

    const invalidCharsIndexes = [...dividingIndexes, ...getIndexOfStackItem(stack)];
    const allCombinations =  splitStringByIndexes(sequence, invalidCharsIndexes);
    return getLongestString(allCombinations);
};

module.exports = {getCorrectBracketSequence};
