# -*- coding: utf-8 -*-
"""
Personal Agent Information Diet Entropy Pruner Client
Zero-dependency Shannon information entropy calculator, Jaccard lexical repetition
echo-chamber auditor, and decibel Signal-to-Noise Ratio (SNR) content source ranker.
"""

import math
from typing import Dict, List, Any, Optional

class PersonalAgentInformationDietEntropyPruner:
    """
    Audits personal reading feeds, digital media, and information consumption.
    Computes Shannon entropy diversity, identifies echo-chamber doomscrolling,
    and ranks news/feed sources by decibel Signal-to-Noise Ratio.
    """

    def calculate_feed_information_entropy(
        self,
        category_item_counts: Dict[str, int]
    ) -> Dict[str, Any]:
        """
        Calculates Shannon Information Entropy: H(X) = -sum(p_i * log2(p_i)).
        Normalized Entropy H_norm = H(X) / log2(N).
        """
        if not category_item_counts:
            raise ValueError("Category counts dictionary cannot be empty.")

        total_items = sum(category_item_counts.values())
        if total_items == 0:
            raise ValueError("Total items must be greater than zero.")

        n_categories = len(category_item_counts)
        entropy = 0.0

        for count in category_item_counts.values():
            if count > 0:
                p = count / float(total_items)
                entropy -= p * math.log2(p)

        max_entropy = math.log2(n_categories) if n_categories > 1 else 1.0
        normalized_entropy = round(entropy / max_entropy, 3) if max_entropy > 0 else 1.0

        if normalized_entropy >= 0.80:
            status = "DIVERSE_INTELLECTUAL_DIET"
        elif normalized_entropy >= 0.50:
            status = "MODERATELY_CONCENTRATED"
        else:
            status = "ECHO_CHAMBER_DOOMSCROLL_ALERT"

        return {
            "total_items_analyzed": total_items,
            "unique_categories": n_categories,
            "shannon_entropy_bits": round(entropy, 3),
            "normalized_entropy_score": normalized_entropy,
            "diet_diversity_status": status,
            "pruning_recommendation": "Diversify reading sources" if normalized_entropy < 0.50 else "Maintain current intake balance"
        }

    def audit_information_diet_echo_chamber(
        self,
        item_token_sets: List[List[str]]
    ) -> Dict[str, Any]:
        """
        Measures pairwise Jaccard lexical similarity across consumed articles to detect repetitive echo-chambers.
        J(A, B) = |A cap B| / |A cup B|.
        """
        if len(item_token_sets) < 2:
            raise ValueError("Need at least 2 items to compute echo-chamber index.")

        n = len(item_token_sets)
        similarities = []

        for i in range(n):
            set_a = set(item_token_sets[i])
            for j in range(i + 1, n):
                set_b = set(item_token_sets[j])
                union = len(set_a | set_b)
                if union > 0:
                    sim = len(set_a & set_b) / float(union)
                    similarities.append(sim)

        avg_jaccard = round(sum(similarities) / len(similarities), 3) if similarities else 0.0
        novelty_score = round(1.0 - avg_jaccard, 3)

        return {
            "total_articles_compared": n,
            "average_lexical_similarity": avg_jaccard,
            "intellectual_novelty_score": novelty_score,
            "echo_chamber_severity": "SEVERE_REDUNDANCY" if avg_jaccard >= 0.40 else ("MODERATE_OVERLAP" if avg_jaccard >= 0.20 else "HEALTHY_DISCOURSE_BREADTH"),
            "estimated_wasted_reading_time_pct": round(avg_jaccard * 100.0, 1)
        }

    def rank_content_sources_snr(
        self,
        sources: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Ranks information sources by Signal-to-Noise Ratio (SNR) in Decibels:
        SNR_dB = 10 * log10(Insight_Density / (Clickbait_Density + 1e-4)).
        Source format: {"name": "Substack X", "insight_density": 0.85, "noise_density": 0.15}
        """
        if not sources:
            raise ValueError("Sources list cannot be empty.")

        ranked = []
        for s in sources:
            name = s.get("name", "Unknown")
            signal = max(0.01, min(1.0, float(s.get("insight_density", 0.5))))
            noise = max(0.01, min(1.0, float(s.get("noise_density", 0.5))))

            snr_ratio = signal / noise
            snr_db = round(10.0 * math.log10(snr_ratio), 2)

            ranked.append({
                "source_name": name,
                "insight_density": signal,
                "noise_density": noise,
                "snr_db": snr_db,
                "action": "PRIORITIZE_SUBSCRIBE" if snr_db >= 5.0 else ("KEEP_DIGEST" if snr_db >= 0.0 else "UNSUBSCRIBE_PRUNE")
            })

        ranked.sort(key=lambda x: x["snr_db"], reverse=True)

        return {
            "total_sources_evaluated": len(ranked),
            "sources_ranked": ranked,
            "sources_recommended_for_pruning": [s["source_name"] for s in ranked if s["action"] == "UNSUBSCRIBE_PRUNE"]
        }
