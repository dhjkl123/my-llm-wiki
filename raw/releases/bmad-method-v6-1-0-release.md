---
source_url: https://github.com/bmad-code-org/BMAD-METHOD/releases/tag/v6.1.0
source_type: official-release
ingested: 2026-08-03
retrieved_at: 2026-08-03T22:39:53+09:00
repository: bmad-code-org/BMAD-METHOD
version: 6.1.0
tag: v6.1.0
commit_sha: 521f1e15ca819b855571da5e13623afdee4a2122
license: MIT
sha256: b5d87c315d9c838909f2ab96e0ddc727e5be40c3f2449552a18e3966560f2a39
---
🚀 **BMad v6.1.0 RELEASED!**

🎉 The biggest architectural overhaul since v6 — everything is now a skill!

🪥 **WHITEPORT DESIGN STUDIO** - WDS module now enabled in the installer! Full design-to-code pipeline is here.

🎯 **SKILLS-BASED ARCHITECTURE**
• Every workflow, agent, and task now installs as a unified skill with SKILL.md entrypoints
• All core workflows converted from YAML/XML to clean markdown format
• Legacy workflow engine plumbing removed — leaner, faster, simpler
• All 15 platforms migrated to native Agent Skills format

⚡ **NEW CAPABILITIES**
• Edge Case Hunter runs as a parallel code review layer in Phase 4 — catches boundary conditions other reviews miss
• Experimental Quick Dev preview available — will become the main Phase 4 development tool
• Pi coding agent now supported as a platform
• `@next` install channel — get tip of main without waiting for stable: `npx bmad-method@next install`

🐛 **KEY FIXES**
• Code review no longer gets stuck in infinite loops (removed mandatory minimum issue count)
• Brainstorming ideas no longer silently lost during PRD creation
• npm package 91% smaller (6.2 MB → 555 KB!)

🌍 **INTERNATIONALIZATION**
• Full Chinese (zh-CN) documentation translation
• Starlight i18n routing with fallback to English

📊 **75 commits | 61 PRs merged | 306 files changed | +10,472 / -6,065 lines**

🙏 **CONTRIBUTORS**
@Alex Verkhovsky (51 PRs! 🔥), @Nikolas Hor (6 PRs!)
@cccczl (2 PRs!), @Gani Mohamed Parakadhullah, @Chandan Veerabhadrappa
Community-driven FTW! 🌟

📦 **INSTALL:**
`npx bmad-method install`

⭐ **SUPPORT US:**
🌟 GitHub: github.com/bmad-code-org/BMAD-METHOD/
📺 YouTube: youtube.com/@BMadCode
☕ Donate: buymeacoffee.com/bmad

🔥 **Optimized skills and more WDS workflows coming next!**
