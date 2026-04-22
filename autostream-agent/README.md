# 🚀 AutoStream AI Agent – Social-to-Lead Workflow

## 📌 Overview

This project is a **Conversational AI Agent** built for a fictional SaaS company **AutoStream**, which provides automated video editing tools for content creators.

The agent is designed to:

* Understand user intent
* Answer product and pricing questions using RAG
* Identify high-intent users
* Collect lead information
* Trigger backend actions (mock API)

---

## 🧠 Features

### 1. Intent Detection

The agent classifies user input into:

* Greeting
* Pricing/Product Inquiry
* High-Intent (ready to sign up)

---

### 2. RAG (Retrieval-Augmented Generation)

* Uses a local knowledge base
* Powered by FAISS vector database
* Retrieves relevant information for accurate responses

---

### 3. Lead Capture Workflow

When a user shows high intent, the agent:

1. Asks for:

   * Name
   * Email
   * Platform (YouTube, Instagram, etc.)
2. Calls a mock API **only after collecting all details**

---

### 4. State Management

* Maintains conversation memory across multiple turns
* Tracks user details during lead collection
* Ensures smooth multi-step interaction

---

## 🛠️ Tech Stack

* **Language:** Python 3
* **Framework:** LangChain
* **Vector Store:** FAISS
* **Embeddings:** HuggingFace (all-MiniLM-L6-v2)
* **Architecture:** Rule-based + RAG pipeline

---

## ⚙️ How to Run Locally

### 1. Clone Repository

```bash
git clone <your-repo-link>
cd autostream-agent
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Project

```bash
python app.py
```

---

## 💬 Example Conversation

```
You: Hi, tell me about pricing
Bot: Here are our plans...

You: I want to try Pro plan
Bot: What's your name?

You: Dhruvin
Bot: What's your email?

You: dhruvin@gmail.com
Bot: Which platform?

You: YouTube
Bot: 🎉 You're all set!
```

---

## 🏗️ Architecture Explanation

This project uses LangChain to build a modular conversational agent with a simple yet effective architecture.

Intent detection is implemented using rule-based logic to classify user input into greeting, pricing inquiry, or high-intent categories. Based on the detected intent, the system routes the request to the appropriate handler.

For answering product-related queries, a Retrieval-Augmented Generation (RAG) pipeline is used. A local knowledge base is embedded using HuggingFace embeddings and stored in a FAISS vector database. When a user asks a question, the system retrieves the most relevant information and generates a response.

State management is handled using a global state dictionary that tracks user information such as name, email, and platform. This enables the agent to manage multi-step conversations and ensures that the lead capture process is completed before triggering the backend function.

The tool execution logic ensures that the mock lead capture API is only called after all required user details are collected, preventing premature execution.

---

## 📲 WhatsApp Integration (Concept)

To integrate this agent with WhatsApp:

1. Use a service like Twilio WhatsApp API
2. Set up a webhook endpoint using Flask
3. Receive incoming messages via webhook
4. Pass the message to the AI agent
5. Send the agent’s response back to the user

This enables real-time conversational interaction on WhatsApp.

---

## 🎯 Future Improvements

* Replace rule-based intent detection with LLM-based classification
* Upgrade to LangGraph for advanced state management
* Add web UI (Flask/React)
* Store leads in a real database
* Deploy on cloud (AWS/GCP)

---

## 👨‍💻 Author

Dhruvin Andhariya
