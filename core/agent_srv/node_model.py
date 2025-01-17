from pydantic import BaseModel, Field
from typing_extensions import List, Annotated, TypedDict, Dict, Any, Optional
import asyncio


def generic_reducer(a, b):
    if isinstance(a, dict) and isinstance(b, dict):
        result = a.copy()
        for key in b:
            if key in a:
                result[key] = generic_reducer(a[key], b[key])
            else:
                result[key] = b[key]
        return result
    elif isinstance(a, list) and isinstance(b, list):
        return a + b
    else:
        return b


class CharacterStats(TypedDict):
    name: str
    gender: str
    slogan: str
    description: str
    role: str
    inventory: Dict[str, Any]
    health: int
    energy: int
    education: str


class Decision(TypedDict):
    need_replan: bool
    action_description: List[str]
    action_result: List[str]
    new_plan: List[str]
    daily_objective: List[str]
    meta_seq: List[str]
    reflection: List[str]


class Meta(TypedDict):
    tool_functions: str
    day: str
    available_locations: List[str]


class Prompts(TypedDict):
    daily_goal: str
    refer_to_previous: str
    life_style: str
    daily_objective_ar: str
    task_priority: List[str]
    max_actions: int
    meta_seq_ar: str
    replan_time_limit: int
    meta_seq_adjuster_ar: str
    focus_topic: List[str]
    depth_of_reflection: str
    reflection_ar: str
    level_of_detail: str
    tone_and_style: str


class PublicData(TypedDict):
    market_data: Dict[str, Any]


class RunningState(TypedDict):
    userid: int
    character_stats: Annotated[CharacterStats, generic_reducer]
    decision: Annotated[Decision, generic_reducer]
    meta: Annotated[Meta, generic_reducer]
    prompts: Annotated[Prompts, generic_reducer]
    message_queue: asyncio.Queue
    event_queue: asyncio.Queue
    false_action_queue: asyncio.Queue
    public_data: PublicData
    websocket: Any
    current_pointer: str
    instance: Any


class DailyObjective(BaseModel):
    """Daily objective to follow in future"""

    objectives: List[str] = Field(description="daily objectives list")
    past_objectives: Optional[List[str]] = None


class DetailedPlan(BaseModel):
    """Detailed plan to follow in future"""

    detailed_plan: str = Field(description="detailed plan")


class MetaActionSequence(BaseModel):
    """Meta action sequence to follow in future"""

    meta_action_sequence: List[str] = Field(description="meta action sequence")
    action_emoji_sequence: List[str] = Field(
        description="emoji sequence that describes actions"
    )
    state_emoji_sequence: List[str] = Field(
        description="emoji sequence that describes states"
    )
    description_sequence: List[str] = Field(description="description sequence")


class CV(BaseModel):
    """CV to follow in future"""

    job_id: int = Field(description="job id")
    cv: str = Field(description="cv")


class MayorDecision(BaseModel):
    """Mayor decision to follow in future"""

    decision: str = Field(description="yes or no")
    comments: str = Field(description="comments")


class Reflection(BaseModel):
    reflection: str


class Response(BaseModel):
    """Response to user."""

    response: str


class CharacterArc(BaseModel):
    """Character arc to follow in future"""

    belief: str = Field(description="belief")
    mood: str = Field(description="mood")
    values: str = Field(description="values")
    habits: str = Field(description="habits")
    personality: str = Field(description="personality")


class AccommodationDecision(BaseModel):
    """Accommodation decision including accommodation_id and lease_weeks."""

    accommodation_id: int = Field(description="ID of the chosen accommodation")
    lease_weeks: int = Field(description="Number of weeks to lease (1-12)")
    comments: str = Field(description="comments")


if __name__ == "__main__":
    import pprint

    run = RunningState()

    pprint(run)
