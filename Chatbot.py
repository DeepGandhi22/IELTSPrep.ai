import os, io
import streamlit as st
import google.generativeai as genai
from prompts import generated_que_wt1, generated_que_wt2
from prompts import user_que_feedback_wt1, user_que_feedback_wt2, gen_feedback_wt1, gen_feedback_wt2
from prompts import generate_cue_card_topic
from audio_recorder_streamlit import audio_recorder
from dotenv import load_dotenv

# Set environment variables to control logging
os.environ['GRPC_VERBOSITY'] = 'ERROR'
os.environ['GRPC_TRACE'] = ''
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
os.environ['ABSL_LOGGING_LEVEL'] = '0'

load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')

# Configure the API key
genai.configure(api_key=api_key)

# Create the model
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

# Initialize session state variables
if 'generated_question' not in st.session_state:
    st.session_state.generated_question = {}
if 'feedback' not in st.session_state:
    st.session_state.feedback = {}
if 'current_section' not in st.session_state:
    st.session_state.current_section = None
if 'show_generated_question' not in st.session_state:
    st.session_state.show_generated_question = {}
if 'cue_card_topic' not in st.session_state:
    st.session_state.cue_card_topic = None
if 'audio_bytes' not in st.session_state:
    st.session_state.audio_bytes = None
if 'transcription' not in st.session_state:
    st.session_state.transcription = None
if 'provide_feedback' not in st.session_state:
    st.session_state.provide_feedback = False
if 'feedback_text' not in st.session_state:
    st.session_state.feedback_text = None
if 'article' not in st.session_state:
    st.session_state.article = None
if 'provide_answers' not in st.session_state:
    st.session_state.provide_answers = False
if 'generated_questions' not in st.session_state:
    st.session_state.generated_questions = None
if 'powered_by_text' not in st.session_state:
    st.session_state.powered_by_text = st.sidebar.empty()
if 'topic_category' not in st.session_state:
    st.session_state.topic_category = None
if 'with_suggestions' not in st.session_state:
    st.session_state.with_suggestions = None

# Define topic categories
topic_categories = [
    "Personal experiences",
    "Family and relationships",
    "Work and education",
    "Hobbies and interests",
    "Travel and places",
    "Technology and media",
    "Environment and nature",
    "Society and culture",
    "Health and lifestyle",
    "Random (any category)"
]


# Define the custom CSS
custom_css = """
<style>
.sidebar-footer {
    font-size: 12px;  /* Adjust the font size as needed */
}
</style>
"""

# Inject the custom CSS
st.markdown(custom_css, unsafe_allow_html=True)


# Function to transcribe audio using Gemini API
def transcribe_audio(audio_bytes):
    # Assuming the Gemini API has a method to transcribe audio
    prompt = "Transcribe the following audio:"
    response = model.generate_content([prompt, {"mime_type": "audio/wav", "data": audio_bytes}])
    # Replace with actual transcription method
    return response.text

def remove_extra_words(transcription):
    prompt = "Remove filler words from the provided text"
    response = model.generate_content([prompt, transcription])
    # Replace with actual transcription
    return response.text

# Sidebar
st.sidebar.title("IELTS Exam Prep")
exam_section = st.sidebar.radio("Choose a section:", ("Reading", "Writing", "Speaking"))

# Clear feedback when changing sections
if st.session_state.current_section != exam_section:
    st.session_state.feedback = {}
    st.session_state.current_section = exam_section

# Task selection and options
if exam_section == "Writing":
    task = st.sidebar.selectbox("Choose a writing task:", ("Writing Task 1", "Writing Task 2"))
    option = st.sidebar.radio("Choose an option:", ("Provide question and answer", "Get a practice question"))

    # Reset show_generated_question when switching tasks or options
    if 'last_task' not in st.session_state or st.session_state.last_task != (task, option):
        st.session_state.show_generated_question[task] = False
        st.session_state.last_task = (task, option)

# Update the Speaking section in the sidebar
elif exam_section == "Speaking":
    task = st.sidebar.selectbox("Choose a speaking part:", ("Practice Cue Card",))
    option = st.sidebar.radio("Choose an option:", ("Generate a new cue card", "Use an existing cue card"))
    
    if option == "Generate a new cue card":
        st.session_state.topic_category = st.sidebar.selectbox("Select a topic category:", topic_categories)
        st.session_state.with_suggestions = st.sidebar.radio("Include suggestions?", ("With suggestions", "Without suggestions"))
else:
    task = None
    option = None

# Add the About Me section
st.sidebar.markdown("---")  # Optional: Add a separator line
st.sidebar.subheader("About Me")
st.sidebar.markdown("Hi, I'm Deep Gandhi a Masters student at University of Windsor working towards building my career in the field of AI and Machine Learning. Connect with me on [LinkedIn](https://www.linkedin.com/in/deepgandhi22/).")

# Add the disclaimer section
st.sidebar.markdown("---")  # Optional: Add a separator line
st.sidebar.subheader("Disclaimer")
st.sidebar.markdown("This application is intended for IELTS exam preparations purposes only and may not be 100% accurate. So bands that you have got from the feedback of LLM does not reflect the band you will get in real-life exam. Please use this as a tool to help you or guide you in the preparation of IELTS exam.")

st.sidebar.markdown("---")
st.sidebar.markdown('<div class="sidebar-footer">Powered by Gemini 1.5 Flash</div>', unsafe_allow_html=True)
# Main app
st.title(f"IELTS {exam_section} Prep")

# Handle Writing tasks
if exam_section == "Writing":
    if option == "Provide question and answer":
        question = st.text_area("Enter your IELTS question:")
        answer = st.text_area("Enter your answer:")
        if st.button("Get Feedback"):
            if task == "Writing Task 1":
                prompt = user_que_feedback_wt1(question, answer)
            else:  # Writing Task 2
                prompt = user_que_feedback_wt2(question, answer)
            response = model.generate_content(prompt)
            st.session_state.feedback[task] = response.text
            st.markdown("**Feedback:**")
            st.markdown(response.text)

    elif option == "Get a practice question":
        if st.button("Generate New Question"):
            if task == "Writing Task 1":
                prompt = generated_que_wt1()
            else:  # Writing Task 2
                prompt = generated_que_wt2()
            response = model.generate_content(prompt)
            st.session_state.generated_question[task] = response.text
            st.session_state.show_generated_question[task] = True
            st.session_state.feedback[task] = ""  # Clear previous feedback

        if st.session_state.show_generated_question.get(task, False):
            st.markdown(f"**Generated Question:**\n\n{st.session_state.generated_question[task]}")
            user_answer = st.text_area("Your answer to the generated question:")
            if st.button("Submit Answer"):
                if task == "Writing Task 1":
                    prompt = gen_feedback_wt1(st.session_state.generated_question[task], user_answer)
                else:  # Writing Task 2
                    prompt = gen_feedback_wt2(st.session_state.generated_question[task], user_answer)
                response = model.generate_content(prompt)
                st.session_state.feedback[task] = response.text
                st.markdown("**Feedback:**")
                st.markdown(response.text)

# Update the Speaking section in the main app
elif exam_section == "Speaking":
    if task == "Practice Cue Card":
        if option == "Generate a new cue card":
            if st.button("Generate New Cue Card Topic"):
                prompt = generate_cue_card_topic(st.session_state.topic_category, st.session_state.with_suggestions)
                st.session_state.cue_card_topic = model.generate_content(prompt)
                st.session_state.transcription = None  # Reset transcription
                st.session_state.provide_feedback = False  # Reset feedback flag
                st.session_state.feedback_text = None  # Reset feedback text
        
        elif option == "Use an existing cue card":
            user_cue_card_topic = st.text_area("Enter your own cue card topic:")
            if st.button("Use Custom Cue Card Topic"):
                st.session_state.cue_card_topic = user_cue_card_topic
                st.session_state.transcription = None  # Reset transcription
                st.session_state.provide_feedback = False  # Reset feedback flag
                st.session_state.feedback_text = None  # Reset feedback text

        if st.session_state.cue_card_topic:
            st.markdown("**Cue Card Topic:**")
            st.markdown(st.session_state.cue_card_topic)
            st.markdown("**Instructions:**")
            st.markdown("1. Read the cue card topic carefully.")
            st.markdown("2. You have 1 minute to prepare your response.")
            st.markdown("3. Speak for 1-2 minutes on the given topic.")
            st.markdown("4. Click the 'Record' button when you're ready to start speaking.")

            # Record audio
            st.markdown("**Record your response:**")
            audio_bytes = audio_recorder()

            if audio_bytes:
                st.audio(audio_bytes, format="audio/wav")
                st.session_state.audio_bytes = audio_bytes  # Store in session state

            if st.button("Transcribe Audio"):
                st.session_state.transcription = transcribe_audio(audio_bytes)
                st.session_state.transcription = remove_extra_words(st.session_state.transcription)
                st.session_state.provide_feedback = False  # Reset feedback flag

            if st.session_state.transcription:
                st.markdown("**Transcription:**")
                st.markdown(st.session_state.transcription)

                if st.button("Provide Feedback"):
                    st.session_state.provide_feedback = True

            if st.session_state.provide_feedback:
                feedback_prompt = f"Provide feedback on the following IELTS Speaking response for the cue card topic: '{st.session_state.cue_card_topic}'. Response: {st.session_state.transcription}"
                feedback_response = model.generate_content(feedback_prompt)
                st.session_state.feedback_text = feedback_response.text
                st.session_state.provide_feedback = False  # Reset feedback flag

            if st.session_state.feedback_text:
                st.markdown("**Feedback:**")
                st.markdown(st.session_state.feedback_text)


# Handle Reading section
else:  # Reading section
    article = st.text_area("Enter your article here")
    if st.button("Submit"):
        st.session_state.article = article
        prompt = f"Generate IELTS reading level of questions from the given article:\n\n{article}"
        response = model.generate_content(prompt)
        st.session_state.generated_questions = response.text

    if st.session_state.generated_questions:
        st.markdown(st.session_state.generated_questions)

        if st.button("Provide Answers"):
            st.session_state.provide_answers = True

    if st.session_state.provide_answers:
        prompt = f"Please provide answers to the following questions based on the article:\n\nQuestions:\n{st.session_state.generated_questions}\n\nArticle:\n{st.session_state.article}"
        response = model.generate_content(prompt)
        answers = response.text
        st.markdown("**Answers:**")
        st.markdown(answers)
