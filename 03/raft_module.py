"""Small Raft leader-election simulation for Praktikum Modul 3."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class RaftNode:
    node_id: int
    term: int = 0
    role: str = "FOLLOWER"
    log: list[str] = field(default_factory=list)


class RaftCluster:
    def __init__(self, node_ids: list[int]) -> None:
        if not node_ids:
            raise ValueError("cluster requires at least one node")
        self.nodes = [RaftNode(node_id) for node_id in node_ids]
        self.leader: RaftNode | None = None

    def elect_leader(self, candidate_id: int) -> RaftNode:
        candidate = next(node for node in self.nodes if node.node_id == candidate_id)
        term = max(node.term for node in self.nodes) + 1
        for node in self.nodes:
            node.term = term
            node.role = "FOLLOWER"
        candidate.role = "LEADER"
        self.leader = candidate
        return candidate

    def append(self, entry: str) -> None:
        if self.leader is None:
            raise RuntimeError("elect a leader first")
        self.leader.log.append(entry)


if __name__ == "__main__":
    cluster = RaftCluster([1, 2, 3])
    leader = cluster.elect_leader(2)
    cluster.append("command-1")
    print(f"Node {leader.node_id} elected leader in term {leader.term}")
    print(leader.log)
    assert leader.role == "LEADER"
