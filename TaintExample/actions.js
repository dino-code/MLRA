

function GetCellValues() {
    var table = document.getElementById('table1');
    for (var r = 0, n = table.rows.length; r < n; r++) {
        for (var c = 0, m = table.rows[r].cells.length; c < m; c++) {
            alert(table.rows[r].cells[c].innerHTML);
        }
    }
}

function displayVal() {
    alert(document.getElementById('[0][0]').nodeValue)
}

let button = document.getElementById('button')

button.onclick = () => displayVal();