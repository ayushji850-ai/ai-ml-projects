def zero_shot(topic):
    return f"""You are an AI Study Assistant for a B.Tech student.
Explain: {topic}
Give a simple definition, key concepts, one real-world example, three important points, and one quiz question.
"""

def one_shot(topic):
    return f"""You are an AI Study Assistant.
Example:
Topic: Binary Search
Style: Definition -> key idea -> example -> key points.
Now use the same style for: {topic}
"""

def few_shot(topic):
    return f"""You are an AI Study Assistant.
Example 1: RAM -> definition -> purpose -> example -> key points.
Example 2: Compiler -> definition -> purpose -> example -> key points.
Now answer: {topic} using the same compact structure.
"""

def task_decomposition(topic):
    return f"""Solve this educational task: {topic}
Break it into:
1. Identify the concept/task.
2. Identify required facts or formulas.
3. Explain the parts.
4. Connect the parts.
5. Give the final exam-ready answer.
Give concise step summaries, not private hidden chain-of-thought.
"""

def cot_safe(topic):
    return f"""Solve: {topic}
Give only:
1. High-level approach
2. Key steps
3. Final answer
4. Quick verification
Do not reveal private hidden chain-of-thought.
"""

def self_consistency(topic):
    return f"""Solve: {topic} using three independent candidate approaches.
For each, give a concise approach summary and result.
Compare the results and provide the most consistent final answer.
Do not reveal private hidden chain-of-thought.
"""

def tree_of_thoughts(topic):
    return f"""Explore: {topic} through three branches:
A) direct explanation
B) example-based explanation
C) exam-oriented explanation
Give concise results for each branch and synthesize a final answer.
Do not reveal private hidden chain-of-thought.
"""

def react_style(topic):
    return f"""Use a ReAct-style workflow for: {topic}
Format:
Thought summary: concise goal
Action: useful operation/information
Observation: result
Final: student-friendly answer
Do not reveal private hidden chain-of-thought.
"""

METHODS = {
    "Zero-shot": zero_shot,
    "One-shot": one_shot,
    "Few-shot": few_shot,
    "Task Decomposition": task_decomposition,
    "Chain-of-Thought-style": cot_safe,
    "Self-Consistency": self_consistency,
    "Tree-of-Thoughts-style": tree_of_thoughts,
    "ReAct-style": react_style,
}
