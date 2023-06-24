
let myrequet = new XMLHttpRequest();

myrequet.onreadystatechange=function (){
    if( this.readyState === 4 && this.status === 200  ){
        //console.log(this.responseText);
        let myJsObject = JSON.parse(this.responseText);

        //console.log(myJsObject);

        for(let i=0; i < myJsObject.length; i++ ){
            let div = document.createElement("div");
            let repoName =document.createTextNode(myJsObject);
            div.appendChild(repoName);
            document.body.appendChild(div);
            
        }
        
    }

};
myrequet.open("GET"," https://api.polygon.io/v2/reference/news?apiKey=1NNmc2_KMQIUXj09BSlPxkZzT6zSeJOS",true);
myrequet.send();

//1NNmc2_KMQIUXj09BSlPxkZzT6zSeJOS
//      
//       https://api.github.com/users/ElzeroWebSchool/repos 
