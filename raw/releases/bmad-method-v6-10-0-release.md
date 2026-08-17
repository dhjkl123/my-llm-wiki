---
source_url: "https://github.com/bmad-code-org/BMAD-METHOD/releases/tag/v6.10.0"
source_type: official-release
ingested: 2026-08-03
retrieved_at: "2026-08-03T23:03:06+09:00"
repository: bmad-code-org/BMAD-METHOD
version: 6.10.0
tag: v6.10.0
commit_sha: 081e64ee5aab2316b912883f7bee528ee143ce36
license: MIT
sha256: 576c6600af29f138977765bbaaeffe9ece5b88af4ab7b84f9233e21bf0b556c2
---
### ✨ Headline

**bmad-loop lands as an installable module, and the automator that came before it steps aside.** **bmad-loop** — the successor project for unattended dev-loop orchestration, adversarial review, and deferred-work sweeps — is now selectable straight from the installer picker, driven by the new **bmad-dev-auto** skill: a single-iteration unattended worker that clarifies intent, creates or resumes a spec, implements, reviews, and finalizes, all off a spec-frontmatter state machine an orchestrator can poll. **bmad-automator**, the experimental predecessor, is now deprecated in its favor.

**Also in this release:** party-mode gets an anti-consensus room and two sync fixes, the code-review/edge-case-hunter pipeline gets sharper severity triage and a named-set generalization pass, and **bmad-investigate** is retired.

### 💥 Breaking Changes

* **bmad-automator deprecated, replaced by bmad-loop** (#2532). New installs no longer show BMad Automator in the picker. Existing installs are untouched and keep showing, with a migration hint pointing to BMad Loop. If you're on Automator, plan the move to `bmad-loop`.

### 🎁 Features

* **bmad-loop — new marketplace module** (#2532). BMad's unattended-dev orchestrator ships as an opt-in installer module (`bmad-loop`, not selected by default). Its skills live behind a `.claude-plugin/marketplace.json` rather than a normal `module.yaml` folder, so the installer gained a `marketplace-plugin` registry flag that routes it through the existing custom-plugin resolver, and now fails loudly instead of installing an empty module if resolution comes up short. Installing the module only stages files — finish setup by running the `bmad-loop-setup` skill, which installs the orchestrator and wires up per-project hooks and policy; automation doesn't run until that completes. A new `post-install-message` registry field surfaces this instruction right after install (blocking on interactive installs so it isn't missed, non-blocking with `--yes`).
* **bmad-dev-auto — new unattended workflow skill** (#2500 and nine follow-ups). A Quick Dev sibling built to keep moving without a human in the loop, driven entirely off spec-frontmatter status so an orchestrator like bmad-loop can poll it. Hardened through the release: an append-only review-triage log with loopback tracking (#2505); an end-of-run commit so the worktree stays clean into the next iteration (#2506); a fix to the Blind Hunter reviewer, which was wrongly denied project access ("blind" means blind to intent, not to the codebase) (#2507); re-entry on a completed spec to trigger a fresh follow-up review pass (#2508); a `final_revision` recorded in frontmatter at exit, the only link back from an out-of-tree spec to its in-tree commits (#2522); a closed gap where Finalize could leave `status: draft` on an otherwise-done run (#2536); and a hardened contract requiring subagents to be invoked synchronously, since there's no event loop to resume a yielded turn (#2543). Reference doc at `docs/reference/dev-auto.md` (#2519), retitled "Autonomous Development Loops" (#2521). Some of the same prompt fixes were backported to Quick Dev (#2501).
* **party-mode: anti-consensus club** (#2530). New built-in persona group (Wildcard, Level, Killjoy, Splinter) for decision rooms that resist fast agreement while keeping a human in control. Launch with `--party=anti-concensus-club`, and use `--mode subagent` for best results. These can be configured as defaults if you use bmad customize and specify that.
* **Two new elicitation methods: Subtraction and Map Is Not the Territory** (#2515). Subtraction counters additive bias; Map Is Not the Territory guards against over-trusting a lossy model.
* **Edge Case Hunter: named-set generalization pass** (#2524). Catches diffs that special-case some members of a fixed set (enum, status code, sentinel, flag) while leaving the rest as silent unhandled branches. Measured catch-rate improvement of 50% to 100% on a real regression, at a 19% token cost per run.

### 🐛 Fixes

* **party-mode stays interactive and the room stays in sync** (#2531). Fixes a bug, observed under Codex, where a runtime treated the opening prompt as one-shot and closed spawned agents once satisfied. Party mode is open-ended by default now, ending only on explicit signal, with an opt-in `--non-interactive` flag; standing agents are kept alive and resumed rather than dropped.
* **party-mode: agent-team sync corrected to point-to-point** (#2539). Claude Code Agent Teams communicate mailbox-style, not over a shared broadcast channel, so an idle member doesn't see exchanges it isn't addressed in. Docs updated so the lead relays turns; subagent mode, which is genuinely broadcast, is unchanged.
* **Code-review triage severity calibration hardened** (#2523). Requires reading surrounding source (call sites, guards) before rating severity instead of judging from the diff hunk alone, fixing over-rated unreachable findings, and drops a "prefer conservative when uncertain" tie-breaker that was inflating severity.
* **Deletion audit folded into Edge Case Hunter** (#2525). Retires the standalone deletion-contract auditor layer, which added cold-start cost for near-zero yield, in favor of a gated deletion check inside Edge Case Hunter's existing turn.
* **Review layer invocation normalized** (#2526). Removes stale "no access/control" wording from code-review/quick-dev/dev-auto prompts and normalizes Blind Hunter / Edge Case Hunter invocation phrasing.
* **Installer accepts Windows custom module paths** (#2511). Local paths like `C:\modules\foo`, `C:/modules/foo`, and `.\foo` no longer fall through to the Git-URL parser and get rejected.
* **bmad-help reads central config** (#2541). Its config data source now goes through the shared four-layer TOML resolver instead of legacy `config.yaml`/`user-config.yaml`, fixing `communication_language` and `project_knowledge` not reaching the skill.

### 📚 Docs

* **bmad-forge-idea wording tightened** (#2513). Overview, session, persona, and exit language rewritten more directly; no behavior change.
* **validate-skills exempts deprecated skills from the trigger-phrase check** (#2486). Thin compatibility shims (`bmad-create-prd`, `bmad-edit-prd`, `bmad-validate-prd`, `bmad-create-architecture`) intentionally omit a trigger phrase to steer users to their replacement.

### 🗑️ Removed

* **bmad-investigate retired.** It reached the same conclusions as plain investigation at higher cost; the case-file artifact didn't justify the overhead.
