console.clear();

frogJump = (X, Y, D) => {
  return Math.ceil((Y - X) / D);
};

console.log(`${frogJump(10, 85, 30)}`);
