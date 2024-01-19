function isCorrectIP(str){
    //   checks if number has any leading zeros or characters
    //   and proceeds to check if number is > 0 and < 255
      return parseInt(str).toString() == str ? parseInt(str)>=0 && parseInt(str)<=255 : false ;
    }
    
    function isValidIP(str) {
      let array = str.split('.'); //split into their octets
      return array.length==4? array.every(isCorrectIP) : false;
      
    }