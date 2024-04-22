import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class GraphSimulator:
    def __init__(self):
        self.graph = nx.Graph()
        self.root = tk.Tk()
        self.root.title("Graph Simulator")
        self.figure = plt.figure()
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.ax = self.figure.add_subplot(111)
        self.ax.set_axis_off()
        self.canvas.draw()
        
    def add_node(self, node):
        if node == '':
            self.show_message("Invalid Node")
        else:
            self.graph.add_node(node)
            self.draw_graph()
        
    def remove_node(self, node):
        if node in self.graph:
            self.graph.remove_node(node)
            self.draw_graph()
        else:
            self.show_message("Node not found.")
        
    def add_edge(self, node1, node2, weight):
        try:
            weight = float(weight)
            self.graph.add_edge(node1, node2, weight=weight)
            self.draw_graph()
        except ValueError:
            self.show_message("Invalid weight. Please enter a number.")
        
    def remove_edge(self, node1, node2):
        if self.graph.has_edge(node1, node2):
            self.graph.remove_edge(node1, node2)
            self.draw_graph()
        else:
            self.show_message("Edge not found.")
        
    def draw_graph(self):
        self.ax.clear()
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, ax=self.ax)
        labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels, ax=self.ax)
        self.canvas.draw()
        
    def show_message(self, message):
        messagebox.showinfo("Message", message)

def main():
    graph_simulator = GraphSimulator()
    
    node_label = tk.Label(graph_simulator.root, text="Add or remove node:")
    node_label.pack()
    
    node_entry = tk.Entry(graph_simulator.root)
    node_entry.pack()
    node_entry.focus_set()
    
    edge_label = tk.Label(graph_simulator.root, text="Add or remove edge between nodes:")
    edge_label.pack()
    
    node1_edge_entry = tk.Entry(graph_simulator.root)
    node1_edge_entry.pack()
    
    node2_edge_entry = tk.Entry(graph_simulator.root)
    node2_edge_entry.pack()
    
    weight_label = tk.Label(graph_simulator.root, text="Edge weight:")
    weight_label.pack()
    
    weight_entry = tk.Entry(graph_simulator.root)
    weight_entry.pack()
    
    add_node_button = tk.Button(graph_simulator.root, text="Add Node", command=lambda: graph_simulator.add_node(node_entry.get()))
    add_node_button.pack()
    
    remove_node_button = tk.Button(graph_simulator.root, text="Remove Node", command=lambda: graph_simulator.remove_node(node_entry.get()))
    remove_node_button.pack()
    
    add_edge_button = tk.Button(graph_simulator.root, text="Add Edge", command=lambda: graph_simulator.add_edge(node1_edge_entry.get(), node2_edge_entry.get(), weight_entry.get()))
    add_edge_button.pack()
    
    remove_edge_button = tk.Button(graph_simulator.root, text="Remove Edge", command=lambda: graph_simulator.remove_edge(node1_edge_entry.get(), node2_edge_entry.get()))
    remove_edge_button.pack()
    
    graph_simulator.root.mainloop()

if __name__ == "__main__":
    main()
