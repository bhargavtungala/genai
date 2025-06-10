from typing_extensions import TypedDict
from typing import Literal, Optional
from langgraph.graph import StateGraph, START, END

class CalcState(TypedDict):
    number1: float
    number2: float
    operator: Literal['+','-']
    result: Optional[float]

def add(state: CalcState) -> CalcState:
    '''
    add mode
    '''
    state['result']= state['number1'] + state['number2']
    return state

def sub(state: CalcState) ->CalcState:
    state['result']= state['number1'] - state['number2']
    return state


def my_router(state: CalcState) -> Literal['add','sub']:
    if state['operator']== '+':
        return 'add'
    else:
        return 'sub'
    




#add nodes
graph_builder = StateGraph(CalcState)
graph_builder.add_node('add', add)
graph_builder.add_node('sub',sub)

#add edges
graph_builder.add_conditional_edges(START, my_router)
graph_builder.add_edge('sub', END)
graph_builder.add_edge('add', END)

graph=graph_builder.compile()
