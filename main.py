import openai
import instructor
from openai import OpenAI
import time
openaisecretkey = "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"
client = OpenAI(api_key=openaisecretkey)


assistant = client.beta.assistants.create(
    name="Math Tutor",
    instructions="You are a personal math tutor. Write and run code to answer math questions.",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4-1106-preview"
)

thread = client.beta.threads.create()

message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
)

run = client.beta.threads.runs.create(
  thread_id=thread.id,
  assistant_id=assistant.id,
  instructions="Please address the user as Jane Doe. The user has a premium account."
)


"""
run = client.beta.threads.runs.retrieve(
  thread_id=thread.id,
  run_id=run.id
)
"""

messages = client.beta.threads.messages.list(
  thread_id=thread.id
)

print(messages)