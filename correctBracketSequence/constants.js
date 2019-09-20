module.exports = {
    open: ['(', '[', '{'],
    closed: [')', ']', '}'],
    types: {
        '(': 'round',
        ')': 'round',
        '[': 'square',
        ']': 'square',
        '{': 'figure',
        '}': 'figure',
    },
};
