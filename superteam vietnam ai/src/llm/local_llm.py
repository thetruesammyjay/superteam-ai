from transformers import AutoModelForCausalLM, AutoTokenizer
from config import Config

class LocalLLM:
    def __init__(self):
        self.model_path = Config.LOCAL_LLM_PATH
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_path)
        self.model = AutoModelForCausalLM.from_pretrained(self.model_path)

    def generate(self, prompt: str, max_tokens: int = 100):
        inputs = self.tokenizer(prompt, return_tensors = "pt")
        outputs = self.model.generate(inputs["input_ids"], max_length=max_tokens)
        return self.tokenizer.decode(output[0], skip_special_tokens=True)