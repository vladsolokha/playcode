function palindrome(str) {
    const newStr = str.replace(/[^A-Z0-9]/ig, '');
    for (let i = 0; i < newStr.length/2+1; i++) {
      if (newStr.charAt(i) === newStr.charAt(newStr.length-(i+1))) {
        return true;
      }
    }
    return false;
  }
  
  
  
  palindrome("eye"); //returns True
  palindrome("wjeiransioef"); //returns False
  