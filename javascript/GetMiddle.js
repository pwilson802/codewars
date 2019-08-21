// https://www.codewars.com/kata/get-the-middle-character/train/javascript

function getMiddle(s)
{
  if(s.length % 2 ===0){
    even = true
  }
  else{
    even = false
  }
  if(even == true){
    return s.slice(s.length / 2 -1, s.length / 2 + 1)
  }
  else{
    return s[s.length/2-0.5]
  }
}