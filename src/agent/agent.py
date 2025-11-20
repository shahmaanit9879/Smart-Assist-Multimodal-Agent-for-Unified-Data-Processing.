from openai import OpenAI
import json

client = OpenAI()

class SmartAssistAgent:
    def __init__(self, rag_system):
        self.rag = rag_system

    def plan(self, query):
        return f"Understanding: {query}. Retrieving information…"

    def act(self, query):
        context = self.rag.retrieve(query)
        return self.generate_answer(query, context)

    def generate_answer(self, query, context):
        prompt = f"""
        You are SmartAssist, a multimodal AI agent.

        USER QUESTION:
        {query}

        CONTEXT FROM RAG:
        {context}

        Provide a helpful final answer.
        """

        response = client.responses.create(
            model="gpt-4o-mini",
            input=prompt
        )
        return response.output_text

    def run(self, query):
        plan_step = self.plan(query)
        answer = self.act(query)
        return {"plan": plan_step, "answer": answer}
