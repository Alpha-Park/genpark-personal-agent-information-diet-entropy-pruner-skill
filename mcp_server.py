# -*- coding: utf-8 -*-
"""
Personal Agent Information Diet Entropy Pruner FastMCP Server
"""

import json
from typing import Dict, List, Any, Optional
from mcp.server.fastmcp import FastMCP
from client import PersonalAgentInformationDietEntropyPruner

mcp = FastMCP("genpark-personal-agent-information-diet-entropy-pruner-skill")
pruner = PersonalAgentInformationDietEntropyPruner()

@mcp.tool()
def calculate_feed_information_entropy(category_item_counts_json: str) -> str:
    """
    Calculates Shannon information entropy of reading feeds to assess intellectual diversity.
    """
    counts = json.loads(category_item_counts_json)
    res = pruner.calculate_feed_information_entropy(counts)
    return json.dumps(res, indent=2)

@mcp.tool()
def audit_information_diet_echo_chamber(item_token_sets_json: str) -> str:
    """
    Measures pairwise Jaccard lexical overlap to detect echo-chamber redundancy.
    """
    tokens = json.loads(item_token_sets_json)
    res = pruner.audit_information_diet_echo_chamber(tokens)
    return json.dumps(res, indent=2)

@mcp.tool()
def rank_content_sources_snr(sources_json: str) -> str:
    """
    Ranks digital news and newsletter sources by Signal-to-Noise Ratio (SNR) in Decibels.
    """
    sources = json.loads(sources_json)
    res = pruner.rank_content_sources_snr(sources)
    return json.dumps(res, indent=2)

def main():
    print("Testing Information Diet Entropy Pruner FastMCP Server:")
    print(calculate_feed_information_entropy(json.dumps({"AI": 15, "Philosophy": 5, "Finance": 8})))

if __name__ == "__main__":
    main()
