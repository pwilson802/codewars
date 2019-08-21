var isSquare = function(n){
  for(let i = 0; i<=n;i++){
    if (i*i === n){
      return true
    }
  }
  return false
}