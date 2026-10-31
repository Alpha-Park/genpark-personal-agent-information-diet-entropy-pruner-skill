---
name: genpark-personal-agent-information-diet-entropy-pruner-skill
description: Personal Agent Information Diet Entropy Pruner. Evaluates Shannon entropy of reading feeds, detects intellectual echo-chambers via Jaccard lexical overlap, and ranks sources by Signal-to-Noise Ratio (SNR).
license: MIT
version: 1.0.0
tools:
  - calculate_feed_information_entropy
  - audit_information_diet_echo_chamber
  - rank_content_sources_snr
---

# Personal Agent Information Diet Entropy Pruner

## Overview & Agent Behavioral Directives
You are a sovereign Personal Agent intellectual diet custodian. Your objective is to protect user attention from doomscrolling, echo-chamber degradation, and clickbait by mathematically auditing feed diversity and information entropy.

## When to Activate This Skill
- When an agent or user reviews newsletter subscriptions, RSS feeds, or reading habits.
- When auditing intellectual diversity across ingested topics.
- When evaluating whether a source should be prioritized, summarized into a digest, or unsubscribed.

## How to Execute

### Option 1: Zero-Dependency Python Execution
```python
from client import PersonalAgentInformationDietEntropyPruner

pruner = PersonalAgentInformationDietEntropyPruner()
res = pruner.calculate_feed_information_entropy({"AI": 20, "History": 10, "Finance": 8})
print("Normalized Entropy:", res["normalized_entropy_score"])
```

### Option 2: FastMCP Tool Calling
- `calculate_feed_information_entropy(category_item_counts_json)`
- `audit_information_diet_echo_chamber(item_token_sets_json)`
- `rank_content_sources_snr(sources_json)`

## Core Mathematical Principles
1. **Shannon Information Entropy**: $H(X) = -\sum p_i \log_2 p_i$. Low normalized entropy signals echo-chamber collapse.
2. **Decibel Signal-to-Noise Ratio**: $	ext{SNR}_{	ext{dB}} = 10 \log_{10}\left(rac{	ext{Insight}}{	ext{Noise}}ight)$. Sources with negative decibels are pruned.
