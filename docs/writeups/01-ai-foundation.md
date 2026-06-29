# AI Foundation

**Phase:** 1 — Part 1 Complete

**Completed:** April 2026

**Status:** ✅ Complete

---

## Objective

Before integrating NeuroSOC with Wazuh SIEM, the AI layer needed to be reliable, secure, and resilient. There was no point processing security logs if the analysis engine itself could fail unexpectedly.

The primary objective of this phase was to build a dependable AI inference layer that could later be connected to real-time security events without requiring changes to the overall architecture.

---

# What I Built

By the end of this phase, the AI foundation was fully operational.

Implemented:

- **Gemini 2.5 Flash** as the primary AI model using direct HTTP POST requests instead of the official SDK.
- **Groq (Llama 3.3 70B Versatile)** configured as the automatic fallback provider.
- Automatic failover logic that retries Gemini requests before seamlessly switching to Groq whenever Gemini becomes unavailable.
- Environment variable support (`.env`) for securely managing API keys instead of hardcoding secrets into the source code.
- A GitHub-ready project structure with configuration files, dependency management, and documentation.

The AI layer is now stable enough to begin processing real Wazuh security events.

---

# Challenges & Solutions

## 1. The official Gemini SDK became a dead end

My initial approach was to use Google's official `google-generativeai` Python library.

Although this seemed like the obvious solution, I repeatedly encountered configuration issues and inconsistent behavior while attempting to generate responses. After spending significant time debugging the SDK, I decided to remove it entirely.

### Solution

Instead of relying on the SDK, I implemented direct HTTP requests using Python's `requests` library.

This provided:

- Complete control over every API request
- Easier debugging
- Smaller dependency footprint
- Better understanding of how the Gemini API actually works

### Lesson Learned

Official SDKs are convenient, but understanding the underlying HTTP API makes debugging significantly easier and avoids unnecessary abstraction.

---

## 2. Gemini Free Tier proved unreliable

Once Gemini was working correctly, another issue quickly appeared.

Because the project currently relies on the free API tier, Gemini occasionally returned rate-limit errors, temporary service failures, and request timeouts—especially when multiple requests were sent within a short period.

For a cybersecurity tool, this creates a serious reliability problem. An AI assistant that stops responding whenever traffic increases cannot be trusted in a SOC environment.

### Solution

Instead of relying on a single AI provider, I redesigned the architecture around a multi-provider approach.

Gemini remains the primary reasoning engine, while **Groq (Llama 3.3 70B Versatile)** serves as the automatic fallback model.

If Gemini fails after multiple retry attempts, NeuroSOC transparently switches to Groq and continues processing requests without interrupting the workflow.

The user never needs to manually select the fallback provider.

### Lesson Learned

Reliability is more important than choosing a single "best" AI model.

Designing resilient systems that continue operating during failures is a core engineering principle, especially in security-focused software.

---

# Architecture Decisions

During development, the original fallback design used a locally hosted Ollama model.

Although this provided complete offline availability, it introduced additional hardware requirements, slower inference, and increased project complexity.

After evaluating different options, I replaced the local fallback with Groq's hosted inference platform.

This decision provided:

- Faster inference speeds
- Access to larger language models
- Generous free-tier request limits
- Simpler deployment
- A cleaner architecture while preserving automatic failover

The project remains flexible enough that additional AI providers can be integrated in the future with minimal code changes.

---

# What's Next

With the AI foundation complete, the next phase focuses on integrating NeuroSOC with Wazuh SIEM.

Upcoming work includes:

- Connect NeuroSOC to Wazuh alert output.
- Parse and normalize raw security events into structured AI input.
- Design prompts for anomaly detection and incident classification.
- Generate AI-assisted security assessments from live Wazuh alerts.
- Build the reporting pipeline for SOC analysts.

This phase marks the transition from building the AI infrastructure to solving real cybersecurity problems using live security telemetry.