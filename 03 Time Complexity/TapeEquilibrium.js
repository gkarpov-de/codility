console.clear();
let A = [1, 1, 3];

TapeEquilibrium = A => {
  let minDiff = Math.maxint;
  let N = A.length;
  let dif = -A.reduce((acc, cur) => (acc += cur));

  for (let p = 1; p < N; p++) {
    dif = dif + 2 * A[p - 1];
    let absDif = Math.abs(dif);
    minDiff = minDiff < absDif ? minDiff : absDif;
  }

  return minDiff;
};

console.log(`${TapeEquilibrium(A)}`);
