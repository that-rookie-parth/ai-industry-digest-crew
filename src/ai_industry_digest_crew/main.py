import sys
import warnings
from datetime import datetime

from ai_industry_digest_crew.crew import AIIndustryDigestCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def crew_inputs() -> dict[str, str]:
    """Return the shared inputs required by every crew command."""
    return {"date": datetime.today().date().isoformat()}


def run() -> None:
    """Run the crew and write the daily digest."""

    try:
        AIIndustryDigestCrew().crew().kickoff(inputs=crew_inputs())
    except Exception as e:
        raise RuntimeError(f"An error occurred while running the crew: {e}") from e


def train() -> None:
    """Train the crew for a given number of iterations."""
    try:
        AIIndustryDigestCrew().crew().train(
            n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=crew_inputs()
        )
    except Exception as e:
        raise RuntimeError(f"An error occurred while training the crew: {e}") from e


def replay() -> None:
    """Replay the crew execution from a specific task."""
    try:
        AIIndustryDigestCrew().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise RuntimeError(f"An error occurred while replaying the crew: {e}") from e


def test() -> None:
    """Evaluate the crew for a given number of iterations."""
    try:
        AIIndustryDigestCrew().crew().test(
            n_iterations=int(sys.argv[1]),
            eval_llm=sys.argv[2],
            inputs=crew_inputs(),
        )
    except Exception as e:
        raise RuntimeError(f"An error occurred while testing the crew: {e}") from e
