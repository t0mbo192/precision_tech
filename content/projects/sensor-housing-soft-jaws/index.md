# Soft Jaw Fixture for a Sensor Housing Run

A start-to-finish sample walkthrough: machined soft jaws and CAM programming for a 24-piece run of 6061 aluminum sensor housings. Every image below is a placeholder slot — swap in real screenshots and shop photos as they get captured.

> STATUS: demo project — layout preview only. All images are placeholders.

## Overview

The job: a small sensor housing with a tight bore, a sealing boss, and thin walls that do not tolerate sloppy workholding. The customer needed 24 pieces with a repeatable op-2 setup, so the plan was a matched set of machined soft jaws that locate off the op-1 profile and let every part drop in the same way, every time.

This page doubles as the template for how project walkthroughs are documented here: specs first, then each step with a screenshot slot and a short caption.

## Job specs

```
part ......... sensor housing, rev B
material ..... 6061-T6 aluminum
qty .......... 24 pcs
machine ...... 3-axis VMC, 10k rpm spindle
workholding .. 6 in vise + machined soft jaws
critical ..... bore dia +/- 0.001 in, boss height +/- 0.002 in
finish ....... bead blast + clear anodize (outsourced)
```

## Step 01 — CAD model and stock planning

Modeled the housing from the customer print, then built a stock body around it to plan how much material each op removes. Rev B added a relief cut near the boss, which changed where the part could be gripped in op 2 — catching that in CAD is a lot cheaper than catching it at the machine.

![Placeholder slot for the CAD model screenshot](/images/placeholders/cad-model.svg)

_fig 01 — housing model, rev B, with op-1 stock body overlaid_

## Step 02 — Soft jaw design

The jaws are the actual project. Each jaw gets a machined nest that mirrors the op-1 profile, a small clearance pocket for the boss, and stop pads so the part seats at a consistent Z. Jaw stock is bored while clamped at working pressure so the nest is round when it matters.

![Placeholder slot for the soft jaw design screenshot](/images/placeholders/soft-jaws.svg)

_fig 02 — jaw pair with part nested, clearance pocket highlighted_

Design notes that drove the geometry:

- Nest depth holds 60 percent of the part wall — enough grip without crushing
- Boss clearance pocket oversized 0.020 in so chips have somewhere to go
- Witness step on the fixed jaw for a quick visual seat check

## Step 03 — CAM programming

Two ops. Op 1 runs from saw-cut stock in hard jaws: face, rough, finish the profile and drill everything reachable. Op 2 flips into the soft jaws for the back side, boss, and the finish bore. Toolpath order was arranged so the bore is the last feature cut, after the part has stopped moving from clamping and heat.

![Placeholder slot for the CAM toolpath screenshot](/images/placeholders/cam-toolpaths.svg)

_fig 03 — op-2 toolpaths, finish bore pass highlighted_

```
op 1 .... face / adaptive rough / finish profile / spot + drill
op 2 .... face to height / rough boss / finish boss / finish bore / chamfer all
tools ... 7 total, all standard stock — no specials to order
cycle ... 11 min op 1, 8 min op 2 (est)
```

## Step 04 — Setup and first article

Setup sheet, tool list, and offsets documented so the whole job can be rerun by someone else without archaeology. First article ran with feed override dialed back on the finish bore until the numbers proved out.

![Placeholder slot for the machine setup photo](/images/placeholders/machine-setup.svg)

_fig 04 — op-2 setup: soft jaws installed, part seated against stop pads_

![Placeholder slot for the first article photo](/images/placeholders/first-article.svg)

_fig 05 — first article off the machine, before deburr_

## Step 05 — Inspection and results

Bore checked with a bore gauge set against ring standards; boss height on the surface plate with a drop indicator. Once the first article passed, every fifth part got the full check and the rest got the quick check.

![Placeholder slot for the inspection data screenshot](/images/placeholders/inspection.svg)

_fig 06 — inspection summary across the run_

```
bore dia ...... 24/24 within +/- 0.001 in, spread 0.0006 in
boss height ... 24/24 within +/- 0.002 in
scrap ......... 0 parts
rework ........ 1 part (cosmetic, re-blasted before anodize)
```

## Lessons learned

1. Boring the jaws at working clamp pressure was the single biggest factor in bore repeatability
2. Cutting the finish bore last, after the part settled, tightened the spread noticeably
3. The witness step turned seat checks from a judgment call into a yes/no answer
4. A setup sheet written for a stranger is a setup sheet that survives six months of not running the job

[Back to projects](/projects)
