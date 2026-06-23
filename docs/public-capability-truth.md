# Public Capability Truth

Last verified: 2026-06-23

This document describes the public AgentNOMOS capability boundary verified by the read-only public-export audit.

## Public operating mode

AgentNOMOS public governance capabilities are **advisory and read-only**.

The following public execution flags are false:

```json
{
  "public_chat_live_execution": false,
  "wallet_signing": false,
  "settlement_authorizes_execution": false,
  "phase8_authorized": false
}
```

A public preflight result evaluates the supplied action context. It does not execute the action and does not grant production authority.

## Public MCP capability families

The published NOMOS MCP surface currently exposes five advisory capability families:

1. governance preflight
2. scan
3. discovery
4. x402 quote
5. receipt verification

These are not payment or execution tools.

An x402 quote describes a possible payment requirement. It does not transfer value.

Receipt verification checks supplied evidence or receipt material. It does not authorize execution.

## Payment and execution boundary

> Payment is not permission.

A payment, quote, settlement result or receipt must never be interpreted as authority to perform a consequential action.

Execution requires a separate, explicit authority and enforcement path that is not publicly enabled by this kit.

## Capability matrix

| Capability | Public live | Advisory/read-only | Executes action | Notes |
|---|---:|---:|---:|---|
| Governance preflight | Yes | Yes | No | Returns an advisory decision |
| Scan | Yes | Yes | No | Public-safe analysis only |
| Discovery | Yes | Yes | No | Finds available capabilities |
| x402 quote | Yes | Yes | No | Quote only; no payment |
| Receipt verification | Yes | Yes | No | Verification only |
| Wallet signing | No | No | No | Not publicly enabled |
| Payment settlement as authority | No | No | No | Settlement is not permission |
| Autonomous execution | No | No | No | Not publicly enabled |
| Phase 8 execution | No | No | No | Not authorized |

## Public knowledge interface

The public AgentNOMOS entity currently uses:

- 175 public RAG cards: 155 core cards plus 20 persona/industry cards
- supported languages: English, German, Spanish, Chinese and Turkish
- a public safe-answer filter
- codename redaction for public output
- demo/projection mode with no public live execution

Counts can change as public packs are revised. Claims should include a verification date or reference a live machine-readable source when one exists.

## External discovery

The ToolOracle-hosted NOMOS MCP endpoint is an external and optional discovery surface. The AgentNOMOS Governance Kit has no hard dependency on ToolOracle.

The correct NOMOS endpoint is:

```text
https://tooloracle.io/mcp/nomos
```

Do not use the generic `/mcp` route as the NOMOS endpoint.

## Source of truth

This document is based on the read-only public-export audit sealed on 2026-06-23:

```text
Report SHA-256:
68a1ff9ba8ddae083772e0831df694b727e37009184118b51e908b71b3d4afc3
```

The private server report path is intentionally not part of the public repository.
