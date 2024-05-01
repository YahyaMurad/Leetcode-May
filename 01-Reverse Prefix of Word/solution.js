/**
 * @param {string} word
 * @param {character} ch
 * @return {string}
 */
var reversePrefix = function(word, ch) {
    idx = word.indexOf(ch);
    substr = word.substring(0, idx + 1);
    splitSubstr = substr.split("");
    reverseSplitSubstr = splitSubstr.reverse();
    joinedReverseSplitSubstr = reverseSplitSubstr.join("");

    return joinedReverseSplitSubstr + word.substring(idx + 1);
    
};

console.log(reversePrefix("abcdefd", "d"))