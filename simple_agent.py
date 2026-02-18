class SimpleAgent:
    """
    A very basic rule-based agent.
    Replace this logic with LLM or LangChain agent if needed.
    """

    def act(self, question: str) -> str:
        question = question.lower()

        if "2+2" in question:
            return "4"
        elif "newton" in question:
            return "Newton is the father of classical mechanics."
        else:
            return "I don't know"