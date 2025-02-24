# prompt_definitions.py
# -*- coding: utf-8 -*-
"""
集中存放所有提示词 (Prompt)，整合雪花写作法、角色弧光理论、悬念三要素模型等
并包含新增加的短期摘要/下一章关键字提炼提示词，以及章节正文写作提示词。
"""

# =============== 摘要与下一章关键字提炼 ===============
summarize_recent_chapters_prompt = """\
You are a seasoned editor of long-form novels. Please analyze the following merged text (which may include the content of recent chapters):
{combined_text}
Now, based on the current progress of the story, please complete the following two tasks:
1) Write a concise and clear "short-term summary" of the current plot in no more than 200 words.
2) Extract the keywords for the "next chapter" (such as key items, important characters, locations, events, plot points, etc.), which can be listed using commas or bullet points.
Please output in the following format (no additional explanation required):
Short-term summary: <Write the short-term summary here>
Next chapter keywords: <Write the keywords for the next chapter here>
"""

# =============== 1. 核心种子设定（雪花第1层）===================
core_seed_prompt = """\
As a professional writer, please use the first step of the "Snowflake Method" to construct the story's core:
Theme: {topic}
Type: {genre}
Length: Approximately {number_of_chapters} chapters (each chapter {word_number} words)
Please summarize the essence of the story in a single-sentence formula, for example:
"When [protagonist] encounters [core event], they must [key action], otherwise [disastrous consequence]; meanwhile, [a hidden greater crisis] is brewing."
Requirements:
1. Must include explicit conflict and潜在危机 (hidden greater crisis)
2. Reflect the core driving force of the characters
3. Hint at the key contradictions in the world
4. Use 25-100 words to express precisely
Return only the core story text, without any explanation.
"""

# =============== 2. 角色动力学设定（角色弧光模型）===================
character_dynamics_prompt = """\
Based on the core seed:
{core_seed}

Please design 3-6 core characters with dynamic potential, each including:
Characteristics:
- Background, appearance, gender, age, occupation, etc.
- Hidden secrets or potential weaknesses (can be related to the world or other characters)

Core Motivation Triangle:
- Surface Pursuit (material goals)
- Deep Desires (emotional needs)
- Soul Needs (philosophical level)

Character Arc Design:
Initial State → Triggering Event → Cognitive Dissonance → Transformation Point → Final State

Relationship Conflict Web:
- Relationships or points of conflict with other characters
- Value conflicts with at least two other characters
- A cooperative bond
- A hidden betrayal possibility

Requirement:
Provide only the final text, without any explanations.
"""

# =============== 3. 世界构建矩阵（三维度交织法）===================
world_building_prompt = """\
To serve the core conflict "{core_seed}", please construct a three-dimensional interwoven world view:
1. Physical Dimension:
- Spatial Structure (geographical × social strata distribution map)
- Timeline (chronology of key historical events)
- Rule System (vulnerabilities in physical/magical/social rules)
2. Social Dimension:
- Power Structure Fault Lines (conflicts between classes/races/organizations that can trigger disputes)
- Cultural Taboos (taboos that can be broken and their consequences)
- Economic Lifelines (key points of resource contention)
3. Metaphorical Dimension:
- Visual Symbol System贯穿全书 (such as recurring imagery)
- Climate/Environmental Changes Mirroring Psychological States
- Architectural Styles Hinting at Civilizational Dilemmas

Requirement:
Each dimension must include at least 3 dynamic elements that can interact with character decisions.
Provide only the final text, without any explanations.
"""

# =============== 4. 情节架构（三幕式悬念）===================
plot_architecture_prompt = """\
Construct a three-act suspense structure based on the following elements:
Core Seed: {core_seed}
Character System: {character_dynamics}
Worldview: {world_building}

Design according to the following structure:
First Act (Trigger)
- Signs of abnormality in the daily state (3 setups)
- Introduction of the story:展示主线、暗线、副线的开端 (introduction of the main plot, subplot, and hidden plot)
- Key Event: The catalyst that breaks the balance (must alter the relationships of at least 3 characters)
- Wrong Decision: The protagonist's erroneous response due to cognitive limitations

Second Act (Confrontation)
- Plot Escalation: The intersection of the main plot and subplot
- Dual Pressure: External obstacles intensify + internal setbacks
- False Victory: A turning point that appears to resolve but actually deepens the crisis
- Dark Night of the Soul: The moment of worldview颠覆 (cognitive颠覆) (the moment of worldview upheaval)

Third Act (Resolution)
- Cost Revealed: The core value that must be sacrificed to resolve the crisis
- Nested Twists: At least three layers of cognitive upheaval (surface resolution → new crisis → ultimate decision)
- Aftermath: Leave 2 open-ended suspense factors

Each stage must include 3 key turning points and their corresponding foreshadowing resolutions.
Provide only the final text, without any explanations.
"""

# =============== 5. 章节目录生成（悬念节奏曲线）===================
chapter_blueprint_prompt = """\
Based on the novel architecture:
{novel_architecture}
Design the rhythm distribution for {number_of_chapters} chapters:
1. Chapter Cluster Division:
- Each 3-5 chapters form a suspense unit, containing a complete small climax
- Set up a "cognitive roller coaster" between units (2 consecutive tense chapters → 1 relief chapter)
- Reserve multi-perspective setups for key turning point chapters
2. Each chapter must clearly define:
- Chapter positioning (characters/events/themes, etc.)
- Core suspense type (information gap/moral dilemma/time pressure, etc.)
- Emotional tone transition (e.g., from suspicion → fear → resolution)
- Foreshadowing operations (setup/strengthening/recovery)
- Cognitive upheaval intensity (1-5 levels)
Output format example:
Chapter n - [Title]
Chapter positioning: [characters/events/themes/...]
Core function: [advancement/turning point/revelation/...]
Suspense density: [tight/progressive/explosive/...]
Foreshadowing operations: setup(A clue) → strengthening(B conflict)...
Cognitive upheaval: ★☆☆☆☆
Chapter summary: [one-sentence summary]
Chapter n+1 - [Title]
Chapter positioning: [characters/events/themes/...]
Core function: [advancement/turning point/revelation/...]
Suspense density: [tight/progressive/explosive/...]
Foreshadowing operations: setup(A clue) → strengthening(B conflict)...
Cognitive upheaval: ★☆☆☆☆
Chapter summary: [one-sentence summary]
Requirements:
- Use concise language to describe, with each chapter summary controlled to within 100 words.
- Arrange the rhythm reasonably to ensure the continuity of the overall suspense curve.
- Do not include a conclusion chapter before generating {number_of_chapters} chapters.
Provide only the final text, without any explanations.
"""

chunked_chapter_blueprint_prompt = """\
Based on the novel architecture:
{novel_architecture}
We need to generate the rhythm distribution for a total of {number_of_chapters} chapters.
Current chapter list (if empty, it indicates initial generation):
{chapter_list}
Now please design the rhythm distribution from Chapter {n} to Chapter {m}:
1. Chapter Cluster Division:
- Each 3-5 chapters form a suspense unit, containing a complete small climax
- Set up a "cognitive roller coaster" between units (2 consecutive tense chapters → 1 relief chapter)
- Reserve multi-perspective setups for key turning point chapters
2. Each chapter must clearly define:
- Chapter positioning (characters/events/themes, etc.)
- Core suspense type (information gap/moral dilemma/time pressure, etc.)
- Emotional tone transition (e.g., from suspicion → fear → resolution)
- Foreshadowing operations (setup/strengthening/recovery)
- Cognitive upheaval intensity (1-5 levels)
Output format example:
Chapter n - [Title]
Chapter positioning: [characters/events/themes/...]
Core function: [advancement/turning point/revelation/...]
Suspense density: [tight/progressive/explosive/...]
Foreshadowing operations: setup(A clue) → strengthening(B conflict)...
Cognitive upheaval: ★☆☆☆☆
Chapter summary: [one-sentence summary]
Chapter n+1 - [Title]
Chapter positioning: [characters/events/themes/...]
Core function: [advancement/turning point/revelation/...]
Suspense density: [tight/progressive/explosive/...]
Foreshadowing operations: setup(A clue) → strengthening(B conflict)...
Cognitive upheaval: ★☆☆☆☆
Chapter summary: [one-sentence summary]
Requirements:
- Use concise language to describe, with each chapter summary controlled to within 100 words.
- Arrange the rhythm reasonably to ensure the continuity of the overall suspense curve.
- Do not include a conclusion chapter before generating {number_of_chapters} chapters.
Provide only the final text, without any explanations.
"""

# =============== 6. Global Summary Update ===================
summary_prompt = """\
Here is the text of the newly completed chapter:
{chapter_text}

This is the current global summary (can be empty):
{global_summary}

Please update the global summary based on the new content added in this chapter.
Requirements:
- Retain existing important information while incorporating new plot points
- Describe the progress of the entire book in concise and coherent language
- Objectively depict, do not elaborate or explain
- Keep the word count within 2000 words

Return only the updated global summary text, without any explanations.
"""

# =============== 7. Character State Update ===================
create_character_state_prompt = """\
Based on the current character dynamics settings: {character_dynamics}

Please generate a character state document with the following format:
Character A Attributes:
├── Items:
    ├── Item (add if there are initial items, otherwise "None"): Description
    ...
├── Abilities
    ├── Skill 1 (add if there are initial skills, otherwise "None"): Description
    ...
├── Status
    ├── Physical Status:
        ├── Buff/Debuff
    ├── Mental Status: Description

├── Relationship Network with Major Characters
    ├── Character B: Description (add if there is an initial relationship, otherwise "No relationship")
    ├── Character C: Description (add if there is an initial relationship, otherwise "No relationship")
    ...
├── Triggered or Deepened Events
    ├── No events
    ...

Character B Attributes:
├── Items
    ├──...
├── Abilities
    ├──...
├── Status
    ├──...
├── Relationship Network with Major Characters
    ├──...
├── Triggered or Deepened Events
    ├──...

Character C Attributes:
......

New Characters:
- (Fill in the basic information of any new characters or temporary appearances here)

Requirements:
Return only the prepared character state text, without any explanations.
"""

update_character_state_prompt = """\
Here is the text of the newly completed chapter:
{chapter_text}

This is the current character state document:
{old_state}

Please update the main character states with the following format:
Character A Attributes:
├── Items:
    ├── Item (prop): Description
    ├── XX Sword (weapon): Description
    ...
├── Abilities
    ├── Skill 1: Description
    ├── Skill 2: Description
    ...
├── Status
    ├── Physical Status:
        ├── Buff/Debuff
    ├── Mental Status: Description

├── Relationship Network with Major Characters
    ├── Character B: Description
    ├── Character C: Description
    ...
├── Triggered or Deepened Events
    ├── Event 1: Description
    ├── Event 2: Description
    ...

Character B Attributes:
├── Items
    ├──...
├── Abilities
    ├──...
├── Status
    ├──...
├── Relationship Network with Major Characters
    ├──...
├── Triggered or Deepened Events
    ├──...

Character C Attributes:
......

New Characters:
- Briefly describe any new characters or temporary appearances, do not elaborate, and remove characters who have faded from the story.

Requirements:
- Directly add or delete information on the existing document
- Do not change the original structure, keep the language concise and organized

Return only the updated character state text, without any explanations.
"""

# =============== 8. Chapter Writing ===================
# 8.1 First Chapter Draft Prompt
first_chapter_draft_prompt = """\
Upcoming creation: Chapter {novel_number} 《{chapter_title}》
Chapter Positioning: {chapter_role}
Core Function: {chapter_purpose}
Suspense Density: {suspense_level}
Foreshadowing Operations: {foreshadowing}
Cognitive Upheaval: {plot_twist_level}
Chapter Summary: {chapter_summary}
Available Elements:
- Main Characters (may be unspecified): {characters_involved}
- Key Items (may be unspecified): {key_items}
- Spatial Coordinates (may be unspecified): {scene_location}
- Time Pressure (may be unspecified): {time_constraint}
Reference Documents:
- Novel Setting:
{novel_setting}
Please complete the main text of Chapter {novel_number}, with a word count of {word_number} words. Design at least 2 or more dynamically tense scenes as follows:
1. Dialogue Scene:
   - Subtext Conflict (surface discussion A, actual博弈 B)
   - Power Dynamics (reflected through asymmetrical dialogue lengths)
   - At least 1 double entendre hinting at future crisis
2. Action Scene:
   - Environmental Interaction Details (at least 3 sensory descriptions)
   - Rhythm Control (short sentences accelerate + metaphors decelerate)
   - Actions reveal hidden character traits
3. Psychological Scene:
   - Cognitive Dissonance (behavioral contradictions)
   - Use of Metaphorical Systems (connecting to world symbols)
   - Description of value scales before decision-making
4. Environmental Scene:
   - Spatial Perspective Changes (macro → micro → abnormal focus)
   - Unconventional Sensory Combinations (e.g., "hearing the weight of sunlight")
   - Dynamic Environment Reflecting Psychology (environment mirrors character psychology)
   - Hidden Clue Implantation (environment hints at future events)
Set a "hook-link twist" at the end: conclude by resolving old suspense, creating new suspense, introducing a new crisis, overturning a perception, or a surprising twist.
Format Requirements:
- Return only the chapter main text;
- Do not use sub-chapter titles;
- Do not use markdown format.
Additional Guidance (may be unspecified): {user_guidance}
"""

# 8.2 Subsequent Chapter Draft Prompt
next_chapter_draft_prompt = """\
Reference Documents:
- Novel Setting:
{novel_setting}
- Global Summary:
{global_summary}
- Character State:
{character_state}
Local Knowledge Base Excerpts:
{context_excerpt}
Upcoming creation: Chapter {novel_number} 《{chapter_title}》
Chapter Positioning: {chapter_role}
Core Function: {chapter_purpose}
Suspense Density: {suspense_level}
Foreshadowing Operations: {foreshadowing}
Cognitive Upheaval: {plot_twist_level}
Chapter Summary: {chapter_summary}
Available Elements:
- Main Characters (may be unspecified): {characters_involved}
- Key Items (may be unspecified): {key_items}
- Spatial Coordinates (may be unspecified): {scene_location}
- Time Pressure (may be unspecified): {time_constraint}
End of Previous Chapter:
{previous_chapter_excerpt}
Based on the ending of the previous chapter, begin completing the main text of Chapter {novel_number}, with a word count of {word_number} words. Ensure smooth continuity with the previous chapter's ending.
Design at least 2 or more dynamically tense scenes as follows:
1. Dialogue Scene:
   - Subtext Conflict (surface discussion A, actual博弈 B)
   - Power Dynamics (reflected through asymmetrical dialogue lengths)
   - At least 1 double entendre hinting at future crisis
2. Action Scene:
   - Environmental Interaction Details (at least 3 sensory descriptions)
   - Rhythm Control (short sentences accelerate + metaphors decelerate)
   - Actions reveal hidden character traits
3. Psychological Scene:
   - Cognitive Dissonance (behavioral contradictions)
   - Use of Metaphorical Systems (connecting to world symbols)
   - Description of value scales before decision-making
4. Environmental Scene:
   - Spatial Perspective Changes (macro → micro → abnormal focus)
   - Unconventional Sensory Combinations (e.g., "hearing the weight of sunlight")
   - Dynamic Environment Reflecting Psychology (environment mirrors character psychology)
   - Hidden Clue Implantation (environment hints at future events)
Set a "hook-link twist" at the end: conclude by resolving old suspense, creating new suspense, introducing a new crisis, overturning a perception, or a surprising twist.
Format Requirements:
- Return only the chapter main text;
- Do not use sub-chapter titles;
- Do not use markdown format.
Additional Guidance (may be unspecified): {user_guidance}
"""
