function printUpsideDown(name) {
    const upsideDownMap = {
        'a': '\u0250', 'b': 'q', 'c': '\u0254', 'd': 'p', 'e': '\u01DD',
        'f': '\u025F', 'g': '\u0183', 'h': '\u0265', 'i': '\u0131', 'j': '\u027E',
        'k': '\u029E', 'l': '\u0283', 'm': '\u026F', 'n': 'u', 'o': 'o',
        'p': 'd', 'q': 'b', 'r': '\u0279', 's': 's', 't': '\u0287',
        'u': 'n', 'v': '\u028C', 'w': '\u028D', 'x': 'x', 'y': '\u028E',
        'z': 'z', ' ': ' ', '.': '.', ',': ',',
    };

    let upsideDownName = '';
    for (let char of name.toLowerCase()) {
        upsideDownName += upsideDownMap[char] || char;
    }

    // Reverse the string to make it upside down
    upsideDownName = upsideDownName.split('').reverse().join('');

    console.log(upsideDownName);
}

// Example usage:
printUpsideDown('Samuel Nathaniel');
