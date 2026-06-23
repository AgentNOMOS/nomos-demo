# AgentNOMOS Public Decision Model

## Purpose

The public decision model evaluates a proposed AI-agent action before execution. It is intentionally narrower than any private production system.

The public model returns one of three advisory states:

- `ADVISORY_ALLOW`
- `HOLD_FOR_REVIEW`
- `BLOCK`

Every result must state:

```json
{"not_executed": true}
```

## Evaluation order

1. **Identity** — Is the actor clearly identified?
2. **Authority** — Is there explicit, current authority for the exact action and target?
3. **Scope** — Are amount, environment, tools, records, recipients and duration bounded?
4. **Risk** — What financial, privacy, security, operational, legal or reputational harm can occur?
5. **Human review** — Does the action require a separate human decision?
6. **Evidence readiness** — Can the decision and any later execution be reconstructed?

## ADVISORY_ALLOW

Use only when all supplied facts establish a low-risk, bounded, reversible or non-consequential action with explicit authority and no need for human review.

This is not execution authorization.

## HOLD_FOR_REVIEW

Use when material facts, authority, approval, evidence or boundaries are missing or ambiguous, or when the action could create a consequential external effect.

Typical hold cases include:

- payments or value transfer
- production deployment or restart
- publication or outbound communication
- permission or account changes
- use of personal, confidential or regulated data
- destructive or difficult-to-reverse changes

## BLOCK

Use when the request conflicts with explicit policy or scope, attempts to bypass safeguards, exposes secrets, appears tampered with, or requests unauthorized harmful action.

## Fail-closed invariants

- Unknown authority is not verified authority.
- Unknown high-impact risk is not low risk.
- General access is not specific permission.
- A previous approval is not automatically current approval.
- A model explanation is not evidence of authorization.
- A preflight result never performs the proposed action.

## Public/private boundary

This document describes only the public-safe contract. It must not be interpreted as a full description of private infrastructure, enforcement logic, policy sources or production execution controls.
