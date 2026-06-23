# Public Evidence Model

## Purpose

The public AgentNOMOS evidence model identifies what should be preserved so a governance decision can be reviewed or reconstructed later.

Evidence supports accountability. It does not automatically establish truth, legality, authority or execution.

## Evidence before action

For a consequential action, the pre-action record should contain only the minimum public-safe material required to establish:

- actor identity or role
- delegated authority reference
- exact proposed action and target
- environment and scope limits
- relevant policy or rule version
- risk result
- required human approval identity and timestamp, when applicable
- unresolved uncertainties
- input or request hash when a stable canonical form exists
- planned output, artifact or change hash when applicable
- rollback, interruption or recovery plan when applicable

## Evidence after action

The public skill does not execute actions. When a separate authorized system performs an action, its own post-action record may include:

- execution system identity
- execution timestamp
- outcome status
- affected target reference
- output or change hash
- receipt identifier
- interruption or rollback status
- error or exception class

A public preflight must not fabricate this post-action evidence.

## Receipt semantics

A receipt is a record associated with a request, decision or separately performed action.

A receipt does not independently prove:

- that the actor had authority
- that an external action actually occurred
- that source data was correct
- that the action was lawful or compliant
- that payment created permission

Receipt verification checks the supported integrity or structure of supplied receipt material. It does not authorize a new action.

## Integrity properties

Where hashes or signatures are used, the record should state:

- algorithm or verification method
- exact object that was hashed or signed
- canonicalization rules
- signer or issuer identifier
- verification result
- verification timestamp

The term `signed` must not be used unless a verifiable cryptographic signature is actually present.

## Replayability

A governance decision is replayable only when the relevant input, policy/version context and decision contract can be reconstructed.

Replayability means decision reconstruction or re-evaluation. It does not mean autonomous re-execution.

## Data minimization and redaction

Evidence must not unnecessarily contain:

- passwords, tokens, cookies or private keys
- complete personal or regulated records
- production credentials
- internal network topology
- customer data unrelated to the decision

Use stable identifiers, hashes and neutral placeholders instead of sensitive raw values whenever possible.

If a secret appears in a request, the public skill must not repeat it. It must mark `secret_exposure_detected: true` and return `BLOCK`.

## Missing or conflicting evidence

- Missing material evidence for a high-impact action requires `HOLD_FOR_REVIEW`.
- Apparently tampered actor or evidence material requires `BLOCK`.
- Unverifiable claims must remain explicitly uncertain.
- A model explanation is not a substitute for an approval record.

## Public boundary

This document defines a public-safe evidence vocabulary. It does not expose private evidence stores, signing keys, internal retention rules, production logs or customer records.
