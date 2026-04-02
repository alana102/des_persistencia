var obj = {
    foo : 'foo',
    toJSON : function(){
        return 'bar';
    }
};

var myJSON = JSON.stringify(obj);
console.log(myJSON);
myJSON = JSON.stringify({x : obj});
console.log(myJSON);
