# Review the whole candidate

Combine real automated reports with visual review of every state and transitions. Do not promise to detect every possible defect in advance.

| Area | Checks |
| --- | --- |
| Encoding/grid | Upstream dimensions/version, format, byte limit, cell geometry, counts, required/unused cells, transparency and bleed. |
| Extraction | Complete connected groups, no clipping or detached fragments, shared scale/registration rather than per-frame stretching. |
| Appearance | Photo-derived markings, eyes, face, material and proportions stay consistent and readable at native size. |
| Body construction | Track each limb shoulder/hip to extremity. A lifted paw replaces its grounded foreleg, rather than adding a fifth limb. Distinguish hind paws from duplicates; inspect tail/ears/props and occlusion. |
| Semantics | Calm living idle; alternating directional gait; attached wave; real jump and landing; work means processing, not running; waiting, failure and review remain distinct. |
| Playback | No size pops, floating baseline, sudden limbs, reversed cadence, clipping or flashes. Review idle→jump→idle and the whole gaze loop. |
| Gaze | Unambiguous cardinals, intended diagonal components, coherent ordering/boundaries, no whole-body turntable. Follow upstream blind review when applicable. |
| Host/tool errors | Missing capabilities, incompatible runtime, decode failures, missing files, tool errors, expired uploads and denied UI are blockers, not successful completion. |

## Repair loop

1. Find the smallest affected source rows; retain originals.
2. Describe the defect by frame/state and concrete landmarks.
3. Ground visual edits in the stored sheet, canonical art and identity references. Preserve successful rows.
4. Rebuild, validate and render affected previews. Inspect related states for the same defect.
5. Show revised motion and wait for explicit user approval again.

Use the upstream distinction between a documented subtle intermediate warning and a hard failure. Never downgrade extra limbs, clipping, wrong/ambiguous cardinals, identity changes or visible reversals just to finish.

## Confirmation

> 动态预览已完成，包括眨眼、跑动、挥爪、跳跃、等待、思考和张望。请看一下外形和动作；回复“确认”后，我再创建并设为当前伙伴。需要调整的话，直接说哪里不对。

For an existing pet, say “更新” instead of “创建”. An actual affirmative user response is required. Keep work local/Library and leave persisted artwork and selection unchanged until then. The animation must come from the exact candidate bytes intended for upload.
