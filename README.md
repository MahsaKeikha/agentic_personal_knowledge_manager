# F162 | Agentic Personal Knowledge Manager | L3 Gold Standard | v1.0

A governed five-agent reference architecture for personal knowledge management across capture, source provenance, organization, retrieval, synthesis, review, privacy, retention, permissions, and user-controlled knowledge changes.

F162 is a knowledge-support system. It is not an autonomous archivist with authority over the user's information, a document custodian, records officer, legal authority, identity system, access-control administrator, or external publisher. It cannot destructively delete or overwrite source knowledge, share private knowledge externally, store highly sensitive data without consent, impersonate the user, change permissions or ownership, or silently rewrite user-authored content.

## Knowledge-management lifecycle

```text
Capture
        -> Source and Provenance Registration
        -> Organization and Linking
        -> Retrieval
        -> Synthesis and Uncertainty Review
        -> User Review
        -> User-Controlled Retention, Revision, or Sharing
```

The workflow fails closed when required reviews are missing or when material capture-fidelity, provenance, organization, retrieval, synthesis, privacy, retention, or change-history issues remain unresolved.

## Five-agent architecture

| Agent | Responsibility | Core question |
|---|---|---|
| Capture Agent | Preserves notes, documents, excerpts, dates, authorship, attachments, context, and source boundaries | What information was actually captured, and what must not be altered? |
| Organize Agent | Structures tags, folders, entities, topics, projects, chronology, links, duplicates, and supersession | How should knowledge be organized without destroying source meaning? |
| Retrieval Agent | Finds relevant knowledge using scope, source, recency, authority, ranking, and ambiguity controls | What stored evidence is most relevant to this request? |
| Synthesis Agent | Combines source-grounded material while preserving disagreement, uncertainty, provenance, and distinction between source facts and generated interpretation | What can responsibly be inferred from the available knowledge? |
| Review Agent | Reviews fidelity, privacy, retention, revisions, permissions, provenance, and user approval before consequential changes | Is this knowledge package safe and faithful enough for user-controlled use? |

## Repository structure

```text
AGENTS/
├── capture_agent.py
├── organize_agent.py
├── retrieval_agent.py
├── synthesis_agent.py
└── review_agent.py

SKILLS/
├── tagging.py
├── linking.py
├── retrieval_reasoning.py
├── summarization.py
└── quality_review.py

TOOLS/
├── note_store.py
├── source_registry.py
├── tag_index.py
├── search_index.py
└── approval_gate.py

orchestration/
memory/
observability/
evals/
benchmarks/
examples/
docs/
prompts/
config/
safety/
tests/
.github/workflows/ci.yml
run.py
pyproject.toml
README.md
```

## Source-first architecture

The central design principle is that captured source material and generated knowledge products are different objects. A source can be summarized, tagged, linked, quoted, annotated, or superseded, but the original source should remain distinguishable from those transformations.

## Capture fidelity

The executable policy requires `capture_fidelity_reviewed`. `capture_fidelity_gap` blocks release when material content, attribution, date, context, quotation, attachment, or authorship fidelity issues remain unresolved.

## Source versus note

A source is material originating from a person, document, file, message, website, recording, dataset, or other evidence object. A note is the user's or system's interpretation, annotation, summary, question, or reflection about that source.

F162 should never silently convert a generated summary into the original source.

## Exact quotations

Quoted text should remain clearly marked and should not be rewritten while still presented as a quotation.

## Paraphrases

Paraphrases should be labeled as paraphrases when confusion with the source wording is material.

## Authorship

The system should preserve who created a source, note, annotation, summary, or synthesis whenever known.

## Timestamps

Capture date, source publication date, event date, modification date, and retrieval date can differ. These should remain distinct when material.

## Attachments

Attachments should preserve filename, type, source relationship, version, and capture context where available.

## Partial captures

A clipped excerpt should not be treated as though the complete source was captured. Missing surrounding context should remain visible.

## OCR and extraction

Text extracted from scanned or image-based documents can contain recognition errors. F162 should preserve extraction uncertainty and, when necessary, the link to the original page or image.

## Audio and transcripts

Transcripts can contain speaker-attribution and recognition errors. Generated transcripts should not be represented as verbatim ground truth without qualification.

## Source provenance

The executable policy requires `source_provenance_reviewed`. `source_provenance_gap` blocks release when material source identity, location, version, citation, rights, or provenance issues remain unresolved.

## Source registry

`TOOLS/source_registry.py` can preserve source identifier, title, author, origin, date, capture date, version, format, location, access state, rights, reliability, relationship to other sources, and supersession status.

## Source identity

Files with similar names, forwarded messages, copied notes, screenshots, and duplicated exports can refer to different or identical underlying sources. Identity should not be inferred solely from display name.

## Versioning

Documents, notes, and data can change. Version-sensitive knowledge should preserve which version supported a claim or summary.

## Supersession

A newer version can supersede an older version without erasing the older record. Historical versions can be important for understanding changes and decisions.

## Citations

Generated syntheses should retain citations or source references sufficient to trace material claims back to supporting knowledge objects.

## Broken references

Deleted, moved, inaccessible, or expired sources should be flagged rather than silently treated as available evidence.

## Rights and usage

A user may possess a document without having unrestricted rights to republish it. The system should distinguish private knowledge use from external redistribution.

## Organization architecture

The executable policy requires `organization_linking_reviewed`. `organization_linking_gap` blocks release when material duplicate, entity-linking, taxonomy, tag, relationship, chronology, or supersession issues remain unresolved.

## Tags

Tags should support retrieval rather than become an uncontrolled vocabulary. Synonyms, aliases, capitalization, singular versus plural, and hierarchical relationships can be normalized where useful.

## Taxonomies

Taxonomies can organize topics, projects, people, organizations, research themes, life areas, document types, or other user-defined domains.

A taxonomy should not force every item into one rigid hierarchy when multiple views are useful.

## Folders

Folders can provide location-based organization while tags and links provide cross-cutting organization.

## Backlinks

Backlinks can show where a note, source, concept, project, or entity is referenced elsewhere.

## Entities

Entities can include people, organizations, places, products, projects, concepts, events, and documents. Entity resolution should preserve ambiguity when names collide.

## Aliases

Different names can refer to the same entity, and the same name can refer to different entities. Alias mapping should remain reviewable.

## Relationships

Links can encode relationships such as supports, contradicts, cites, summarizes, belongs to, depends on, supersedes, derived from, or related to.

## Knowledge graph boundaries

Graph edges are assertions. The system should preserve whether a relationship came directly from a source, from the user, or from generated inference.

## Chronology

Events should preserve event date separately from the date on which the note or source was captured.

## Duplicates

Duplicate detection should distinguish exact duplicate, near duplicate, version, quoted copy, derived summary, and independent source repeating the same information.

## Deduplication

Automatic deduplication should not destructively remove knowledge when the system cannot confidently distinguish duplicate from independent evidence.

## Contradictions

Conflicting notes or sources should be preserved and linked rather than merged into artificial consensus.

## Retrieval architecture

The executable policy requires `retrieval_quality_reviewed`. `retrieval_quality_gap` blocks release when material recall, precision, stale-result, missing-source, ranking, ambiguity, or query-scope issues remain unresolved.

## Query intent

Retrieval should distinguish requests for exact source text, factual recall, broad research, recent information, a known document, a person's notes, a project history, or a generated synthesis.

## Scope

A query can be scoped by project, folder, source type, date, person, tag, privacy level, workspace, or other boundary.

F162 should not silently search beyond the user's intended scope.

## Precision and recall

Highly precise retrieval can miss relevant sources, while broad retrieval can introduce noise. Retrieval strategies should match the task.

## Recency

Recent sources can be more relevant for current facts, while older sources can be essential for history, rationale, or original decisions.

## Authority

A primary source can deserve more weight than a secondary summary for some claims. Authority is claim dependent.

## Ranking

Ranking should not erase lower-ranked contradictory evidence when disagreement is material.

## Search index

`TOOLS/search_index.py` can maintain searchable representations while preserving links back to canonical sources.

## Embeddings

Semantic embeddings can improve retrieval but can also surface conceptually similar yet factually unrelated content. Retrieved items should remain grounded in identifiable sources.

## Keyword search

Exact keyword and phrase search can be necessary for names, codes, quotations, dates, or specialized terminology.

## Hybrid retrieval

Combining semantic and lexical retrieval can improve coverage, especially when user vocabulary differs from source vocabulary.

## Stale retrieval

A once-relevant source can become outdated. Version and recency should remain available to the ranking process.

## Missing knowledge

Failure to retrieve evidence should not be converted into evidence that the information does not exist.

## Synthesis architecture

The executable policy requires `synthesis_uncertainty_reviewed`. `synthesis_uncertainty_gap` blocks release when material unsupported inference, contradiction, source conflict, confidence, or distinction between source fact and generated synthesis remains unresolved.

## Source facts versus synthesis

Generated synthesis is a new knowledge object. It should preserve which claims are directly supported, inferred, uncertain, disputed, or unknown.

## Summaries

A summary should preserve the source's main meaning, material qualifications, and relevant disagreement. Compression should not turn nuanced statements into categorical claims.

## Multi-source synthesis

When sources agree, the synthesis can summarize the convergence. When sources conflict, the synthesis should identify the disagreement and relevant evidence rather than silently choosing one side.

## Confidence

Confidence should reflect evidence quality, source agreement, recency, completeness, and ambiguity rather than writing style.

## Unknowns

Unknown or missing information should remain unknown rather than being filled with plausible-sounding generated content.

## Assumptions

Assumptions introduced during synthesis should be explicit when material.

## Inference chains

Long inference chains can magnify error. Important conclusions should remain traceable to direct evidence and intermediate reasoning.

## Hallucination control

F162 must not invent sources, quotes, authors, dates, events, relationships, citations, file contents, user decisions, or historical facts.

## Review architecture

The executable policy requires `user_change_approval_reviewed`. The Review Agent verifies fidelity, privacy, retention, user intent, and change provenance before consequential knowledge changes.

## Privacy architecture

The executable policy requires `privacy_sensitivity_reviewed`. `privacy_sensitivity_risk` blocks release when material private, confidential, personal, third-party, credential, financial, legal, health, or sensitive-data handling issues remain unresolved.

## Personal information

Knowledge bases can contain names, addresses, messages, relationships, finances, employment, legal matters, identity documents, calendars, travel, health, and other personal information.

## Third-party information

Information about another person can be private even if the user possesses it. The system should avoid unnecessary exposure or redistribution.

## Credentials and secrets

Passwords, API keys, one-time codes, private keys, seed phrases, authentication tokens, and similar secrets should not be stored in ordinary knowledge notes.

## Financial information

Bank records, tax documents, account identifiers, investment records, and payment information can require stronger protection and access controls.

## Legal information

Contracts, disputes, legal advice, immigration records, estate documents, and litigation material can be confidential or privileged.

## Health information

Medical records and health-related notes can be highly sensitive. Storage, access, sharing, and retention should reflect user intent and applicable controls.

## Minors and vulnerable persons

Sensitive knowledge concerning minors or vulnerable people deserves additional caution around access, sharing, and inference.

## Classification

Users can classify knowledge by sensitivity such as public, internal, private, confidential, highly sensitive, or another user-defined scheme.

## Data minimization

Capture should preserve useful context without collecting unnecessary sensitive detail.

## Need to know

Access to a knowledge object should reflect legitimate user intent and permissions rather than maximum technical availability.

## External sharing boundary

`share_private_knowledge_externally` is protected. Creating a summary is different from sending it to another person or publishing it.

## Sensitive-storage boundary

`store_highly_sensitive_data_without_consent` is protected. F162 should not decide on its own that a sensitive item belongs in persistent memory.

## Permission boundary

`change_access_permissions_or_ownership` is protected. The system should not broaden or narrow access rights without explicit authorization.

## User impersonation boundary

`impersonate_user_in_external_communication` is protected. The system can prepare drafts but cannot present itself externally as the user without authorized execution.

## Memory and retention architecture

The executable policy requires `memory_retention_reviewed`. `memory_retention_risk` blocks release when material retention, deletion, forgetting, stale memory, user preference, expiration, or scope issues remain unresolved.

## Persistent versus session knowledge

Not all useful context should become permanent memory. Temporary working context and durable knowledge should be distinguishable.

## Retention

Retention policies can vary by source type, sensitivity, legal requirement, project lifecycle, user preference, and practical value.

## Expiration

Time-sensitive knowledge can have an expiration or review date after which it should be revalidated before reuse.

## Forgetting

Users should be able to remove or retire information they no longer want retained, subject to any legitimate system or legal constraints outside this reference architecture.

## Stale memory

Old preferences, roles, relationships, projects, locations, or plans should not silently override newer confirmed information.

## Correction

When the user corrects a fact, the system should preserve the correction and avoid repeatedly resurfacing the superseded version as current truth.

## Retraction

A source or claim can later be retracted or invalidated. Retraction state should remain visible to downstream synthesis.

## Destructive-change boundary

`delete_or_overwrite_source_knowledge` is protected. F162 can propose deletion, archival, merge, or supersession, but destructive actions require explicit user authorization.

## Silent-rewrite boundary

`silently_rewrite_user_authored_content` is protected. User-authored notes should not be rewritten in place without making the edit visible or obtaining authorization.

## Revision architecture

Generated revisions should preserve source text, proposed changes, rationale, and approval state when the original content matters.

## Merge operations

Merging notes can improve organization but can also erase provenance. The merged object should retain references to source notes.

## Archive versus delete

Archiving preserves history while reducing active clutter. Deletion removes access and should require stronger certainty and authorization.

## Knowledge ownership

The system should preserve the distinction between user-owned notes, shared workspace content, third-party documents, licensed material, and generated artifacts.

## Copyright and intellectual property

Personal knowledge management can include copyrighted books, papers, articles, code, images, presentations, and recordings. Private analysis does not automatically imply rights to redistribute content.

## Attribution

Where attribution matters, the system should preserve the original author or source rather than making generated synthesis appear to be the user's original work.

## Plagiarism boundaries

F162 can help cite and paraphrase sources but should not intentionally disguise copied material as original authorship.

## Research notes

Research notes should distinguish direct evidence, quotation, paraphrase, hypothesis, interpretation, question, and conclusion.

## Literature reviews

Literature synthesis should preserve citations, methodological limitations, disagreement, publication dates, and retractions where material.

## Meeting notes

Meeting notes can preserve attendees, date, decisions, actions, unresolved questions, and whether statements were verified or merely discussed.

## Decision records

Decision records should preserve the decision, options, rationale, evidence, assumptions, dissent, owner, date, and conditions for review.

## Project knowledge

Project knowledge can connect goals, requirements, decisions, tasks, research, risks, deliverables, stakeholders, and lessons learned.

## Personal journals

Journal entries can contain private reflections, emotional states, incomplete thoughts, and sensitive third-party information. Generated interpretation should not overwrite the original entry.

## Idea management

Ideas can be captured without being treated as commitments, facts, or finished plans.

## Reading notes

Reading notes should preserve title, author, source, location or page when useful, direct quotations, and the user's interpretation.

## Learning systems

Knowledge management can support spaced review, concept linking, flashcards, questions, and teaching notes while preserving source fidelity.

## Contact knowledge

Notes about people should avoid unnecessary sensitive profiling and should distinguish facts provided by the person from user impressions or generated inferences.

## Temporal knowledge

Facts can change. Employment, relationships, addresses, roles, policies, product information, research consensus, and project status may need effective dates.

## Event sourcing

For important mutable knowledge, preserving a sequence of changes can be more reliable than overwriting the current state without history.

## Change provenance

`provenance_change_gap` blocks release when material capture, edit, merge, summary, link, deletion, retention, source, or user-approval provenance is incomplete.

## Audit trail

A useful audit trail can record who or what changed a knowledge object, what changed, when, why, source references, and approval state.

## Observability

The `observability/` layer supports traceability across capture, source registration, linking, retrieval, synthesis, privacy classification, retention, revisions, approvals, and protected-action attempts.

Useful telemetry includes orphaned sources, broken references, duplicate clusters, stale notes, unresolved contradictions, uncited synthesis claims, sensitive-data flags, expired knowledge, destructive-change attempts, and pending approvals.

## Required reviews

The executable policy requires all eight conditions:

```text
capture_fidelity_reviewed
source_provenance_reviewed
organization_linking_reviewed
retrieval_quality_reviewed
synthesis_uncertainty_reviewed
privacy_sensitivity_reviewed
memory_retention_reviewed
user_change_approval_reviewed
```

Missing any condition fails closed.

## Fail-closed governance

The implemented policy blocks release when:

- content, attribution, date, context, quotation, attachment, or authorship fidelity remains unresolved
- source identity, location, version, citation, rights, or provenance remains unresolved
- duplicate, entity-linking, taxonomy, tag, relationship, chronology, or supersession issues remain unresolved
- recall, precision, stale results, missing sources, ranking, ambiguity, or query-scope issues remain unresolved
- unsupported inference, contradiction, source conflict, confidence, or source-versus-synthesis distinctions remain unresolved
- private, confidential, personal, third-party, credential, financial, legal, health, or other sensitive-data issues remain unresolved
- retention, deletion, forgetting, stale memory, user preference, expiration, or scope issues remain unresolved
- capture, edit, merge, summary, link, deletion, retention, source, or user-approval provenance is incomplete
- any required review is missing
- user change approval is missing

## Protected actions

```text
delete_or_overwrite_source_knowledge
share_private_knowledge_externally
store_highly_sensitive_data_without_consent
impersonate_user_in_external_communication
change_access_permissions_or_ownership
silently_rewrite_user_authored_content
```

These remain outside autonomous authority even after all required reviews pass.

## Human authority boundaries

F162 must not autonomously destroy source knowledge, broaden sharing, retain highly sensitive information without consent, impersonate the user, change access permissions, erase provenance, or silently rewrite original content.

The user or properly authorized workspace owners retain authority over deletion, sharing, permissions, retention, publication, ownership, and consequential knowledge changes.

## Explicit failure states

```text
CAPTURE FIDELITY REVIEW REQUIRED
SOURCE PROVENANCE REVIEW REQUIRED
ORGANIZATION AND LINKING REVIEW REQUIRED
RETRIEVAL QUALITY REVIEW REQUIRED
SYNTHESIS AND UNCERTAINTY REVIEW REQUIRED
PRIVACY AND SENSITIVITY REVIEW REQUIRED
MEMORY AND RETENTION REVIEW REQUIRED
USER CHANGE APPROVAL REQUIRED
CAPTURE FIDELITY GAP
SOURCE PROVENANCE GAP
ORGANIZATION OR LINKING GAP
RETRIEVAL QUALITY GAP
SYNTHESIS OR UNCERTAINTY GAP
PRIVACY OR SENSITIVITY RISK
MEMORY OR RETENTION RISK
PROVENANCE OR CHANGE-HISTORY GAP
DESTRUCTIVE KNOWLEDGE CHANGE PROHIBITED
PRIVATE KNOWLEDGE SHARING PROHIBITED
UNCONSENTED SENSITIVE STORAGE PROHIBITED
USER IMPERSONATION PROHIBITED
PERMISSION OR OWNERSHIP CHANGE PROHIBITED
SILENT USER-CONTENT REWRITE PROHIBITED
```

## End-to-end reference workflow

1. Capture the knowledge object while preserving original content, context, authorship, dates, attachments, and source boundaries.
2. Register the source with identity, location, version, rights, citation, capture date, and supersession state.
3. Classify the object as source, user note, annotation, generated summary, synthesis, decision record, or other appropriate type.
4. Organize using tags, taxonomies, entities, chronology, backlinks, relationships, duplicates, and supersession while preserving provenance.
5. Retrieve using the user's intended scope, source authority, recency, semantic relevance, exact-match needs, privacy, and ambiguity controls.
6. Synthesize only from identifiable evidence, preserving contradictions, assumptions, unknowns, confidence, and source-versus-inference distinctions.
7. Review privacy, third-party information, sensitive data, credentials, sharing boundaries, and access requirements.
8. Review persistence, retention, expiration, stale memory, corrections, retractions, forgetting, archive, merge, and deletion implications.
9. Preserve complete change provenance for edits, links, merges, summaries, revisions, retention changes, and user approvals.
10. Apply fail-closed governance and present consequential changes for user approval.
11. Maintain canonical sources separately from derived artifacts.
12. Keep destructive edits, private sharing, unconsented sensitive storage, impersonation, permission changes, and silent rewriting outside autonomous authority.

## Evaluation and held-out governance suite

The repository contains evaluation logic under `evals/` and benchmark cases under `benchmarks/`.

Evaluation should test capture fidelity, source traceability, version handling, duplicate detection, linking quality, retrieval relevance, stale-source handling, contradiction preservation, synthesis grounding, privacy, retention, provenance, and protected-action behavior.

The behavioral verification layer includes direct governance tests and a 10-scenario held-out suite covering missing review, approved knowledge-package release, capture-fidelity gaps, source-provenance gaps, organization-linking gaps, retrieval-quality gaps, synthesis-uncertainty gaps, privacy risks, retention risks, and change-provenance gaps.

## Verification gates

CI runs on Python 3.10, 3.11, and 3.12 and requires:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

These gates verify syntax-critical linting, fail-closed governance, held-out scenarios, and execution of the governed five-agent personal-knowledge workflow.

## Reproducibility

A reproducible knowledge product should preserve source identifiers, versions, query scope, retrieval set, ranking or selection logic where material, synthesis version, assumptions, citations, transformations, review findings, and approval state.

## Extension points

Organization-specific implementations can add governed integrations for note applications, document libraries, cloud storage, email, calendars, reference managers, task systems, research databases, knowledge graphs, vector stores, and collaboration platforms.

Any integration capable of deleting source files, editing originals, changing permissions, sharing private material, sending external messages, or modifying persistent sensitive memory should remain behind explicit user authorization, previews, least privilege, audit logging, and recoverable workflows where feasible.

## Example applications

Potential governed uses include research notebooks, second-brain systems, reading notes, literature reviews, project knowledge bases, meeting notes, decision journals, personal archives, learning systems, idea libraries, source-grounded writing, and long-term personal knowledge retrieval.

F162 is not an autonomous records officer, document owner, permission administrator, external publisher, identity authority, or substitute for the user's judgment about what should be remembered, changed, shared, or forgotten.

## Design principles

1. Preserve canonical source material separately from generated summaries and interpretations.
2. Make every material synthesis traceable to identifiable source knowledge.
3. Preserve contradictions, uncertainty, version history, and source context rather than forcing artificial consistency.
4. Treat privacy, third-party information, credentials, sensitive data, retention, and access as first-class knowledge concerns.
5. Never fabricate sources, quotations, authorship, dates, file contents, citations, user decisions, or completed actions.
6. Prefer archive, supersession, and reversible change over destructive modification when certainty is low.
7. Keep user-authored content visibly distinct from machine-generated rewrites and suggestions.
8. Fail closed when fidelity, provenance, organization, retrieval, synthesis, privacy, retention, or change history is incomplete.
9. Keep deletion, private sharing, sensitive storage, impersonation, permission changes, and silent rewrites under explicit human control.

## Scope statement

F162 demonstrates a governed multi-agent architecture for personal knowledge management. It combines specialized capture, organize, retrieval, synthesis, and review agents with deterministic note, source, tag, search, and approval tools, observability, held-out evaluation, and fail-closed governance while preserving strict user authority over destructive changes, sensitive retention, permissions, sharing, external communication, and original content.

Author: Mahsa Keikha
