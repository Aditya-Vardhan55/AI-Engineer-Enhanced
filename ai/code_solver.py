import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def solve_code_problem(problem):
    response = openai.ChatCompletion.create(
        model = "gpt-4",
        messages = [
            {"role": "system", "content": "You are a coding expert. Solve this problem."},
            {"role": "user", "content": problem},
        ]
    )
    return response.choices[0].message.content 