# set api key from .env file
import ell
from dotenv import load_dotenv

load_dotenv()


ell.init(verbose=True, store="./logdir")

# Using Model registration and automatic model discoxverdy
ell.models.ollama.register(base_url="http://localhost:11434/v1")

# Define the model to use
# MODEL = "phi3:3.8b"
MODEL = "closex/neuraldaredevil-8b-abliterated:latest"


# Define a function that uses the model to generate two drafts.
@ell.simple(model=MODEL, temperature=1)
def write_two_drafts(idea: str):
    """You are an joke writer.
    Write TWO short jokes about the given idea.
    (output the drafts as a numbered list)
    """
    return f"Write jokes about {idea}."


# Define a function that uses the model to choose the best draft.
@ell.simple(model=MODEL, temperature=0)
def choose_the_best_draft(drafts: str):
    """You are an expert fiction Judge."""
    return f"Choose the best draft from the following drafts:\n {drafts}"


# Run the pipeline
idea = "Donald Trump"
drafts = write_two_drafts(idea)

best_draft = choose_the_best_draft(drafts)

# type(drafts)

# print(drafts)
