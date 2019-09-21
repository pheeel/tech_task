const {isSequencesIsNear, isTypeTheSame, getLongestString} = require('./helpers');
const brackets = require('./constants');

const getCorrectBracketSequence = sequence => {
    // Base cases
    if (typeof sequence !== 'string' || !sequence) return false;
    
    const bracketList = sequence.split('');
    const matches = [];
    let stack = [];
    let match = '';

    for (const bracket of bracketList) {
        if (stack.length === 0 && match) {
            matches.push(match);
            match = '';
        }

        if (brackets.open.includes(bracket)) {
            stack.push(bracket);
        }

        if (brackets.closed.includes(bracket) && stack.length !== 0) {
            const lastOpenBracket = stack.pop();
            if (isTypeTheSame(lastOpenBracket, bracket)) {
                match = `${lastOpenBracket}${match}${bracket}`;
            } else {
                if (match) {
                    if (matches !== [] && isSequencesIsNear(matches[matches.length-1], matches, sequence)) {
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
    const result = getLongestString(matches);
    if (!result) return false;
    return result;
};

console.log(getCorrectBracketSequence('[{}()]{}'));

module.exports.getCorrectBracketSequence = getCorrectBracketSequence;
