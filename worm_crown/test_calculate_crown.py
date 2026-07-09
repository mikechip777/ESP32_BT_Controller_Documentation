#!/usr/bin/env python3
"""Sanity checks for the corrected crown calculation."""

from __future__ import annotations

import math
import sys

from calculate_crown import WormInput, WheelBlankInput, calculate_crown


def approx(a: float, b: float, tol: float = 0.02) -> bool:
    return abs(a - b) <= tol


def main() -> int:
    r = calculate_crown()
    d = r["display"]
    w = r["wheel"]
    worm = r["worm_derived"]

    assert approx(d["m"], 2.021, 0.001), d["m"]
    assert approx(d["d1"], 23.96, 0.02), d["d1"]
    assert approx(d["d"], 303.19, 0.02), d["d"]
    assert approx(d["da"], 307.23, 0.02), d["da"]
    assert approx(d["df"], 298.34, 0.02), d["df"]
    assert approx(d["a"], 163.57, 0.02), d["a"]
    assert approx(d["lambda_deg"], 4.8, 0.1), d["lambda_deg"]

    # Center distance must NOT equal the Rev A (major-diameter) value
    assert abs(d["a"] - 165.58) > 1.5, "a still looks like Rev A"

    # Identity checks
    assert approx(w["center_distance_a_mm"], (worm["pitch_diameter_d1_mm"] + w["pitch_diameter_d_mm"]) / 2)
    assert approx(worm["pitch_diameter_d1_mm"], 28.0 - 2 * w["module_m_mm"])
    assert approx(w["module_m_mm"], 6.35 / math.pi)

    # Lead angle consistency
    lam = math.degrees(
        math.atan(w["worm_lead_L_mm"] / (math.pi * worm["pitch_diameter_d1_mm"]))
    )
    assert approx(lam, d["lambda_deg"], 0.05)

    print("All crown calculation checks passed.")
    print(f"  d1={d['d1']}  d={d['d']}  a={d['a']}  λ={d['lambda_deg']}°")
    return 0


if __name__ == "__main__":
    sys.exit(main())
