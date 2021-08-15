/*
need list of sorted names
can use quick sort to do this
need a list of names to search and match
*/

let names = ['a','b','c','d','e','f','g'];
let name = ['c','a'];

let data;
let target;
const binary_search = (data, target) => {
    let first = 0;
    let last = data.length - 1;

    while (first <= last) {
        let midpoint = ((first + last) / 2).floor;
        if (data.indexOf(midpoint) == target) {
            return midpoint;
        } else if (data.indexOf(midpoint) < target) {
            first = midpoint + 1;
        } else {
            last = midpoint - 1;
        }
    }
    return undefined;
}

for (const name of names) {
    let position = binary_search(names, name);
    console.log(position);
}