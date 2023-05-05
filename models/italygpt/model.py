import requests, time, ast, json
from bs4 import BeautifulSoup
from hashlib import sha256

class Model:
    # answer is returned with html formatting
    next_id = None
    messages = []
    answer = None
    
    def __init__(self):
        r = requests.get("https://italygpt.it")
        soup = BeautifulSoup(r.text, "html.parser")
        self.next_id = soup.find("input", {"name": "next_id"})["value"]

    def GetAnswer(self, prompt: str, messages: list = []):
        try:
            r = requests.get("https://italygpt.it/question", params={"hash": sha256(self.next_id.encode()).hexdigest(), "prompt": prompt, "raw_messages": json.dumps(messages)}).json()
        except Exception as e:
            r = requests.get("https://italygpt.it/question", params={"hash": sha256(self.next_id.encode()).hexdigest(), "prompt": prompt, "raw_messages": json.dumps(messages)}).text
            if "too many requests" in r.lower():
                # rate limit is 5 requests per 1 minute
                time.sleep(20)
                return self.create(prompt, messages)
            else:
                print(f"There was an error getting the response, consider re-initializing the italygpt instance. {e}")
                return
        if r.get("error") != None:
            error = r["error"]
            if "ip is banned" in error.lower():
                print("Your ip was banned. Support email is: support@ItalyGPT.it")
                return
            elif "proxy not allowed" in error.lower():
                print("You are using a proxy, italygpt api calls do not allow proxies.")
                return
            elif "prompt too long" in error.lower():
                print("Your prompt is too long (max characters is: 1000)")
                return
            else:
                print(f"There was an error with your request: {error}")
                return
        self.next_id = r["next_id"]
        self.messages = ast.literal_eval(r["raw_messages"])
        self.answer = r["response"]
        return self