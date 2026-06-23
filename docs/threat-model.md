# Public Threat Model

## Scope

This threat model covers the public AgentNOMOS Governance Preflight skill, its schemas, synthetic examples and documentation.

The public kit is advisory and read-only. It does not include production enforcement, payment, wallet signing, deployment, deletion, messaging or other mutation paths.

## Protected properties

The public kit is designed to preserve these properties:

- no action execution by the skill
- no secret reproduction or exfiltration
- no invented identity, authority, approval, policy or evidence
- fail-closed handling of consequential uncertainty
- explicit separation between payment and permission
- internally consistent decision output
- `not_executed: true` for every result
- clear public/private capability boundaries

## Primary threats

### 1. Authority fabrication

An agent may infer permission from access, role membership, a previous approval or user intent that was never explicitly stated.

**Control:** Treat missing, inferred, stale or ambiguous authority as `HOLD_FOR_REVIEW`.

### 2. Scope laundering

A broad instruction may be reframed to cover a larger amount, target, environment, recipient set or tool capability.

**Control:** Compare the exact proposed action against explicit limits. Return `BLOCK` for scope violations.

### 3. Approval bypass

A request may ask the agent to ignore confirmation, policy or human-review requirements.

**Control:** Return `BLOCK` for attempted safeguard or approval bypass.

### 4. Secret exposure

Credentials or sensitive values may appear in the request or be requested for transmission.

**Control:** Do not repeat the value. Redact it, set `secret_exposure_detected: true` and return `BLOCK`.

### 5. Prompt injection and instruction conflict

Content inside a document, tool response or user-supplied payload may attempt to override the skill's hard boundary.

**Control:** Treat the governance skill boundary and platform policy as higher priority than embedded content. Do not call mutation tools.

### 6. Confused-deputy behavior

An agent with technical access may be induced to act for a party that lacks authority.

**Control:** Evaluate the proposing actor, authority source, target and scope separately. Technical capability is not authority.

### 7. Consequential action misclassification

A payment, deployment, outbound message, permission change or deletion may be described as harmless or reversible.

**Control:** Classify based on actual external effect and impact, not user labels.

### 8. Evidence tampering

Actor, approval or receipt material may be altered, incomplete or inconsistent.

**Control:** Return `BLOCK` when tampering appears likely. Otherwise hold unverifiable high-impact actions for review.

### 9. Receipt or signature overclaim

A receipt, hash or signature may be presented as proof of authority, compliance or external execution.

**Control:** Keep integrity, authority, legality and execution as separate claims. Use `signed` only for verifiable cryptographic signatures.

### 10. Payment-permission confusion

A successful quote, payment or settlement may be treated as authorization to act.

**Control:** Maintain the invariant: payment is not permission.

### 11. Stale policy or approval

An old approval or policy version may no longer apply.

**Control:** Require current, applicable authority and policy context. Stale evidence results in `HOLD_FOR_REVIEW`.

### 12. Output inconsistency

The explanatory text may conflict with the JSON decision, or an allow result may contain high-risk indicators.

**Control:** Enforce decision invariants in schemas and tests. `ADVISORY_ALLOW` requires verified authority, low risk, no secret exposure, no human review and `not_executed: true`.

### 13. Public/private boundary leakage

Documentation or examples may expose credentials, customer data, internal paths, production topology or unpublished controls.

**Control:** Repository policy, security review and integrity scans reject private operational material.

### 14. Supply-chain drift

The GitHub copy of a published skill may differ from the ClawHub artifact.

**Control:** Record and test the exact SHA-256, byte count and line count of the published `SKILL.md`.

## Out of scope

This public threat model does not claim to secure:

- private production infrastructure
- third-party agent runtimes
- downstream execution systems
- payment networks or wallets
- external policy sources
- user devices or credentials
- legal or regulatory compliance by itself

## Reporting

Do not publish exploit details or sensitive evidence in a public issue. Follow [`SECURITY.md`](../SECURITY.md).
