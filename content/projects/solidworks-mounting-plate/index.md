# Modeling a Mounting Plate in SolidWorks

A feature-by-feature walkthrough of modeling a bolt-on mounting plate in SolidWorks: a rectangular plate with a central bore and four counterbored holes for 5/16 socket head cap screws.

> Feature-based modeling: build the part the way it would actually be made, one deliberate step at a time.

## Overview

It's a small part, but it exercises the whole core modeling workflow — sketch, extrude, place holes, then refine with fillets and chamfers. The finished plate is a real-world component: it bolts to a mating surface with four corner screws and passes a shaft or fitting through the center bore.

Modeling starts with picking the right first feature, the one everything else references. For a plate like this, that's the rectangular body. Get the base sketch fully defined and the rest of the features hang off it cleanly.

## Step 01 — Base sketch and extrude

The first feature sets the overall footprint. I sketched the outer profile as a fully dimensioned rectangle, 3.50 in by 2.50 in, on the front plane, then extruded it to the plate thickness. Fully defining the sketch here, with no under-constrained geometry, keeps every later feature stable when a dimension changes.

![Sketch of the plate profile dimensioned 3.50 by 2.50 inches, extruded to thickness](/images/projects/mounting-plate/01-sketch-extrude.png)

_fig 01 — base sketch, 3.50 by 2.50, extruded to the plate body_

## Step 02 — Bore and mounting holes

Next, the holes. A single bore through the center passes the main feature; four counterbored holes in the corners take 5/16 socket head cap screws so the heads sit flush below the surface. Placing them with the Hole Wizard and the proper fastener callout keeps the counterbore diameter and depth correct for the screw instead of guessing dimensions.

![Plate with a center bore and four counterbored corner holes](/images/projects/mounting-plate/02-hole-features.png)

_fig 02 — center bore plus four counterbores sized for 5/16 socket head cap screws_

## Step 03 — Corner fillets and chamfers

With the functional features in place, the part gets refined. Fillets on the four outside corners remove the sharp edges, and chamfers break the top edges of the counterbores. These aren't only cosmetic: rounded corners are safer to handle and easier to machine, and chamfered hole edges help the screws start clean.

![Plate with rounded corner fillets and chamfered counterbore edges](/images/projects/mounting-plate/03-fillets-chamfers.png)

_fig 03 — corner fillets and counterbore chamfers added_

## Step 04 — Back-side chamfer

The last feature breaks the back edge. A chamfer around the back face finishes the part and removes the sharp burr edge left where the extrude meets the back plane — the kind of detail that matters once a part is actually handled and assembled.

![Plate with a chamfer added around the back edge](/images/projects/mounting-plate/04-back-chamfer.png)

_fig 04 — back-side edge chamfer, part complete_

## What it demonstrates

- Choosing the right base feature and fully defining the base sketch
- Sizing holes to real fasteners with the Hole Wizard rather than raw numbers
- Using fillets and chamfers deliberately, for function as much as finish
- A clean, ordered feature tree that stays editable as requirements change

[Back to projects](/projects)
