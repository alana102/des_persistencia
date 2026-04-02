var myJSON = '{"name":"Alana", "idade":19, "cidade":"Canindé"}';
var myObj = JSON.parse(myJSON);
document.getElementById("demo").innerHTML = myObj.name;
