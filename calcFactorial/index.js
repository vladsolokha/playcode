//factoral function calculates factoral of given number

function calcFactorial(num) {
    if (num < 1 || undefined || num === "") {
      return 1;
    } else {
        return calcFactorial(num-1)*(num);
    }
  }
  
  function clickHandler() {
    console.log("clicked")
    let valueNum = document.getElementById("valueNum").value;
    res = calcFactorial(valueNum);
    console.log(`res: ${res}`);
    document.getElementById("res").innerHTML = res;
  }
  
  