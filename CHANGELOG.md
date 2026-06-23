# Changelog

All notable public changes to the AgentNOMOS Governance Kit will be documented here.

The repository does not yet have a tagged GitHub release.

## Unreleased

### Added

- Exact published OpenClaw skill `agentnomos-governance-preflight` v1.0.0
- Artifact manifest with verified SHA-256, byte count and line count
- Request and result JSON Schemas
- Synthetic examples for advisory allow, human-review hold and secret-exposure block
- Public decision, authority, evidence, terminology, capability and threat models
- Security and contribution policies
- Contract and repository-integrity tests
- GitHub Actions workflow for public tests
- Repository-wide MIT-0 license

### Changed

- Replaced the README-only demo positioning with the AgentNOMOS Governance Kit
- Corrected the installation flow to the official `clawhub install @owner/slug` CLI form
- Clarified that public capabilities are advisory and read-only
- Defined payment, settlement, receipts, signatures, replayability, approval and execution separately

### Security

- Preserved `not_executed: true` as a public invariant
- Added automated verification of the published skill artifact
- Added high-confidence secret-marker checks for public files

## ClawHub skill 1.0.0 — 2026-06-23

- Published `agentnomos-governance-preflight`
- License: MIT-0
- SHA-256: `fb42f45dd1994c1ae62bc543cc2227c552074c2681a51f75980b1815942b430e`
- Mode: advisory and read-only
- Execution: disabled
