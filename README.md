# AgentNOMOS Governance Kit

> Public-safe examples, schemas and installable skills for governance before consequential AI-agent actions.

AgentNOMOS evaluates whether a proposed agent action is sufficiently identified, authorized, scoped, reviewable and evidenced **before execution**.

This repository is the public implementation and demonstration layer. It does not expose private production infrastructure, secrets, customer data, payment credentials or autonomous execution paths.

## Current status

- OpenClaw skill: `agentnomos-governance-preflight` v1.0.0
- Mode: read-only and advisory
- Decisions: `ADVISORY_ALLOW`, `HOLD_FOR_REVIEW`, `BLOCK`
- Execution: never performed by the public skill
- Published skill SHA-256: `fb42f45dd1994c1ae62bc543cc2227c552074c2681a51f75980b1815942b430e`
- ClawHub security audit: passed

## Install from ClawHub

Install the official ClawHub CLI:

```bash
npm i -g clawhub
```

Then install the skill in your agent workspace:

```bash
clawhub install @agentnomos/agentnomos-governance-preflight
```

The official ClawHub CLI uses the `clawhub install @owner/slug` form. The installed skill remains advisory and does not execute actions.

## What this repository contains

```text
skills/       Installable public agent skills and artifact manifests
schemas/      Machine-readable request and result contracts
examples/     Synthetic governance scenarios and expected outputs
docs/         Capability, decision, authority, evidence, terminology and threat models
tests/        Public-safe deterministic contract and repository-integrity cases
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
  "declared_authority": null,
  "scope": {
    "amount": {"currency": "EUR", "value": 4200},
    "environment": "production"
  },
  "environment": "production",
  "external_effect": true,
  "reversibility": "partially_reversible",
  "financial_effect": "value_transfer",
  "data_sensitivity": "internal"
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

## Documentation

- [`docs/public-capability-truth.md`](docs/public-capability-truth.md)
- [`docs/decision-model.md`](docs/decision-model.md)
- [`docs/authority-model.md`](docs/authority-model.md)
- [`docs/evidence-model.md`](docs/evidence-model.md)
- [`docs/public-terms.md`](docs/public-terms.md)
- [`docs/threat-model.md`](docs/threat-model.md)

## Public surfaces

- Website: https://agentnomos.com
- ClawHub: https://clawhub.ai/AgentNOMOS/agentnomos-governance-preflight
- GitHub profile: https://github.com/AgentNOMOS

## Repository policy

Only synthetic, public or explicitly approved material belongs here. Server paths, internal service names, credentials, private datasets, production topology and unpublished controls must remain outside the repository.

## License

The OpenClaw skill published through ClawHub is distributed under MIT-0. Repository-wide licensing will be finalized before the first tagged GitHub release.
