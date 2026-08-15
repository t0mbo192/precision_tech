---
category: tool-building
summary: Read-only audit of Windows hardening settings.
---

# win-audit — Read-Only Windows Hardening Audit

A PowerShell audit that checks the Windows settings which actually get exploited when they are missing, scores the result, and writes both a JSON file and a self-contained HTML report. It reads state and changes nothing — a guarantee enforced by a test, not just a promise in the README.

> Most "is this machine safe" questions come down to a short list of settings that are either right or wrong.

## Overview

Answering whether a Windows host is hardened means checking firewall profiles, BitLocker, SMB signing, local administrators, patch level, RDP exposure and PowerShell logging. Every one of those lives in a different console, and checking them by hand is slow enough that it quietly stops happening.

win-audit answers the whole list in one command, shows the evidence behind each result, and gives the specific remediation for anything it flags. It has no dependencies outside a stock Windows install.

```
win-audit 1.2.0 · WORKSTATION-01 · Windows 11 Pro 25H2 (26200.8875)
Not elevated - BitLocker and optional-feature checks will report Error.
[Firewall]
Pass    FW-001     Firewall enabled on all network profiles
Warn    FW-002     Default inbound action is Block
[SMB]
Fail    SMB-001    SMBv1 server protocol is disabled
Fail    SMB-004    SMB server requires message signing
Score 57.5/100 (grade F)   Pass 8  Warn 8  Fail 6  Error 6
```

## Read-only, and provably so

An audit tool runs with high privilege on machines people care about. "It only reads" is exactly the kind of claim that decays as a codebase grows and someone adds a convenient auto-fix.

So the constraint is enforced mechanically. A test parses the check code with the PowerShell abstract syntax tree and fails the build if a state-changing cmdlet ever appears in it. The same assertion runs against the payload sent to remote hosts. The guarantee is a property of the build, not of anyone's discipline during review.

## Reporting

Each check carries a stable identifier — `FW-001`, `SMB-004` — so results stay comparable across runs and across machines. Findings are graded Pass, Warn, Fail or Error, with Error reserved for checks that could not run rather than checks that failed. A run without administrator rights reports Error for BitLocker instead of silently reporting a pass.

Output goes to two places: JSON for anything that needs to consume the results, and a self-contained HTML report for reading and sharing.

## What it demonstrates

- Practical Windows hardening knowledge across firewall, SMB, encryption, accounts, patching and logging
- Enforcing a safety property with AST analysis in CI instead of trusting convention
- Distinguishing "this check failed" from "this check could not run" — an honest scoring model
- Producing output for both machines and people from one run
- Dependency-free PowerShell that runs on a stock Windows host, locally or remotely

_Source repository is currently private; happy to walk through the code on request._

[Back to projects](/#projects)
