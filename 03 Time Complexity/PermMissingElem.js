console.clear();

let A = [1, 2, 3, 8, 5, 6, 7, 9, 10, 11];

PermMissingElem = A => {
  let N = A.length + 1;
  let sum = ((1 + N) * N) / 2;

  if (N > 1)
    sum -= A.reduce((sum, cur) => {
      return sum + cur;
    });

  return sum;
};

console.log(`${PermMissingElem(A)}`);
