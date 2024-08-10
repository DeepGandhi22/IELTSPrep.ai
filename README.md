# Building an AI-Powered IELTS Exam Prep Chatbot from Scratch: A Step-by-Step Guide

This repository contains the code and documentation for creating an AI-powered chatbot designed to assist with IELTS exam preparation. The chatbot leverages the Gemini LLM, Streamlit, and Python to provide personalized study assistance, including practice questions, feedback on writing tasks, and speaking cue card practice.

## Why Create This Chatbot?

The primary motivation for building this AI-powered chatbot was to enhance my knowledge in the field of Large Language Models (LLMs) and to address a significant challenge faced during solo preparation for the IELTS exam. As an individual preparing without access to classroom resources, I needed expert guidance for speaking and writing tasks. This chatbot serves as a personalized study assistant, generating practice questions, offering IELTS-level feedback, and providing speaking cue card practice.

## Step-by-Step Approach to Building the Chatbot

### 1. Choosing the Tech Stack

- **Frontend Technology**: Streamlit was chosen for its user-friendly interface, ease of learning, and suitability for developing chatbot applications.
- **LLM Selection**: Gemini 1.5 Flash was selected for its multimodal capabilities and extensive documentation, making it ideal for processing audio, files, and images.

### 2. Defining the Required Features

- **Writing Task Feedback and Question Generation**: Provides detailed feedback on IELTS writing tasks, offering corrections and guidance based on IELTS standards.
- **Audio Feedback for Speaking Tasks**: Integrates audio input capabilities to provide feedback on speaking tasks using Gemini's multimodal features.
- **Reading Task Question Generation**: Generates practice questions from any provided article, enabling targeted reading practice.

### 3. Building the Application

- **Set Up the Development Environment**:
  - Install Python, Streamlit, and necessary libraries.
  - Configure the Gemini 1.5 Flash API for integration.
  - Utilize GitHub for version control.
  
- **Implement the Core Features**:
  - **Writing Task Feedback and Question Generation**:
    - Integrate the LLM for generating prompts and feedback.
    - Implement a user-friendly Streamlit interface.
    - Design prompts using IELTS marking criteria to guide the LLM.
  - **Audio Feedback for Speaking Tasks**:
    - Use `streamlit-mic-recorder` for audio recording.
    - Implement speech-to-text and feedback features using Gemini's capabilities.
  - **Reading Task Question Generation**:
    - Develop a module to generate reading comprehension exercises using prompt engineering.
    
- **Test and Optimize**:
  - Conduct unit testing to ensure prompt accuracy.
  - Iteratively refine prompts based on testing outcomes.

### 4. What's Next?

Future enhancements include:
- Expanding Speaking Practice to cover all parts of the IELTS exam.
- Fine-tuning the model with a specialized dataset for better accuracy.
- Expanding the chatbot to support preparation for other language exams.

## Getting Started

### Prerequisites

- Python 3.x
- Streamlit
- Gemini 1.5 Flash API access

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ielts-prep-chatbot.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ielts-prep-chatbot
   ```
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up the Gemini 1.5 Flash API by adding your API key to the environment variables.

### Running the Application

To start the chatbot, run:
```bash
streamlit run app.py
```

## Contributing

Contributions are welcome! If you have any ideas for new features or would like to collaborate on another project, feel free to reach out.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Connect with Me

- [LinkedIn](https://www.linkedin.com/in/deepgandhi22/)
- [Try My Project](https://link-to-your-project-demo)
