from AGENTS import capture_agent, organize_agent, retrieval_agent, review_agent, synthesis_agent
from safety.policy import authorize


def run(case: dict) -> dict:
    result = {
        "capture": capture_agent.run(case),
        "organize": organize_agent.run(case),
        "retrieval": retrieval_agent.run(case),
        "synthesis": synthesis_agent.run(case),
        "review": review_agent.run(case),
    }
    governance = authorize("release_knowledge_package", case.get("governance", {}))
    result["governance"] = governance
    result["released"] = governance["allowed"]
    return result
