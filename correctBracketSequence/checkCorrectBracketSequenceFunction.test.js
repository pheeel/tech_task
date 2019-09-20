const testModule = require('./getCorrectBracketSequence');

const bracketCombination = [
    ['Empty string', '', false],
    ['Non-string input value', 1, false],
    ['Incorrect sequence', '{([)', false],
    ['Incorrect sequence at the start', '{([){()}', '{()}'],
    ['Incorrect sequence at the end', '{()}{([)', '{()}'],
    ['Adjacent sequences', '[]{}()', '[]{}()'],
    ['Several inner sequences', '[(){}]', '[(){}]'],
    ['Several inner sequences with adjacent sequence', '[(){}]{()}', '[(){}]{()}'],
    ['Inner correct sequence', '{[(()]}', '()'],
    ['Several correct split sequences with different length ', '[{}([])]}{({})', '[{}([])]'],
    ['Several correct divided sequences with the same length ', '[{}]][]()[{}()', '{}()'],
];

describe('Check bracket balance', () => {
    test.each(bracketCombination)('for %s',(name, inputSequence, outputSequence) => {
        expect(testModule.getCorrectBracketSequence(inputSequence)).toEqual(outputSequence);
    });
});
