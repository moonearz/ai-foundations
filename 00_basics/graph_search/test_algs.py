import networkx as nx
import pytest

from algs import depth_first_search, breadth_first_search, branch_and_bound


search_algorithms = [
    depth_first_search,
    breadth_first_search,
    branch_and_bound
]


@pytest.mark.parametrize("search", search_algorithms)
def test_direct_edge(search):
    graph = nx.Graph()
    graph.add_edge("A", "B")

    path = search(graph, "A", "B")

    assert path == ["A", "B"]


@pytest.mark.parametrize("search", search_algorithms)
def test_simple_path(search):
    graph = nx.Graph()
    graph.add_edges_from([
        ("A", "B"),
        ("B", "C"),
        ("C", "D"),
    ])

    path = search(graph, "A", "D")

    assert path[0] == "A"
    assert path[-1] == "D"
    assert is_valid_path(graph, path)


@pytest.mark.parametrize("search", search_algorithms)
def test_branching_graph(search):
    graph = nx.Graph()
    graph.add_edges_from([
        ("A", "B"),
        ("A", "C"),
        ("B", "D"),
        ("C", "E"),
        ("D", "F"),
        ("E", "F"),
    ])

    path = search(graph, "A", "F")

    assert path[0] == "A"
    assert path[-1] == "F"
    assert is_valid_path(graph, path)


@pytest.mark.parametrize("search", search_algorithms)
def test_no_path(search):
    graph = nx.Graph()
    graph.add_edges_from([
        ("A", "B"),
        ("C", "D"),
    ])

    path = search(graph, "A", "D")

    assert path is None


@pytest.mark.parametrize("search", search_algorithms)
def test_start_equals_goal(search):
    graph = nx.Graph()
    graph.add_edges_from([
        ("A", "B"),
        ("B", "C"),
    ])

    path = search(graph, "A", "A")

    assert path == ["A"]


@pytest.mark.parametrize("search", search_algorithms)
def test_empty_graph(search):
    graph = nx.Graph()

    path = search(graph, "A", "B")

    assert path is None


@pytest.mark.parametrize("search", search_algorithms)
def test_cycle(search):
    graph = nx.Graph()
    graph.add_edges_from([
        ("A", "B"),
        ("B", "C"),
        ("C", "A"),
    ])

    path = search(graph, "A", "C")

    assert path[0] == "A"
    assert path[-1] == "C"
    assert is_valid_path(graph, path)


def is_valid_path(graph: nx.Graph, path: list) -> bool:
    return all(
        graph.has_edge(path[i], path[i + 1])
        for i in range(len(path) - 1)
    )