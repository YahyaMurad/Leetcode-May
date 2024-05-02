/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxK = function (nums) {
  let numbers = new Set(nums);
  let res = -1;
  
  for (const x of numbers) {
    if (x > 0 && numbers.has(-x)) {
      res = Math.max(res, x);
    }
  }

  return res;
};