let conversationHistory = [];
let promptEl = document.getElementById('chat-input');
let answerEl = document.getElementById('chat-answer');

function addNewQuestion() {
    let userLogEl = document.createElement('p');
    userLogEl.classList.add('chat-log-user');
    userLogEl.innerText = "You: " + promptEl.value;
    answerEl.appendChild(userLogEl);

    conversationHistory.push({
        "role": "user",
        "content": promptEl.value
    });

    let botLogEl = document.createElement('p');
    botLogEl.classList.add('chat-log-bot');
    botLogEl.innerText = "I'm thinking...";
    answerEl.appendChild(botLogEl);

    let data = {
        "model": "llama3",
        "messages": conversationHistory,
        "stream": false
    };

    fetch('http://kev-chatbot.westeurope.azurecontainer.io:11434/api/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        botLogEl.innerText = "Me: " + data['message']['content'];
        conversationHistory.push({
            "role": "assistant",
            "content": data['message']['content']
        });

        // Scroll to the bottom of the chat
        botLogEl.scrollIntoView({ behavior: 'smooth' });
    });

    promptEl.value = "";
    promptEl.placeholder = "Anything else ?";
}

promptEl.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault(); // Empêche l'action par défaut de la touche Entrée
        addNewQuestion();
    }
}); 