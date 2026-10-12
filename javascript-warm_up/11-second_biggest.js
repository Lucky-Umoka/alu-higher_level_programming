#!/usr/bin/node
const nums = process.argv.slice(2).map(Number).sort((a, b) => b - a);
if (nums.length < 2) {
  console.log(0);
} else {
  console.log(nums[1]);
}
