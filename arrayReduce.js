nums = [1,2,3,4]
fn = function sum(accum, curr) { return accum + curr; }
init = 0
var reduce = function(nums, fn, init) {
    let result = init
    for(let i = 0; i < nums.length; i++) { 
        result = fn(result, nums[i])
    }
    return result
};

reduce(nums,fn,0)