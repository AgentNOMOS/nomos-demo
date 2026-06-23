# Security Policy

## Scope

This repository contains public-safe governance skills, schemas, examples and documentation.

It must never contain:

- passwords, API keys, private keys, seed phrases or tokens
- production credentials or authorization headers
- customer, employee or regulated personal data
- private server paths, infrastructure inventories or internal network topology
- live payment, wallet-signing, settlement or autonomous execution material
- unpublished policy rules or private evidence records

## Supported public capability

The current public capability is a read-only advisory governance preflight. It does not execute the proposed action and every valid result must preserve:

```json
{"not_executed": true}
```

## Reporting a vulnerability

Do not disclose exploitable details in a public issue.

Report suspected vulnerabilities through the security contact published on https://agentnomos.com or through GitHub private vulnerability reporting when enabled.

Include:

1. affected file or public endpoint
2. reproducible steps using synthetic data
3. expected and observed behavior
4. potential impact
5. suggested mitigation, if known

Do not test against third-party accounts, production wallets, private data or systems you are not authorized to access.

## Fail-closed rule

When identity, authority, scope, approval, evidence or policy status is missing or ambiguous, public AgentNOMOS examples must return `HOLD_FOR_REVIEW` or `BLOCK`, never silently default to approval.
