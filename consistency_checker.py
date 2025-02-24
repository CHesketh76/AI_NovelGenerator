# consistency_checker.py
# -*- coding: utf-8 -*-
from llm_adapters import create_llm_adapter

# ============== 增加对“剧情要点/未解决冲突”进行检查的可选引导 ==============
CONSISTENCY_PROMPT = """\
Please check for any obvious conflicts or inconsistencies between the novel's setting and the latest chapter. If any are found, list them:

- Novel Setting:
{novel_setting}

- Character States (may contain important information):
{character_state}

- Global Summary:
{global_summary}

- Recorded Unresolved Conflicts or Plot Points:
{plot_arcs}  # May not be output if empty

- Latest Chapter Content:
{chapter_text}

If there are any conflicts or inconsistencies, please explain. If there are any unresolved conflicts that have been ignored or need to be advanced, please mention them as well. Otherwise, return “No obvious conflicts”.
"""

def check_consistency(
    novel_setting: str,
    character_state: str,
    global_summary: str,
    chapter_text: str,
    api_key: str,
    base_url: str,
    model_name: str,
    temperature: float = 0.3,
    plot_arcs: str = "",
    interface_format: str = "OpenAI",
    max_tokens: int = 2048,
    timeout: int = 600
) -> str:
    """
    调用模型做简单的一致性检查。可扩展更多提示或校验规则。
    新增: 会额外检查对“未解决冲突或剧情要点”（plot_arcs）的衔接情况。
    """
    prompt = CONSISTENCY_PROMPT.format(
        novel_setting=novel_setting,
        character_state=character_state,
        global_summary=global_summary,
        plot_arcs=plot_arcs,
        chapter_text=chapter_text
    )

    llm_adapter = create_llm_adapter(
        interface_format=interface_format,
        base_url=base_url,
        model_name=model_name,
        api_key=api_key,
        temperature=temperature,
        max_tokens=max_tokens,
        timeout=timeout
    )

    # 调试日志
    print("\n[ConsistencyChecker] Prompt >>>", prompt)

    response = llm_adapter.invoke(prompt)
    if not response:
        return "Review Agent has not responded"

    # 调试日志
    print("[ConsistencyChecker] Response <<<", response)

    return response
