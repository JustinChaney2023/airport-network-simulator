# Will integrate at a future time
# metrics.py
from dataclasses import dataclass, field
import statistics, time
from typing import List

@dataclass
class Bench:
    start: float = field(default_factory=time.perf_counter)
    latencies: List[float] = field(default_factory=list)
    sent: int = 0
    recv: int = 0

    def mark_sent(self) -> None:
        self.sent += 1

    def mark_recv(self, since_send_seconds: float) -> None:
        self.recv += 1
        self.latencies.append(since_send_seconds)

    def report(self) -> str:
        dur = max(time.perf_counter() - self.start, 1e-6)
        tput = self.recv / dur
        if not self.latencies:
            return f"msgs={self.recv} throughput={tput:.1f}/s (no latency samples)"
        p50 = statistics.median(self.latencies)
        p95 = statistics.quantiles(self.latencies, n=20)[18]
        return (
            f"msgs={self.recv} throughput={tput:.1f}/s "
            f"p50={p50*1000:.1f}ms p95={p95*1000:.1f}ms"
        )
