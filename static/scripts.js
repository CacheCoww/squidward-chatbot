document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#form').onsubmit = () => {
        const request = new XMLHttpRequest();

        const input = document.querySelector('#inputtext').value;
        generateLi(input, "you");
        request.open('POST', '/talk');

        request.onload = () => {
           let data = JSON.parse(request.responseText);
           
           console.log(data);
           generateLi(data, "other")

        }

        const data = new FormData();
        data.append('inputtext', input);
        

        request.send(data);
        return false;

    }


});

function generateLi(text, person){
   // const div = document.createElement('div');
    //div.className = "messages";
    const div = document.createElement('div');
    
    const ol = document.querySelector(".conversation");
    const li = document.createElement('li');
    li.className = person;
    li.innerHTML = text;  
   // div.appendChild(li); 
   if (person == "other"){
       person = "Squidbot"
   }
   div.innerHTML = person;
   div.className = "chatname"
   ol.appendChild(div); 
    ol.appendChild(li);
}