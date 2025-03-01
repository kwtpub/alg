var once = function(fn) {
    k = 0 
    return function(...args){
        if(k == 0) { 
            k++
            return fn(args)
        }
    }
};


 let fn = (a,b,c) => (a + b + c)
let onceFn = once(fn)

onceFn(1,2,3); // 6
onceFn(2,3,6); // returns undefined without calling fn
 