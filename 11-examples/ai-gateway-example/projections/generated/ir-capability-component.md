%% GENERATED FILE — do not edit by hand.
%% Source: ../../ir/architecture-ir.json
%% Generator: 11-examples/ai-gateway-example/generate_projections.py

# Capability / component projection (from Architecture IR)

```mermaid
flowchart TB
  E_CAP_0001["User Authentication"]
  E_CAP_0015["AI Request Routing"]
  E_CAP_0016["Provider Failover"]
  E_COMP_0003["Auth Service"]
  E_COMP_0010["AI Gateway Lambda"]
  E_IFACE_0012["AI Gateway REST API"]
  E_COMP_0010 -->|"implements"| E_CAP_0015
  E_COMP_0010 -->|"implements"| E_CAP_0016
  E_CAP_0015 -->|"depends on"| E_CAP_0001
  E_COMP_0010 -->|"depends on"| E_COMP_0003
  E_COMP_0010 -->|"exposes"| E_IFACE_0012
```
