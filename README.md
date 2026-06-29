# 🛡️ NeuroSOC — AI-Integrated Security Operations Center Analyst
🧠 Why This Exists
The cybersecurity landscape is undergoing a fundamental shift. Tools like XBOW are autonomously finding and chaining vulnerabilities. Anthropic's research and Google Project Zero are using AI to discover zero-days faster than any human team ever could. AI-powered attackers are already in the wild — compressing time-to-exploit from days to minutes.
The threat is no longer just hackers. It's AI-equipped hackers.
This project is my response to that reality. Instead of waiting for enterprise vendors to productize this shift, I am building it from scratch — an AI-native SOC analyst that learns, detects, and eventually hunts threats autonomously.

"It's not AI replacing cybersecurity professionals. It's AI-equipped professionals replacing those who aren't."
— The reason this repo exists.
🗺️ Project Roadmap
✅ Phase 1 — AI-Augmented SOC Analyst (Current)
The foundation. A working AI analyst that reads logs from Wazuh and makes triage decisions.

 Project architecture design
 Wazuh SIEM setup and log ingestion pipeline
 Log normalization and formatting layer
 Gemma integration via Autoroute
 Anomaly detection prompting pipeline
 Risk Accept / Reject / Escalate decision engine
 Terminal-based analyst interface
 Testing with real log samples

🔄 Phase 2 — Dual-Agent Log Analysis (Planned)
Two AI agents working in parallel — one beside the SIEM, one as an independent stream — both feeding a central correlation layer.

 SIEM-side autonomous agent
 Independent log capture agent
 Cross-validation and consensus logic
 Agentic memory for behavioral baselining
 Alert deduplication and noise reduction

🔬 Phase 3 — Autonomous Threat Hunter (Research Phase)
A top-level AI that receives synthesized data from Phase 2 and actively discovers new and emerging attack patterns — not just detecting known threats, but predicting unknown ones.

 Threat vector synthesis engine
 Attack pattern discovery via LLM reasoning
 MITRE ATT&CK mapping layer
 Threat report generation
 Human-in-the-loop review interface
 🧰 Tech Stack
LayerTechnologyReasonSIEMWazuhOpen-source, production-grade, real SOC adoptionAI RuntimeAutorouteFree local LLM orchestrationAI ModelGemma (via Autoroute)Lightweight, capable, swappableLanguagePythonStandard for security toolingInterfaceTerminal (CLI)Rapid iteration, scriptableFuture ModelTBD (Claude / GPT / local)Model-agnostic design

Design principle: The AI layer is intentionally model-agnostic. Swap Gemma for any other model without changing the pipeline.


🚀 Getting Started

⚠️ This project is in active development. Setup instructions will be updated as each phase is completed.

Prerequisites

Python 3.10+
Wazuh (self-hosted or cloud) — Installation Guide
Autoroute (for local LLM access) — Autoroute Docs
Gemma model pulled via Autoroute
#💡 Inspiration & Context
This project sits at the intersection of several real-world developments:

XBOW (Horizon3 AI) — Autonomous penetration testing AI finding real CVEs in production systems
Anthropic Security Research — AI breaking sandboxes and chaining vulnerabilities at non-human speed
Google Project Zero + AI — AI-assisted zero-day discovery compressing disclosure timelines
Enterprise SOC Reality — Most SOCs are drowning in alert fatigue; AI triage is no longer optional

This is not an academic exercise. This is training for the security landscape that already exists.

🤝 Contributing
This is a solo learning project for now. Once Phase 1 is stable, contributions and feedback are welcome. Open an issue if you want to discuss the architecture or suggest improvements.

⚠️ Disclaimer
This project is for educational and defensive security purposes only. All testing is performed in isolated lab environments. No tools or techniques in this project are intended for unauthorized access to any systems.

📬 Contact
Built by ISHAAN BANSAL — documenting the journey from SOC analyst to AI security engineer.

GitHub: @Gitishaan1
LinkedIn: https://www.linkedin.com/in/ishaan-bansal-b333b0379
 