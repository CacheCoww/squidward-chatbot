document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#form').onsubmit = () => {
        const request = new XMLHttpRequest();
        const input = document.querySelector('#inputtext').nodeValue;
        request.open('POST', '/talk');

        request.onload = () => {
           const data = JSON.parse(request.responseText);
           
           print(result);

        }

        const data = new FormData();
        data.append('inputtext', input);

        request.send(data);
        return false;

    }


});