"""Narration script + scene specs for the JEV explainer (voiced). Each scene = one narration clip."""
SCENES = [
 dict(id="cover", say="", min_dur=2.6),
 dict(id="hook", say="Okay, so here's something I noticed. When you put an LLM inside your code, you're usually not asking it to write. You're asking it to decide."),
 dict(id="ticket", say="Say a support ticket comes in. I was charged twice for my ride. Your app needs two answers. How urgent is it? And which team should get it?"),
 dict(id="llm", say="With a normal LLM, you just send the text and ask. And it writes something like: this seems fairly urgent, probably the finance team. Now your code has to figure out what fairly urgent means. High? Medium? And which team is the finance team, in your system? That's parsing, and validating. And the wording changes every time."),
 dict(id="problems", say="The founder of TypeSafe AI points out three problems. The output is a string you have to parse. Writing it word by word is slow, and costly. And LLMs are often overconfident. When they're wrong, they don't tell you."),
 dict(id="system1", say="That's where System One models come in. The name comes from Kahneman. System one is fast and intuitive. System two is slow, and step by step. Reasoning models lean toward system two. These are built for fast decisions."),
 dict(id="input", say="Their first model is called Jev. You give it two things. First, your program state. That's just the data you already have. The ticket text, the customer info, the history. It doesn't need to be clean. Second, a schema. Before you ask anything, you list every allowed answer. Urgency: low, medium, or high. Team: billing, safety, or support."),
 dict(id="output", say="Jev can only pick from those options. It returns all of them at once, not word by word. And each one comes with a confidence score. Urgency: high, eighty-two percent. Team: billing, ninety-one percent."),
 dict(id="branch", say="So your code doesn't have to guess. If it's confident, it acts. If it isn't, it hands the case to a human, or to a full LLM."),
 dict(id="numbers", say="TypeSafe reports latency between seventy and five hundred milliseconds, and a very low cost. But these are their own numbers, and it's still early access. So I'd wait for independent tests."),
 dict(id="limits", say="And to be clear, Jev can't write free text at all. No chat, no code. And, can't hallucinate, only means it always matches your schema. Not that it's always right."),
 dict(id="end", say="So it doesn't replace the LLM. It replaces the LLM as a classifier. Not a chat model. A decision model.", tail=2.2),
]
