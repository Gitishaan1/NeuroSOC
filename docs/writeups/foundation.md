Week 01 — Building the AI Foundation

Phase: 1 — Part 1 Complete

Date: April 2026

Status: ✅ Done

What I Built

The goal of Part 1 was simple but critical — get the AI layer ready before touching any logs or SIEM integration. No point connecting Wazuh to an AI that isn't working properly.

By the end of this part, the foundation is solid:

Gemini Flash 2.5 configured as the primary model via direct HTTP POST requests to the Gemini API
Ollama configured as an automatic fallback model (runs locally, always available)
Automatic failover logic — if Gemini fails 2 times consecutively, the system silently switches to Ollama and continues without crashing
Both models tested and responding correctly

The AI network is now ready to be pointed at real log data in Part 2.

Problems I Hit

1. The google-generativeai library was a dead end
My first instinct was to use Google's official Python library (google-generativeai) to talk to Gemini. Seemed like the obvious choice. After spending a significant amount of time configuring it and debugging multiple different errors, I couldn't get a clean response out of it.
The fix: Ditched the library entirely. Instead, I craft the API request manually in Python using the requests module — a direct HTTP POST to the Gemini API endpoint with the API key embedded in the request. This worked immediately and gave me full control over the request structure.
Lesson learned: Sometimes the official SDK adds more complexity than it removes. A raw HTTP request is always a valid option, and understanding what's actually being sent to the API is a useful skill anyway.

3. Gemini is unreliable under heavy load
Once Gemini was working, a new problem appeared — the model is a free-tier, heavily used API. Under load it would return errors saying it was unavailable. Longer prompts (which is exactly what log analysis will produce) made this worse, timing out or returning the same overload error.
Relying on a single external free-tier model for a security tool is not acceptable. If the AI goes down, the analyst goes down.
The fix: Designed and implemented a fallback system. The code tracks Gemini failures, and after 2 consecutive failures it automatically switches to the local Ollama model for that request. Ollama runs entirely on local hardware — no API, no rate limits, no downtime. The switch is seamless from the user's perspective.
Lesson learned: In security tooling, resilience isn't optional. A system that works 80% of the time is not a system you can trust. Building the fallback this early means the rest of the project inherits that reliability from day one.


What's Next — Part 2
With the AI foundation stable, Part 2 moves into the actual SOC work:

Connect the AI to Wazuh SIEM log output
Build the log parsing and formatting layer so raw Wazuh logs become clean, structured input the AI can reason about
Design the anomaly detection prompting pipeline — teaching the AI what to look for in security logs
First real test: feed live logs, get back an actual security assessment