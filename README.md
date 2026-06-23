# AgentNOMOS Governance Kit

> Public-safe examples, schemas and installable skills for governance before consequential AI-agent actions.

AgentNOMOS evaluates whether a proposed agent action is sufficiently identified, authorized, scoped, reviewable and evidenced **before execution**.

This repository is the public implementation and demonstration layer. It does not expose private production infrastructure, secrets, customer data, payment credentials or autonomous execution paths.

## Current status

- OpenClaw skill: `agentnomos-governance-preflight` v1.0.0
- Mode: read-only and advisory
- Decisions: `ADVISORY_ALLOW`, `HOLD_FOR_REVIEW`, `BLOCK`
- Execution: never performed by the public skill
- ClawHub security audit: passed

Install from ClawHub:

```bash
openclaw skills install @agentnomos/agentnomos-governance-preflight
```

## What this repository contains

```text
skills/       Installable public agent skills
schemas/      Machine-readable request and result contracts
examples/     Synthetic governance scenarios and outputs
docs/         Decision, authority, evidence and threat models
tests/        Public-safe deterministic contract cases
```

## Core decision flow

```text
Proposed action
      |
      v
Identity -> Authority -> Scope -> Risk -> Human review -> Evidence readiness
      |
      v
ADVISORY_ALLOW | HOLD_FOR_REVIEW | BLOCK
      |
      v
not_executed: true
```

`ADVISORY_ALLOW` is not production authorization. It only means the supplied facts satisfy the narrow public preflight contract.

## Example

Input:

```json
{
  "actor": "invoice-agent",
  "action": "approve payment",
  "target": "invoice-4821",
  "environment": "production",
  "amount": {"currency": "EUR", "value": 4200},
  "declared_authority": null
}
```

Expected decision:

```json
{
  "system": "AgentNOMOS Governance Preflight",
  "decision": "HOLD_FOR_REVIEW",
  "authority_status": "missing",
  "risk_level": "high",
  "human_review_required": true,
  "not_executed": true
}
```

## Safety boundary

The public kit must not:

- execute payments, deployments, deletions or outbound messages
- sign wallet or blockchain transactions
- request, store or reveal secrets
- bypass human approval or platform policy
- represent an advisory preflight as legal approval
- claim private production capabilities are publicly available

See [`SECURITY.md`](SECURITY.md) for reporting and disclosure guidance.

## Public surfaces

- Website: https://agentnomos.com
- ClawHub: https://clawhub.ai/AgentNOMOS/agentnomos-governance-preflight
- GitHub profile: https://github.com/AgentNOMOS

## Repository policy

Only synthetic, public or explicitly approved material belongs here. Server paths, internal service names, credentials, private datasets, production topology and unpublished controls must remain outside the repository.

## License

The OpenClaw skill published through ClawHub is distributed under MIT-0. Repository-wide licensing will be finalized before the first tagged GitHub release.
