console.clear();

let A = [3, 8, 9, 7, 6];

cyclicRotation = (A, K) => {
  for (let cnt = 0; cnt < K; cnt++) {
    A.unshift(A.pop());
  }
}; 

cyclicRotation(A, 3);
console.log(A);
