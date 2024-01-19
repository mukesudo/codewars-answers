function toTime(seconds) {
    //code here
      let hours = seconds/3600.0;
      let minutes = (hours-Math.floor(hours))*60;
      return Math.floor(hours)+' hour(s) and '+Math.floor(minutes)+' minute(s)' 
    
    }