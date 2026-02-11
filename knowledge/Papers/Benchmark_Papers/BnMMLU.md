

[ref](https://arxiv.org/pdf/2505.18951?)


Questions:

1. what is zero shot and what is 5 shot?
2. what is ner?
3. what is angular distance?
4. what does it mean by corpus or corpora?


Answers:
## 1. **Zero-shot vs 5-shot (Few-shot Learning)**

**Think of it like a cooking test:**

- **Zero-shot**: You walk into a kitchen exam and are asked to make "Biryani" but you've never seen a recipe or example before. You only know what biryani _is conceptually_. You have to figure it out from scratch using your general cooking knowledge.
- **5-shot**: Before the exam, you're shown 5 example biryanis with their recipes. Now when asked to make biryani, you have reference examples to learn from.

**In the paper's context**: They tested models in **zero-shot** mode - meaning they gave the model questions directly without showing any example question-answer pairs first. This is harder but more realistic for testing true understanding.

---

## 2. **NER (Named Entity Recognition)**

**Analogy: Highlighting a news article**

Imagine you're reading a newspaper article with a highlighter set. Your job is to:

- Mark all **people's names** in yellow
- Mark all **places** in green
- Mark all **organizations** in pink
- Mark all **dates** in blue

That's essentially what NER does - it identifies and categorizes important "entities" (specific things) in text.

**Example in Bengali:**

```
"সামান ঢাকায় আন্তর্জাতিক ইসলামী বিশ্ববিদ্যালয়ে পড়েন।"
(Saman studies at International Islamic University in Dhaka.)
```

NER would identify:

- **Person**: সামান (Saman)
- **Organization**: আন্তর্জাতিক ইসলামী বিশ্ববিদ্যালয় (IIUC)
- **Location**: ঢাকা (Dhaka)

---

## 3. **Angular Distance**

I don't see this term specifically in this paper, but it's a common concept in ML/NLP:

**Analogy: Clock hands**

Imagine two clock hands pointing in different directions. Angular distance measures "how far apart" they're pointing - measured in degrees (0° to 180°).

**In NLP/ML context**: Words or sentences are converted to vectors (arrays of numbers). Angular distance (or cosine similarity) measures how "similar" two word/sentence vectors are by calculating the angle between them:

- **0°** = identical meaning
- **90°** = completely unrelated
- Small angles = similar concepts

**Example**: "cat" and "dog" might have a small angular distance (both animals), while "cat" and "democracy" would have a large angular distance.

---

## 4. **Corpus / Corpora**

**Analogy: A library collection**

- **Corpus** (singular) = A specific collection of texts gathered for study
- **Corpora** (plural) = Multiple such collections

**Think of it like:**

- A "Bengali newspaper corpus" = All the Bengali newspaper articles you've collected (maybe 100,000 articles)
- A "medical corpus" = Collection of medical textbooks and research papers
- "Training corpora" = Multiple different text collections used to train a model

**In the paper**: They mention "Bengali training corpora" - these are the large collections of Bengali text that language models are trained on. The paper points out that Bengali has **limited high-quality corpora** compared to English, which is why models perform worse.

---

## Context from Your Paper

The **BnMMLU paper** is creating a Bengali version of MMLU (Massive Multitask Language Understanding) - essentially a comprehensive test for AI models in Bengali across 23 subjects. They're using:

- **Zero-shot testing**: No example answers given to models
- Testing on **138,949 questions** from textbooks and exam guides
- Evaluating how well models handle **factual knowledge, procedural application, and reasoning** in Bengali

The big finding: There's a huge gap between English and Bengali model performance, showing we need better Bengali datasets and training approaches - which directly relates to your **BanglaSafe** work! 🎯