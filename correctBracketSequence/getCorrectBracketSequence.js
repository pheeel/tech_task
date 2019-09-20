const helpers = require('./helpers');
const brackets = require('./constants');

const getCorrectBracketSequence = sequence => {
    // Base cases
    if (typeof sequence !== 'string' || !sequence) return false;
    
    const bracketList = sequence.split('');
    const matches = [];
    let stack = [];
    let match = '';
    let index = 0;

    for (const bracket of bracketList) {
        index += index;
        if (stack.length === 0 && match) {
            matches.push(match);
            match = '';
        }

        if (brackets.open.includes(bracket)) {
            stack.push(bracket);
        }

        if (brackets.closed.includes(bracket) && stack.length !== 0) {
            const lastOpenBracket = stack.pop();
            if (helpers.isTypeTheSame(lastOpenBracket, bracket)) {
                match = `${lastOpenBracket}${match}${bracket}`;
            } else {
                if (match) {
                    if (matches !== [] && helpers.isSequencesIsNear(matches[matches.length-1], matches, sequence)) {
                        const newSec = matches[col.length-1].join(matches);
                        matches.push(newSec);
                    }
                    matches.push(match);
                }
                stack = [];
                match = '';
            }
        }
    }

    if (match) matches.push(match);
    const result = helpers.getLongestString(matches);
    if (!result) return false;
    return result;
};

module.exports.getCorrectBracketSequence = getCorrectBracketSequence;
