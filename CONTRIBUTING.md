# Contributing

Contributions are welcome when they improve the public-safe AgentNOMOS governance kit without exposing private infrastructure or weakening fail-closed behavior.

## Suitable contributions

- synthetic governance examples
- JSON Schema improvements
- documentation clarifications
- test cases for authority, scope, risk and evidence handling
- adapters for public agent harnesses that remain read-only by default
- accessibility and developer-experience improvements

## Not suitable for this repository

- credentials, keys, tokens or secrets
- private server paths or production topology
- customer or regulated personal data
- live wallet, signing, settlement or payment material
- autonomous execution code
- instructions that bypass platform policy or human approval
- unsupported claims about legal or regulatory compliance

## Pull-request requirements

A pull request should include:

1. a concise problem statement
2. public-safe test or example data
3. expected decision behavior
4. confirmation that `not_executed` remains `true`
5. confirmation that no secret or private production detail is included

Changes that broaden execution capability require a separate security review and are out of scope for the initial public kit.
