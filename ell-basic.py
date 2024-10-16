# set api key from .env file
import ell
from dotenv import load_dotenv

load_dotenv()


# Using Model registration and automatic model discovery

ell.init(verbose=True, store="./logdir")
# Use models automatically registered by asking ollama
ell.models.ollama.register(base_url="http://localhost:11434/v1")


MODEL = "phi3:3.8b"


@ell.simple(model=MODEL, temperature=0.1)
def write_a_story():
    # SYSTEM PROMPT
    """
    You are an Indian and speak english like an Indian in Heavy South Indian accent. 
    """
    return "Introduce yourself in short to a Swiss."


response = write_a_story()
