# AI Chatbox Integration for resumé Website

## Overview

This project seamlessly incorporates an AI-based chatbox into your resumé website, providing an interactive user experience. The AI model is provided by Open AI (GPT3.5) and powered by the cutting-edge Eden AI services, crafted in Python, and integrated into the website.

Other AI models providers are also available, at your convenience, such as Meta, Gemini, Anthropic, Mistral, etc.

## Requirements

Before executing the code, ensure you have met the following prerequisites:

- A locally installed Python interpreter.
- An API key from Eden AI services, obtainable directly from their official website. A complimentary free plan is available, albeit with certain usage restrictions. (Other paid plans are also available.)

## Getting Started

1. Clone the repository to your local machine:

    ```bash
    git clone git@github.com:kstarkiller/simplon_brief09_chatbot_integration.git
    ```

2. Navigate to the project directory:

    ```bash
    cd simplon_brief09_chatbot_integration (or whatever you locally named this project)
    ```

3. Install the required Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Acquire your Eden AI API key:

    - Visit the [Eden AI website](https://edenai.io/).
    - Register for an account and retrieve your API key from the user dashboard.

5. Configure the application:

    - Open the `bot_api.py` file.
    - Replace the placeholder for the API key with your authentic Eden AI API key.

6. Launch the application:

    ```bash
    python bot_api.py
    ```

7. Launch the Python server to run the `index.html` file:

    ```bash
    python -m http.server 8001
    ```

8. Access the website:

    Open your preferred web browser and navigate to [http://localhost:8001](http://localhost:8001) to experience the resumé website enriched with the seamlessly integrated AI chatbox.

## Usage

The AI-powered chatbox elevates the user engagement on your resumé website. Visitors can interact with the chatbox, posing queries or seeking specific information, thereby fostering a personalized and dynamic user experience.
This chatbox is configure to be generalist and answer in a friendly yet respectful way.

## Support and Issues

Should you encounter any challenges or have inquiries, kindly [raise an issue](https://github.com/kstarkiller/simplon_brief09_chatbot_integration/issues) on the GitHub repository. I welcome contributions and value your feedback!

