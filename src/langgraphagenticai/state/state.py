from typing import TypedDict, list, Annotated
from langgraph.graph.message import add_messages

class State(TypedDict):
    '''
    Represent the structure of the state used in graph
    '''
    messages: Annotated[list, add_messages]