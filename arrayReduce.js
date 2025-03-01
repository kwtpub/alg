nums = [1,2,3,4,5]
fn = function sum(accum, curr) { return accum + curr; }
init = 0
var reduce = function(nums, fn, init) {
    let result = []
    for(let i = 0; i < nums.langth; i++) { 
        result += fn(init,nums[i])
    }
    return result
};

reduce(nums,fn,0)