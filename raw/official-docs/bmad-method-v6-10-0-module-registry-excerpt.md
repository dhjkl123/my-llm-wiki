---
source_url: "https://github.com/bmad-code-org/BMAD-METHOD/blob/081e64ee5aab2316b912883f7bee528ee143ce36/bmad-modules.yaml#L37-L95"
source_type: official-github-file-excerpt
ingested: 2026-08-03
retrieved_at: "2026-08-03T23:03:06+09:00"
repository: bmad-code-org/BMAD-METHOD
document_path: "bmad-modules.yaml"
version: 6.10.0
tag: v6.10.0
commit_sha: 081e64ee5aab2316b912883f7bee528ee143ce36
license: MIT
excerpt_lines: "37-95"
sha256: 7886e5af7e19e3ca8606a6c7b62f662563b50417b0b96b037ba9b2e6bd4f9e99
---
  bmad-loop:
    url: https://github.com/bmad-code-org/bmad-loop
    module-definition: src/bmad_loop/data/skills/bmad-loop-setup/assets/module.yaml
    code: bmad-loop
    # bauto is the pre-rename code (module was bmad-auto before both the repo
    # and its contents were renamed to bmad-loop); keeps existing bauto
    # installs migrating forward instead of being orphaned.
    aliases: [bauto]
    name: "BMad Loop"
    description: "Deterministic, Python-based unattended dev loop with adversarial review"
    defaultSelected: false
    type: bmad-org
    default_channel: stable
    # Skills live outside a single module.yaml dir; resolve them from
    # .claude-plugin/marketplace.json via the plugin resolver (see external-manager).
    marketplace-plugin: true
    post-install-message: |
      BMad Loop installed. To finish setup, run the bmad-loop-setup skill
      from your agent:

        > use the bmad-loop-setup skill

      It installs the bmad-loop orchestrator tool and wires up the per-project
      hooks and policy. The automation skills don't run until setup completes.

  bmad-method-test-architecture-enterprise:
    url: https://github.com/bmad-code-org/bmad-method-test-architecture-enterprise
    module-definition: src/module.yaml
    code: tea
    name: "BMad Test Architect"
    description: "Quality strategy, test automation, and release gates for enterprise teams"
    defaultSelected: false
    type: bmad-org
    npmPackage: bmad-method-test-architecture-enterprise
    default_channel: stable

  bmad-builder:
    url: https://github.com/bmad-code-org/bmad-builder
    module-definition: skills/module.yaml
    code: bmb
    name: "BMad Builder"
    description: "Build AI agents, workflows, and modules from a conversation"
    defaultSelected: false
    type: bmad-org
    npmPackage: bmad-builder
    default_channel: stable

  bmad-automator:
    url: https://github.com/bmad-code-org/bmad-automator
    module-definition: skills/module.yaml
    code: automator
    name: "BMad Automator Epic Builder Experimental"
    description: "EXPERIMENTAL: only supports claude and codex currently"
    defaultSelected: false
    type: experimental
    npmPackage: bmad-story-automator
    default_channel: next
    deprecated: true
    deprecation-message: "BMad Automator has been deprecated and is replaced by BMad Loop (bmad-loop). Install BMad Loop instead."
