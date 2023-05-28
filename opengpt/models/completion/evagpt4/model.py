import requests
import json

class Model:
    def __init__(self):
        self.url = "https://ava-alpha-api.codelink.io/api/chat"
        self.headers = {
            "content-type": "application/json"
        }
        self.payload = {
            "model": "gpt-4",
            "temperature": 0.6,
            "stream": True
        }
        self.accumulated_content = ""

    def _process_line(self, line):
        line_text = line.decode("utf-8").strip()
        if line_text.startswith("data:"):
            data = line_text[len("data:"):]
            try:
                data_json = json.loads(data)
                if "choices" in data_json:
                    choices = data_json["choices"]
                    for choice in choices:
                        if "finish_reason" in choice and choice["finish_reason"] == "stop":
                            break
                        if "delta" in choice and "content" in choice["delta"]:
                            content = choice["delta"]["content"]
                            self.accumulated_content += content
            except json.JSONDecodeError as e:
                return

    def ChatCompletion(self, messages):
        self.payload["messages"] = messages

        with requests.post(self.url, headers=self.headers, data=json.dumps(self.payload), stream=True) as response:
            for line in response.iter_lines():
                self._process_line(line)

        accumulated_content = self.accumulated_content
        self.accumulated_content = ""

        return accumulated_content
