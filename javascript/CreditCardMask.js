// https://www.codewars.com/kata/5412509bd436bd33920011bc/train/javascript
// return masked string
function maskify(cc) {
    var hash_num = cc.length - 4
    var hashes = ""
    for(var x = hash_num; x > 0; x-- ){
      hashes = hashes + '#'
    }
    var end_nums = cc.slice(-4)
    return hashes + end_nums
  
  }