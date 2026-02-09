# Bengali NLP papers face uphill battle at top venues: A realistic assessment

Two Bengali NLP papers targeting ACL/NAACL/EMNLP face **significant challenges** for main conference acceptance, though strategic revisions could improve their prospects. The landscape for low-resource language research is competitive but offers clear opportunities—if methodological rigor matches the community's expectations.

---

## What actually gets accepted at ACL, NAACL, and EMNLP

These three conferences form the top tier of NLP research, with **acceptance rates hovering around 20-23%** for main tracks. Understanding their expectations is crucial for realistic assessment.

**Acceptance rates for 2024-2025:**
- **ACL 2025**: 20.3% main (1,699/8,360 submissions)
- **NAACL 2025**: 22% main, 37% including Findings
- **EMNLP 2024**: 20.8% main, 37.7% combined with Findings

The review system now uses ACL Rolling Review (ARR) with three primary scoring dimensions: **Soundness** (1-5), **Excitement** (1-5), and an **Overall Assessment**. Papers scoring 4+ on Soundness and 3.5+ on Excitement typically reach Findings; main conference requires additional distinction in novelty, impact, or excitement.

The most common rejection reasons cluster around methodology failures: missing statistical significance testing, insufficient baselines, reproducibility issues, and overclaiming. Notably, reviewers are explicitly warned against dismissing papers for being "not surprising," "too niche," or "only tested on non-English"—but this doesn't mean weak methodology gets a pass.

**What separates winners from losers:**
- Clear research questions with well-defined contributions
- **4-6+ downstream task evaluations** with appropriate baselines (mBERT, XLM-R, language-specific models, AND recent LLMs like GPT-4)
- Statistical significance testing with confidence intervals
- Human evaluation for generation tasks
- Ablation studies demonstrating component contributions
- Code, data, and model release

---

## BanglaLlama: Honest probability assessment

### Technical overview

BanglaLlama (arXiv:2410.21200) presents a family of Bangla-adapted LLaMA models (1B, 3B, 8B parameters) with vocabulary extension (16,000 Bangla tokens) and instruction tuning on **224,000 translated samples** from Alpaca and Orca datasets.

### Acceptance probability: LOW

**Main Conference (ACL/NAACL/EMNLP): 20-30%**
**Findings: 40-50%**
**Workshop: 60-70%**

### Critical weaknesses that could sink this paper

The paper has **fundamental methodological gaps** that reviewers will flag immediately:

**Missing baselines are the fatal flaw.** The paper only compares against base Meta-LLaMA variants. It completely ignores BanglaBERT (NAACL 2022 Findings)—the established standard for Bengali NLP with **27.5 GB** training data and the BLUB benchmark. No comparison with multilingual baselines (mBERT, XLM-R), existing BanglaLLM variants on HuggingFace, or commercial models (GPT-3.5, Claude). This omission alone justifies rejection.

**TigerLLM (ACL 2025 Short Paper) directly challenges reproducibility.** This concurrent work explicitly states that BanglaLlama shows "low and non-reproducible results, often performing worse than their base models." Having peer-reviewed work questioning your results before you submit is devastating.

**No human evaluation.** The paper relies entirely on LLM-as-a-judge evaluation. While this is increasingly accepted, top venues expect human validation, especially for a language where evaluating quality requires native speakers.

**Translation-based data raises quality concerns.** Using machine-translated English instruction data (Alpaca, Orca) is a known limitation. Successful recent papers like TigerLLM use **native Bengali instruction data** (100k samples from volunteer annotators), which captures cultural nuances translation misses.

**Missing ablations and significance testing.** No systematic analysis of vocabulary extension impact, training duration, or dataset composition. No confidence intervals or statistical tests reported.

### Strengths that reviewers will acknowledge

The paper does contribute valuable resources: open-source models across three sizes, 224k instruction-tuning samples, and practical tokenization improvements. The scope (multiple model sizes, multiple task categories) shows ambition. These strengths position it well for Findings or workshop acceptance.

### What's needed for main conference acceptance

1. **Add comprehensive baselines**: BanglaBERT, BanglaGPT, mBERT, XLM-R, GPT-3.5-turbo
2. **Use standard benchmarks**: Evaluate on BLUB (Bangla Language Understanding Benchmark)
3. **Include human evaluation**: Native Bengali speakers rating output quality
4. **Add statistical significance**: Bootstrap confidence intervals, paired t-tests
5. **Address TigerLLM concerns**: Run head-to-head comparisons, explain discrepancies
6. **Ablation studies**: Show vocabulary extension impact, dataset size effects

---

## Political Bias paper: Clarification and assessment

### Important note on paper identity

The arXiv link (2510.03898) corresponds to **"Read Between the Lines: A Benchmark for Uncovering Political Bias in Bangla News Articles"** by Lia et al.—a workshop paper already accepted at **BLP-2025** (Second Workshop on Bangla Language Processing, ACL 2025). This is different from the title provided, which may be an earlier version or alternative framing.

### Technical overview

This paper introduces a 200-article benchmark for political stance detection (Government Leaning, Government Critique, Neutral) with evaluation of **28 LLMs**. Inter-annotator agreement is substantial (κ = 0.78).

### Acceptance probability

**Main Conference: 25-35%** (needs significant expansion)
**Findings: 40-50%**
**Workshop: Already accepted at BLP-2025**

### Critical weaknesses

**Dataset size is critically small.** With only **200 samples**, this benchmark lacks statistical power. Comparable accepted papers use 1,000-21,000+ samples:
- P-Stance (English): 21,574 tweets
- IndiBias (NAACL 2024): 1,500+ samples
- BorderLines (NAACL 2024): 251 territories × 49 languages

**Methodology follows standard patterns without novelty.** The paper applies zero/few-shot prompting to existing LLMs—a well-established approach. Compare to successful bias papers that introduce novel methods like "extreme anchor comparison" (Bang et al., ACL 2024) or demonstrate real-world harm (EMNLP 2024 voter influence study showing 24% opinion shift).

**No human baseline comparison.** How well do human experts perform on this task? Without this, it's impossible to contextualize model performance.

**Government-centric framing limits generalizability.** The labels are specific to Bangladesh's political landscape, making cross-cultural comparison difficult.

### Strengths

The paper addresses a genuine gap—political bias detection for Bengali is unexplored. The evaluation of 28 models across size categories is comprehensive. Cultural specificity (Bangladeshi socio-political context) is a strength, not weakness. The finding that models systematically over-predict government-leaning stances is novel and concerning.

### Path to main conference

1. **Scale to 1,000+ samples minimum** (ideally 5,000+)
2. **Add fine-tuning experiments** with BanglaBERT and Bengali LLMs
3. **Include human performance baseline**
4. **Compare with established bias frameworks** (anchor comparison methods, Political Compass instruments)
5. **Add temporal analysis** showing bias patterns over time
6. **Release code and data publicly**

---

## How these papers compare to recently accepted work

### Low-resource language model papers (2023-2025 accepted)

The bar for low-resource language model papers is **higher than many expect**:

| Paper | Venue | Languages | Key Innovation | Why Accepted |
|-------|-------|-----------|----------------|--------------|
| **SambaLingo** | EMNLP 2024 MRL | 9 languages, 7B-70B | Vocabulary extension + DPO alignment | Comprehensive methodology, released checkpoints |
| **Democratizing LLMs** | ACL 2024 Main | 34 languages | Unsupervised prompting matching supervised | Novel method, 7B matches 175B performance |
| **BanglaBERT** | NAACL 2022 Findings | Bengali | First large Bengali model + BLUB benchmark | Resource creation, established standard |
| **AfroXLMR** | COLING 2022 Best Paper | 17 African + 3 | MAFT + vocabulary pruning | Novel adaptation method, efficiency gains |

**BanglaLlama comparison**: These papers either introduce novel methods (SambaLingo's DPO, Democratizing's unsupervised prompting) or create comprehensive benchmarks (BanglaBERT's BLUB). BanglaLlama's translation-based approach with standard fine-tuning is methodologically incremental.

### Bias detection papers (2023-2025 accepted)

Successful bias papers demonstrate rigorous methodology:

| Paper | Venue | Innovation | Scale |
|-------|-------|------------|-------|
| **Political Bias Measurement** (Bang et al.) | ACL 2024 | Anchor comparison + framing analysis | 14,000 samples, 14 topics, 11 models |
| **BorderLines** (Li et al.) | NAACL 2024 | Geopolitical bias via territorial disputes | 251 territories, 49 languages |
| **Hidden Persuaders** | EMNLP 2024 | Real-world voter influence study | User study showing 24% opinion shift |

**Bengali Political Bias comparison**: The 200-sample dataset is roughly **70x smaller** than Bang et al.'s work. Without novel methodology or demonstrated real-world impact, the contribution appears incremental.

---

## Research directions with high acceptance probability

### What's HOT for Bengali NLP right now

Based on recent acceptances and identified gaps:

**Tier 1: Highest probability**
- **Comprehensive Bengali LLM evaluation benchmark** (MMLU-style for Bangladesh curriculum, cultural knowledge) — This fills the largest gap
- **Bengali cultural values alignment** using World Values Survey frameworks — Directly addresses underexplored dimension
- **Large-scale native Bengali instruction dataset** — 100k+ non-translated samples would be a major resource contribution

**Tier 2: Strong probability**
- **Bengali safety red-teaming dataset** — Zero Bengali-specific safety evaluation exists
- **Bengali code-mixed NLU** — Social media Bengali-English processing is underexplored
- **Efficient tokenization** addressing Bengali's 2-3x token overhead

**Tier 3: Emerging opportunities**
- **RAG for Bengali knowledge tasks**
- **Multimodal Bengali** (speech-text integration)
- **Bengali dialect processing** (only 3 of many dialects have datasets)

### Research gaps confirmed by literature

- No comprehensive LLM evaluation benchmark for Bengali (B-REASO emerging but limited)
- No Bengali safety evaluation at all
- No Bengali cultural values benchmark
- Limited dialogue/conversational AI resources
- Code-switching datasets inadequate for real-world social media

---

## Publication strategy recommendations

### Which venue for each paper

**BanglaLlama → Target EMNLP 2026**

EMNLP has historically been more receptive to resource papers and empirical studies. The paper's strength is its contribution of usable models and datasets—EMNLP values this. Submit with significant revisions addressing baselines and evaluation.

Alternative: ACL 2026 if you can address TigerLLM reproducibility concerns and add comprehensive evaluation.

**Political Bias Paper → Workshop is appropriate**

The paper is already accepted at BLP-2025, which is the right level for current scope. For main conference targeting:
- Expand to 1,000+ samples
- Target EMNLP 2026 (October) given empirical focus
- Or ACL 2026 Theme Track on "Explainability" (if you frame bias as interpretability)

### Submission timeline for 2026

| Conference | Submit to ARR | Commitment Deadline | Notification | Conference |
|------------|---------------|---------------------|--------------|------------|
| **ACL 2026** | January 5, 2026 | March 14, 2026 | April 4, 2026 | July 2-7, San Diego |
| **EMNLP 2026** | May 25, 2026 (est.) | August 2026 (est.) | September 2026 (est.) | October 24-29, Budapest |
| **NAACL 2027** | TBD | TBD | TBD | TBD |

**Critical ARR note**: Starting May 2025, ALL authors must register as reviewers. Non-compliance results in desk rejection.

### Strategic backup flow

```
ACL 2026 (Jan submission) → [rejected] → Revise → May ARR → EMNLP 2026
                          → [Findings] → Still valuable publication
```

### Workshop options if main conference seems risky

- **TrustNLP @ ACL 2026** (direct submission: March 5, 2026) — Bias/fairness focus
- **C3NLP @ ACL 2026** — Cross-cultural considerations
- **LoResLM workshop** — Language models for low-resource languages
- **AfricaNLP** — Despite name, accepts South Asian low-resource work

### Findings vs. Main: Is Findings "good enough"?

**Yes, with caveats.** Findings papers:
- Published in ACL Anthology (permanent, citable)
- Receive citations comparable to A-ranked venues (one tier below main)
- Increasingly accepted by PhD programs and industry
- But some committees still distinguish main from Findings

For a transfer application, **Findings at ACL/EMNLP** demonstrates research capability and peer-reviewed publication. It's significantly better than an arXiv preprint alone.

---

## Actionable recommendations for transfer application success

### For immediate impact (next 3 months)

1. **BanglaLlama revision priority**: Add BanglaBERT, mBERT, GPT-3.5 baselines. Run on BLUB benchmark. Add human evaluation (even small-scale: 100 samples, 3 annotators). Include statistical significance.

2. **Political Bias expansion**: If you have access to annotators, scale to 500+ samples now. Add BanglaBERT fine-tuning experiments.

3. **Start new project with higher ceiling**: A Bengali LLM evaluation benchmark (MMLU-style) would be highly impactful and achievable with systematic effort.

### For your application narrative

Frame your work as **addressing digital equity for 300 million Bengali speakers**. The low-resource language angle is compelling, but reviewers and admissions committees will scrutinize methodology. Having:
- One main conference paper (even Findings)
- Evidence of addressing reviewer feedback
- Clear research trajectory toward impactful problems

...is stronger than multiple weak preprints.

### Brutal reality check

These papers, as currently written, are unlikely to receive main conference acceptance at ACL/NAACL/EMNLP. However:
- BanglaLlama has a reasonable shot at **Findings** with moderate revisions
- The Political Bias paper's workshop acceptance is appropriate and valuable
- Both demonstrate research initiative and technical competence

For a transfer application, **one strong Findings paper with a clear path to main conference work** is more valuable than multiple preprints. Focus revision effort strategically, and consider starting a higher-ceiling project (evaluation benchmark, safety dataset) that addresses the confirmed research gaps in Bengali NLP.