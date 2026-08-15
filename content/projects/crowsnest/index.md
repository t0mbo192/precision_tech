---
category: tool-building
summary: Reports which hosts a machine is talking to.
---

# crowsnest — Seeing What a Machine Talks To

A terminal tool that answers one question about network traffic: what is this machine talking to, and what is talking to it? It reads the same packets Wireshark does and reports each host once, in plain language, then stays quiet.

> Wireshark tells you everything. crowsnest tells you who.

## Overview

Packet capture gives you everything and, in doing so, gives you nothing you can act on quickly. Open Wireshark on a busy interface and you get thousands of rows of frames when the actual question is much smaller: which hosts has this machine contacted, and which ones reached in from outside?

crowsnest sits on that question alone. It reads live traffic through `tshark`, resolves each host to a name and the organisation behind it, and prints one line the first time a host appears. No repeats, no per-packet noise.

```
crowsnest live · eth0 · this machine 192.168.1.120
each host is reported once, when first seen. Ctrl-C for a summary.
08:22:13  ↑  github.com                     GitHub - code hosting
08:22:13  ↑  ord37s57-in-f10.1e100.net      Google infrastructure
08:22:13  ↑  browser-intake-datadoghq.com   Datadog - monitoring / telemetry
08:22:14  ↑  20.42.65.92                    Microsoft Corporation
08:22:19  ↓  laptop.lan                     Local network device
08:22:24  ↓  203.0.113.5                    DigitalOcean, LLC
```

The direction marker carries most of the value. `↑` means this machine opened the connection; `↓` means something else opened it. On a quiet host, an unexpected `↓` is the line worth reading twice.

## Naming the other end

An address like `20.42.65.92` has no reverse DNS name, which makes it useless at a glance. crowsnest resolves ownership from an ASN database, fetched once with `crowsnest asn --fetch`, so that address renders as "Microsoft Corporation" instead. Turning anonymous numbers into recognisable organisations is what makes a scrolling list scannable.

For a framed view instead of a stream, `--dashboard` gives live transfer rates and a search box over the same data.

## Being honest about the limits

Almost all traffic is encrypted. crowsnest reports _which hosts_ were contacted — derived from DNS lookups and the server name in the TLS handshake — and never page contents or URLs. That is a hard limit for anything reading packets, not a gap in this tool.

Stating that plainly in the documentation matters more than it looks. A security tool that overstates its reach teaches the person using it the wrong thing about their own network.

## Packaging

The tool is only useful if it installs without a fight, so each platform gets a first-class path:

- **macOS** — a Homebrew tap, `brew install t0mbo192/tap/crowsnest`
- **Debian, Ubuntu, Raspberry Pi OS** — a `.deb` package that pulls in its own dependencies
- **Windows** — a PowerShell install script
- **Other Linux** — a shell installer

Wireshark is the one real dependency, since `tshark` does the capture. The macOS and Debian packages pull it in automatically; the script installers check for it and offer to install it.

## What it demonstrates

- Reading live network traffic and reducing it to the signal a person actually needs
- DNS and TLS SNI inspection, plus ASN lookups to attribute hosts to organisations
- Deliberate scoping — building the small answer well rather than a Wireshark clone
- Documenting a security tool's blind spots as prominently as its features
- Cross-platform packaging and release engineering across four install channels

[View the repository on GitHub](https://github.com/t0mbo192/crowsnest)

[Back to projects](/#projects)
