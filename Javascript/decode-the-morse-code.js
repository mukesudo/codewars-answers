decodeMorse = function(morseCode){
    //your code here
    let outerMorseCodeArray = morseCode.split('   ');
    for(let i=0;i<outerMorseCodeArray.length;i++)
      {
        let innerMorseCodeArray = outerMorseCodeArray[i].split(' ');
        for(let j=0;j<innerMorseCodeArray.length;j++)
          {
            innerMorseCodeArray[j]=MORSE_CODE[innerMorseCodeArray[j]];
          }
        outerMorseCodeArray[i]=innerMorseCodeArray.join('')
      }
    return outerMorseCodeArray.join(' ').trim();
  }