import streamlit as st
from generator import generate_response

st.set_page_config(
    page_title="RGCCSO AI Prompt Generator",
    page_icon="🤖",
    layout="wide"
)

st.title("🧠 RGCCSO AI Prompt Engineering")

st.caption("Transform simple ideas into professional AI prompts using the RGCCSO Framework.")

st.markdown("""
Convert your simple idea into a structured **RGCCSO Prompt**.
""")

# User Input
user_input = st.text_area(
    "💡 Enter your idea",
    placeholder="""
Examples:

• Build a Hospital Management System
• Create an AI Resume Builder
• Design a Smart Traffic System
• Make a Personal Finance Tracker
• Build an AI Interview Coach
• Create a Voice Assistant
"""
)

# Generate Button
generate = st.button("🚀 Generate Prompt")

if generate:
    if user_input.strip() == "":
        st.warning("Please enter an idea first.")
    else:
        with st.spinner("🤖 Gemini is generating your prompt..."):
            answer = generate_response(user_input)

        st.success("✅ RGCCSO Prompt Generated")
        st.markdown("---")
        st.subheader("📄 Generated Prompt")
        st.markdown(answer)
        st.markdown("---")
        
        st.download_button(
    "📥 Download Prompt",
    data=answer,
    file_name="rgccso_prompt.txt",
    mime="text/plain"
)