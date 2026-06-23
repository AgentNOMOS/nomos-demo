# Public Terms and Semantics

AgentNOMOS uses precise terms because governance claims can otherwise be misunderstood as authority or execution.

## Advisory decision

A public AgentNOMOS decision is a structured assessment of the supplied facts.

It is not:

- legal advice
- regulatory certification
- production authorization
- a wallet signature
- a payment instruction
- an execution command

## `ADVISORY_ALLOW`

The supplied facts describe a narrow, low-risk and sufficiently authorized action under the public decision contract.

It does not execute the action and does not override another approval or enforcement system.

## `HOLD_FOR_REVIEW`

Material authority, approval, scope, evidence or risk information is missing, ambiguous or consequential enough to require a separate review.

## `BLOCK`

The proposed action conflicts with an explicit policy or scope, attempts to bypass safeguards, exposes secrets, appears tampered with or is clearly unauthorized.

## Receipt

A receipt is a record associated with a request, decision or separately performed action.

A receipt can support later review, but it does not by itself prove that:

- the underlying source was factually correct
- the actor had authority
- the action was legally permissible
- an external system actually executed the action

## Receipt verification

Receipt verification checks the integrity, structure or supported provenance of supplied receipt material.

It does not authorize a new action and does not settle a payment.

## Signed

`Signed` may be used only when a specific artifact includes a verifiable cryptographic signature and the verification method is disclosed.

Do not describe every AgentNOMOS response as signed.

## Replayable

A decision is replayable only when the relevant input, policy/version context and decision material can be reconstructed or re-evaluated.

Replayability is not the same as autonomous re-execution.

## Evidence

Evidence is the material used to support, reconstruct or verify a decision. It can include identifiers, timestamps, policy versions, hashes, approvals and receipts.

Evidence quality is separate from risk severity.

## Approval

Approval means a separate, explicit and current authorization by an actor or control that has authority for the exact action and scope.

A model recommendation, payment, quote, receipt or previous approval is not automatically current approval.

## Execution

Execution means creating an external effect such as sending, paying, signing, publishing, deploying, deleting or mutating state.

Public AgentNOMOS skills and examples do not execute actions.

## Settlement

Settlement is a payment-state concept. It is not permission and does not authorize a consequential action.

## Public-safe invariant

Every public preflight result must preserve:

```json
{"not_executed": true}
```
