import streamlit as st
import PyPDF2
import io
import os
import google.generativeai as genai 
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI Resume Critiquer", page_icon="📃", layout="centered")

st.title("AI Resume Critiquer")
st.markdown("Upload your resume and get AI-powered feedback tailored to your needs!")

# --- CHANGE 1: Load the Gemini API Key ---
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

uploaded_file = st.file_uploader("Upload your resume (PDF or TXT)", type=["pdf", "txt"])
job_role = st.text_input("Enter the job role you're targeting (optional)")

analyze = st.button("Analyze Resume")

# --- File extraction functions (no changes needed) ---
def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    return uploaded_file.read().decode("utf-8")
# --- End of file extraction ---

if analyze and uploaded_file:
    
    # --- CHANGE 2: Add a check for the API key ---
    if not GEMINI_API_KEY:
        st.error("GEMINI_API_KEY not found. Please add it to your .env file.")
        st.stop()
    
    try:
        # Add a spinner for better user experience
        with st.spinner("Your resume is being analyzed by AI..."):
            
            file_content = extract_text_from_file(uploaded_file)
            
            if not file_content.strip():
                st.error("File does not have any content...")
                st.stop()
            
            # The prompt is the same as before
            prompt = f"""Please analyze this resume and provide constructive feedback. 
            Focus on the following aspects:
            1. Content clarity and impact
            2. Skills presentation
            3. Experience descriptions
            4. Specific improvements for {job_role if job_role else 'general job applications'}
            
            Resume content:
            {file_content}
            
            Please provide your analysis in a clear, structured format with specific recommendations."""
            
            # --- CHANGE 3: The Gemini API Call ---
            
            # Configure the API key
            genai.configure(api_key=GEMINI_API_KEY)
            
            # Set up generation configuration
            generation_config = {
                "temperature": 0.7,
                #c"max_output_tokens": 2048,
            }

            # Define the system instruction (what you had as 'system' role)
            system_instruction = "You are an expert resume reviewer with years of experience in HR and recruitment."

            # Initialize the model
            model = genai.GenerativeModel(
                model_name="gemini-2.5-flash", # A great, fast model
                generation_config=generation_config,
                system_instruction=system_instruction
            )

            # Make the API call
            response = model.generate_content(prompt)
            
            # --- End of Gemini API Call ---

            st.markdown("### Analysis Results")
            # --- CHANGE 4: How to read the response ---
            st.markdown(response.text)
    
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        # Add a specific check for the permission error
        if "permission" in str(e).lower():
            st.error("This is often due to an invalid API key or billing not being set up for your Google Cloud project.")