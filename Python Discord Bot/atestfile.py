from perspective import PerspectiveAPI
import os
from dotenv import load_dotenv
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
p = PerspectiveAPI(GOOGLE_API_KEY)
def check_if_toxic(text):
    result = p.score(text)
    print(result["TOXICITY"])
    
check_if_toxic("fuck you")