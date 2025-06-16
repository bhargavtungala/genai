## Graphs, Node, Edges, and state in langgraph
*lets create a new folder and activate a virtual environment


Graphs, Node, Edges and State in Langgraph
Lets create a new folder and activate virtual environment
mkdir basic-graph
cd basic-graph
python -m venv .venv
# source .venv/bin/activate
.venv/Scripts/activate
Ensure pip install -U "langgraph-cli[inmem]" is executed
create a new file called as requirements.txt with langgraph in it
Now install pip install -r requirements.txt
Lets create a file called as

main.py
langgraph.json
Lets create a State in main.py

from typing_extensions import TypedDict

class State(TypedDict):
    message: str
Now we need nodes, nodes in the simplest form are python functions.
Langgraph has two built in nodes START and END to start and end the workflow
from typing_extensions import TypedDict
from langgraph.graph import START, END

class State(TypedDict):
    message: str

def node_1(state: State) -> State:
    """This is node 1
    """
    state['message'] += "node 1"

def node_2(state: State) -> State:
    """This is node 2
    """
    state['message'] += "node 1"

def node_3(state: State) -> State:
    """This is node 3
    """
    state['message'] += "node 1"


Node takes state as input and gives back state as output

Refer to the main.py code below

from typing_extensions import TypedDict
from langgraph.graph import START, END,StateGraph

class State(TypedDict):
    message: str

def node_1(state: State) -> State:
    """This is node 1
    """
    state['message'] += "node 1"
    return state

def node_2(state: State) -> State:
    """This is node 2
    """
    state['message'] += "node 2"
    return state

def node_3(state: State) -> State:
    """This is node 3
    """
    state['message'] += "node 3"
    return state


builder:StateGraph = StateGraph(State)

# add nodes
builder.add_node("node_1", node_1)
builder.add_node("node_2", node_2)
builder.add_node("node_3", node_3)

# add edges
builder.add_edge(START, "node_1")
builder.add_edge("node_1", "node_2")
builder.add_edge("node_2", "node_3")
builder.add_edge("node_3", END)

graph = builder.compile()

# graph.invoke()
langgraph.json
{
    "graphs": {
        "first": "./main.py:graph"


    },
    "dependencies":  ["."]

}
requirements.txt
langraph
langgraph-cli[inmem]
Run the code using langgraph dev