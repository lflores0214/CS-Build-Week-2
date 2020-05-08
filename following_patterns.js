

function areFollowingPatterns(strings, patterns) {
    if( strings.length != patterns.length){
        return false
    }
    let hashPS = {};
    let hashSP = {};
    for (let i = 0; i< strings.length; i++){
        let currentPattern = patterns[i]
        let currentString = strings[i]
        if(!hashPS[currentPattern]) {
            hashPS[currentPattern] = currentString
        } else if (hashPS[currentPattern] != currentString){
            return false
        }
        if(!hashSP[currentString]) {
            hashSP[currentString] = currentPattern
        } else if(hashSP[currentString] != currentPattern){
            return false
        }
    }
    return true
}
string = ["cat", "dog", "doggy"]
pattern = ["a", "b", "b"]

console.log(areFollowingPatterns(string, pattern))