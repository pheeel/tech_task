const testModule = require('./getCorrectBracketSequence');

const bracketCombinations = [
    ['Empty string', '', false],
    ['Non-string input value', 1, false],
    ['String with incorrect symbols', 'test!{', false],
    ['String with incorrect symbols and bracket sequence', '/<>test![{}]/!--+ ', '[{}]'],
    ['Incorrect sequence', '{([)', false],
    ['Incorrect sequence at the start', '{([){()}', '{()}'],
    ['Incorrect sequence at the end', '{()}{([)', '{()}'],
    ['Several inner sequences', '[(){}]', '[(){}]'],
    ['Inner correct sequence', '{[(()]}', '()'],
    ['Adjacent sequences', '[]{}()', '[]{}()'],
    ['Several inner sequences with adjacent sequence', '[(){}]{()}', '[(){}]{()}'],
    ['Several correct split sequences with different length', '[{}([])]}{({})', '[{}([])]'],
    ['Several correct divided sequences with the same length', '[{}]][]()[{}()', '{}()'],
];

describe('Check bracket balance', () => {
    test.each(bracketCombinations)('for %s',(name, inputSequence, outputSequence) => {
        expect(testModule.getCorrectBracketSequence(inputSequence)).toEqual(outputSequence);
    });
});
