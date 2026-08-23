"""Fail-closed governance for F162 Agentic Personal Knowledge Manager."""

PROTECTED_ACTIONS = {
    "delete_or_overwrite_source_knowledge",
    "share_private_knowledge_externally",
    "store_highly_sensitive_data_without_consent",
    "impersonate_user_in_external_communication",
    "change_access_permissions_or_ownership",
    "silently_rewrite_user_authored_content",
}

REQUIRED_REVIEWS = (
    "capture_fidelity_reviewed",
    "source_provenance_reviewed",
    "organization_linking_reviewed",
    "retrieval_quality_reviewed",
    "synthesis_uncertainty_reviewed",
    "privacy_sensitivity_reviewed",
    "memory_retention_reviewed",
    "user_change_approval_reviewed",
)


def authorize(action: str, context: dict | None = None) -> dict:
    context = context or {}
    if action in PROTECTED_ACTIONS:
        return {"allowed": False, "reason": "destructive knowledge change, external sharing, sensitive-data storage, impersonation, permission change, or silent rewrite is outside autonomous authority"}
    missing = [key for key in REQUIRED_REVIEWS if not context.get(key)]
    if missing:
        return {"allowed": False, "reason": "missing required knowledge-management review", "missing": missing}
    checks = {
        "capture_fidelity_gap": "material content, attribution, date, context, quotation, attachment, or authorship fidelity issue unresolved",
        "source_provenance_gap": "material source identity, location, version, citation, rights, or provenance issue unresolved",
        "organization_linking_gap": "material duplicate, entity-linking, taxonomy, tag, relationship, chronology, or supersession issue unresolved",
        "retrieval_quality_gap": "material recall, precision, stale-result, missing-source, ranking, ambiguity, or query-scope issue unresolved",
        "synthesis_uncertainty_gap": "material unsupported inference, contradiction, source conflict, confidence, or distinction between source fact and generated synthesis unresolved",
        "privacy_sensitivity_risk": "material private, confidential, personal, third-party, credential, financial, legal, health, or sensitive-data handling issue unresolved",
        "memory_retention_risk": "material retention, deletion, forgetting, stale memory, user preference, expiration, or scope issue unresolved",
        "provenance_change_gap": "material capture, edit, merge, summary, link, deletion, retention, source, or user-approval provenance incomplete",
    }
    blockers = [message for key, message in checks.items() if context.get(key)]
    if blockers:
        return {"allowed": False, "reason": "personal-knowledge governance blocker", "blockers": blockers}
    return {"allowed": True, "reason": "personal knowledge package approved for user-controlled use"}


def review_required(action: str) -> bool:
    return action in PROTECTED_ACTIONS
