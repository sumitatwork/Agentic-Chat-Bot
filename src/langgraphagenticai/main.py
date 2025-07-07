import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMs.groqllm import GroqLLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit

def load_langraph_agentic_app():
    '''
    Loads and runs the LangGraph Agentic AI application with Streamlit UI.
    This function initializes the UI, handles user input, configures the LLm model,
    sets up the graph based on the selected use case, and siplays the output while
    implementing exception handling for robustness.
    '''
    
    ## Load UI
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input from the UI")
        return
    
    user_message = st.chat_input("Enter your message: ")

    if user_message:
        try:
            ## Configure LLM
            obj_llm_config = GroqLLM(user_controls_input=user_input)
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("Error: LLM model could not be initialized")
                return

            ## Initialize and setup the graph on use case
            usecase = user_input.get("selected_usecase")
            if not usecase:
                return

            ## Graph builder
            graph_builder = GraphBuilder(model=model)
            try:
                graph = graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase=usecase,graph=graph, user_message=user_message).display_result_on_ui()

            except Exception as e:
                st.error(f"Errorddd: Graph setup failed: {e}")
        except Exception as e:
            st.error(f'Errorsss: Graph setup failed: {e}')
            return


    # if user_message:
    #     try:
    #         ## Configure LLM
    #         obj_llm_config = GroqLLM(user_controls_input = user_input)
    #         model = obj_llm_config.get_llm_model()

    #         if not model:
    #             st.error("Error: LLM model could not be initialized")
    #             return
            
    #         ## Initialize and set up graph based on use case
    #         usecase = user_input.get('selected_usecase')
    #         if not usecase:
    #             st.error("Error: No use case selected")
    #             return