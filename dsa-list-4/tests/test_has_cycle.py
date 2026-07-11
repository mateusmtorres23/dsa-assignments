import pytest

from challenges.has_cycle import has_cycle

from data_structures.graph_examples import (
    GRAPH_WITHOUT_CYCLE,
    GRAPH_WITH_CYCLE,
    GRAPH_WITH_SELF_LOOP,
    DISCONNECTED_GRAPH,
    DISCONNECTED_GRAPH_WITH_CYCLE,
)


@pytest.mark.parametrize(
    "graph, expected",
    [
        pytest.param(
            GRAPH_WITHOUT_CYCLE,
            False,
            id="simple-acyclic-graph",
        ),
        pytest.param(
            GRAPH_WITH_CYCLE,
            True,
            id="simple-cycle",
        ),
        pytest.param(
            GRAPH_WITH_SELF_LOOP,
            True,
            id="self-loop",
        ),
        pytest.param(
            DISCONNECTED_GRAPH,
            False,
            id="disconnected-without-cycle",
        ),
        pytest.param(
            DISCONNECTED_GRAPH_WITH_CYCLE,
            True,
            id="disconnected-with-cycle",
        ),
        pytest.param(
            {},
            False,
            id="empty-graph",
        ),
    ],
)
def test_has_cycle(graph, expected):

    result = has_cycle(graph)

    assert result is expected


def test_single_vertex_without_edges():

    graph = {
        "A": [],
    }

    assert has_cycle(graph) is False


def test_two_vertices_without_cycle():

    graph = {
        "A": ["B"],
        "B": [],
    }

    assert has_cycle(graph) is False


def test_two_vertices_with_cycle():

    graph = {
        "A": ["B"],
        "B": ["A"],
    }

    assert has_cycle(graph) is True


def test_longer_cycle():

    graph = {
        "A": ["B"],
        "B": ["C"],
        "C": ["D"],
        "D": ["A"],
    }

    assert has_cycle(graph) is True


def test_cycle_not_reachable_from_first_node():

    graph = {
        "A": ["B"],
        "B": [],
        "C": ["D"],
        "D": ["E"],
        "E": ["C"],
    }

    assert has_cycle(graph) is True


def test_preserves_graph():

    graph = {
        "A": ["B"],
        "B": ["C"],
        "C": [],
    }

    original = {
        node: neighbors.copy()
        for node, neighbors in graph.items()
    }

    has_cycle(graph)

    assert graph == original
