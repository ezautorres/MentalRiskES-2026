# MentalRiskES: Early detection of mental disorders risk in Spanish

## Description
According to a recent report by the World Health Organization, there is 1 in
every 8 people in the world suffering from a mental disorder. The COVID-19
pandemic has raised the prevalence of anxiety and depression to more than 26%
in just one year. Suicide is the fourth leading cause of death among 15-29
year-olds. The organisation considers that early identification is a key
effective intervention to prevent these problems.

Consequently, there is a growing interest in detecting and identifying mental
disorders in social media streams. This answers a demand from society due to
the high increase in these problems among the population, in several kinds of
mental risks:
- eating disorders,
- dysthymia,
- anxiety,
- depression,
- suicidal ideation,
- and others.
Actually, relevant evaluation campaigns like the Cross-Lingual Evaluation
Forum (CLEF) have hosted during the last years the Early-Risk Identification
task (eRisk). Unfortunately, these campaigns have focused mainly on English,
leaving aside other languages, like Spanish. 

This proposal describes the fourth edition of a novel task on early risk
identification of mental disorders in Spanish comments from social media
sources. The first, second and third editions took place in the IberLEF
evaluation forum as part of the SEPLN 2023, 2024 and 2025. The task was
resolved as an online problem, that is, the participants had to detect a
potential risk as early as possible in a continuous stream of data. Therefore,
the performance not only depended on the accuracy of the systems but also on
how fast the problem is detected. These dynamics are reflected in the design
of the tasks and the metrics used to evaluate participants. For this fourth
edition, we propose two novel tasks, the first subtask is about the detection
of the symptoms and the second subtask consists of decision support.

## Task 1: Early Symptom Detection in Therapeutic Conversations.
This task focuses on the early identification of mental health symptoms
expressed by a patient during a therapeutic dialogue, by mapping patient
language to standardized clinical questionnaires.

Participants are given therapist–patient conversations that unfold over
multiple chat messages. After each patient turn, systems must infer the
patient’s responses to a set of validated psychometric instruments,
including
- PHQ-9,
- CompACT-10,
- and GAP-7,
based on the dialogue observed up to that point.

Rather than directly predicting abstract symptom labels, systems are required
to estimate how the patient would respond to each questionnaire item,
effectively translating natural language into structured clinical assessments. 

Key characteristics of the task include:
- The task is framed as a multiclass classification problem at the item level,
where each question has a fixed set of possible responses (e.g.,
Likert-scale options).

- No labeled training data are provided. Systems must rely on zero-shot, weakly
supervised, or knowledge-based approaches (e.g., pretrained language models,
prompting strategies, or external resources).

## Task 2: Therapist Response Selection.
Evaluates NLP systems as decision-support tools for therapists in a multi-turn
setting. At each interaction step, systems receive the latest user message
along with three candidate therapist responses, and must select the most
appropriate option according to expert-defined best practices.

Importantly, the full conversation history is not provided explicitly at each
step. Instead, teams are expected to maintain and accumulate context across
successive turns, effectively reconstructing the dialogue as the interaction
progresses. 

This process is repeated over multiple rounds, simulating a continuous therapeutic
conversation. 

Key characteristics of the task include: 
- Each instance consists of the current user message and three candidate
therapist responses.
- The dialogue history must be implicitly tracked by the system across turns,
as it is not re-supplied.
- Responses are selected rather than generated, ensuring a controlled and
ethically safe evaluation setting.
- Candidate responses may include both AI-generated and human-authored
interventions, with one option identified by experts as the most appropriate.

## Dataset

## Evaluation