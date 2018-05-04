function chrono() {
    var startTime = 0,
      start = 0,
      end = 0,
      diff = 0,
      timerID = 0;
    
    end = new Date();
    diff = end - start;
    diff = new Date(diff);
    var msec = diff.getMilliseconds();
    var sec = diff.getSeconds();
    var min = diff.getMinutes();
    var hr = diff.getHours()-1;
    
    if (min < 10) { min = "0" + min; }
    if (sec < 10) { sec = "0" + sec; }
  
    document.getElementById("chronotime").innerHTML = hr + ":" + min + ":" + sec;
    timerID = setTimeout("chrono()", 10)
  }
  
  function chronoStart() {
    start = new Date();
    chrono();
  }
  
  chronoStart();