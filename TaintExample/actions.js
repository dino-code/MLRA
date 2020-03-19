let row = [];
let matrix1 = [];

let val = document.getElementById('[0][0]1');
let button = document.getElementById('button');

function myFunction() {
    for (let i = 0; i < 3; ++i) {
        for (let j = 0; j < 3; ++j) {
            let ID = '[' + i + '][' + j + ']1';
            let val = document.getElementById(ID).value;
            row.push(val);
        }
        matrix1.push(row);
        row = [];
    }

    document.getElementById("matrix1").innerHTML = matrix1;


}



