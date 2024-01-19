function countBits(n) {
    // Program Me
    let str ='';
    let remainder,count = 0;
    if(n==0)
      {
        return 0;
      }
    if(n==1)
      {
        return 1;
      }
    else
      {
        while(n>0)
          {
            remainder=n%2;
            str= str.concat(remainder.toString());
            n=Math.floor(n/2);
            if(n==1)
              {
                str= str.concat('1');
                break;
              }
          }
        for(let i=0;i<str.length;i++)
          {
            if(str[i]=='1')
              {
                count++;
              }
          }
      }
    return count;
  }