const answerEl = document.getElementById('chat-answer');
const promptEl = document.getElementById('chat-input');
const buttonEl = document.getElementById('chat-send');

function addNewQuestion() {
    let userLogEl = document.createElement('p');
    userLogEl.classList.add('chat-log-user');
    userLogEl.innerText = "You: " + promptEl.value;
    answerEl.appendChild(userLogEl);

    let botLogEl = document.createElement('p');
    botLogEl.classList.add('chat-log-bot');
    botLogEl.innerText = "I'm thinking...";
    answerEl.appendChild(botLogEl);

    fetch('http://localhost:8000/' + promptEl.value, {
        method: 'POST',
        })
        .then(response => {
            // console.log(response.json());
        return response.json();
        })
        .then(data => {
            console.log(data);
            botLogEl.innerText = "Me: " + data;
    });

    promptEl.placeholder = "Anything else ?";
};

promptEl.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault(); // Empêche l'action par défaut de la touche Entrée
        addNewQuestion();
    }
});