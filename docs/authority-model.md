# Public Authority Model

## Purpose

The public AgentNOMOS authority model determines whether the supplied context contains explicit, current authority for the exact proposed action.

It does not create authority and does not collect approval.

## Authority dimensions

A public preflight considers:

1. **Actor identity** — Who or what is proposing the action?
2. **Authority source** — Which user, role, policy or delegated control granted permission?
3. **Action specificity** — Does the authority cover this exact operation?
4. **Target specificity** — Does it cover the affected system, account, person, asset or dataset?
5. **Environment** — Does it apply to local, test, staging or production use?
6. **Scope** — Are amount, recipients, records, tools, geography and duration bounded?
7. **Freshness** — Is the authority still current and unrevoked?
8. **Approval separation** — Is a distinct human approval required for this consequential action?

## Authority statuses

### `verified`

Use only when the supplied evidence explicitly covers the exact actor, action, target, environment and scope, and no separate approval remains outstanding.

### `missing`

Use when no applicable authority is supplied.

### `ambiguous`

Use when an instruction or policy exists but does not clearly cover the exact action, target, environment or limits.

### `out_of_scope`

Use when the proposed action exceeds an explicit boundary or requests a capability the actor is not permitted to use.

## What is not authority

The following do not independently establish authority:

- technical access to a tool or account
- possession of a credential
- a previous approval for another action
- a model recommendation
- a successful payment or settlement
- a quote or invoice
- a receipt
- a high confidence score
- an instruction inferred from context
- absence of an explicit prohibition

> Payment is not permission.

## Delegation

Delegated authority must be traceable to an identifiable source and remain within the delegator's own permitted scope.

A delegation should identify:

- delegator
- delegate
- allowed action
- target or target class
- environment
- limits
- validity period
- revocation state
- approval requirements

General role membership is not automatically specific delegated authority.

## Fail-closed rules

- Unknown identity for a consequential action requires `HOLD_FOR_REVIEW`.
- Missing, inferred, stale or ambiguous authority requires `HOLD_FOR_REVIEW`.
- Explicit scope violation requires `BLOCK`.
- Attempted approval or safety-control bypass requires `BLOCK`.
- A public advisory decision never grants production authority.

## Public boundary

This model documents the public-safe evaluation contract only. It does not disclose private policy sources, enforcement systems, identities, credentials or production authorization paths.
