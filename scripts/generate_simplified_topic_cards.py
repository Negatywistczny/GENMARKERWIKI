#!/usr/bin/env python3
"""Generator uproszczonych kart tematycznych (md/, sekcje 1–4).

TYMCZASOWO WYŁĄCZONY — pseudokarty z markerem <!-- topic-card --> usunięte.
Pełne karty md/ pozostają jedynym źródłem treści na gene.html.
"""

from __future__ import annotations

TOPIC_CARDS_ENABLED = False


def main() -> int:
    if not TOPIC_CARDS_ENABLED:
        print(
            "Generator pseudokart jest wyłączony (TOPIC_CARDS_ENABLED=False).",
            flush=True,
        )
        return 1
    raise RuntimeError("Przywróć implementację dopiero po naprawie jakości §4.")


if __name__ == "__main__":
    raise SystemExit(main())
