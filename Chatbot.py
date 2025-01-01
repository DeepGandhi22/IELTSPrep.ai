import os
import streamlit as st
import google.generativeai as genai
from prompts import generated_que_wt1, generated_que_wt2
from prompts import user_que_feedback_wt1, user_que_feedback_wt2, gen_feedback_wt1, gen_feedback_wt2
from prompts import generate_cue_card_topic, generate_answer, reading_question, speaking_feedback
from dotenv import load_dotenv
from azure.cognitiveservices.speech import SpeechConfig, SpeechRecognizer, AudioConfig
import azure.cognitiveservices.speech as speechsdk
import logging

# Load environment variables
load_dotenv()

# Set environment variables for logging and error handling
os.environ['GRPC_VERBOSITY'] = 'ERROR'
os.environ['GRPC_TRACE'] = ''
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
os.environ['ABSL_LOGGING_LEVEL'] = '0'

# Fetch API keys from environment
api_key = os.getenv('GEMINI_API_KEY')
azure_speech_key = os.getenv('AZURE_SPEECH_KEY')
azure_region = os.getenv('AZURE_REGION')

# Ensure keys are loaded properly
if not all([api_key, azure_speech_key, azure_region]):
    raise ValueError("Missing required environment variables. Ensure .env file is properly configured.")

# Configure Gemini API
genai.configure(api_key=api_key)
generation_config = {
    "temperature": 1.35,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
}
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

# Set page config for Streamlit
st.set_page_config(
    page_title="IELTS.ai",
    page_icon=":books:"
)

# Initialize session state
if 'generated_question' not in st.session_state:
    st.session_state['generated_question'] = {}
if 'feedback' not in st.session_state:
    st.session_state['feedback'] = {}
if 'current_section' not in st.session_state:
    st.session_state['current_section'] = None
if 'audio_bytes' not in st.session_state:
    st.session_state['audio_bytes'] = None
if 'transcription' not in st.session_state:
    st.session_state['transcription'] = None
if 'provide_feedback' not in st.session_state:
    st.session_state['provide_feedback'] = False
if 'feedback_text' not in st.session_state:
    st.session_state['feedback_text'] = None
if 'article' not in st.session_state:
    st.session_state['article'] = None
if 'generated_questions' not in st.session_state:
    st.session_state['generated_questions'] = None
if 'cue_card_topic' not in st.session_state:
    st.session_state['cue_card_topic'] = None


# Define topic categories for speaking section
topic_categories = [
    "Personal experiences", "Family and relationships", "Work and education",
    "Hobbies and interests", "Travel and places", "Technology and media",
    "Environment and nature", "Society and culture", "Health and lifestyle",
    "Random (any category)"
]

# Sidebar content
st.sidebar.title("IELTS Exam Prep")
exam_section = st.sidebar.radio("Choose a section:", ("Writing", "Speaking", "Reading"))


# Configure logging
logging.basicConfig(level=logging.INFO)

# Function to transcribe audio using Azure Speech API
def transcribe_audio_azure():
    try:
        # Create an instance of a speech configuration with your Azure credentials
        speech_config = speechsdk.SpeechConfig(subscription=azure_speech_key, region=azure_region)

        # Set the audio input to microphone
        audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)

        # Create a speech recognizer with the given settings
        recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

        # Start the recognition pr  ocess (this will block until finished)
        st.write("Recording audio... Please speak into the microphone.")
        result = recognizer.recognize_once()  # Recognize a single phrase

        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            st.write(f"Recognized: {result.text}")
            return result.text
        elif result.reason == speechsdk.ResultReason.NoMatch:
            st.write("No speech could be recognized.")
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            st.write(f"Speech Recognition canceled: {cancellation_details.reason}")
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                st.write(f"Error details: {cancellation_details.error_details}")
    except Exception as e:
        logging.error(f"An error occurred during audio transcription: {e}")
        st.write("An error occurred during audio transcription. Please try again.")
    return None

# Clear feedback when changing sections
if st.session_state['current_section'] != exam_section:
    st.session_state['feedback'] = {}
    st.session_state['current_section'] = exam_section

# Handle writing section
if exam_section == "Writing":
    task = st.sidebar.selectbox("Choose a writing task:", ("Writing Task 1", "Writing Task 2"))
    option = st.sidebar.radio("Choose an option:", ("Provide question and answer", "Get a practice question"))

    # Reset show_generated_question when switching tasks or options
    if 'last_task' not in st.session_state or st.session_state['last_task'] != (task, option):
        st.session_state['show_generated_question'] = False
        st.session_state['last_task'] = (task, option)

    if option == "Provide question and answer":
        question = st.text_area("Enter your IELTS question:")
        answer = st.text_area("Enter your answer:")
        if st.button("Get Feedback"):
            prompt = user_que_feedback_wt1(question, answer) if task == "Writing Task 1" else user_que_feedback_wt2(question, answer)
            response = model.generate_content(prompt)
            st.session_state['feedback'][task] = response.text
            st.markdown("**Feedback:**")
            st.markdown(response.text)

    elif option == "Get a practice question":
        if st.button("Generate New Question"):
            prompt = generated_que_wt1() if task == "Writing Task 1" else generated_que_wt2()
            response = model.generate_content(prompt)
            st.session_state['generated_question'][task] = response.text
            st.session_state['show_generated_question'] = True
            st.session_state['feedback'][task] = ""  # Clear previous feedback
        if st.session_state['show_generated_question']:
            st.markdown(f"**Generated Question:**\n\n{st.session_state['generated_question'][task]}")
            user_answer = st.text_area("Your answer to the generated question:")
            if st.button("Submit Answer"):
                feedback_prompt = gen_feedback_wt1(st.session_state['generated_question'][task], user_answer) if task == "Writing Task 1" else gen_feedback_wt2(st.session_state['generated_question'][task], user_answer)
                response = model.generate_content(feedback_prompt)
                st.session_state['feedback'][task] = response.text
                st.markdown("**Feedback:**")
                st.markdown(response.text)

# Handle speaking section
# Speaking Section (Updated)
elif exam_section == "Speaking":
    task = st.sidebar.selectbox("Choose a speaking part:", ("Practice Cue Card",))
    option = st.sidebar.radio("Choose an option:", ("Generate a new cue card",))

    if option == "Generate a new cue card":
        st.session_state['topic_category'] = st.sidebar.selectbox("Select a topic category:", topic_categories)
        st.session_state['with_suggestions'] = st.sidebar.radio("Include suggestions?", ("With suggestions", "Without suggestions"))

    if st.button("Generate New Cue Card Topic"):
        prompt = generate_cue_card_topic(st.session_state['topic_category'], st.session_state['with_suggestions'])
        response = model.generate_content(prompt)
        st.session_state['cue_card_topic'] = response.text
        st.session_state['transcription'] = None
        st.session_state['provide_feedback'] = False
        st.session_state['feedback_text'] = None

    if st.session_state['cue_card_topic']:
        st.markdown("**Cue Card Topic:**")
        st.markdown(st.session_state['cue_card_topic'])
        st.markdown("**Instructions:**")
        st.markdown("1. Read the cue card topic carefully.")
        st.markdown("2. Record your answer and click 'Transcribe Audio' to get feedback.")
        
        # Record and transcribe audio using Azure
        if st.button("Start Recording"):
            st.session_state['transcription'] = transcribe_audio_azure()

        # Show transcribed text if available
        if st.session_state['transcription']:
            st.markdown("**Transcription:**")
            st.markdown(st.session_state['transcription'])

        if st.session_state['transcription'] and st.button("Provide Feedback"):
            feedback_prompt = speaking_feedback(st.session_state['cue_card_topic'], st.session_state['transcription'])
            feedback_response = model.generate_content(feedback_prompt)
            st.session_state['feedback_text'] = feedback_response.text
            st.session_state['provide_feedback'] = False

        if st.session_state['feedback_text']:
            st.markdown("**Feedback:**")
            st.markdown(st.session_state['feedback_text'])

# Handle reading section
else:
    article = st.text_area("Enter your article here")
    if st.button("Submit"):
        st.session_state['article'] = article
        prompt = reading_question(st.session_state['article'])
        response = model.generate_content(prompt)
        st.session_state['generated_questions'] = response.text

    if st.session_state['generated_questions']:
        st.markdown(st.session_state['generated_questions'])
        if st.button("Provide Answers"):
            answers_prompt = generate_answer(st.session_state['article'], st.session_state['generated_questions'])
            response = model.generate_content(answers_prompt)
            st.markdown("**Answers:**")
            st.markdown(response.text)