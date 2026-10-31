# -*- coding: utf-8 -*-
import json
from client import PersonalAgentInformationDietEntropyPruner

pruner = PersonalAgentInformationDietEntropyPruner()

print("=" * 64)
print("DEMO: Personal Information Diet & Shannon Entropy Pruner")
print("=" * 64)

# 1. Shannon Entropy of Reading Feed
counts = {"AI_Research": 25, "Macro_Economics": 12, "Neuroscience": 8, "Product_Design": 10, "Celebrity_Gossip": 2}
diet = pruner.calculate_feed_information_entropy(counts)
print(f"\n1. Feed Diversity Entropy (Score: {diet['normalized_entropy_score']}):")
print(f"   Status: {diet['diet_diversity_status']} (Shannon Bits: {diet['shannon_entropy_bits']})")

# 2. Echo chamber redundancy check
article_tokens = [
    ["llm", "agents", "mcp", "anthropic", "reasoning", "benchmarks"],
    ["llm", "agents", "mcp", "openai", "reasoning", "benchmarks"],
    ["crispr", "genomics", "longevity", "telomeres", "cellular"]
]
echo = pruner.audit_information_diet_echo_chamber(article_tokens)
print(f"\n2. Echo Chamber Audit:")
print(f"   Novelty Score: {echo['intellectual_novelty_score']} ({echo['echo_chamber_severity']})")
print(f"   Estimated Wasted Time: {echo['estimated_wasted_reading_time_pct']}%")

# 3. Decibel SNR source ranking
sources = [
    {"name": "ArXiv AI Weekly", "insight_density": 0.90, "noise_density": 0.10},
    {"name": "Tech Crunch Drama", "insight_density": 0.25, "noise_density": 0.75},
    {"name": "Stratechery Ben Thompson", "insight_density": 0.85, "noise_density": 0.15}
]
snr = pruner.rank_content_sources_snr(sources)
print(f"\n3. Content Sources Ranked by SNR (dB):")
for s in snr["sources_ranked"]:
    print(f"   [{s['snr_db']:+5.1f} dB] {s['source_name']}: {s['action']}")
