# Capability checks and honest completion

This skill orchestrates an installed pipeline. It does not ship or relicense the Pets implementation. Resolve skill paths from the host catalog, never a fixed home directory or cached plugin version.

| Capability | Handling |
| --- | --- |
| Pets plugin and create/update skills | Required for persisted ChatGPT Pets. Discover them; if absent, guide official plugin installation/connection. Do not promise support in every Codex build/account. |
| Built-in image generation | Required for art. Explain a missing capability. A separate API workflow is optional only after explicit user choice and may require credentials/billing. |
| Python 3.10+ and Pillow | Prefer configured dependency runtimes. `preflight.py` is read-only. Do not assume system Python is new enough or use sudo pip. |
| HEIC | Use pillow-heif or a supported platform decoder. If unavailable and not installable, ask for a JPEG/PNG export; avoid repeated failed conversions. |
| Library | Use when available/required. If mandatory but absent, get a one-time explicit local-storage exception. |
| Animation preview | Show actual playback/player and ordered stills plus GIF/MP4. A static picture is not motion approval. |
| Desktop display | Needs a supported setting tool or permitted UI. Server selection does not prove a desktop window is visible. Respect denied access. |

## Run record

Keep requested name, photo path, storage preference, identity brief, current phase, candidate digest, reports/previews, approval message/reference, and stable pet ID after creation. Exclude secrets, upload sessions and expiring links.

Phases: inputs → identity → animation → awaiting_animation_approval → approved → uploaded → selected → desktop_visible.

- Corrections invalidate approval and return to animation.
- Failed operations do not advance the phase.
- Selected is a partial result when desktop control is unavailable, never proof of desktop_visible.
- On resume, inspect records, digests and current server state before retrying mutations.
