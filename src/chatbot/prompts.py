from langchain.prompts import PromptTemplate

class GPTgPrompt():
    def __init__(self):
        self.prompt = PromptTemplate(
                                input_variables=[""],
                                template="What is a good name for a company that makes {product}?",
                                )