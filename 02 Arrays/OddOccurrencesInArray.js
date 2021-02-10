const { performance } = require("perf_hooks");

let a = [
  1,
  1,
  1,
  2,
  3,
  4,
  5,
  1,
  2,
  3,
  4,
  5,
  7,
  1,
  1,
  1,
  2,
  3,
  4,
  5,
  1,
  2,
  3,
  4,
  5,
  7,
  11
];

getUnpairItem = a => {
  if (a.length < 1) {
    return null;
  }

  const set = new Set()
  a.forEach(element => {
    if(set.has(element)) {
      set.delete(element)
    } else {
      set.add(element)
    }
  })

  retVal = set.values().next().value
  return retVal
}

console.clear()
t0 = performance.now()
const val = getUnpairItem(a)
console.log(`Get unpaired item took: ${(performance.now() - t0).toFixed(3)}ms`)
console.log(val)
