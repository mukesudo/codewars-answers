function rot13(message){
    //your code here
    const capital_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];
    const small_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"];
    let characters = message.split('');
    
    characters = characters.map((character)=>{
        if(character>='A' && character<='Z'){
          return capital_letters.at(((capital_letters.indexOf(character)+13)%capital_letters.length));
        }
        else if(character>='a' && character<='z'){
          return small_letters.at(((small_letters.indexOf(character)+13)%small_letters.length));
        }
        else{
          return character;
        }
          
    })
    return characters.join('')
    
    
  }