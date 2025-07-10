from src.langgraphagenticai.state.state import State

class ChatBotWithToolNode:
    '''
    Chatbot logic enhanced with tool integration
    '''
    def __init__(self, model):
        self.llm = model

    def process(self, state: State) -> dict:
        '''
        Processes the input state and generates a response with tool integration.
        '''
        user_input = state['messages'][-1] if state['messages'] else ""
        llm_response = self.llm.invoke([{'role': 'user', 'content': user_input}])

        ## Simulate tool-specific logic
        tools_response = f"Tool integration for: '{user_input}'"

        return {"messages": [llm_response, tools_response]}