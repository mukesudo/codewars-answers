function createPhoneNumber(numbers){
    let str = numbers.join('');
    return `(${str.slice(0,3)}) ${str.slice(3,6)}-${str.slice(6,10)}`;
  }