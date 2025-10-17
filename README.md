# Airport Network Simulator (TCP)
![Python](https://img.shields.io/badge/python-3.13+-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

Simulates a hub-and-spoke airline network over **TCP sockets**. A **Scheduler** assigns routes; **Airport** nodes act as both servers and clients exchanging structured "flight" messages.

- **Why:** teaching tool for networks (routers/links/IXP analogy)
- **What:** multi-node messaging, retry/backoff, structured logging, config-driven topology
- **Outputs:** throughput (msgs/s), all routes in logs, delivery Success

## Quick start (60 seconds)

```bash
# Tested on python 3.13.9
python -m src.main

                 [Scheduler]
                     |
            +---------+---------+
            |                   |
[BET]---[ANC]---[SEA]      [SEA]---[JNU]
            |                   | 
        [FAI]              [FAI]

{ "src":"ANC", "dst":"SEA", "payload":"Passenger Name" or "Cargo" }
 ```

## Architecture Overview

- **Scheduler**: central controller that reads a YAML topology and randomly dispatches flight messages.
- **Airport Node**: acts as both TCP server and client; handles incoming connections, forwards messages based on routing table, logs arrivals.
- **Message Schema**: JSON or YAML packets with `src`, `dst`, `payload`, and optional `ttl` + `ts` timestamps.
- **Config File**: defines airports, routes, and scheduler frequency (flights/minute).
- **Logging**: structured text logs of all deliveries; aggregated by scheduler for throughput metrics.

###### first/last-name JSONs sourced from: 
https://github.com/terryweiss/ink-collector/tree/master/tests/nottests
