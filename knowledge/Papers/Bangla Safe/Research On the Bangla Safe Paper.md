
# Bengali NLP benchmarks, research gaps, and the path to top-venue publication

**Bengali NLP has reached an inflection point.** Despite serving ~300 million speakers (7th globally), Bengali lacks safety evaluation, hallucination detection, bias benchmarks, and agentic evaluation — capability dimensions that Chinese, Arabic, and Korean already cover. The highest-impact research opportunity is a culturally grounded Bengali safety benchmark targeting the NeurIPS 2026 Datasets & Benchmarks track (projected deadline ~May 15, 2026), where the acceptance rate stands at **25.2%** and low-resource language papers have a proven track record. Fifteen Bengali-specific benchmarks now exist, but they cluster heavily around knowledge QA and sentiment analysis, leaving critical deployment-readiness dimensions entirely unaddressed. A researcher with workshop-level publications (BanglaLlama, political bias detection) can break into top venues by filling these gaps with native (not translated) benchmarks framed as revealing fundamental multilingual LLM limitations — not "just Bengali NLP."

---

## Part 1: The complete landscape of Bengali NLP benchmarks and models

### Bengali-specific benchmarks span 15+ datasets but cluster narrowly

The Bengali benchmark ecosystem has grown rapidly since 2022 but concentrates on knowledge-based MCQ and basic NLU tasks. Here is the full inventory:

**Foundational benchmarks:**

|Benchmark|Tasks|Scale|Venue|Year|Key Limitation|
|---|---|---|---|---|---|
|**BLUB**|Sentiment, NLI, NER, QA|4 task datasets|Findings of NAACL 2022|2022|Only 4 tasks; uses machine-translated data for NLI|
|**BanglaNLG**|MT, summarization, QA, dialogue, cross-lingual summ.|6 NLG tasks|Findings of EACL 2023|2023|No billion-parameter model evaluation|
|**BenLLM-Eval**|Summarization, QA, paraphrasing, NLI, transliteration, classification, sentiment|7 tasks across 8 datasets|LREC-COLING 2024|2024|Zero-shot only; tested only GPT-3.5, LLaMA-2-13b, Claude-2|
|**BEnQA**|Parallel Bengali-English science QA (STEM)|~5,161 parallel questions|Findings of ACL 2024|2024|Text-only (no figures); MCQ format; limited to STEM|

**2025-era benchmarks (the acceleration phase):**

|Benchmark|Tasks|Scale|Venue|Year|Key Limitation|
|---|---|---|---|---|---|
|**BnMMLU**|41-domain MCQ (STEM, humanities, social sciences)|**134,375** question-option pairs|arXiv / under review|2025|Text-only; no NLG evaluation|
|**B-REASO**|Multi-level, multi-field evaluation (5 fields, multiple difficulty levels)|Multi-subject suite|Findings of EMNLP 2025|2025|MCQ-only format|
|**BLUCK**|Bengali cultural knowledge, history, linguistics|2,366 MCQs across 23 categories|BanglaLP Workshop @ AACL 2025|2025|Small scale; factual-knowledge MCQs only|
|**BLanCK**|Folk traditions, culinary arts, regional dialects|Cultural knowledge dataset|arXiv|2025|Limited scope|
|**BengaliMoralBench**|Moral reasoning across 5 domains, 50 subtopics|3,000 scenarios|arXiv|2025|Ethics-only; doesn't evaluate social biases systematically|
|**SOMADHAN**|Complex math word problems with step-by-step solutions|**8,792** problems|arXiv|2025|Math-only|
|**P6JIGGASHA**|Physics reasoning evaluation|Physics domain|BanglaLP Workshop @ ACL 2025|2025|Single domain|
|**BnSentMix**|Bengali-English code-mixed sentiment analysis|Sentiment only|BLP Workshop 2025|2025|Single task (sentiment)|
|**BanglaMedQA**|Medical QA evaluation|Biomedical MCQs|arXiv|2025|Domain-specific only|

Additional smaller-scale benchmarks include BanglaQuAD (open-domain QA), BanglaRQA (reading comprehension, 62.4% EM best), Uddipok (reading comprehension, 2023), BengaliFig (435 culturally grounded riddles), Reveal-Bangla (cross-lingual multi-step reasoning), and Vashantor (32,500 sentences across 5 regional dialects for translation).

### Multilingual benchmarks with Bengali coverage

Bengali appears in **9+ multilingual benchmark suites**, though often through machine translation rather than native construction:

- **MMLU-ProX** (2025): 13 languages; Bengali achieves ~57.6% vs. English 70.3% (Qwen2.5-72B) — a **12.7 percentage point gap**
- **IndicNLPSuite / IndicGLUE** (EMNLP 2020 Findings): 12 Indian languages including Bengali; provides IndicCorp (8.8B tokens), IndicBERT, IndicFT
- **IndicXTREME** (ACL 2023): 20 Indic languages, 9 NLU tasks, 105 evaluation sets; Bengali covered across IndicSentiment, IndicXNLI, IndicCOPA, IndicQA, and more
- **Belebele** (Meta, 2023): 122 language variants; Bengali in both native script and romanized; ~900 questions per language
- **MGSM** (2022): Bengali translations of GSM8K for math reasoning
- **IndicMMLU-Pro** (2025): 9 Indic languages via IndicTrans2 translation
- **XCR-Bench** (2026): Cross-cultural reasoning with separate West Bengal and Bangladesh variants
- **DIWALI** (EMNLP 2025 Oral): Cultural text adaptation benchmark
- **ViMUL-Bench** (EMNLP 2025): Multilingual video LMM benchmark with Bengali

### Bengali-specific language models now span the full architecture spectrum

The model ecosystem has matured significantly:

|Model|Architecture|Size|Training Data|Venue|Year|
|---|---|---|---|---|---|
|**BanglaBERT**|ELECTRA discriminator|~110M|Bangla2B+ (27.5 GB)|NAACL 2022|2021-22|
|**BanglaT5**|T5-based seq2seq|Base/Small|27.5 GB Bengali text|EACL 2023|2022-23|
|**BanglaByT5**|Byte-level encoder-decoder|~300M|14 GB curated corpus|arXiv|2025|
|**TigerLLM**|LLaMA 3.2 (1B) / Gemma 2 (9B)|1B, 9B|Bangla-TextBook (163 textbooks, 9.9M tokens) + 100K instructions|ACL 2025 Short|2025|
|**TituLLMs**|LLaMA 3.2 + extended tokenizer (96K vocab)|1B, 3B|~37B tokens|ACL 2025 Findings|2025|
|**BanglaLlama**|LLaMA-based (1B, 3B, 8B variants)|1B–8B|CulturaX Bengali (12.4M articles) + 224K instructions|arXiv|2024|
|**TigerCoder**|Code LLM|1B, 9B|Includes MBPP-Bangla benchmark|arXiv|2025|

Additional models include sahajBERT, IndicBERT v1/v2 (AI4Bharat), IndicBART, and Paramanu. **No centralized Bengali NLP leaderboard exists** comparable to the Open LLM Leaderboard — results remain scattered across individual papers and GitHub repositories, and no unified evaluation platform (like CLUE for Chinese or KLUE for Korean) has emerged.

---

## Part 2: What Bengali NLP is missing — and what other languages already have

### Seven critical capability dimensions remain completely unaddressed

The gap analysis reveals a stark pattern: Bengali benchmarks cover knowledge retrieval and basic NLU well, but **deployment-critical dimensions** are entirely absent.

**Completely missing (no Bengali benchmark exists):**

1. **Safety / red-teaming** — English has ALERT (45K+ prompts), HarmBench; Arabic has a dedicated safeguard evaluation dataset (5,799 questions); Korean has AssurAI (35 risk factors). Bengali has **zero** safety benchmarks.
2. **Bias / fairness (BBQ-style)** — Korean has KoBBQ (**76,048 samples**, 12 bias categories, TACL 2024); Chinese has CBBQ; Arabic has AraDiCE. Bengali has **nothing** measuring systematic social biases (gender, religion, caste, regional identity).
3. **Hallucination detection** — English has HaluEval, TruthfulQA, FActScore. Chinese has HalluQA. Bengali: **zero** hallucination-specific evaluation.
4. **Factuality evaluation** — No Bengali TruthfulQA or FACTBENCH equivalent.
5. **Agentic evaluation (tool use, planning)** — English has SWE-bench, WebArena, AgentBench. No equivalent exists for **any** non-English language at scale.
6. **RAG evaluation** — Arabic has ALRAGE (part of OALL v2). Bengali has only BanglAssist (20 queries from one company — not a benchmark).
7. **Instruction-following measurement** — English has IFEval, MT-Bench, AlpacaEval. No Bengali equivalent.

**Nascent but severely underdeveloped:**

- **Code-switching at scale** — BnSentMix covers sentiment only. No multi-task Banglish benchmark despite Banglish being the dominant digital communication mode (~52.9M social media users in Bangladesh).
- **Dialect processing** — Vashantor covers 5 dialects (32,500 sentences) for translation only. No dialect-aware QA, NLU, or generation benchmarks.
- **Multimodal (vision-language)** — No dedicated Bengali VQA, image captioning, or document understanding benchmark.
- **Domain-specific (legal/medical/financial)** — Medical: MediBeng (ASR only), BanglaMedQA (small). Legal: one 250-question study. Financial: only BnMMLU subtasks.

### The comparative gap with peer languages is dramatic

|Capability|Chinese|Arabic|Korean|Hindi|**Bengali**|
|---|---|---|---|---|---|
|MMLU-style knowledge|CMMLU, C-Eval, SuperCLUE|ArabicMMLU (14K+)|KMMLU (35K, 45 subjects)|IndicMMLU-Pro|BnMMLU (134K) ✓|
|Safety/red-teaming|SafetyBench, SC-Safety|Safeguard eval (5.8K)|AssurAI (35 risk factors)|❌|**❌**|
|Bias (BBQ-style)|CBBQ|AraDiCE|KoBBQ (76K)|❌|**❌**|
|Hallucination|HalluQA|Emerging|❌|❌|**❌**|
|Cultural evaluation|SuperCLUE|7+ benchmarks (2025)|CLIcK|⚠️|⚠️ BLUCK, BLanCK|
|Comprehensive eval suite|10+ major benchmarks|ORCA (33 tasks), OALL v2|KLUE ecosystem|Airavata framework|**❌ No unified suite**|
|Domain (legal/medical)|Well-established|MizanQA, GATmath|Korean Legal LU (EMNLP 2024)|⚠️|**❌ Near-zero**|
|Multimodal|MMBench-CN, SEED-Bench|⚠️|⚠️|BharatBench ⚠️|**❌**|
|Instruction-following|✓ (IFEval-CN)|❌|❌|Airavata human eval|**❌**|
|Total dedicated benchmarks|**50+**|**40+**|**15+**|**10+**|**~15**|

The most striking finding: **Arabic went from ~10 benchmarks to 40+ between 2024-2025**, driven by coordinated community effort. Bengali could follow a similar trajectory, but coordinated effort has not yet materialized. Chinese NLP's evaluation ecosystem is orders of magnitude more developed. Korean benefits enormously from industry investment (NAVER, Kakao).

### What recent surveys flag as Bengali NLP's open problems

Multiple 2024-2025 surveys converge on five structural challenges:

1. **Tokenization inefficiency** — Bengali requires **2-5× more tokens** than English for equivalent content, directly degrading LLM performance. This relationship between tokenization efficiency and accuracy has been empirically documented.
2. **Translation vs. native construction** — Most benchmarks are translations from English, missing cultural nuances and introducing artifacts. The Māori benchmark paper (NeurIPS 2024) demonstrated that translated benchmarks contain systematic errors for low-resource languages.
3. **No alignment data** — Zero DPO, RLHF, or safety alignment datasets exist for Bengali, making it impossible to properly align models for Bengali users.
4. **Cross-lingual transfer limitations** — Multilingual models show **10-20% performance degradation** on Bengali vs. English. Even Hindi-focused models (Airavata) perform poorly on Bengali despite script similarities.
5. **Data scarcity for advanced tasks** — Bengali has ~30B tokens in the largest corpus (Sangraha) vs. ~2T for English — a **67× gap**.

---

## Part 3: How to get a benchmark paper into NeurIPS Datasets & Benchmarks

### The NeurIPS D&B track has become highly competitive but welcomes low-resource work

The track has grown from 447 submissions in 2022 to **1,995 in 2025**, with acceptance rates converging toward the main track's ~25%. For 2024: **1,820 submissions, 459 accepted (25.2%)**, with 56 spotlights and 11 orals.

**The six review criteria that matter:**

1. **Utility and quality** — Impact, originality, novelty, relevance to the NeurIPS community
2. **Completeness of documentation** — Datasheets, Data Cards, or Data Statements required
3. **Accessibility** — Data must be findable without contacting authors; code must be open-source. Non-compliance triggers desk rejection in 2025+
4. **Reproducibility** — All results must be easily reproducible with accessible datasets and code
5. **Ethical considerations** — Bias documentation, responsible use guidelines, licensing
6. **Hosting and maintenance plan** — Long-term accessibility guarantees

**Two new 2025 requirements are now mandatory:**

The **Croissant metadata format** (itself published at NeurIPS 2024 D&B) is a JSON-LD schema.org-based metadata format that makes datasets machine-readable for ML frameworks. Since 2025, every submission must include a valid Croissant file. Datasets must be hosted on persistent public repositories — Hugging Face, Kaggle, OpenML, or Dataverse are preferred. Invalid metadata or inaccessible data can trigger desk rejection. The format includes a Responsible AI extension for documenting biases and sensitive content. An online validation tool is available at mlcommons.org.

### What successful NeurIPS D&B papers look like

**Scale varies enormously** — there is no minimum size requirement. Both massive-scale and expert-curated papers succeed:

- **DataComp-LM** (NeurIPS 2024 Best Paper runner-up): 240 trillion token Common Crawl pool, 53-task evaluation suite — succeeded through massive community infrastructure impact
- **MMLU-Pro** (NeurIPS 2024 D&B): Addressed benchmark saturation with harder, expert-verified questions — succeeded by solving a clear community pain point
- **PRISM Alignment Dataset** (NeurIPS 2024 D&B Best Paper): Data from 75 countries benchmarking 20+ LLMs — succeeded through societal value and multicultural scope
- **Muharaf** (NeurIPS 2024 D&B): 1,600 historic Arabic manuscript page images with expert transcription — succeeded as a **small-scale, expert-curated, low-resource language** contribution
- **Māori benchmark** (NeurIPS 2024 D&B): Critiqued existing multilingual benchmarks for Indigenous languages — succeeded through community-centered approach highlighting translation inadequacy

**Critical insight for Bengali researchers**: The Māori and Muharaf papers prove that **low-resource language datasets get accepted at NeurIPS D&B** when they demonstrate cultural authenticity, expert curation, and reveal fundamental limitations of existing evaluation approaches. A Bengali safety or bias benchmark that exposes how existing multilingual safety measures fail for Bengali would fit this template perfectly.

### The proven formula for multilingual/low-resource benchmark acceptance

Successful papers share these traits: native (not translated) content reflecting cultural context; comprehensive baselines evaluating **10+ state-of-the-art models**; community-centered design involving native speakers; rigorous data quality analysis documenting issues; multi-dimensional coverage combining multiple tasks or difficulty levels; and a framing that reveals broader insights about multilingual LLM limitations rather than "just" serving one language.

---

## Part 4: Getting benchmark papers into ACL, EMNLP, and NAACL

### The ARR system determines everything — understand its mechanics

All ACL, EMNLP, NAACL, and EACL submissions now go through ACL Rolling Review (ARR) with bi-monthly cycles. Reviews use three scores:

**Soundness (1-5):** Whether claims are sufficiently supported. Score ≥3 ("Acceptable: sufficient support for main claims") is essentially required for any acceptance. **Excitement (1-5):** Whether the work would generate interest. Score 5 = "Would recommend to others." Critically, **reviewer excitement is neither necessary nor sufficient** for main conference acceptance — resource papers for underserved languages may not excite individual reviewers but still warrant main track acceptance due to impact. **Overall Recommendation:** Explicit recommendation for outcome: Award consideration, Main conference, Findings, Resubmit, or Do not resubmit.

Area Chairs assign meta-review scores: **≥4 = Main conference worthy, 3.5 = borderline, 3 = Findings worthy, ≤2 = Resubmit.** The distinction between Main and Findings is **not** about completeness — Findings papers may be fully complete. Main conference papers must be "distinguished in some respect" through novelty, impact, or excitement. Inter-reviewer agreement (Krippendorff's alpha) is only ~0.3, highlighting significant subjectivity.

### Recent successful multilingual benchmark papers at *ACL venues

The trend strongly favors multilingual and low-resource benchmark work:

- **Aya Model** (ACL 2024 **Best Paper**): Instruction-finetuned multilingual model — demonstrated that a well-executed multilingual resource contribution can win the top award
- **DIALECTBENCH** (ACL 2024): NLP benchmarks for dialects and closely-related languages
- **IndicLLMSuite** (ACL 2024): Blueprint for creating Indic language pre-training datasets
- **KMMLU** (NAACL 2024): Korean knowledge benchmark — 35,030 native questions across 45 subjects
- **Indic-QA** (NAACL 2025 Findings): QA capability benchmark for 11 Indian languages
- **M-IFEval** (NAACL 2025 Findings): Multilingual instruction-following evaluation
- **SeaEval** (NAACL 2024): Cross-lingual alignment to cultural reasoning

**Key difference from NeurIPS D&B**: ACL venues strongly value **linguistic analysis** — understanding _why_ models fail on specific linguistic phenomena. Pure scale without insight is less valued. Bengali benchmark papers should include detailed error analysis, typological discussion, and connect findings to broader linguistic theory. Papers that "package existing data" without generating insights tend to go to Findings or get rejected.

---

## Part 5: The biggest unsolved problems in LLM evaluation

### Benchmark saturation has created an evaluation crisis

Top models now exceed **90% on MMLU** and **90% on AIME 2025**. Only Humanity's Last Exam (Phan et al., 2025) retains discriminative power — no model clears 30%. This saturation, combined with systematic contamination, has triggered a paradigm shift toward dynamic and adaptive evaluation.

**The three structural problems identified by a survey of 283 benchmarks** (Ni et al., arXiv 2508.15361): data contamination undermining validity, cultural and linguistic bias in evaluation design, and the failure of static benchmarks to simulate real-world scenarios.

### Six specific evaluation gaps that represent publication opportunities

**1. Agentic safety evaluation is the frontier problem.** AgentHarm (ICLR 2025) covers 110 harmful behaviors but is English-only and single-turn. OPENAGENTSAFETY (2025) found unsafe actions in **51.2-72.7%** of safety-vulnerable tasks. MCP-SafetyBench evaluates Model Context Protocol deployments. The critical gap: no agentic safety evaluation exists for non-English languages, and multi-turn adversarial settings remain poorly covered.

**2. Contamination detection methods are unreliable.** Samuel et al. (COLING 2025) found current detection methods have "non-trivial limitations" and "notable difficulties detecting instruction fine-tuning contamination." A fundamental fidelity-resistance tradeoff has been discovered — no strategy achieves both high fidelity to original benchmarks and high contamination resistance.

**3. Multilingual safety remains dangerously understudied.** Yong et al. (EMNLP 2025 Main) reviewed ~300 publications and found a "significant and growing language gap." Simply translating malicious prompts to low-resource languages bypasses safety alignment, with unsafe rates increasing **20-25 percentage points** for low-resource languages. The June 2025 multilingual joint testing exercise by government AI Safety Institutes found that LLM-as-judge evaluators fail to account for regional context.

**4. Dynamic and adaptive benchmarks are emerging but immature.** LiveBench (ICLR 2025 Spotlight) updates monthly with objective ground-truth questions. ATLAS (2025) uses Item Response Theory to reduce evaluation items by **90%** while maintaining precision. Stanford HELM has integrated Rasch model-based adaptive testing (Pearson correlation 0.99 with average scores). These approaches naturally mitigate contamination through diverse test forms.

**5. Process-level reasoning evaluation barely exists.** Current benchmarks evaluate final answers but not reasoning chains. With o1/R1-style models, evaluating _how_ a model reasons — not just _what_ it concludes — is increasingly critical. No standardized framework exists for trajectory-level evaluation of reasoning processes.

**6. LLM-as-judge reliability is poorly understood cross-linguistically.** Known biases include verbosity preference, position bias, and cultural blindness. EMNLP 2025 found LLM judges fail to account for regional context and cultural nuances — a finding with direct implications for Bengali evaluation.

---

## Part 6: Your highest-probability paths to top-venue acceptance

### Concrete Bengali-focused project ideas, ranked by acceptance probability × impact

**Rank 1: BanglaSafe — Bengali LLM safety benchmark → Target NeurIPS 2026 D&B**

This is the highest-impact opportunity because safety benchmarks exist for English, Chinese, Arabic, and Korean — but **zero** for Bengali. Include toxicity detection, harmful content generation resistance, Bangladesh-specific safety concerns (political sensitivity, religious contexts, social norms), jailbreak resistance testing, and cultural taboo navigation. Evaluate 15+ models including GPT-4o, Claude, Gemma, Llama, TituLLM, TigerLLM, and BanglaLlama. Frame it as revealing how "safety that works in English won't work elsewhere" — directly building on the EMNLP 2025 findings by Yong et al. Include Croissant metadata, host on Hugging Face, and provide comprehensive documentation. The Māori and Muharaf precedents prove this category gets accepted.

**Rank 2: BanglaHalu — Bengali hallucination detection and factuality evaluation → Target EMNLP 2026**

Hallucination detection is a hot research area (papers at ICLR 2025, NeurIPS 2024, EMNLP 2024). No Bengali hallucination evaluation exists. Include factual hallucination on Bangladesh/Bengali knowledge, cross-lingual hallucination (when models default to English knowledge for Bengali questions), and summarization faithfulness. This would be the first non-English hallucination benchmark for a South Asian language. Submit via ARR May 2026 cycle for EMNLP 2026 commitment.

**Rank 3: BanglaBBQ — Bengali bias and fairness benchmark → Target ACL 2026 or EMNLP 2026**

KoBBQ (Korean, 76K samples, TACL 2024) provides a proven template. Create a Bengali equivalent covering 10+ bias categories relevant to Bangladesh/Bengali context: gender, religion (Islam, Hinduism, Buddhism, Christianity), regional identity (Dhaka vs. Chittagong vs. Sylhet), socioeconomic status, caste, age, disability, nationality, occupation, and education level. The ACL 2026 theme of "Explainability of NLP Models" aligns well — frame it as _explaining_ when and why Bengali models exhibit biases.

**Rank 4: BanglaMix — comprehensive Bengali-English code-switching benchmark → Target EMNLP 2026**

Banglish is the dominant digital communication mode for 52.9M Bangladeshi social media users. GLUECoS and LinCE exist for Hindi-English but not Bengali-English at scale. Go beyond BnSentMix's sentiment-only coverage to include NER, NLI, QA, toxicity detection, and summarization on code-mixed text. This would serve a massive real-world user base.

### Language-agnostic evaluation gap with highest publication potential

**Cross-lingual agentic safety evaluation** sits at the intersection of two hot topics (agent safety + multilingual safety) where all current benchmarks are English-only. A framework that tests whether LLM agents behave safely when operating in Bengali, Arabic, Swahili, and other non-English languages — with tool use, multi-turn interactions, and culturally grounded harm definitions — would be genuinely novel. Target NeurIPS 2026 main track or ICLR 2027.

**Adaptive/dynamic benchmarking for multilingual evaluation** is another strong direction. ATLAS and LiveBench pioneered adaptive testing for English. Applying Item Response Theory to multilingual benchmarks — calibrating item difficulty across languages, measuring cross-lingual transfer efficiency, and generating contamination-resistant test forms — would advance both evaluation methodology and multilingual NLP.

### Your actionable timeline from February 2026

|Window|Action|Target Venue|Deadline|
|---|---|---|---|
|**Now → Mar 14**|Commit existing ARR paper (if Jan 2026 cycle submitted)|ACL 2026|**Mar 14, 2026**|
|**Now → Mar 16**|Submit new paper to ARR March cycle|EMNLP 2026 or NAACL 2027|**Mar 16, 2026**|
|**Mar → May 15**|Develop BanglaSafe safety benchmark + paper|**NeurIPS 2026 D&B**|**~May 15, 2026** (projected)|
|**Mar → May 25**|Develop BanglaHalu or BanglaBBQ|EMNLP 2026 via ARR May cycle|**May 25, 2026**|
|**Jun → Aug 3**|Backup: submit to ARR August cycle|EMNLP 2026 commitment|**Aug 3, 2026**|
|**Jun → Oct**|Develop language-agnostic evaluation paper|**ICLR 2027**|**~Oct 2026** (projected)|

**Confirmed dates:** ACL 2026 in San Diego (Jul 2-7); EMNLP 2026 in Budapest (Oct 24-29); NeurIPS 2026 in Sydney (Dec 6-12); ICML 2026 in Seoul (Jul 6-11, deadlines passed). NAACL typically alternates years; next standalone event likely 2027. ARR cycles run bimonthly (Mar 16, May 25, Aug 3, Oct 12).

### Strategic principles for the workshop-to-main-conference transition

**Frame insights, not just resources.** Workshop papers describe "what we did"; main conference papers need "what we discovered that's surprising." Lead with findings like "Bengali tokenization efficiency inversely correlates with accuracy" or "safety alignment collapses when prompts shift to Bengali" — then present the benchmark as the tool that enabled these discoveries.

**Don't frame as "just Bengali."** Position work as a case study revealing fundamental multilingual LLM limitations. Lead with the insight, not the language. Include English baselines to quantify the performance gap. Connect to the 300M speaker population for real-world impact arguments.

**Scale your experimental design.** Workshop papers test 2-3 models; main conference papers evaluate **10-15+ models** across zero-shot, few-shot, and fine-tuned settings, with comprehensive error analysis and ablation studies.

**Target the right tracks.** ACL 2026 explicitly lists "Resources and Evaluation," "Multilinguality and Language Diversity," "Safety and Alignment in LLMs," and "Low-resource Methods for NLP" as topic areas. NeurIPS D&B specifically welcomes dataset papers with lower methodological novelty requirements than the main track. EMNLP is traditionally the strongest venue for empirical/resource papers.

---

## Conclusion: Three key insights for charting your path

First, **Bengali NLP's biggest gap is not knowledge benchmarks — it's deployment readiness.** BnMMLU (134K questions) already provides strong knowledge evaluation. The missing pieces are all about making Bengali LLMs safe, reliable, and trustworthy: safety, bias, hallucination, and instruction-following evaluation. Filling any one of these gaps would be a first-of-its-kind contribution.

Second, **the NeurIPS D&B track is your highest-probability target for a benchmark paper.** It has proven receptivity to low-resource language work (Māori, Muharaf, MACD), a 25% acceptance rate, single-blind review (avoiding anonymization complications with hosted datasets), and clear, well-defined review criteria. The projected May 2026 deadline gives you approximately three months to develop a Bengali safety benchmark — ambitious but feasible if you scope it to 3,000-5,000 natively constructed evaluation items with comprehensive model baselines.

Third, **the multilingual safety gap is the single most impactful intersection** of Bengali-specific and language-agnostic research. The EMNLP 2025 finding that safety "that works in English won't automatically work elsewhere" — with **20-25 percentage point** unsafe rate increases for low-resource languages — is a crisis that your position as a Bengali NLP researcher uniquely equips you to address. A Bengali safety benchmark isn't just a resource contribution; it's evidence for a fundamental claim about the limits of current LLM alignment approaches.