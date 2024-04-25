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

    console.log(conversationHistory);

    let botLogEl = document.createElement('p');
    botLogEl.classList.add('chat-log-bot');
    botLogEl.innerText = "I'm thinking...";
    answerEl.appendChild(botLogEl);

    fetch('http://kev-chatbot.westeurope.azurecontainer.io:8000/chatbot', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            "model": "phi3",
            "messages": conversationHistory,
            "stream": false
        }),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        if (data.message) {
            console.log(data);
            botLogEl.innerText = "Me: " + data.message.content;
            conversationHistory.push({
                "role": "assistant",
                "content": data.message.content
            });
    
            // Scroll to the bottom of the chat
            botLogEl.scrollIntoView({ behavior: 'smooth' });
        } else {
            console.error('Server response does not contain a message property');
        }
    })
    .catch(error => {
        console.error('Error:', error);
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