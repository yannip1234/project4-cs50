
document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('#new-post-form').onsubmit = function (){
        const content = document.querySelector('#post-content').value;
        fetch('/post', {
            method: 'POST',
            body: JSON.stringify({
                content: content
            }),
            headers: { "X-CSRFToken": document.querySelector("input[name='csrfmiddlewaretoken']").value }
        })
           .then(response => response.json())
            .then(result => {
                console.log(result);
            })
    }

});