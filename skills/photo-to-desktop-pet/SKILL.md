---
name: photo-to-desktop-pet
description: Turn a personal pet photo and name into an animated ChatGPT Pets companion with Codex, visual repair, and mandatory user approval of the animation before upload or activation. Use for this photo-to-companion workflow, not animal care or unrelated desktop-pet apps.
---

# Photo to Desktop Pet

Guide a nontechnical user from one front-facing pet photo and a name to a validated, user-approved animated companion. Speak in the user's language. Handle technical work; ask only for missing inputs, needed account connections, animation approval, and device settings that cannot be operated through supported interfaces.

## 1. Inputs and capabilities

Reuse the photo and name already in the chat. Ask for both together if missing. Preserve the supplied name, including non-Latin names; use a separate ASCII folder slug. Prefer a clear front-facing photo. Explain concrete visibility problems before asking for another photo. Treat unseen body markings as conservative inferences, not observed facts.

Discover installed Pets tools and `work-pets:create-pet`. Read and follow that skill and its bundled sprite-sheet/upload contracts for production, validation and lifecycle operations. For an existing companion, use `work-pets:update-pet` and preserve its stable ID. These are required dependencies: never replace their scripts with a size-only checker or fabricate a pet when they are unavailable. See [capabilities.md](references/capabilities.md) for fallbacks and completion levels.

Use built-in image generation and the imagegen skill for all new/edited art. Never silently switch to a paid API/CLI or request an API key for built-in generation. Prefer a configured bundled Python runtime; upstream scripts need Python 3.10+ and Pillow. Run `scripts/preflight.py` with the chosen interpreter. Resolve reversible environment issues within authorization, requesting only permissions the host actually requires.

Use local storage by default, or Library when available/required. If an upstream skill mandates Library but it is unavailable, obtain a one-time explicit local-storage exception and remember it for revisions. Never upload source photos to GitHub or publicly share a pet as part of creation.

## 2. Establish identity

Preserve the original photo and normalize orientation. `scripts/prepare_reference.py` decodes supported images to a reference PNG; HEIC needs pillow-heif. Use an isolated run folder. Write a short identity brief covering visible colors, markings, eyes, muzzle, ears, silhouette and expression, distinguishing observations from inferences.

Generate a canonical full-body reference grounded in the photo, readable at normal pet size. Show it and invite corrections. Incorporate requested corrections into affected rows. Approval of this still never substitutes for the final animation approval below.

## 3. Produce, inspect and repair

Run the upstream bundled preparation, grounded row generation, extraction, assembly and validation pipeline. Follow its current layout/state definitions instead of maintaining a second schema here. Generate coherent state strips, not a complete atlas in one generation call. Attach canonical art and identity references to later visual jobs. Preserve successful rows when repairing a local failure.

Read [review-and-approval.md](references/review-and-approval.md). Inspect the actual final frames and playback, not merely a successful exit code. Cover technical errors and observable visual defects; anatomy is one category, not the entire review. Check limbs during lifts, scale across idle/jump, attached parts, direction meaning and transitions at native size. `scripts/make_review_sheet.py` exposes suspect rows frame by frame; it is a review aid, not a validator.

Classify failures: source art, identity, semantics, anatomy, geometry, extraction, registration, transparency, encoding, upload or host capability. Use deterministic fixes for deterministic failures and image generation for visual changes. Rebuild affected previews and rerun upstream gates against the exact final encoded file. Do not claim checks passed without real output. If a root failure repeats twice, change strategy instead of waiving it.

## 4. Mandatory animation approval — stop here

Show animation from the exact candidate atlas, a complete labeled contact sheet, at least four representative stills, and GIF/MP4 downloads required by the upstream contract. Cover every standard state and the look loop, not only the nicest motion. If inline playback is unavailable, provide an ordered player/frame strips and usable animation files.

Ask explicitly: “这是完整动态预览。外形和动作都符合你的预期吗？确认后我再创建并设为当前伙伴；需要修改的话，告诉我哪个动作或位置。” For revisions, say “更新” instead of “创建”.

**Wait for an explicit affirmative response to this candidate. Do not call `prepare_pet_upload`, `create_pet`, sprite-sheet `update_pet`, or `select_pet` before it.** Authorization to make a pet, approval of a still, elapsed time or silence is not animation approval. Corrections return to step 3. Any visual change requires revised motion preview and renewed approval. Leave the installed pet unchanged while review is pending.

Record candidate path, SHA-256, preview/report paths, and the user's actual approval message/reference. Recompute the digest before upload. Changed candidate bytes invalidate approval until the revised preview is approved.

## 5. Upload, select and check device display

After approval and validation, follow the upstream upload-session contract. Create/update once and verify the stable pet ID. Retry only under the tool's idempotency rules. Use the exact supplied name. Select when the user requested an active companion; verify by ID in the paginated listing. Persist the stable ID, not an expiring URL or upload-session ID.

Separately check the local desktop mini-companion display. Prefer a supported setting tool; otherwise use permitted UI automation. If access is denied, stop that approach and guide the user using their actual screen. Do not edit private app databases/preferences or bypass UI restrictions. Never invent a menu path or infer desktop visibility from `active_pet_id` alone.

Report observed outcomes distinctly: approved files saved, pet created/updated, pet selected, desktop visibly enabled. State remaining steps plainly. Deliver local previews and the atlas. Preserve previous revisions and stable identity. Never silently publish a repository, pet share link, source photo or other public artifact.
