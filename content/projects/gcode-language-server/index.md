---
category: tool-building
summary: Diagnostics, hover docs and completions for CNC G-code, built as a language server.
---

# G-Code Language Server — The Linter G-Code Never Had

Semantic diagnostics, hover documentation and completions for CNC G-code, built as a language server. A Python process tracks machine modal state line by line and catches the mistakes a syntax highlighter structurally cannot see; a thin TypeScript shim connects it to VS Code.

> A colorizer can tell you a word is a word. It cannot tell you cutter comp is still active at M30.

## Overview

The G-code tooling that exists is mostly colouring and counting — a TextMate grammar plus pattern matching. That approach has no model of what the machine is doing, so there is a whole class of errors it can never report:

- A `G1` cutting move issued with no feedrate
- Cutter compensation still active when the program reaches `M30`
- A Z move after a tool change with no `G43` tool length offset applied

None of those are malformed text. Each one is valid G-code that is wrong _given what came before it_. Catching them means tracking modal state through the program the way the control will, which is exactly what a linter-style language server does and a grammar never can.

This project is active and still being developed — it sits at the junction of the CNC work I have done for years and the software side I have been building toward.

## Architecture

Two processes talk JSON-RPC over stdin and stdout. On the editor side, `src/extension.ts` is a thin shim whose only job is to spawn the server and relay messages. On the other side sits a three-layer Python stack:

```
server/server.py        pygls glue - LSP translation, no G-code knowledge
server/gcode_parser.py  the modal-state engine - zero dependencies
server/dialects.py      rules, codes and hover text as plain data tables
```

The glue layer translates between LSP messages and the parser and knows nothing about G-code. The engine below it walks modal state and has no dependencies at all, which makes it the single place a different parsing engine would plug in. Every dialect fact — which rules apply, which codes exist, what the hover text says — sits in data tables rather than in the logic that reads them.

Static syntax colouring lives in `syntaxes/*.json` and is deliberately _not_ part of the language server — colours and diagnostics are separate concerns that get conflated in most G-code tooling.

The split is the point. All the G-code intelligence lives in Python, and because it speaks the Language Server Protocol rather than a VS Code API, the same server drives Neovim, Kate and Zed with no extra work. The TypeScript side is roughly forty lines whose only job is to spawn the server.

## How a lint round-trips

1. Opening `part1.nc` matches the `.nc` extension registered to language `gcode`, activating the extension.
2. `extension.ts` spawns `python server/server.py` as a child process.
3. VS Code sends `initialize`; the server advertises diagnostics, hover and completion.
4. `textDocument/didOpen` carries the full file text across.
5. The server walks the modal state line by line and pushes `publishDiagnostics` back — squiggles appear and the Problems panel fills.
6. Each edit sends `didChange`, debounced 300 ms, and re-lints. Hovering `G43` fires a `hover` request answered from the dialect tables.

## Keeping the engine testable on its own

Because dialect knowledge sits in data tables rather than scattered through the parser, supporting another control means editing tables, not logic. And because the modal-state engine carries no dependencies, the interesting part runs without an editor anywhere in the picture:

```
python server\gcode_parser.py examples\demo.nc
```

That also makes the swap point obvious: keep the per-line check method on the parser class and a different engine drops in without touching anything else.

## What it demonstrates

- Modelling machine state to produce diagnostics that pattern matching cannot reach
- Implementing the Language Server Protocol with pygls — lifecycle, diagnostics, hover, completion
- Choosing a protocol boundary that buys editor portability for free
- Separating domain knowledge as data from the logic that consumes it
- Turning two decades of CNC experience into tooling that catches errors at review instead of at the machine

[View the repository on GitHub](https://github.com/t0mbo192/gcode-language-server)

[Back to projects](/#projects)
