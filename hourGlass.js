//see hourGlass.py for description

let hg = [
    [1, 1, 1, 0, 0, 0], 
    [0, 1, 0, 0, 0, 0], 
    [1, 1, 1, 0, 0, 0], 
    [0, 0, 2, 4, 4, 0], 
    [0, 0, 0, 2, 0, 0], 
    [0, 0, 1, 2, 4, 0]
]
// ans 19
let hg2 = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 9, 2, -4, -4, 0], [0, 0, 0, -2, 0, 0], [0, 0, -1, -2, -4, 0]]
// ans 13
let hg3 = [[-9, -9, -9, 1, 1, 1], [0, -9, 0, 4, 3, 2], [-9, -9, -9, 1, 2, 3], [0, 0, 8, 6, 6, 0], [0, 0, 0, -2, 0, 0], [0, 0, 1, 2, 4, 0]]
// ans 28

const answer = function hourGlass(arr) {
    let hourglassTotalList = [ ];
    let range = [...Array(4).keys()];
    for (let column of range) {
        for (let row of range) {

        let top_row = arr[column][row] + arr[column][row+1] + arr[column][row+2];
        let mid_row = arr[column+1][row+1];
        let end_row = arr[column+2][row] + arr[column+2][row+1] + arr[column+2][row+2];
        let total_hourglass = top_row + mid_row + end_row;
        hourglass_total_list.push(total_hourglass);
        }
    return Math.max(hourglassTotalList)    
    }
}

console.log(answer[hg]);
console.log(answer[hg2]);
console.log(answer[hg3]);
