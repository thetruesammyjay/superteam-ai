from llm.local_llm import LocalLLM

class ContentAdvisor:
    def __init__(self):
        self.llm = LocalLLM()

    def refine_content(self, draft: str):
        
        refined_content = self.llm.generate(f"Refine this content: {draft}", max_tokens=100)
        return refined_content
    
    def suggest_keywords(self, text: str):
        keywords = self.llm.generate(f"Suggest keywords for: {text}", max_tokens=20)
        return keywords.split(",")