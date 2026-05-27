import os
import google.generativeai as genai
from dotenv import load_dotenv
from backend.services.vector_store import vectorstore

load_dotenv()
system_message = (
    "You are a helpful shop assistant. Answer only about the shop's product catalog. "
    "Use a friendly tone. If irrelevant, say: 'I can only help with product-related queries, sir.'"
)

def get_relevant_context(query):
    results = vectorstore.similarity_search(query, k=1)
    if results:
        metadata = results[0].metadata
        return (
            f"Product Name: {metadata.get('ProductName')}\n"
            f"Brand: {metadata.get('ProductBrand')}\n"
            f"Price: {metadata.get('Price')}\n"
            f"Gender: {metadata.get('Gender')}\n"
            f"Color: {metadata.get('PrimaryColor')}\n"
            f"Description: {results[0].page_content}"
        )
    return "No relevant search found."

def generate_response(query, history):
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    model = genai.GenerativeModel("gemini-2.5-flash")

    history.append(f"User: {query}")
    context = get_relevant_context(query)
    prompt = f"{system_message}\n\n" + "\n".join(history) + f"\n\nContext:\n{context}\n\nAssistant:"
    response = model.generate_content(prompt).text
    history.append(f"Assistant: {response}")
    return response, history