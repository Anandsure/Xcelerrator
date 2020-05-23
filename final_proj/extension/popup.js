alert("first alert")

// const fs = require('fs')    

document.getElementById("testbtn").addEventListener("click", ()=>{
    // alert('clicked')
    var x = document.getElementById("link").value
    alert(x)
    
    // fs.writeFile('Output.txt', x, (err) => { 
      
    //     // In case of a error throw err. 
    //     if (err) throw err; 
    // }) 
})

