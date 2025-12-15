"""
Module to handle Gemini-based chat functionality with book content
"""
import os
import logging
from typing import List, Optional
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Initialize logging
logger = logging.getLogger(__name__)

# Initialize Gemini API
try:
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    gemini_model = genai.GenerativeModel('gemini-pro')
    logger.info("Successfully configured Gemini API")
except Exception as e:
    logger.error(f"Failed to configure Gemini API: {e}")
    gemini_model = None


def get_gemini_response(query: str, context: Optional[str] = None, selected_text: Optional[str] = None) -> dict:
    """
    Get response from Gemini API with book content context
    """
    if not gemini_model:
        raise Exception("Gemini API not configured")

    try:
        if selected_text:
            # Use only the selected text as context
            prompt = f"Based on the following selected text: '{selected_text}', please answer this question: {query}"
        elif context:
            # Use provided context (e.g., search results from book)
            prompt = f"Based on the following book content, please answer the question. If the content doesn't contain the answer, say so clearly.\n\n{context}\n\nQuestion: {query}"
        else:
            # General question without specific context
            prompt = f"Please answer the following question about embodied AI systems, robotics, or related topics: {query}"

        response = gemini_model.generate_content(prompt)

        return {
            "response": response.text,
            "citations": ["Gemini AI Response"]  # Placeholder for citations
        }
    except Exception as e:
        logger.error(f"Error calling Gemini API: {e}")
        raise Exception(f"Error calling Gemini API: {str(e)}")