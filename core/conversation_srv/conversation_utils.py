from core.conversation_srv.conversation_prompts import *
from core.utils.llm_factory import LLMSelector
from core.conversation_srv.conversation_model import *

llm_selector = LLMSelector()


def conversation_llm(prompt_template, model_name, output_type, temperature=1):
    return prompt_template | llm_selector.get_llm(
        model_type="CHAT", model_name=model_name, temperature=temperature
    ).with_structured_output(output_type)


conversation_topic_planner = conversation_llm(
    prompt_template=conversation_topic_planner_prompt,
    model_name="gpt-4o-mini",
    output_type=ConversationTopics
)

conversation_planner = conversation_llm(
    prompt_template=conversation_planner_prompt,
    model_name="gpt-4o-mini",
    output_type=PreConversationTask
)

conversation_check = conversation_llm(
    prompt_template=conversation_check_prompt,
    model_name="gpt-4o-mini",
    output_type=CheckResult,
    temperature=0
)

conversation_responser = conversation_llm(
    prompt_template=conversation_responser_prompt,
    model_name="gpt-4o-mini",
    output_type=PreResponse
)

impression_update = conversation_llm(
    prompt_template=impression_update_prompt,
    model_name="gpt-4o-mini",
    output_type=ImpressionUpdate
)

conversation_intimacy_mark = conversation_llm(
    prompt_template=intimacy_mark_prompt,
    model_name="gpt-4o-mini",
    output_type=IntimacyMark
)


