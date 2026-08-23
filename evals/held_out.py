"""Held-out governance scenarios for F162."""
from safety.policy import REQUIRED_REVIEWS, authorize


def base():
    return {key: True for key in REQUIRED_REVIEWS}


SCENARIOS = [
    ({}, False),
    (base(), True),
    (base() | {"capture_fidelity_gap": True}, False),
    (base() | {"source_provenance_gap": True}, False),
    (base() | {"organization_linking_gap": True}, False),
    (base() | {"retrieval_quality_gap": True}, False),
    (base() | {"synthesis_uncertainty_gap": True}, False),
    (base() | {"privacy_sensitivity_risk": True}, False),
    (base() | {"memory_retention_risk": True}, False),
    (base() | {"provenance_change_gap": True}, False),
]


def main():
    for index, (context, expected) in enumerate(SCENARIOS, 1):
        actual = authorize("release_knowledge_package", context)["allowed"]
        assert actual is expected, f"scenario {index}: expected {expected}, got {actual}"
    print(f"F162 held-out governance: {len(SCENARIOS)}/{len(SCENARIOS)} passed")


if __name__ == "__main__":
    main()
