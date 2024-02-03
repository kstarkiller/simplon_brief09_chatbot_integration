const answerEl = document.getElementById('chat-answer');
const promptEl = document.getElementById('chat-input');
const buttonEl = document.getElementById('chat-send');

function addNewQuestion() {
    let logsEl = document.createElement('p');
    logsEl.classList.add('chat-log');
    logsEl.innerText = "Je réflechis..."
    answerEl.appendChild(logsEl);

    fetch('http://localhost:8000/' + promptEl.value, {
        method: 'POST'
        })
        .then(response => {
        return response.json();
        })
        .then(data => {
            console.log(data);
            logsEl.innerText = "Vous : \"" + promptEl.value + "\"\n\nMa réponse : " + data;
    });

    promptEl.innerText = "Anything else ?";
};

// fetch('http://localhost:8000/test/' + promptEl.value)
// .then(response => {
// return response.json();
// })
// .then(data => {
//     logsEl.innerText = "Vous : \"" + promptEl.value + "\"\n\nMa réponse : " + data;
// });