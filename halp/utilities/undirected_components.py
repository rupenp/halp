"""
.. module:: undirected_components
   :synopsis: Provides various methods for finding connected components in 
            an undirected hypergraph.
"""
import numpy as np
from scipy import sparse

from halp.undirected_hypergraph import UndirectedHypergraph


def connected_components(H):
    """Extracted all components in the hypergraph.

    :param H: the hypergraph to find the node mapping on.
    :returns: list -- of all components, each component containing list of
                      vertices that belong to the component.

    """
    components = []
    nodes = H.get_node_set()
    while nodes:
        n = nodes.pop()
        group = {n}
        queue = [n]
        while queue:
            n = queue.pop(0)
            neighbors = set()
            for e in H.get_star(n):
                neighbors.update(H.get_hyperedge_nodes(e))
            neighbors.difference_update(group)
            nodes.difference_update(neighbors)
            group.update(neighbors)
            queue.extend(neighbors)
        components.append(group)
    return components
