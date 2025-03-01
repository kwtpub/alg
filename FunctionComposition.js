
functions = [x => x + 1, x => x * x, x => 2 * x]


var compose = function(functions) {

    return function(x) {
        let val = x;
        for(let i = functions.length - 1; i > -1 ; i-- ) {
            val = functions[i](val)
        }
        return val
    }
};
fn = compose(functions)

console.log(fn(4))