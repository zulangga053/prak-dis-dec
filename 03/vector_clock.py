"""Reusable vector-clock implementation for Praktikum Modul 3."""

from __future__ import annotations


class VectorClock:
    def __init__(self, num_processes: int, process_id: int) -> None:
        if num_processes < 1 or not 0 <= process_id < num_processes:
            raise ValueError("process_id must be within the process count")
        self.clocks = [0] * num_processes
        self.process_id = process_id

    def increment(self) -> None:
        self.clocks[self.process_id] += 1

    def send(self) -> list[int]:
        self.increment()
        return self.clocks.copy()

    def receive(self, message: list[int]) -> None:
        if len(message) != len(self.clocks):
            raise ValueError("message size must match the vector size")
        self.clocks = [
            max(local, remote) for local, remote in zip(self.clocks, message)
        ]
        self.increment()

    def happens_before(self, other: "VectorClock") -> bool:
        return (
            self.clocks != other.clocks
            and all(local <= remote for local, remote in zip(self.clocks, other.clocks))
            and any(local < remote for local, remote in zip(self.clocks, other.clocks))
        )

    def concurrent_with(self, other: "VectorClock") -> bool:
        return not self.happens_before(other) and not other.happens_before(self)

    def __repr__(self) -> str:
        return f"P{self.process_id}: {self.clocks}"


if __name__ == "__main__":
    p0, p1 = VectorClock(2, 0), VectorClock(2, 1)
    p0.increment()
    p1.receive(p0.send())
    print(p0, p1)
    assert p0.happens_before(p1)
