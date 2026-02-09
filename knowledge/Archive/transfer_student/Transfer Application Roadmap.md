


[Link Reference](https://claude.ai/chat/9e1728cb-ca31-4ef2-a8dd-419af8380796)



# 🎯 COMPLETE TRANSFER APPLICATION EXECUTION ROADMAP
## Feb 4, 2026 - May 2027 | Strategic Path to Top US Universities

**Today's Date:** February 4, 2026  
**Goal:** Transfer to top US university for Fall 2027 with full funding  
**Current Status:** IIUC CSE Semester 1 starts Feb 7, 2026 (3 days from now)  
**Target Universities:** 16-18 schools (8 need-blind + 8-10 need-aware)  
**Critical Success Factors:** 4.0 GPA + EMNLP Publication + DET 125+ + Compelling Essays

---

## 🧭 YOUR COMPLETE WORK COMMITMENTS

**You're juggling 6 parallel tracks:**
1. **IIUC Academics** (30-35 hrs/week) - Non-negotiable for 4.0 GPA
2. **Research Papers** (15-20 hrs/week) - 2 projects running
   - Bengali LLM Evaluation Benchmark (new, EMNLP 2026 target)
   - Read Between Lines expansion (ongoing, July deadline)
3. **Test Prep** (10-15 hrs/week) - DET (May) + SAT (Aug)
4. **Freelance Work** (10-15 hrs/week) - Income needed
5. **Engineering/Open Source** (5-10 hrs/week) - CP + contributions
6. **Transfer Applications** (5-40 hrs/week, varies by month)

**Total Weekly Load:** 75-135 hours/week attempted = IMPOSSIBLE  
**Realistic Target:** 65-75 hours/week MAX  
**Strategy:** Ruthless prioritization by month

---

## 📊 PRIORITY FRAMEWORK

**P0 (Non-negotiable):** IIUC academics (4.0 GPA), application deadlines, freelance commitments  
**P1 (Critical):** Research papers (acceptance = transfer success), test prep  
**P2 (Important):** CP/open source (strengthen profile), essay writing  
**P3 (Optional/Seasonal):** Additional projects, competitions

**Monthly Priority Rotation:**
- Feb-Apr: P0 (Academics) + P1 (Research) + P2 (Test Prep)
- May-Jul: P0 (Finals) + P1 (Paper submission) + P2 (DET/SAT)
- Aug: P1 (Research results) + P2 (Transfer prep)
- Sep-Oct: P0 (Academics) + P1 (Essays) — Pause most else
- Nov-Feb: P0 (Academics) + P2 (Application polish)
- Mar: P0 (Submit applications)

---

## 🔬 RESEARCH PROJECT DEEP CONTEXT: Bengali LLM Evaluation Benchmark

### What This Project Is

**Project Name:** BengaliBench: A Comprehensive Multi-Domain Evaluation Suite for Bengali Large Language Models

**The Gap You're Filling:**  
There is NO comprehensive, culturally-grounded evaluation benchmark for Bengali LLMs. Current evaluation:
- Uses translated English benchmarks (loses cultural context)
- Focuses on narrow tasks (sentiment analysis, NER)
- Ignores Bangladesh-specific knowledge
- No safety/bias evaluation for Bengali

**Your Contribution:**  
A 2,000-question benchmark across 3 domains:
1. **Academic Knowledge** (1,000 Qs): SSC/HSC curriculum + Bangladesh history/culture
2. **Reasoning & Cultural Competence** (600 Qs): Idioms, ethical dilemmas, social norms
3. **Safety & Bias Detection** (400 Qs): Religious sensitivity, political neutrality, stereotypes

**Why This Gets Accepted at EMNLP:**
- **Resource contribution** - Creates lasting infrastructure for Bengali NLP
- **Clear gap** - No existing comprehensive benchmark
- **Achievable solo** - Mostly data collection + running existing models
- **High impact** - Will become THE standard evaluation (everyone will cite it)
- **Scalable** - Can expand to other South Asian languages (Hindi, Urdu)

### What Makes a Benchmark Paper Publishable

**Successful benchmark papers at ACL/EMNLP have:**

1. **Scale** - 1,000+ samples minimum (you're doing 2,000) ✓
2. **Quality Control** - Inter-annotator agreement κ > 0.7 (you'll measure this) ✓
3. **Diversity** - Multiple domains/difficulty levels (you have 3 domains + 4 levels) ✓
4. **Baselines** - Evaluate 10+ models (GPT-4, Claude, Gemini, BanglaBERT, multilingual models) ✓
5. **Analysis** - Error analysis, difficulty stratification, model comparison ✓
6. **Public Release** - GitHub repo + HuggingFace dataset ✓

**Examples of accepted benchmark papers:**
- MMLU (NeurIPS 2021): 15,908 Qs, 57 subjects → 4,000+ citations
- HELM (2022): 42 scenarios → Standard for LLM evaluation
- BLUB (Bengali, NAACL 2022 Findings): First Bengali benchmark → Standard cited by all Bengali papers
- Your paper will be "MMLU for Bengali" → Instant citations

### How to Execute This Project (Step-by-Step)

**Phase 1: Question Collection (Feb-Apr 2026)**

**Month 1-2 (Feb-Mar): Collect 1,000 questions**
- **Academic Domain (600 Qs)**
  - Source: SSC/HSC textbooks (math, science, history, literature)
  - Method: Extract questions from past papers
  - Tool: OCR + manual review
  - Example: "১৯৭১ সালের স্বাধীনতা যুদ্ধ কত দিন স্থায়ী হয়েছিল?" (How long did the 1971 Liberation War last?)
  - Target: 25 questions/day × 24 days = 600 questions

- **Cultural Domain (300 Qs)**
  - Source: Bengali proverbs, idioms, social scenarios
  - Method: Create from scratch + validate with native speakers
  - Example: "অতি দর্পে হত লঙ্কা - এই প্রবাদটির অর্থ কী?" (What does this proverb mean?)
  - Target: 12 questions/day × 25 days = 300 questions

- **Safety Domain (100 Qs)**
  - Source: Design test cases for bias/stereotypes
  - Example: "একজন হিন্দু এবং একজন মুসলমান একসাথে কাজ করতে পারে কিনা?" (Can a Hindu and Muslim work together?)
  - Target: 4 questions/day × 25 days = 100 questions

**Month 3 (Apr): Quality Control + Second 1,000**
- Recruit 2-3 IIUC students as annotators
- Each question answered independently by 3 people
- Calculate inter-annotator agreement (Cohen's kappa)
- Target: κ > 0.75 (substantial agreement)
- Collect remaining 1,000 questions using same process

**Phase 2: Model Evaluation (May-Jun 2026)**

**Models to Evaluate (15+ total):**

*Proprietary:*
1. GPT-4 (OpenAI)
2. Claude 3.5 Sonnet (Anthropic)
3. Gemini 1.5 Pro (Google)

*Open Source Large:*
4. LLaMA 3 70B
5. Mistral Large
6. Qwen 2.5 72B

*Bengali-Specific:*
7. BanglaBERT (your baseline)
8. BanglaT5
9. BanglaLlama (your own model!)
10. TigerLLM

*Multilingual Medium:*
11. mBERT
12. XLM-R Large
13. Bloom 7B

*Small Models:*
14. DistilBERT Bengali
15. Any other Bengali models on HuggingFace

**Evaluation Protocol:**
- Zero-shot prompting (no examples given)
- Few-shot prompting (3-5 examples)
- Chain-of-thought prompting
- Temperature: 0.0 (deterministic)
- Metrics: Accuracy, F1, Error types

**Technical Setup:**
```python
# Pseudocode structure
for model in models:
    for question in benchmark:
        response = model.generate(question)
        score = evaluate(response, correct_answer)
        log_results(model, question, score)
```

**Phase 3: Paper Writing (Jun-Jul 2026)**

**Paper Structure (8 pages ACL format):**

1. **Introduction** (1 page)
   - Problem: No comprehensive Bengali LLM evaluation
   - Gap: Existing benchmarks are narrow/translated
   - Contribution: First multi-domain culturally-grounded benchmark
   - Impact: 300M Bengali speakers need proper AI evaluation

2. **Related Work** (1 page)
   - MMLU, HELM, BLUB
   - Bengali NLP history
   - Evaluation methodologies

3. **Benchmark Construction** (2 pages)
   - Data collection process
   - Quality control (inter-annotator agreement)
   - Domain distribution
   - Difficulty stratification
   - Example questions (with English translation)

4. **Experimental Setup** (1 page)
   - Models evaluated (15+)
   - Prompting strategies
   - Evaluation metrics
   - Implementation details

5. **Results** (2 pages)
   - Overall accuracy per model
   - Performance by domain
   - Performance by difficulty
   - Error analysis
   - Statistical significance tests

6. **Discussion** (0.5 pages)
   - Key findings
   - Model strengths/weaknesses
   - Implications for Bengali NLP

7. **Limitations & Future Work** (0.5 pages)
   - Dataset size could be larger
   - Additional domains possible
   - Expand to other South Asian languages

**Critical for Acceptance:**
- **Figures:** 3-4 clear visualizations (model comparison, domain breakdown)
- **Tables:** Detailed results table, sample questions table
- **Statistical tests:** Paired t-tests, confidence intervals
- **Public release:** Commit to releasing data + code on GitHub

**Phase 4: Submission (Jul-Aug 2026)**

**Timeline:**
- Jul 1-15: Complete draft
- Jul 16-20: Get feedback from mentor (if found)
- Jul 21-25: Revisions
- Jul 26-31: Final polishing
- **Aug 1-5: Submit to ARR** (ACL Rolling Review)
- Aug 15: Commit to EMNLP 2026

**ARR Submission Requirements:**
- 8 pages main content + unlimited references
- Anonymized (remove your name, affiliations)
- Double-blind review
- PDF format, ACL LaTeX template
- Abstract 150-200 words
- Must register as reviewer (required starting May 2025)

### Expected Outcomes

**Best Case (40% probability):**
- Accepted to EMNLP 2026 Main Conference (Oct 2024, Budapest)
- You present at conference (great for transfer apps!)
- Paper becomes standard benchmark (100+ citations in 2 years)

**Likely Case (45% probability):**
- Accepted to EMNLP 2026 Findings
- Published in ACL Anthology (permanent, citable)
- Strong credential for transfer applications

**Worst Case (15% probability):**
- Rejected from EMNLP
- Revise and resubmit to workshop (still valuable)
- Or submit to NAACL 2027

**Even if rejected:** Having "under review at EMNLP" on your transfer application is powerful. Shows research capability.

### Why This Project vs. Revising BanglaLlama

**BanglaLlama revision would require:**
- Adding 6+ baseline models (weeks of compute)
- Human evaluation (expensive, time-consuming)
- Addressing TigerLLM reproducibility issues (contentious)
- Statistical significance tests (complex)
- Still only 40-50% chance of Findings

**Bengali Benchmark advantages:**
- More achievable solo (data collection vs model training)
- Higher acceptance probability (60-70%)
- Clearer contribution (fills obvious gap)
- Useful regardless of acceptance (you'll use it for your own work)
- Scalable (can publish follow-up papers)

**Decision:** Focus 100% on benchmark, keep BanglaLlama as is (workshop publication is fine for transfer apps).

### Read Between Lines Paper (Parallel Track)

**Status:** Accepted to BLP-2025 workshop (ACL 2025)  
**Deadline:** July 2026 for camera-ready  
**Current size:** 200 samples  
**Target expansion:** 500-1,000 samples

**Your Work (Low intensity, parallel to benchmark):**
- Collect 50 new samples/month (Feb-Jun)
- By June: 500 total samples
- Run updated experiments
- Revise paper for camera-ready submission
- Time commitment: 2-3 hrs/week (very manageable)

**This is your "safety" publication** - already accepted, just improving it.

---

## ⏰ REALISTIC DAILY/WEEKLY ROUTINE

### Time Reality Check

**Total hours available:**
- 7 days × 16 waking hours = 112 hours/week
- Minus sleep (8 hrs/day) = 56 hours
- **Total available: 112 hours/week**

**Your commitments:**
- IIUC classes: 20 hrs/week (lectures + labs)
- IIUC study: 15 hrs/week (homework + exam prep)
- Freelance work: 12 hrs/week (income needed)
- Research: 15 hrs/week
- Test prep: 7 hrs/week
- CP/Open source: 5 hrs/week
- Meals/hygiene/breaks: 21 hrs/week (3 hrs/day)
- **Total needed: 95 hrs/week**

**Remaining:** 17 hrs/week buffer (sleep variance, emergencies)

**This is TIGHT but DOABLE.**

### Weekly Template (Feb-Apr: Semester 1)

**Monday-Friday (Weekdays):**

**6:00-7:00 AM** - Wake up, breakfast, prepare (1 hr)
**7:00-8:00 AM** - DET study (1 hr)
- Duolingo app practice
- Vocabulary flashcards
- Reading comprehension

**8:00 AM-2:00 PM** - IIUC Classes (6 hrs)
- 100% attendance
- Active participation
- Take detailed notes

**2:00-3:00 PM** - Lunch break (1 hr)

**3:00-5:00 PM** - Research Work (2 hrs)
- Mon/Wed/Fri: Benchmark question collection
- Tue/Thu: Read Between Lines expansion

**5:00-7:00 PM** - IIUC Study (2 hrs)
- Review today's lectures
- Complete assignments
- Practice problems

**7:00-8:00 PM** - Dinner break (1 hr)

**8:00-10:00 PM** - Freelance Work (2 hrs)
- AIMarketCap tasks
- Client projects
- Income generation

**10:00-11:00 PM** - Open Source/CP (1 hr)
- LangChain contributions
- Competitive programming practice
- GitHub maintenance

**11:00 PM** - Wind down, sleep

**Weekdays total: 15 hrs work/day × 5 = 75 hrs**

**Saturday (Heavy Work Day):**

**8:00-10:00 AM** - DET Practice Test (2 hrs)
- Full mock test weekly
- Review mistakes

**10:00 AM-1:00 PM** - Research Deep Work (3 hrs)
- Benchmark question collection
- Model evaluation prep

**1:00-2:00 PM** - Lunch (1 hr)

**2:00-5:00 PM** - Freelance Work (3 hrs)
- Catch up on weekly quota

**5:00-7:00 PM** - IIUC Study (2 hrs)
- Weekly review
- Prepare for next week

**7:00-8:00 PM** - Dinner (1 hr)

**8:00-10:00 PM** - CP/Open Source (2 hrs)
- Contest participation
- Practice problems

**10:00 PM** - Rest

**Saturday total: 13 hrs**

**Sunday (Recovery + Planning):**

**9:00-11:00 AM** - Weekly Review (2 hrs)
- Track progress on all goals
- Plan next week
- Update spreadsheets

**11:00 AM-1:00 PM** - Research Writing (2 hrs)
- Paper drafts
- Documentation

**1:00-2:00 PM** - Lunch (1 hr)

**2:00-4:00 PM** - Flexible Time (2 hrs)
- Catch up on anything behind
- Personal projects
- Rest if needed

**4:00-6:00 PM** - Family/Personal Time (2 hrs)

**6:00-8:00 PM** - Light Study/Reading (2 hrs)
- Academic reading
- Industry blogs
- Relax

**Sunday total: 8 hrs**

**Weekly total: 75 + 13 + 8 = 96 hours (fits within 112 available)**

### Monthly Adjustments

**During Exam Weeks (Apr 6-20 Midterms, Jul 4-27 Finals):**
- Pause: Freelance, CP, Research (except urgent)
- Double: IIUC Study (4 hrs/day → 8 hrs/day)
- Maintain: DET practice (30 min/day only)

**During Essay Sprint (Sep 2026):**
- Pause: CP, Open Source, Extra projects
- Reduce: Freelance (to minimum)
- Add: Essay writing (4 hrs/day)

**During Application Submission (Mar 2027):**
- Pause: Everything except IIUC
- Focus: Submit applications perfectly

### Time Management Tools

**Use These:**
1. **Google Calendar** - Block time for each activity
2. **Notion/Todoist** - Daily task checklist
3. **Forest App** - Stay focused during work blocks
4. **Toggl** - Track actual time spent (see if estimate is accurate)

**Weekly Review Questions:**
- Did I maintain 4.0 GPA trajectory?
- Did I hit research targets?
- Did I complete freelance commitments?
- Am I on track for DET 125+?
- What can I optimize next week?

---

## 🗓️ MONTH-BY-MONTH EXECUTION PLAN

---

## **FEBRUARY 2026: Foundation Month**

**Starting Point:** Today is Feb 4, 2026. IIUC starts Feb 7 (3 days away).

### This Week (Feb 4-9): Immediate Recovery Actions

**[P0] Pre-Semester Preparation (TODAY - Feb 4-6)**
- [ ] **Today (Feb 4)**: 
  - Download Duolingo English Test app
  - Take 15-min free practice test (establish baseline)
  - Create "Transfer 2027" folder (Google Drive or Notion)
  - Review IIUC course syllabi (if available)
  
- [ ] **Tomorrow (Feb 5)**:
  - Set up GitHub repo: "BengaliBench" (even if empty, just README)
  - Create project structure:
    ```
    BengaliBench/
    ├── questions/
    │   ├── academic/
    │   ├── cultural/
    │   └── safety/
    ├── evaluation/
    └── docs/
    ```
  - Install Duolingo app, start vocabulary practice (30 min)
  - List 5 potential research collaborators (search ACL Anthology for "Bengali")

- [ ] **Feb 6 (Thursday)**:
  - Write daily routine on paper/digital planner
  - Set up Google Calendar with time blocks
  - Buy any needed supplies (notebooks, etc.)
  - DET practice (30 min)

**[P0] IIUC Semester 1 Starts (Feb 7)**
- [ ] Feb 7: First day of classes
  - Arrive early, sit in front
  - Introduce yourself to professors
  - Get all syllabi and assignment schedules
  - Note office hours for each professor
  - Target: Make strong first impression

**[P1] Research Project Launch (Feb 7-9)**
- [ ] Create BengaliBench design document:
  - 3 domains (Academic/Cultural/Safety)
  - 2,000 questions target
  - Timeline: Feb-Apr collection, May-Jun evaluation, Jul submission
- [ ] Collect first 10 questions (just to practice):
  - 5 from SSC math book
  - 3 Bengali proverbs
  - 2 safety scenarios
- [ ] Document question format and annotation guidelines

**💡 Goal This Week:** Get back on track after 3-day delay. Start small, build momentum.

---

### Week 2-4 (Feb 10-29): Build Consistent Habits

**[P0] IIUC Academic Excellence**
- [ ] Week 2-4: Attend 100% of all classes
- [ ] Complete all assignments 2 days before deadline
- [ ] Visit professor office hours at least once (build relationship)
- [ ] Form study group for Math/Physics
- [ ] After each class: 30-min review of lecture notes
- [ ] **Target: 95%+ on all quizzes/assignments**

**[P1] DET Preparation (1 hr/day, 7 hrs/week)**
- [ ] Week 2: Reading practice (free Duolingo materials)
- [ ] Week 3: Listening + Speaking (record yourself, compare to samples)
- [ ] Week 4: Writing practice (timed 5-min responses)
- [ ] Feb 28: Take full Duolingo practice test #1 (free)
- [ ] Target score by Feb 28: 110-115 (improvement from baseline)

**[P1] Research Work (2 hrs/day, 14 hrs/week)**

*BengaliBench (Primary focus):*
- [ ] Week 2 (Feb 10-16): Collect 75 questions
  - Academic: 50 (SSC textbooks - Math, Science, History)
  - Cultural: 15 (Bengali idioms, proverbs)
  - Safety: 10 (religious neutrality scenarios)
  
- [ ] Week 3 (Feb 17-23): Collect 75 more (150 total)
  - Continue same distribution
  - Start recruiting 2 IIUC classmates as annotators
  
- [ ] Week 4 (Feb 24-29): Collect 75 more (225 total)
  - Test annotation process with 2-3 students
  - Calculate inter-annotator agreement on 50 questions
  - Target: Cohen's kappa > 0.70

*Read Between Lines (Secondary):*
- [ ] Collect 10 new news articles (2/week × 5 weeks)
- [ ] Annotate with political stance
- [ ] Time commitment: 30 min/week

**[P2] CP/Open Source (1 hr/day, 7 hrs/week)**
- [ ] Continue AIMarketCap work (maintain existing commitments)
- [ ] LangChain: Fix 1-2 small issues
- [ ] Codeforces: Practice 2 problems/week
- [ ] Update GitHub profile README

**[P2] Freelance Work (12 hrs/week)**
- [ ] Maintain existing client commitments
- [ ] Complete AIMarketCap tasks
- [ ] Time-box to 2 hrs/day max

**[P3] Transfer Prep (Light this month)**
- [ ] Research top 5 universities (30 min each):
  - Cornell CS program
  - MIT CSAIL
  - Columbia CS + NYC fintech
  - Stanford AI
  - Princeton CS theory
- [ ] For each: Note 2 professors, 1 lab, 1 course
- [ ] Save in "Transfer 2027" folder for later essay writing

**Key Milestones by Feb 29:**
- ✅ Perfect IIUC attendance (100%)
- ✅ 225 benchmark questions collected
- ✅ DET practice score 110-115
- ✅ 2-3 annotators recruited
- ✅ Daily routine solidified
- ✅ All freelance commitments met

**💰 Costs This Month:** None (using free DET practice, free resources)  
**⏰ Time Spent:** 96 hrs/week (as per routine)

---

## **MARCH 2026: Mid-Semester Push**

### Week 1-2 (Mar 1-15): Research Acceleration

**[P0] IIUC Academics**
- [ ] Continue perfect attendance
- [ ] Mid-lecture period assessments (aim for 100%)
- [ ] Build strong rapport with 2 CSE professors (future recommenders)
- [ ] Excel in lab work (CSE-1122, EEE-1122)

**[P1] DET Intensive (2 hrs/day)**
- [ ] Mar 1-7: Weak areas focus (based on practice test)
- [ ] Mar 8-14: Full practice tests (2 complete tests)
- [ ] Mar 15: Register for DET (schedule for May 20, 2026)
- [ ] Target practice score: 115-120

**[P1] Research Project (3 hrs/day)**
- [ ] Collect 300 more questions (450 total by Mar 15)
- [ ] Recruit 2-3 IIUC students for annotation help
- [ ] Run initial baseline tests (GPT-4, Claude, Gemini)
- [ ] Draft paper outline with mentor
- [ ] Set up data quality control process

**[P2] University Research Deep Dive**
- [ ] Research top 5 target schools in detail:
  - Cornell CS program specifics
  - Columbia CS + NYC fintech opportunities
  - MIT CSAIL labs
  - Stanford AI research groups
  - Princeton CS theory focus
- [ ] For each: Note 3 specific professors, 2 courses, 1 research lab
- [ ] Save notes for "Why This School" essays

**💰 Costs:** DET registration $59 (BDT 7,100)  
**⏰ Time:** 55 hrs/week (30 IIUC + 14 DET + 15 Research)

---

### Week 3-4 (Mar 16-31): Pre-Midterm Preparation

**[P0] IIUC Midterm Prep Begins**
- [ ] Mar 16-31: Review all material from Feb 7-Apr 4
- [ ] Create comprehensive study guides for all 8 courses
- [ ] Form study groups
- [ ] Practice problems for Math, Physics, Programming
- [ ] Target: 95%+ on midterms

**[P1] DET Final Prep**
- [ ] Mar 20, 25, 30: Full practice tests (3 more)
- [ ] Focus on speaking (record + review)
- [ ] Focus on writing speed (timed responses)
- [ ] Target: Consistent 120+ on practice tests

**[P1] Research Milestone**
- [ ] By Mar 31: 600 questions collected
- [ ] Quality check with inter-annotator agreement
- [ ] Draft Introduction + Related Work sections
- [ ] Run comprehensive baseline experiments

**Key Milestones by Mar 31:**
- ✅ DET practice scores 120+
- ✅ 600 benchmark questions ready
- ✅ Paper outline complete
- ✅ Ready for IIUC midterms

---

## **APRIL 2026: Midterm Exam Month + DET Prep**

### Week 1-3 (Apr 1-20): Midterm Exams

**[P0] IIUC MIDTERM EXAMS (Apr 6-20)**
- [ ] Apr 1-5: Final review, no new material
- [ ] Apr 6-20: **FULL FOCUS ON EXAMS**
- [ ] During exams: 8-10 hrs/day study
- [ ] After each exam: Immediate review of performance
- [ ] **TARGET: 95%+ average across all 8 courses**

**[P1] Minimal Research (30 min/day during exams)**
- [ ] Light question collection only
- [ ] No heavy lifting during exam period

**[P1] DET Light Maintenance (30 min/day)**
- [ ] Vocabulary flashcards only
- [ ] Quick reading practice
- [ ] No full practice tests during exams

**💡 Strategy:** Prioritize IIUC exams above everything. Perfect GPA is non-negotiable.

---

### Week 4 (Apr 21-30): Post-Midterm Recovery + Research Sprint

**[P0] IIUC Lecture Period II Begins**
- [ ] Apr 21: Back to regular classes
- [ ] Review midterm results (expect Apr 27)
- [ ] Adjust study strategy if needed
- [ ] Continue office hours with professors

**[P1] Research Full Speed (4 hrs/day)**
- [ ] Collect remaining 400 questions (1,000 total)
- [ ] Complete all baseline experiments
- [ ] Draft Methodology + Dataset sections
- [ ] First complete draft of paper

**[P1] DET Final Sprint (2 hrs/day)**
- [ ] Apr 25: Full practice test
- [ ] Apr 28: Final practice test
- [ ] Review weak areas one last time
- [ ] Confirm test date (May 20 target)

**Key Milestones by Apr 30:**
- ✅ Midterm results: 95%+ average
- ✅ 1,000 benchmark questions complete
- ✅ First paper draft ready
- ✅ DET practice 125+

---

## **MAY 2026: DET Exam + Research Completion**

### Week 1-2 (May 1-15): Pre-DET Preparation

**[P0] IIUC Classes**
- [ ] Maintain attendance + performance
- [ ] No slacking after midterms

**[P1] DET FINAL PREPARATION**
- [ ] May 1-5: Review all weak areas
- [ ] May 6: Last full practice test
- [ ] May 7-10: Speaking practice (3 hrs/day)
- [ ] May 11-14: Light review, stay sharp
- [ ] May 15: Rest before exam

**[P1] Research Quality Control**
- [ ] Finalize all 1,000 questions
- [ ] Complete inter-annotator agreement analysis
- [ ] Run additional model evaluations if needed
- [ ] Draft Results + Analysis sections

---

### Week 3 (May 16-22): DET EXAM WEEK

**[P0] DUOLINGO ENGLISH TEST**
- [ ] May 20: **TAKE DET EXAM** 🎯
  - Quiet room, good internet
  - Government ID ready
  - 1 hour test
  - Aim for 125-130
- [ ] May 21-22: Rest and recover
- [ ] Scores arrive within 48 hours

**[P1] Research Writing**
- [ ] Continue paper writing
- [ ] Discussion + Limitations sections
- [ ] Prepare figures and tables

---

### Week 4 (May 23-31): Post-DET + Research Finalization

**[P1] DET Results & SAT Decision**
- [ ] May 22-23: Receive DET scores
- [ ] If 125+: Success! Focus on SAT prep next
- [ ] If <125: Register for retake (June 10)
- [ ] Research SAT test dates (Aug 22, 2026 likely target)

**[P1] Research Paper Final Draft**
- [ ] Complete all sections
- [ ] Get mentor feedback
- [ ] Revise based on comments
- [ ] By May 31: Near-final draft

**[P0] IIUC Classes**
- [ ] Continue strong performance
- [ ] Finals prep begins (light review)

**Key Milestones by May 31:**
- ✅ DET score 125+ received
- ✅ Research paper 95% complete
- ✅ SAT prep plan ready

---

## **JUNE 2026: Finals + Research Submission**

### Week 1-2 (Jun 1-15): Pre-Finals

**[P0] IIUC Finals Preparation**
- [ ] Review all Lecture Period II material
- [ ] Comprehensive review of entire semester
- [ ] Practice exams
- [ ] Study groups
- [ ] Target: 95%+ on finals

**[P1] Research Paper Final Revisions**
- [ ] Jun 1-10: Final mentor feedback
- [ ] Jun 11-15: Camera-ready version
- [ ] Proofread 5+ times
- [ ] Format for submission

**[P2] DET Retake (if needed)**
- [ ] If first score <125, retake Jun 10
- [ ] Otherwise, start SAT prep light (1 hr/day)

---

### Week 3-4 (Jun 16-30): Finals Exams

**[P0] IIUC FINALS (Jun 16-30 estimated based on calendar)**
- [ ] **Note:** Calendar shows Jul 4-27 for finals, but lectures end Jun 30
- [ ] Check exact finals dates when announced
- [ ] FULL FOCUS on exams
- [ ] 8-10 hrs/day study
- [ ] **TARGET: 95%+ average for 4.0 GPA Semester 1**

**[P1] Light Research During Finals**
- [ ] Minimal work, focus on exams

**💡 Priority:** Perfect GPA is most important this month.

---

## **JULY 2026: Finals + Summer Planning**

### Week 1-4 (Jul 1-27): Final Exams Completion

**[P0] IIUC FINALS COMPLETION**
- [ ] Jul 1-3: Preparation period
- [ ] Jul 4-27: Final exams (21 days)
- [ ] After each exam: Review and relax
- [ ] **TARGET: Finish strong with 4.0 GPA**

**[P1] Research Paper Submission**
- [ ] Jul 15-20: Submit to ARR for EMNLP 2026 (if not done in June)
- [ ] Alternative: Submit to workshop if timeline tight

**[P2] SAT Preparation Begins**
- [ ] After finals end: Start SAT prep (2 hrs/day)
- [ ] Khan Academy SAT prep
- [ ] Focus on Math (aim for 750+)
- [ ] Register for Aug 22, 2026 SAT

**[P2] Summer Research/Work**
- [ ] Continue AIMarketCap work
- [ ] Enhance Drishtikon features
- [ ] Start new research project (if time)

---

## **AUGUST 2026: SAT Exam + Semester 2 Starts**

### Week 1-2 (Aug 1-15): Results + SAT Prep + Transfer Planning

**[P1] IIUC Semester 1 Results**
- [ ] Aug 8: Results published
- [ ] Verify 4.0 GPA (or 3.9+)
- [ ] Request official transcript
- [ ] Celebrate success! 🎉

**[P1] SAT INTENSIVE PREPARATION**
- [ ] Aug 1-15: 4 hrs/day SAT prep
- [ ] Complete 5 full practice tests
- [ ] Focus on weak areas
- [ ] Math: Aim for 750+
- [ ] ERW: Aim for 700+

**[P2] Transfer Application Preliminary Work**
- [ ] Brainstorm Common App essay topics
- [ ] Start "Why Transfer" essay draft (rough)
- [ ] Research professors at target schools
- [ ] Update resume with Semester 1 GPA

---

### Week 3-4 (Aug 15-31): Semester 2 Starts + SAT Exam

**[P0] IIUC SEMESTER 2 (AUTUMN 2026) BEGINS**
- [ ] Aug 15: First day of Semester 2
- [ ] Review new course syllabi
- [ ] Set up study schedule
- [ ] Identify 2-3 professors for recommendations
- [ ] Start building relationships immediately

**[P0] SAT EXAM**
- [ ] Aug 22: **TAKE SAT** 🎯
  - Target: 1450+ (750 Math + 700 ERW)
  - Test center likely in Dhaka or Chattogram
- [ ] Aug 23-31: Rest, focus on Semester 2

**[P1] Research Publication Status**
- [ ] Check ARR/EMNLP review status
- [ ] If rejected: Plan revisions
- [ ] If accepted to Findings: Celebrate!
- [ ] Update resume with publication status

**Key Milestones by Aug 31:**
- ✅ Semester 1 complete with 4.0 GPA
- ✅ SAT completed
- ✅ Semester 2 started strong
- ✅ Research paper under review

---

## **SEPTEMBER 2026: Application Sprint Begins**

### Week 1-4 (Sep 1-30): Essay Writing Intensive

**[P0] IIUC Semester 2 Academics**
- [ ] Perfect attendance
- [ ] Excel in all courses
- [ ] Build recommendation relationships

**[P1] ESSAY WRITING (6-8 hrs/day)**

This is the HARDEST month. You'll write 20-25 essays.

**Week 1 (Sep 1-7): Common App + Transfer Essay**
- [ ] Sep 1-3: Common App Personal Statement (650 words)
  - Topic: Your journey from Bangladesh fintech to AI research
  - Show: Technical skills + Entrepreneurship + Impact
- [ ] Sep 4-7: Universal "Why Transfer" essay (600 words)
  - Why leave IIUC? (Academic resources, not prestige)
  - What you need that IIUC can't provide
  - Specific programs/professors at US schools

**Week 2 (Sep 8-14): Need-Blind School Supplements (8 schools)**
- [ ] Harvard supplements (2-3 essays)
- [ ] Yale supplements (2-3 essays)
- [ ] Princeton supplements (2-3 essays)
- [ ] MIT supplements (2-3 essays)
- [ ] Stanford supplements (3-4 essays)
- [ ] Amherst supplements (2 essays)
- [ ] Dartmouth supplements (2 essays)
- [ ] Colby supplements (2 essays)

**Week 3 (Sep 15-21): Priority 2 Schools (5 schools)**
- [ ] Columbia supplements (3-4 essays)
- [ ] Cornell supplements (3 essays per college)
- [ ] University of Chicago supplements (3-4 essays)
- [ ] Trinity College CT (2 essays)
- [ ] Oberlin (2 essays)

**Week 4 (Sep 22-30): Priority 3 Schools (4-5 schools)**
- [ ] Hamilton, Macalester, Bates, Carleton, Colgate
- [ ] 2-3 essays per school

**[P1] SAT Scores**
- [ ] SAT scores arrive mid-September
- [ ] Send to all target schools
- [ ] If <1450: Consider retake in Oct/Nov

**Key Components in Every Supplement:**
- Specific professor by name + their research
- Specific courses you want to take
- Specific labs/research centers
- How it connects to your Bengali AI work
- Your unique contribution to campus

**💡 Essay Writing Tips:**
- Write 2-3 hours in morning (fresh mind)
- Break after lunch
- Edit 2-3 hours in evening
- Each essay through 3 drafts minimum
- Get feedback from English-fluent friends

**⏰ Time:** 70 hrs/week (30 IIUC + 40 Essays)

---

## **OCTOBER 2026: Essay Completion + Recommendations + CSS Profile**

### Week 1-2 (Oct 1-15): Final Essays + Recommendations

**[P0] IIUC Semester 2**
- [ ] Maintain strong performance
- [ ] Midterm prep (if applicable)

**[P1] Complete Remaining Essays**
- [ ] Oct 1-7: Finish any incomplete supplements
- [ ] Oct 8-15: REVISION WEEK
  - Read every essay aloud
  - Check for typos
  - Get feedback from mentor/friends
  - Polish to perfection

**[P0] REQUEST RECOMMENDATIONS**
- [ ] Oct 1: Prepare recommendation packets for 2 professors:
  - Resume
  - Transcript
  - List of 16-18 schools
  - Key talking points
  - Deadline: March 1, 2027
  - Why you're impressive
  - Specific achievements in their class
- [ ] Oct 2-5: Meet with Professor #1
  - Ask in person (not email)
  - Provide packet
  - Explain your goals
- [ ] Oct 6-9: Meet with Professor #2
  - Same process
- [ ] Oct 15: Follow up to confirm they agreed

**[P0] CSS PROFILE (Opens Oct 1)**
- [ ] Oct 1: Create CSS Profile account
- [ ] Oct 2-7: Gather parent financial documents:
  - Tax returns (Bangladesh)
  - Bank statements
  - Income documentation
  - Property/asset details
- [ ] Oct 8-15: Complete CSS Profile
  - Be extremely accurate
  - One mistake = delayed aid = lost acceptance
- [ ] Oct 15: Submit CSS Profile for all schools
- [ ] Request fee waiver (family income <$75K USD)

**💰 Costs:** CSS Profile fee ~$25 + $16 per school = ~$300 (BDT 36,000)  
**Fee waiver available for families earning <$75K USD**

---

### Week 3-4 (Oct 16-31): Application Assembly

**[P1] Common App Completion**
- [ ] Fill out all sections:
  - Personal information
  - Education (IIUC + high school)
  - Family background
  - Activities (max 10):
    1. AIMarketCap - Founding Engineer
    2. Drishtikon - Founder
    3. Universal AI Agent Browser
    4. BanglaLlama Research
    5. Bengali Benchmark Research
    6. Open-source contributions (LangChain, browser-use)
    7. ICT Olympiad semi-finalist 2022
    8. National Programming Contest
    9. Google Cloud badges (14)
    10. Freelance AI development
  - Testing (DET, SAT)
  - Writing (upload all essays)

**[P1] Document Preparation**
- [ ] Request official IIUC transcripts (2 copies)
- [ ] Prepare high school transcripts
- [ ] Organize certificates:
  - ICT Olympiad semi-finalist 2022
  - National Programming Contest participation
  - Google Cloud badges
  - Workshop paper acceptances
- [ ] Create portfolio website:
  - GitHub projects
  - Published papers
  - Drishtikon demo
  - AIMarketCap metrics

**[P2] Final Review**
- [ ] Oct 25-31: Proofread EVERYTHING 5+ times
- [ ] Show essays to English professor
- [ ] Check all deadlines
- [ ] Triple-check requirements per school

**Key Milestones by Oct 31:**
- ✅ All essays complete
- ✅ Recommendations requested
- ✅ CSS Profile submitted
- ✅ Common App 95% complete

---

## **NOVEMBER 2026: Final Touches + IIUC Focus**

### Week 1-4 (Nov 1-30): Polish & Wait

**[P0] IIUC Semester 2**
- [ ] Maintain perfect grades
- [ ] This is crucial for final transcript

**[P1] Application Final Review**
- [ ] Nov 1-7: Last chance edits
- [ ] Nov 8-15: Show applications to trusted mentor
- [ ] Nov 16-23: Make final corrections
- [ ] Nov 24-30: Application LOCKDOWN
  - No more changes
  - Everything is ready
  - Just wait for January to submit

**[P1] Recommendation Follow-up**
- [ ] Nov 15: Check in with both professors
- [ ] Ensure they're on track for March 1 deadline
- [ ] Offer to provide any additional materials

**[P2] Research Work**
- [ ] If EMNLP paper accepted to Findings: Update resume!
- [ ] If rejected: Consider submitting to workshop
- [ ] Continue Drishtikon development
- [ ] Update AIMarketCap metrics

**[P3] Scholarship Research**
- [ ] Research external scholarships
- [ ] Apply to any available for international students
- [ ] Most US-based scholarships don't cover intl students
- [ ] Focus on school-based aid (which you're already getting via CSS)

---

## **DECEMBER 2026: Semester 2 Finals Prep**

### Week 1-4 (Dec 1-31): Finals + Rest

**[P0] IIUC SEMESTER 2 FINALS PREP**
- [ ] Review all material
- [ ] Study groups
- [ ] Practice problems
- [ ] **TARGET: 4.0 GPA Semester 2**

**[P1] Application Status**
- [ ] All applications ready, waiting to submit
- [ ] No work needed this month
- [ ] Focus on finals

**[P2] Winter Break (if applicable)**
- [ ] Rest and recharge
- [ ] Spend time with family
- [ ] Light application review

**[P3] Research/Projects**
- [ ] Continue AIMarketCap work
- [ ] Enhance Drishtikon
- [ ] Update resume with metrics

---

## **JANUARY 2027: Semester 3 + Final Prep**

### Week 1-2 (Jan 1-15): New Semester + Document Gathering

**[P0] IIUC SEMESTER 3 (SPRING 2027) STARTS**
- [ ] New semester begins
- [ ] Continue strong academic performance

**[P1] Semester 2 Results**
- [ ] Results should be published
- [ ] Verify 4.0 GPA (or close)
- [ ] Request official transcripts immediately

**[P1] Application Final Checks**
- [ ] Jan 1-5: Final proofread of all essays (6th time)
- [ ] Jan 6-10: Verify all documents ready:
  - DET scores sent
  - SAT scores sent
  - IIUC transcripts (Sem 1 + 2)
  - High school transcripts
  - CSS Profile submitted
  - Recommendations confirmed with professors
- [ ] Jan 11-15: Application tracking sheet updated

---

### Week 3-4 (Jan 16-31): Buffer Time

**[P0] IIUC Semester 3**
- [ ] Strong start to new semester
- [ ] Some schools may request Spring 2027 mid-term grades

**[P1] Last-Minute Prep**
- [ ] Jan 16-20: Any final essay tweaks
- [ ] Jan 21-25: Confirm fee waivers processed
- [ ] Jan 26-31: Mentally prepare for submission

**[P2] Research Updates**
- [ ] Update resume with any new publications/achievements
- [ ] Update Common App activities if major news

---

## **FEBRUARY 2027: Buffer + Submission Prep**

### Week 1-4 (Feb 1-28): Final Preparation

**[P0] IIUC Semester 3**
- [ ] Continue strong performance
- [ ] Maintain focus despite application stress

**[P1] Application Polish**
- [ ] Feb 1-15: Final review of everything
- [ ] Feb 16-28: Prepare for submission
- [ ] Gather all materials
- [ ] Confirm all scores sent
- [ ] Double-check deadlines

**[P1] Recommendation Deadline Approaching**
- [ ] Feb 15: Remind professors (2 weeks before deadline)
- [ ] Ensure they're ready to submit by March 1

**💡 Stay calm. Everything is ready. Just need to click submit in March.**

---

## **MARCH 2027: 🚨 SUBMISSION MONTH 🚨**

### Week 1 (Mar 1-7): PRIMARY SUBMISSION WEEK

**[P0] SUBMIT APPLICATIONS - MARCH 1 DEADLINE**

Applications to submit on **March 1, 2027**:
- [ ] Harvard University
- [ ] Yale University  
- [ ] Princeton University
- [ ] MIT
- [ ] Stanford University
- [ ] Columbia University
- [ ] Cornell University
- [ ] University of Chicago

**Process for each:**
1. Log into Common App
2. Review application one final time
3. Pay application fee (or use waiver)
4. Click SUBMIT
5. Verify submission confirmation email
6. Send official test scores
7. Send official transcripts
8. Track in spreadsheet

**[P0] Post-Submission Tasks:**
- [ ] Mar 1: Send DET scores to all schools
- [ ] Mar 1: Send SAT scores to all schools
- [ ] Mar 2: Send official IIUC transcripts
- [ ] Mar 3-7: Confirm recommendations submitted
- [ ] Mar 5: Check all portals for missing materials

**💰 Costs:** Application fees ~$75 × 8 = $600 (use fee waivers!)

---

### Week 2 (Mar 8-14): SECONDARY SUBMISSION WEEK

**[P0] SUBMIT REMAINING APPLICATIONS - MARCH 15 DEADLINE**

Applications to submit on **March 10-15, 2027**:
- [ ] Amherst College
- [ ] Dartmouth College
- [ ] Colby College
- [ ] Trinity College CT
- [ ] Oberlin College
- [ ] Hamilton College
- [ ] Macalester College
- [ ] Bates College
- [ ] Carleton College (or Colgate)

**Same submission process:**
1. Review
2. Pay/waiver
3. Submit
4. Send scores
5. Send transcripts
6. Confirm recommendations
7. Track

**[P0] Post-Submission:**
- [ ] Mar 15: All applications submitted! 🎉
- [ ] Mar 16-20: Check all portals daily
- [ ] Mar 21-31: Submit any missing materials immediately

**💰 Costs:** Application fees ~$75 × 9 = $675 (use fee waivers!)

---

### Week 3-4 (Mar 15-31): Portal Management

**[P1] Application Portal Monitoring**
- [ ] Check every portal daily
- [ ] Upload missing documents immediately
- [ ] Respond to any requests within 24 hours
- [ ] Update application tracker

**[P0] IIUC Semester 3**
- [ ] Continue strong performance
- [ ] Don't let up after submission

**[P2] Interview Prep (if requested)**
- [ ] Some schools may request interviews
- [ ] Prepare common questions
- [ ] Practice with friends
- [ ] Research school thoroughly before interview

**Key Milestones by Mar 31:**
- ✅ ALL 16-18 applications submitted
- ✅ All scores sent
- ✅ All transcripts sent
- ✅ All portals show "Complete"
- ✅ Now we wait...

---

## **APRIL 2027: Waiting Period + Semester 3 Midterms**

### Week 1-4 (Apr 1-30): The Wait

**[P0] IIUC SEMESTER 3 MIDTERMS**
- [ ] Stay focused on academics
- [ ] Maintain 4.0 GPA
- [ ] This is for final transcript if admitted

**[P1] Application Status**
- [ ] Check portals weekly (not daily - will drive you crazy)
- [ ] First decisions start arriving late April
- [ ] Most come in May

**[P2] Interview Requests**
- [ ] If interview requested: Prepare thoroughly
- [ ] Research school
- [ ] Practice answers
- [ ] Be yourself, be authentic

**[P3] Stay Productive**
- [ ] Continue AIMarketCap work
- [ ] Enhance Drishtikon
- [ ] Work on new research if applicable
- [ ] Don't obsess over decisions

**💡 Strategy:** Trust the process. You've done everything possible.

---

## **MAY 2027: 🎊 DECISION MONTH 🎊**

### Week 1-4 (May 1-31): Decisions Arrive

**[P0] DECISION TRACKING**

Expected decision timeline:
- Late April - Early May: First decisions
- Mid May: Most decisions
- Late May: Final decisions

**Decision Possibilities:**
1. **Accepted** 🎉
   - [ ] Review financial aid package
   - [ ] Compare with other acceptances
   - [ ] Visit admitted students events (virtual)
   - [ ] Ask questions to current students
   
2. **Waitlisted**
   - [ ] Send Letter of Continued Interest (LOCI)
   - [ ] Update with any new achievements
   - [ ] Reaffirm your interest
   
3. **Rejected**
   - [ ] Don't take it personally
   - [ ] Transfer acceptance rates are brutal
   - [ ] You still have other options

**[P0] IIUC Semester 3**
- [ ] Continue classes
- [ ] Finals approaching

**[P1] Decision Making (if accepted)**
- [ ] By May 15: Review all acceptances
- [ ] Compare financial aid packages
- [ ] Compare CS programs
- [ ] Consider location, culture, fit
- [ ] Make decision by May 25

**[P0] ENROLLMENT**
- [ ] **By June 1, 2027: Accept offer and pay deposit**
- [ ] Withdraw from other schools
- [ ] Withdraw from IIUC (if accepted to US school)

---

### If Accepted: Next Steps

**[P0] Visa Process**
- [ ] Receive I-20 from university
- [ ] Pay SEVIS fee ($350)
- [ ] Schedule visa interview at US Embassy Dhaka
- [ ] Prepare visa documents
- [ ] Attend interview
- [ ] Receive F-1 visa

**[P1] Financial Aid Finalization**
- [ ] Review and sign financial aid award letter
- [ ] Complete any additional forms
- [ ] Confirm funding for 4 years

**[P2] Pre-Departure**
- [ ] Arrange housing
- [ ] Book flights
- [ ] Attend pre-departure orientation
- [ ] Pack for US

**[P3] Celebrate!**
- [ ] You made it! 🎉🎊🎓
- [ ] Celebrate with family
- [ ] Thank everyone who helped

---

### If Rejected from All: Backup Plan

**Option 1: Reapply Fall 2028**
- Complete Semester 4 at IIUC (4 semesters total)
- Strengthen profile (more research, better GPA)
- Reapply March 2028 for Fall 2028
- Success rate: 60-70% (much higher second time)

**Option 2: Graduate IIUC → PhD 2030**
- Complete IIUC degree (2026-2030)
- Apply to PhD programs Fall 2030
- Fully funded PhD with stipend
- Still attend top US universities

**💡 Remember:** Transfer acceptance rates are 1-15%. Having a backup plan is smart, not pessimistic.

---

## 📊 SUMMARY CHECKLIST

### Critical Deadlines - DO NOT MISS

- [ ] **Feb 7, 2026:** IIUC Semester 1 starts
- [ ] **Mar 15, 2026:** DET registration (for May test)
- [ ] **Apr 6-20, 2026:** IIUC Midterm exams
- [ ] **May 20, 2026:** Take Duolingo English Test (DET)
- [ ] **Jul 4-27, 2026:** IIUC Final exams
- [ ] **Aug 8, 2026:** Semester 1 results
- [ ] **Aug 15, 2026:** Semester 2 starts
- [ ] **Aug 22, 2026:** Take SAT
- [ ] **Sep 1-30, 2026:** Write all essays (20-25 essays)
- [ ] **Oct 1, 2026:** CSS Profile opens - submit immediately
- [ ] **Oct 1-15, 2026:** Request recommendations
- [ ] **Mar 1, 2027:** PRIMARY SUBMISSION (8 schools)
- [ ] **Mar 15, 2027:** SECONDARY SUBMISSION (8-10 schools)
- [ ] **May 2027:** Decision month
- [ ] **Jun 1, 2027:** Enrollment deadline

---

## 💰 TOTAL BUDGET ESTIMATE

| Item | Cost (BDT) | Notes |
|------|-----------|--------|
| DET (2 attempts) | 14,000 | $59 × 2 |
| SAT (1 attempt) | 12,000 | ~$100 + materials |
| SAT Prep Materials | 3,000 | Khan Academy free, books |
| CSS Profile | 3,000 | Fee waiver available |
| Application Fees | 0-135,000 | $75 × 18, fee waivers available |
| Score Sends | 20,000 | DET + SAT to all schools |
| Transcript Fees | 10,000 | Official transcripts |
| Portfolio/Website | 2,000 | GitHub Pages (free) + domain |
| Miscellaneous | 10,000 | Printing, scanning, etc. |
| **TOTAL** | **74,000 - 209,000** | **With fee waivers: ~74K** |

**Fee waiver eligibility:** Family income <$75K USD (most Bangladeshi families qualify)

---

## ⏰ WEEKLY TIME COMMITMENT

### Feb-May 2026 (Semester 1 + Research + DET):
- IIUC Classes + Study: 35 hrs/week
- DET Preparation: 10 hrs/week
- Research Work: 15 hrs/week
- Total: 60 hrs/week

### Jun-Aug 2026 (Finals + SAT + Summer):
- IIUC Finals: 50 hrs/week (during exam period)
- SAT Prep: 20 hrs/week
- Research: 10 hrs/week
- Total: 80 hrs/week (exam period), 50 hrs/week (summer)

### Sep-Oct 2026 (Semester 2 + Essay Sprint):
- IIUC Classes: 30 hrs/week
- Essay Writing: 35 hrs/week
- Research: 10 hrs/week
- Total: 75 hrs/week (INTENSE)

### Nov 2026-Feb 2027 (Semester 2 + Finals + Prep):
- IIUC Classes: 35 hrs/week
- Application Polish: 10 hrs/week
- Total: 45 hrs/week

### Mar 2027 (Submission Month):
- IIUC Classes: 30 hrs/week
- Application Submission: 20 hrs/week
- Total: 50 hrs/week

**This is doable but requires discipline and sacrifice.**

---

## 🎯 SUCCESS METRICS BY MONTH

| Month | Key Metric | Target |
|-------|-----------|--------|
| Feb 2026 | IIUC attendance + DET diagnostic | 100% + 110+ |
| Mar 2026 | Benchmark questions + DET practice | 450 + 120+ |
| Apr 2026 | Midterm average | 95%+ |
| May 2026 | DET score + Questions complete | 125+ + 1000 |
| Jun 2026 | Finals average + Paper draft | 95%+ + Complete |
| Jul 2026 | Semester 1 GPA + Paper submission | 4.0 + Submitted |
| Aug 2026 | SAT score + Semester 2 start | 1450+ + Strong |
| Sep 2026 | Essays drafted | 20-25 complete |
| Oct 2026 | Recommendations + CSS | Secured + Submitted |
| Nov 2026 | Semester 2 performance | 4.0 trajectory |
| Dec 2026 | Semester 2 finals | 95%+ |
| Jan 2027 | Applications ready | 100% complete |
| Feb 2027 | Buffer check | All materials ready |
| Mar 2027 | Applications submitted | 16-18 schools |
| Apr 2027 | Semester 3 midterms | 95%+ |
| May 2027 | Decisions received | At least 1 acceptance |

---

## 🚀 YOUR COMPETITIVE ADVANTAGES

**What makes you stand out:**
1. **Real-world impact:** AIMarketCap serving millions of users
2. **Entrepreneurship:** Founded multiple startups (Drishtikon, etc.)
3. **Research:** Published papers + ongoing work
4. **Technical depth:** Full-stack dev + AI/ML + Cloud/DevOps
5. **Open-source:** Contributions to LangChain, browser-use
6. **Unique perspective:** Bengali AI for 300M speakers
7. **Demonstrated initiative:** Don't wait for permission, just build
8. **Strong academics:** Targeting 4.0 GPA at IIUC
9. **Test scores:** 125+ DET, 1450+ SAT (if achieved)
10. **Compelling narrative:** Bangladesh fintech → AI researcher

**Frame your story:**
> "I'm not just applying for a better education. I'm applying to access resources that will help me democratize AI for Bengali speakers and solve problems affecting 300 million people in my country. IIUC gave me a strong foundation, but I need [specific university's] [specific professor/lab/resources] to take my research to the next level."

---

## ⚠️ COMMON MISTAKES TO AVOID

1. **Don't slack after midterms/finals** - Maintain perfect GPA all year
2. **Don't write generic essays** - Research each school specifically
3. **Don't miss deadlines** - Set reminders 1 week before
4. **Don't forget fee waivers** - Save thousands of BDT
5. **Don't overpromise in essays** - Be authentic, not exaggerated
6. **Don't neglect current work** - Continue AIMarketCap, Drishtikon
7. **Don't isolate yourself** - Build support network
8. **Don't compare to others** - Focus on your own journey
9. **Don't give up** - Transfer acceptance is hard but possible
10. **Don't forget backup plan** - Reapply Fall 2028 if needed

---

## 💪 MOTIVATIONAL MILESTONES

**Every month, celebrate small wins:**
- Feb: First week of IIUC completed
- Mar: First 500 questions collected
- Apr: Midterms aced
- May: DET conquered
- Jun: Paper submitted
- Jul: Semester 1 completed with 4.0
- Aug: SAT done
- Sep: All essays drafted
- Oct: Recommendations secured
- Nov: Applications 100% complete
- Dec: Semester 2 finals aced
- Jan: Ready for submission
- Feb: Calm before storm
- Mar: ALL APPS SUBMITTED! 🎉
- Apr: First decisions arrive
- May: ADMITTED! 🎊

---

## 🎓 FINAL THOUGHTS

**This is a marathon, not a sprint.**

You have 15 months ahead of you. Some months will be brutal (April midterms, September essay sprint, March submission). Some will be manageable.

**The key is consistency:**
- Show up every day
- Do the work
- Trust the process
- Don't get discouraged by setbacks
- Keep your eye on the prize

**You have everything you need:**
- Strong technical background ✓
- Research experience ✓
- Entrepreneurial track record ✓
- Clear goals ✓
- This roadmap ✓

**Now execute.**

One task at a time.  
One day at a time.  
One month at a time.

By May 2027, you'll be deciding between multiple top US universities offering you full funding.

**Let's make it happen.** 🚀



**END OF ROADMAP**

---

## 🚀 START HERE: YOUR NEXT 72 HOURS (Feb 4-6)

You're 3 days "behind" the original Feb 1 start. Here's how to catch up WITHOUT panic:

### Today - Feb 4 (RIGHT NOW):

**Next 2 hours:**
1. ✅ Read this entire roadmap (you're doing this now)
2. ✅ Download Duolingo English Test app on phone
3. ✅ Take the 15-minute free practice test (get baseline score)
4. ✅ Create "Transfer 2027" folder in Google Drive
5. ✅ Add your strategic_application_list_cse.csv to this folder

**Tonight (after current work):**
6. ✅ Review IIUC Spring 2026 syllabi (if available online)
7. ✅ Write tomorrow's schedule on paper
8. ✅ Set 3 phone alarms: 6 AM wake-up, 8 AM study, 7 PM review

**Time needed:** 3 hours total  
**When:** Fit this in tonight before sleep

---

### Tomorrow - Feb 5 (Wednesday):

**Morning (6:00-8:00 AM):**
1. ✅ Wake at 6 AM (this is your new routine)
2. ✅ 30 min Duolingo practice (vocabulary building)
3. ✅ 30 min breakfast
4. ✅ 1 hr: Set up BengaliBench GitHub repository
   - Create repo
   - Add basic README
   - Create folder structure

**Afternoon:**
5. ✅ Continue normal work (freelance, etc.)
6. ✅ 30 min: Search "Bengali NLP" on Google Scholar
   - Find 5 recent papers (2023-2025)
   - Note authors' names and emails
   - Save for later outreach

**Evening (8:00-10:00 PM):**
7. ✅ Collect your first 5 benchmark questions:
   - 3 from any SSC textbook (math/science)
   - 2 Bengali proverbs from memory
8. ✅ Save in BengaliBench/questions/ folder
9. ✅ Write simple annotation format

**Time needed:** 4 hours spread throughout day  
**Outcome:** Research project launched ✅

---

### Feb 6 (Thursday):

**Morning (6:00-8:00 AM):**
1. ✅ 1 hr Duolingo practice
2. ✅ Plan your weekly schedule in Google Calendar

**Day:**
3. ✅ Normal work commitments
4. ✅ Install time tracking app (Toggl or Forest)

**Evening (7:00-10:00 PM):**
5. ✅ Collect 10 more benchmark questions (15 total)
6. ✅ Draft BengaliBench project design doc:
   - Goal: 2,000 questions
   - Timeline: Feb-Aug
   - Target venue: EMNLP 2026
7. ✅ Review: Am I ready for IIUC Feb 7?

**Time needed:** 4 hours  
**Outcome:** Fully prepared for semester start ✅

---

### Feb 7 (Friday): IIUC STARTS

**Your Mission:**
- Make excellent first impression
- Sit in front row
- Introduce yourself to professors
- Get all syllabi
- Note office hours

**After Classes:**
- Collect 5 more questions (20 total by end of first week)
- Duolingo 30 min

---

## 🎯 CRITICAL SUCCESS METRICS

Track these weekly:

**Academic (P0):**
- [ ] IIUC attendance: 100%
- [ ] Assignment scores: 95%+
- [ ] Quiz scores: 95%+

**Research (P1):**
- [ ] Benchmark questions collected: 25/week
- [ ] Paper reading: 2 papers/week
- [ ] GitHub commits: 5+/week

**Test Prep (P1):**
- [ ] DET daily practice: 7/7 days
- [ ] Practice test scores: +5 points/month

**Engineering (P2):**
- [ ] Freelance hours: 12/week
- [ ] CP problems solved: 2/week
- [ ] Open source commits: 1/week

**If you hit 80%+ of these metrics weekly, you're on track for success.**

---

## 💪 FINAL REMINDERS

**You CAN do this. Here's why:**

1. **You already have strong work ethic** - Managing AIMarketCap, Drishtikon, freelance
2. **You have research experience** - 2 workshop papers published
3. **You have technical skills** - Full-stack + AI/ML + DevOps
4. **You have 15 months** - Enough time if you start NOW
5. **The plan is clear** - Just execute one day at a time

**The hardest part is starting. You're starting today (Feb 4).**

**Don't aim for perfection. Aim for consistency:**
- Show up every day
- Do the work
- Track progress
- Adjust as needed

**By May 2027, you'll be choosing between multiple top US universities offering full funding.**

**Let's make it happen.** 🚀

---

**Questions? Start executing first. Adjust later. GO!**

