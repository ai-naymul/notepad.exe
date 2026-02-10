---
title: "Research Paper Reading Roadmap - Path to Top Venues"
created: 2025-02-10
tags: [research, papers, roadmap, NLP, Bengali, transformers]
goal: "Publish at ACL/NAACL/NeurIPS 2025 + Transfer to Top US Unis Fall 2027"
papers_total: 78
papers_completed: 0
implementations_done: 0
research_ideas: 0
current_phase: "Phase 0 - Critical Foundations"
target_venues: [ACL, NAACL, EMNLP, NeurIPS, ICML, ICLR]
---

# 📚 Research Paper Reading Roadmap

**Student**: Andy | **Institution**: IIUC Bangladesh | **Year**: Starting Jan 2026  
**Primary Research Interest**: Bengali NLP, LLMs, Transformer Architectures  
**Competitive Advantage**: Native Bengali speaker + Technical expertise + Drishtikon platform

---

## 🎯 GOALS & TIMELINE

### Primary Goals
1. ✅ Publish 1-2 papers at top venues (ACL/NAACL/EMNLP) by Dec 2025
2. ✅ Build portfolio for US university transfer applications (Fall 2027)
3. ✅ Establish expertise in Bengali NLP (underexplored area = higher publication chance)
4. ✅ Master transformer architectures and modern LLMs

### Reading Schedule
- **Phase 0** (Weeks 1-4): Critical foundations - 10 papers
- **Phase 1** (Months 2-3): Deep learning basics - 15 papers
- **Phase 2** (Months 4-5): Advanced NLP - 15 papers
- **Phase 3** (Months 6-7): Modern LLMs - 12 papers
- **Phase 4** (Months 8-9): Specialization (Bengali NLP) - 10 papers
- **Phase 5** (Months 10-12): Cutting edge + Research - 16 papers

**Weekly Target**: 3-4 papers (adjust based on difficulty)

---

## 📊 PROGRESS TRACKER

```dataview
TABLE 
  status as "Status",
  priority as "Priority",
  implementations as "Impl Status"
FROM #paper
SORT priority DESC
```

**Current Stats**:
- Papers Read: `0/78`
- Implementations: `0/15`
- Notes Written: `0/78`
- Research Ideas: `0`
- Days Active: `0`

---

## 📖 READING METHODOLOGY

### Three-Pass Reading System
**Pass 1** (10 min): Title, abstract, intro, conclusion → Decision: continue?  
**Pass 2** (1 hour): Full read, skip proofs, note methodology  
**Pass 3** (4 hours): Deep dive, challenge assumptions, implementation plan

### Note Template Location
`[[Paper Note Template]]` - Use for every paper

### Implementation Rule
If paper is tagged `#implement`, MUST write code before marking complete

---

# PHASE 0: CRITICAL FOUNDATIONS 🔥
**Duration**: Weeks 1-4 | **Papers**: 10 | **Must Complete Before Moving On**

> These papers are NON-NEGOTIABLE. Every top NLP researcher knows these.

## Week 1: The Transformer (Most Important Week)

### P0.1 | Attention Is All You Need ⭐⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Vaswani, Shazeer, Parmar, Uszkoreit, Jones, Gomez, Kaiser, Polosukhin
- **Year**: 2017
- **Venue**: NeurIPS
- **Tags**: #paper #must-read #implement #transformer #foundation
- **Priority**: CRITICAL - READ THIS FIRST
- **PDF**: https://arxiv.org/abs/1706.03762
- **Code**: https://github.com/tensorflow/tensor2tensor
- **Annotated**: http://nlp.seas.harvard.edu/annotated-transformer/
- **Video**: https://www.youtube.com/watch?v=iDulhoQ2pro
- **Time Estimate**: 
  - Pass 1: 15 min
  - Pass 2: 2 hours
  - Pass 3: 6 hours
  - Implementation: 1 week
- **Why Critical**: 
  - Foundation of ALL modern NLP (BERT, GPT, T5, etc.)
  - Will be referenced in 90% of papers you read
  - Understanding this unlocks everything else
  - Your Bengali NLP research will build on this
- **Implementation Goal**: 
  - [ ] Build transformer from scratch in PyTorch (no libraries)
  - [ ] Train on small machine translation task
  - [ ] Visualize attention weights
- **Key Concepts to Master**:
  - [[Self-Attention Mechanism]]
  - [[Multi-Head Attention]]
  - [[Positional Encoding]]
  - [[Feed-Forward Networks]]
  - [[Layer Normalization]]
  - [[Residual Connections]]
- **For Your Research**:
  - Base architecture for BengaliGPT/BengaliBERT
  - Attention analysis for Bengali syntax
  - Cross-lingual transfer for Bengali
- **Notes**: [[Attention Is All You Need - Notes]]
- **Questions to Answer**:
  1. Why is attention better than RNNs?
  2. How does positional encoding work mathematically?
  3. Why multi-head instead of single attention?
  4. How to adapt for Bengali script?
- **Date Started**: 
- **Date Completed**: 
- **Implementation Status**: [ ]

---

## Week 2: Transfer Learning Revolution

### P0.2 | BERT - Bidirectional Transformers ⭐⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Devlin, Chang, Lee, Toutanova (Google AI)
- **Year**: 2019
- **Venue**: NAACL
- **Tags**: #paper #must-read #implement #bert #transfer-learning #bengali-nlp
- **Priority**: CRITICAL
- **PDF**: https://arxiv.org/abs/1810.04805
- **Code**: https://github.com/google-research/bert
- **HuggingFace**: https://huggingface.co/docs/transformers/model_doc/bert
- **Time Estimate**: 3-4 hours reading + 1 week implementation
- **Why Critical**:
  - Most influential NLP paper post-Transformer
  - Bidirectional pretraining changed everything
  - Direct foundation for BanglaBERT
  - Your research will likely fine-tune BERT
- **Implementation Goal**:
  - [ ] Fine-tune BERT on Bengali classification task
  - [ ] Implement masked language modeling
  - [ ] Compare to training from scratch
- **Research Angles for You**:
  - "BanglaBERT v2: Improved Pretraining for Bengali"
  - "Cross-lingual BERT for Bengali-English"
  - "BERT for Bengali news bias detection" (fits your Drishtikon!)
- **Key Concepts**:
  - [[Masked Language Modeling (MLM)]]
  - [[Next Sentence Prediction (NSP)]]
  - [[Transfer Learning in NLP]]
  - [[Fine-tuning Strategies]]
- **Bengali Application**:
  - Use for Drishtikon's bias detection
  - Train on Bengali Wikipedia + news corpus
  - Compare with mBERT and XLM-R
- **Notes**: [[BERT - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P0.3 | GPT-2 - Language Models as Multitask Learners ⭐⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Radford, Wu, Child, Luan, Amodei, Sutskever (OpenAI)
- **Year**: 2019
- **Venue**: OpenAI Technical Report
- **Tags**: #paper #must-read #gpt #generation #transfer-apps
- **Priority**: CRITICAL
- **PDF**: https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf
- **Code**: https://github.com/openai/gpt-2
- **Why Critical**:
  - Generative pretraining approach
  - Zero-shot task transfer
  - Scaling laws emergence
  - Foundation for GPT-3, ChatGPT
- **Research Angles**:
  - "GPT for Bengali text generation"
  - "Zero-shot Bengali summarization"
  - "Bengali news generation" (Drishtikon application!)
- **Key Concepts**:
  - [[Autoregressive Language Modeling]]
  - [[Zero-Shot Learning]]
  - [[Prompt Engineering]]
  - [[Scaling Laws]]
- **Implementation Goal**:
  - [ ] Train GPT-2 small on Bengali corpus
  - [ ] Generate Bengali news articles
  - [ ] Evaluate perplexity
- **Notes**: [[GPT-2 - Notes]]
- **Date Started**: 
- **Date Completed**: 

---

## Week 3: Word Embeddings & Sequence Models

### P0.4 | Word2Vec - Efficient Word Representations ⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Mikolov, Chen, Corrado, Dean (Google)
- **Year**: 2013
- **Venue**: ICLR
- **Tags**: #paper #must-read #implement #embeddings #foundation
- **Priority**: HIGH
- **PDF**: https://arxiv.org/abs/1301.3781
- **Time Estimate**: 2 hours reading + 2 days implementation
- **Why Critical**:
  - First breakthrough in word embeddings
  - Still used for analysis and baselines
  - Simple but powerful idea
- **Implementation Goal**:
  - [ ] Implement Skip-gram from scratch
  - [ ] Train on Bengali Wikipedia
  - [ ] Analyze Bengali word analogies
  - [ ] Compare CBOW vs Skip-gram
- **Bengali Research**:
  - Create Bengali word analogy dataset
  - Analyze Bengali morphology through embeddings
  - Compare with English embeddings
- **Key Concepts**:
  - [[Word Embeddings]]
  - [[Skip-gram Model]]
  - [[CBOW Model]]
  - [[Negative Sampling]]
- **Notes**: [[Word2Vec - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P0.5 | GloVe - Global Vectors for Word Representation ⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Pennington, Socher, Manning (Stanford)
- **Year**: 2014
- **Venue**: EMNLP
- **Tags**: #paper #embeddings
- **PDF**: https://nlp.stanford.edu/pubs/glove.pdf
- **Code**: https://github.com/stanfordnlp/GloVe
- **Why Read**: Alternative to Word2Vec, matrix factorization perspective
- **Notes**: [[GloVe - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P0.6 | LSTM - Long Short-Term Memory ⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Hochreiter, Schmidhuber
- **Year**: 1997
- **Venue**: Neural Computation
- **Tags**: #paper #must-read #implement #rnn #foundation
- **Priority**: HIGH
- **PDF**: https://www.bioinf.jku.at/publications/older/2604.pdf
- **Why Critical**:
  - Understand RNNs to appreciate Transformers
  - Still used in some sequence tasks
  - Gating mechanism concepts important
- **Implementation Goal**:
  - [ ] LSTM from scratch in NumPy
  - [ ] Train on Bengali text classification
  - [ ] Compare with Transformer
- **Key Concepts**:
  - [[Vanishing Gradients]]
  - [[Gating Mechanisms]]
  - [[Cell State]]
  - [[Forget Gate]]
- **Notes**: [[LSTM - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P0.7 | Seq2Seq Learning with Neural Networks ⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Sutskever, Vinyals, Le (Google)
- **Year**: 2014
- **Venue**: NeurIPS
- **Tags**: #paper #must-read #seq2seq #translation
- **PDF**: https://arxiv.org/abs/1409.3215
- **Why Critical**: Encoder-decoder architecture, precursor to Transformer
- **Bengali Application**: Bengali-English neural machine translation
- **Key Concepts**:
  - [[Encoder-Decoder Architecture]]
  - [[Sequence-to-Sequence Learning]]
- **Notes**: [[Seq2Seq - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P0.8 | Neural Machine Translation with Attention ⭐⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Bahdanau, Cho, Bengio
- **Year**: 2015
- **Venue**: ICLR
- **Tags**: #paper #must-read #attention #translation #foundation
- **Priority**: CRITICAL
- **PDF**: https://arxiv.org/abs/1409.0473
- **Why Critical**:
  - First attention mechanism in NLP
  - Direct precursor to Transformer attention
  - Solved long-sequence problem in NMT
- **Implementation Goal**:
  - [ ] Implement attention mechanism
  - [ ] Build English-Bengali NMT system
  - [ ] Visualize attention alignments
- **Bengali Research Angle**:
  - "Attention Analysis for Bengali Syntax"
  - "Low-Resource Bengali-English Translation"
- **Key Concepts**:
  - [[Attention Mechanism]]
  - [[Alignment Scores]]
  - [[Context Vector]]
- **Notes**: [[Bahdanau Attention - Notes]]
- **Date Started**: 
- **Date Completed**: 

---

## Week 4: Practical Wisdom & Modern LLMs

### P0.9 | A Few Useful Things to Know About ML ⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Pedro Domingos
- **Year**: 2012
- **Venue**: CACM
- **Tags**: #paper #must-read #practical #wisdom #quick-win
- **Priority**: HIGH
- **PDF**: https://homes.cs.washington.edu/~pedrod/papers/cacm12.pdf
- **Time Estimate**: 2-3 hours
- **Why Critical**:
  - Avoid common research pitfalls
  - Practical advice from experienced researcher
  - Will save you months of wasted effort
- **Key Takeaways to Note**:
  - It's generalization that counts
  - Data alone is not enough
  - Overfitting has many faces
  - Feature engineering is key
  - More data beats clever algorithms
- **Apply to Your Research**:
  - How to validate Bengali NLP models properly
  - Feature engineering for news bias detection
  - Handling limited Bengali training data
- **Notes**: [[Pedro Domingos ML Wisdom - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P0.10 | GPT-3 - Language Models are Few-Shot Learners ⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Brown et al. (OpenAI)
- **Year**: 2020
- **Venue**: NeurIPS
- **Tags**: #paper #must-read #gpt3 #scaling #transfer-apps
- **Priority**: HIGH
- **PDF**: https://arxiv.org/abs/2005.14165
- **Why Critical**:
  - Scaling laws demonstrated
  - In-context learning
  - Few-shot prompting
  - Foundation for modern LLM research
- **Research Angles**:
  - "Can small models achieve GPT-3 performance on Bengali?"
  - "Few-shot learning for Bengali tasks"
  - "Prompting strategies for Bengali"
- **Key Concepts**:
  - [[In-Context Learning]]
  - [[Few-Shot Learning]]
  - [[Prompt Engineering]]
  - [[Scaling Laws]]
  - [[Emergent Abilities]]
- **Notes**: [[GPT-3 - Notes]]
- **Date Started**: 
- **Date Completed**: 

---

# PHASE 1: DEEP LEARNING FOUNDATIONS 🧠
**Duration**: Months 2-3 | **Papers**: 15 | **Focus**: Neural Network Fundamentals

> Build solid understanding of how neural networks actually work

## Neural Network Basics

### P1.1 | Backpropagation - Learning Representations ⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Rumelhart, Hinton, Williams
- **Year**: 1986
- **Venue**: Nature
- **Tags**: #paper #must-read #implement #backprop #foundation
- **PDF**: https://www.nature.com/articles/323533a0
- **Implementation Goal**: 
  - [ ] Backprop from scratch in NumPy
  - [ ] Derive gradients manually
  - [ ] Train simple MLP
- **Why Critical**: Core learning algorithm, must understand deeply
- **Notes**: [[Backpropagation - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P1.2 | LeNet - Gradient-Based Learning for Document Recognition ⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: LeCun, Bottou, Bengio, Haffner
- **Year**: 1998
- **Venue**: Proceedings of IEEE
- **Tags**: #paper #must-read #cnn #foundation
- **PDF**: http://yann.lecun.com/exdb/publis/pdf/lecun-01a.pdf
- **Implementation Goal**:
  - [ ] Implement LeNet-5 from scratch
  - [ ] Train on MNIST
  - [ ] Understand convolution operation
- **Why Read**: First successful CNN, convolution concepts
- **Notes**: [[LeNet - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P1.3 | AlexNet - ImageNet Classification with Deep CNNs ⭐⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Krizhevsky, Sutskever, Hinton
- **Year**: 2012
- **Venue**: NeurIPS
- **Tags**: #paper #must-read #implement #alexnet #breakthrough #transfer-apps
- **Priority**: HIGH
- **PDF**: https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf
- **Why Critical**:
  - Proved deep learning works at scale
  - Started modern deep learning era
  - ReLU, dropout, data augmentation
- **Implementation Goal**:
  - [ ] Build AlexNet in PyTorch
  - [ ] Understand ReLU activation
  - [ ] Implement dropout
- **Key Concepts**:
  - [[ReLU Activation]]
  - [[Dropout]]
  - [[Data Augmentation]]
  - [[GPU Training]]
- **Notes**: [[AlexNet - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P1.4 | Dropout - Preventing Overfitting ⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Srivastava, Hinton, Krizhevsky, Sutskever, Salakhutdinov
- **Year**: 2014
- **Venue**: JMLR
- **Tags**: #paper #regularization
- **PDF**: http://jmlr.org/papers/v15/srivastava14a.html
- **Why Read**: Essential regularization technique
- **Apply to Bengali NLP**: Prevent overfitting on small Bengali datasets
- **Key Concepts**: [[Dropout]], [[Ensemble Learning]], [[Regularization]]
- **Notes**: [[Dropout - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P1.5 | Batch Normalization ⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Ioffe, Szegedy (Google)
- **Year**: 2015
- **Venue**: ICML
- **Tags**: #paper #normalization #training
- **PDF**: https://arxiv.org/abs/1502.03167
- **Why Read**: Accelerates training, used in most models
- **Key Concepts**: [[Batch Normalization]], [[Internal Covariate Shift]]
- **Notes**: [[Batch Normalization - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P1.6 | ResNet - Deep Residual Learning ⭐⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: He, Zhang, Ren, Sun (Microsoft)
- **Year**: 2016
- **Venue**: CVPR
- **Tags**: #paper #must-read #implement #resnet #architecture
- **Priority**: HIGH
- **PDF**: https://arxiv.org/abs/1512.03385
- **Why Critical**:
  - Skip connections enable very deep networks
  - Used in modern architectures
  - Solved degradation problem
- **Implementation Goal**:
  - [ ] Build ResNet blocks
  - [ ] Understand skip connections
  - [ ] Train ResNet-18
- **Key Concepts**: [[Residual Connections]], [[Skip Connections]], [[Deep Networks]]
- **Notes**: [[ResNet - Notes]]
- **Date Started**: 
- **Date Completed**: 

## Optimization & Training

### P1.7 | Adam Optimizer ⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Kingma, Ba
- **Year**: 2015
- **Venue**: ICLR
- **Tags**: #paper #optimization #must-read
- **PDF**: https://arxiv.org/abs/1412.6980
- **Why Critical**: Most popular optimizer in deep learning
- **Implementation Goal**: Implement Adam from scratch
- **Key Concepts**: [[Adam Optimizer]], [[Adaptive Learning Rates]], [[Momentum]]
- **Notes**: [[Adam - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P1.8 | Xavier Initialization ⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Glorot, Bengio
- **Year**: 2010
- **Venue**: AISTATS
- **Tags**: #paper #initialization
- **PDF**: http://proceedings.mlr.press/v9/glorot10a.html
- **Why Read**: Proper initialization is critical for training
- **Notes**: [[Xavier Initialization - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P1.9 | Layer Normalization ⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Ba, Kiros, Hinton
- **Year**: 2016
- **Tags**: #paper #normalization
- **PDF**: https://arxiv.org/abs/1607.06450
- **Why Read**: Used in Transformers instead of batch norm
- **Key Concepts**: [[Layer Normalization]]
- **Notes**: [[Layer Normalization - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P1.10 | Understanding LSTM Networks (Blog) ⭐⭐⭐
- **Status**: [ ] Not Started
- **Author**: Christopher Olah
- **Year**: 2015
- **Tags**: #blog #lstm #visual
- **Link**: https://colah.github.io/posts/2015-08-Understanding-LSTMs/
- **Why Read**: Best visual explanation of LSTMs
- **Notes**: [[Understanding LSTMs - Notes]]
- **Date Started**: 
- **Date Completed**: 

## Regularization & Generalization

### P1.11 | On the difficulty of training RNNs ⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Pascanu, Mikolov, Bengio
- **Year**: 2013
- **Venue**: ICML
- **Tags**: #paper #rnn #training
- **PDF**: https://arxiv.org/abs/1211.5063
- **Why Read**: Understand gradient problems in sequences
- **Key Concepts**: [[Vanishing Gradients]], [[Exploding Gradients]], [[Gradient Clipping]]
- **Notes**: [[Training RNNs - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P1.12 | Visualizing and Understanding CNNs ⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Zeiler, Fergus
- **Year**: 2014
- **Venue**: ECCV
- **Tags**: #paper #interpretability #visualization
- **PDF**: https://arxiv.org/abs/1311.2901
- **Why Read**: Understanding what networks learn
- **Notes**: [[Visualizing CNNs - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P1.13 | Deep Learning (Goodfellow Book - Chapter 6-8) ⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Goodfellow, Bengio, Courville
- **Year**: 2016
- **Tags**: #book #foundation #must-read
- **Link**: https://www.deeplearningbook.org/
- **Chapters to Read**:
  - Chapter 6: Deep Feedforward Networks
  - Chapter 7: Regularization
  - Chapter 8: Optimization
- **Notes**: [[Deep Learning Book - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P1.14 | How transferable are features in DNNs? ⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Yosinski, Clune, Bengio, Lipson
- **Year**: 2014
- **Venue**: NeurIPS
- **Tags**: #paper #transfer-learning
- **PDF**: https://arxiv.org/abs/1411.1792
- **Why Read**: Understanding transfer learning deeply
- **Bengali Application**: Transfer from English to Bengali
- **Notes**: [[Transfer Learning Features - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P1.15 | Rethinking the Inception Architecture ⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Szegedy et al. (Google)
- **Year**: 2016
- **Venue**: CVPR
- **Tags**: #paper #architecture
- **PDF**: https://arxiv.org/abs/1512.00567
- **Why Read**: Efficient architecture design principles
- **Notes**: [[Inception v3 - Notes]]
- **Date Started**: 
- **Date Completed**: 

---

# PHASE 2: ADVANCED NLP 📝
**Duration**: Months 4-5 | **Papers**: 15 | **Focus**: Modern NLP Techniques

> Deep dive into NLP-specific architectures and techniques

## Pre-training & Transfer Learning

### P2.1 | ELMo - Deep Contextualized Word Representations ⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Peters, Neumann, Iyyer, Gardner, Clark, Lee, Zettlemoyer
- **Year**: 2018
- **Venue**: NAACL
- **Tags**: #paper #elmo #contextual-embeddings #transfer-learning
- **PDF**: https://arxiv.org/abs/1802.05365
- **Why Critical**:
  - First successful contextual embeddings
  - Precursor to BERT
  - Showed power of pretraining
- **Key Concepts**: [[Contextual Embeddings]], [[BiLSTM]], [[Language Model Pretraining]]
- **Notes**: [[ELMo - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P2.2 | ULMFiT - Universal Language Model Fine-tuning ⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Howard, Ruder
- **Year**: 2018
- **Venue**: ACL
- **Tags**: #paper #transfer-learning #fine-tuning
- **PDF**: https://arxiv.org/abs/1801.06146
- **Why Read**: Systematic approach to transfer learning in NLP
- **Bengali Application**: Transfer learning for Bengali classification
- **Key Concepts**: [[Discriminative Fine-tuning]], [[Slanted Triangular Learning Rates]]
- **Notes**: [[ULMFiT - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P2.3 | RoBERTa - Robustly Optimized BERT Pretraining ⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Liu et al. (Facebook AI)
- **Year**: 2019
- **Venue**: arXiv
- **Tags**: #paper #bert #pretraining #quick-win
- **Priority**: HIGH
- **PDF**: https://arxiv.org/abs/1907.11692
- **Why Critical**:
  - Shows BERT wasn't fully optimized
  - Better pretraining = better results
  - Lessons for Bengali BERT
- **Research Angle**: "Can we apply RoBERTa improvements to BanglaBERT?"
- **Key Improvements**:
  - Remove NSP task
  - Dynamic masking
  - Larger batches
  - More data
- **Notes**: [[RoBERTa - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P2.4 | ALBERT - A Lite BERT ⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Lan et al. (Google)
- **Year**: 2020
- **Venue**: ICLR
- **Tags**: #paper #bert #efficiency
- **PDF**: https://arxiv.org/abs/1909.11942
- **Why Read**: Parameter sharing, efficient BERT
- **Bengali Application**: Efficient Bengali models for deployment
- **Key Concepts**: [[Parameter Sharing]], [[Factorized Embeddings]]
- **Notes**: [[ALBERT - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P2.5 | XLNet - Generalized Autoregressive Pretraining ⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Yang et al. (Google/CMU)
- **Year**: 2019
- **Venue**: NeurIPS
- **Tags**: #paper #pretraining #permutation
- **PDF**: https://arxiv.org/abs/1906.08237
- **Why Read**: Alternative to masked LM, permutation language modeling
- **Key Concepts**: [[Permutation Language Modeling]], [[Two-Stream Attention]]
- **Notes**: [[XLNet - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P2.6 | T5 - Exploring Transfer Learning with Text-to-Text ⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Raffel et al. (Google)
- **Year**: 2020
- **Venue**: JMLR
- **Tags**: #paper #t5 #text-to-text #transfer-apps
- **Priority**: HIGH
- **PDF**: https://arxiv.org/abs/1910.10683
- **Why Critical**:
  - Unified text-to-text framework
  - Comprehensive study of transfer learning
  - Systematic comparison of techniques
- **Bengali Application**: Text-to-text for Bengali tasks
- **Key Concepts**: [[Text-to-Text Framework]], [[C4 Dataset]]
- **Notes**: [[T5 - Notes]]
- **Date Started**: 
- **Date Completed**: 

## Multilingual & Cross-lingual Models

### P2.7 | mBERT - Multilingual BERT ⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Devlin et al. (Google)
- **Year**: 2019
- **Venue**: NAACL
- **Tags**: #paper #multilingual #bert #bengali-nlp
- **Priority**: HIGH for Bengali Research
- **PDF**: https://arxiv.org/abs/1810.04805 (same as BERT)
- **Why Critical for You**:
  - Trained on 104 languages including Bengali
  - Baseline for Bengali tasks
  - Understanding cross-lingual transfer
- **Research Angle**: "Can we beat mBERT on Bengali-specific tasks?"
- **Experiments to Run**:
  - [ ] Evaluate mBERT on Bengali classification
  - [ ] Compare with BanglaBERT
  - [ ] Test zero-shot transfer Bengali→English
- **Notes**: [[mBERT - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P2.8 | XLM-R - Cross-lingual Language Model ⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Conneau et al. (Facebook AI)
- **Year**: 2020
- **Venue**: ACL
- **Tags**: #paper #multilingual #xlm #bengali-nlp
- **Priority**: HIGH for Bengali Research
- **PDF**: https://arxiv.org/abs/1911.02116
- **Why Critical**:
  - Better than mBERT on low-resource languages
  - Trained on 100 languages including Bengali
  - Current SOTA for many Bengali tasks
- **Research Angle**: 
  - "Bengali-specific fine-tuning of XLM-R"
  - "XLM-R for Bengali news classification" (Drishtikon!)
- **Experiments**:
  - [ ] Compare XLM-R vs mBERT on Bengali
  - [ ] Fine-tune for bias detection
- **Notes**: [[XLM-R - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P2.9 | MASS - Masked Sequence to Sequence Pretraining ⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Song et al. (Microsoft)
- **Year**: 2019
- **Venue**: ICML
- **Tags**: #paper #seq2seq #pretraining
- **PDF**: https://arxiv.org/abs/1905.02450
- **Why Read**: Pretraining for generation tasks
- **Bengali Application**: Bengali text generation, summarization
- **Notes**: [[MASS - Notes]]
- **Date Started**: 
- **Date Completed**: 

## Efficient Transformers

### P2.10 | Longformer - Long Document Transformers ⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Beltagy, Peters, Cohan (Allen AI)
- **Year**: 2020
- **Venue**: arXiv
- **Tags**: #paper #efficient #long-context
- **PDF**: https://arxiv.org/abs/2004.05150
- **Why Read**: Handling long documents efficiently
- **Bengali Application**: Long Bengali news articles
- **Key Concepts**: [[Sparse Attention]], [[Sliding Window Attention]]
- **Notes**: [[Longformer - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P2.11 | Reformer - Efficient Transformer ⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Kitaev, Kaiser, Levskaya (Google)
- **Year**: 2020
- **Venue**: ICLR
- **Tags**: #paper #efficient #memory
- **PDF**: https://arxiv.org/abs/2001.04451
- **Why Read**: Memory-efficient transformers
- **Key Concepts**: [[LSH Attention]], [[Reversible Layers]]
- **Notes**: [[Reformer - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P2.12 | Linformer - Linear Complexity Transformer ⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Wang et al. (Facebook AI)
- **Year**: 2020
- **Venue**: arXiv
- **Tags**: #paper #efficient #linear
- **PDF**: https://arxiv.org/abs/2006.04768
- **Why Read**: O(n) complexity instead of O(n²)
- **Notes**: [[Linformer - Notes]]
- **Date Started**: 
- **Date Completed**: 

## Domain Adaptation & Few-Shot Learning

### P2.13 | MAML - Model-Agnostic Meta-Learning ⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Finn, Abbeel, Levine (Berkeley)
- **Year**: 2017
- **Venue**: ICML
- **Tags**: #paper #meta-learning #few-shot
- **PDF**: https://arxiv.org/abs/1703.03400
- **Why Read**: Few-shot learning approach
- **Bengali Application**: Few-shot Bengali classification
- **Notes**: [[MAML - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P2.14 | Matching Networks for One-Shot Learning ⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Vinyals et al. (DeepMind)
- **Year**: 2016
- **Venue**: NeurIPS
- **Tags**: #paper #one-shot #meta-learning
- **PDF**: https://arxiv.org/abs/1606.04080
- **Why Read**: One-shot learning in NLP
- **Notes**: [[Matching Networks - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P2.15 | Don't Stop Pretraining - Domain Adaptation ⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Gururangan et al. (Allen AI)
- **Year**: 2020
- **Venue**: ACL
- **Tags**: #paper #domain-adaptation #pretraining #quick-win
- **PDF**: https://arxiv.org/abs/2004.10964
- **Why Critical for Your Research**:
  - Shows continued pretraining helps
  - Domain-specific vs task-specific adaptation
  - Directly applicable to Bengali news domain
- **Research Angle**: 
  - "Domain-adapted BERT for Bengali news"
  - "Pretraining on Drishtikon's news corpus"
- **Experiments**:
  - [ ] Continue pretraining mBERT on Bengali news
  - [ ] Compare domain-adapted vs general model
- **Notes**: [[Domain Pretraining - Notes]]
- **Date Started**: 
- **Date Completed**: 

---

# PHASE 3: MODERN LLMs & GENERATION 🤖
**Duration**: Months 6-7 | **Papers**: 12 | **Focus**: Latest LLM Developments

> Understanding state-of-the-art language models

## Scaling & Training Large Models

### P3.1 | Scaling Laws for Neural Language Models ⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Kaplan et al. (OpenAI)
- **Year**: 2020
- **Venue**: arXiv
- **Tags**: #paper #scaling-laws #training #transfer-apps
- **Priority**: HIGH
- **PDF**: https://arxiv.org/abs/2001.08361
- **Why Critical**:
  - Predictable relationship between scale and performance
  - Informs model design decisions
  - Understanding compute-optimal training
- **Key Insights**:
  - Performance scales as power law with compute, data, params
  - How to allocate resources optimally
- **Bengali Application**: "What scale needed for good Bengali LM?"
- **Notes**: [[Scaling Laws - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P3.2 | Chinchilla - Training Compute-Optimal LLMs ⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Hoffmann et al. (DeepMind)
- **Year**: 2022
- **Venue**: arXiv
- **Tags**: #paper #scaling-laws #efficient-training #quick-win
- **Priority**: HIGH
- **PDF**: https://arxiv.org/abs/2203.15556
- **Why Critical**:
  - Challenges GPT-3 scaling assumptions
  - Smaller model + more data = better than bigger model
  - Critical for resource-constrained research (like yours!)
- **Key Finding**: Models have been undertrained, not underparameterized
- **Bengali Research**: "Can we train smaller but better Bengali models?"
- **Notes**: [[Chinchilla - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P3.3 | PaLM - Scaling Language Modeling with Pathways ⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Chowdhery et al. (Google)
- **Year**: 2022
- **Venue**: arXiv
- **Tags**: #paper #palm #scaling #transfer-apps
- **PDF**: https://arxiv.org/abs/2204.02311
- **Why Read**: 540B parameter model, impressive capabilities
- **Key Concepts**: [[Pathways]], [[Sparse Activation]], [[Chain-of-Thought]]
- **Notes**: [[PaLM - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P3.4 | LLaMA - Open Foundation Models ⭐⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Touvron et al. (Meta)
- **Year**: 2023
- **Venue**: arXiv
- **Tags**: #paper #llama #open-source #must-read #transfer-apps
- **Priority**: CRITICAL
- **PDF**: https://arxiv.org/abs/2302.13971
- **Why Critical**:
  - Open-source competitive LLM
  - Efficient training recipe
  - Base for many research projects
  - You can actually use this!
- **Research Angle**:
  - Fine-tune LLaMA on Bengali
  - Evaluate on Bengali benchmarks
  - Compare with GPT-3.5
- **Experiments**:
  - [ ] Fine-tune LLaMA-7B on Bengali
  - [ ] Evaluate on Bengali generation tasks
  - [ ] Compare with multilingual models
- **Notes**: [[LLaMA - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P3.5 | LLaMA 2 - Open Foundation and Fine-Tuned Models ⭐⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Touvron et al. (Meta)
- **Year**: 2023
- **Venue**: arXiv
- **Tags**: #paper #llama2 #open-source #rlhf #must-read
- **Priority**: CRITICAL
- **PDF**: https://arxiv.org/abs/2307.09288
- **Why Critical**:
  - Improved LLaMA with RLHF
  - Commercially usable
  - Detailed training methodology
- **Research Use**: Base model for Bengali experiments
- **Notes**: [[LLaMA 2 - Notes]]
- **Date Started**: 
- **Date Completed**: 

## Instruction Following & Alignment

### P3.6 | InstructGPT - Training LMs to Follow Instructions with RLHF ⭐⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Ouyang et al. (OpenAI)
- **Year**: 2022
- **Venue**: arXiv
- **Tags**: #paper #instructgpt #rlhf #alignment #must-read #transfer-apps
- **Priority**: CRITICAL
- **PDF**: https://arxiv.org/abs/2203.02155
- **Why Critical**:
  - Foundation of ChatGPT
  - RLHF methodology
  - Alignment techniques
- **Research Angle**:
  - "RLHF for Bengali instruction following"
  - "Bengali instruction dataset creation"
- **Key Concepts**:
  - [[RLHF]]
  - [[Reward Modeling]]
  - [[PPO Fine-tuning]]
- **Notes**: [[InstructGPT - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P3.7 | Constitutional AI - Harmlessness from AI Feedback ⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Bai et al. (Anthropic)
- **Year**: 2022
- **Venue**: arXiv
- **Tags**: #paper #constitutional-ai #alignment #rlaif
- **PDF**: https://arxiv.org/abs/2212.08073
- **Why Read**: AI feedback instead of human feedback
- **Research Angle**: "Bengali safety with limited human feedback"
- **Key Concepts**: [[RLAIF]], [[Constitutional AI]]
- **Notes**: [[Constitutional AI - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P3.8 | Self-Instruct - Aligning LMs with Self-Generated Instructions ⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Wang et al. (UW/Allen AI)
- **Year**: 2023
- **Venue**: ACL
- **Tags**: #paper #instruction-tuning #self-instruct #quick-win
- **Priority**: HIGH
- **PDF**: https://arxiv.org/abs/2212.10560
- **Why Critical for You**:
  - Generate instruction data automatically
  - No need for expensive human annotation
  - Perfect for low-resource Bengali!
- **Research Angle**: "Self-Instruct for Bengali"
- **Experiments**:
  - [ ] Generate Bengali instruction dataset
  - [ ] Fine-tune LLaMA with self-instruct
- **Notes**: [[Self-Instruct - Notes]]
- **Date Started**: 
- **Date Completed**: 

## Prompting & In-Context Learning

### P3.9 | Chain-of-Thought Prompting ⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Wei et al. (Google)
- **Year**: 2022
- **Venue**: NeurIPS
- **Tags**: #paper #cot #prompting #reasoning
- **PDF**: https://arxiv.org/abs/2201.11903
- **Why Read**: Improve reasoning through intermediate steps
- **Bengali Application**: Bengali math word problems, reasoning tasks
- **Key Concepts**: [[Chain-of-Thought]], [[Reasoning]], [[Prompting]]
- **Notes**: [[Chain-of-Thought - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P3.10 | ReAct - Reasoning and Acting with LLMs ⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Yao et al. (Princeton/Google)
- **Year**: 2023
- **Venue**: ICLR
- **Tags**: #paper #react #reasoning #agents
- **PDF**: https://arxiv.org/abs/2210.03629
- **Why Read**: Combining reasoning with action
- **Research Angle**: "Bengali question answering with ReAct"
- **Notes**: [[ReAct - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P3.11 | The Flan Collection - Instruction Tuning ⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Longpre et al. (Google)
- **Year**: 2023
- **Venue**: arXiv
- **Tags**: #paper #instruction-tuning #flan
- **PDF**: https://arxiv.org/abs/2301.13688
- **Why Read**: Large-scale instruction tuning study
- **Notes**: [[Flan Collection - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P3.12 | Large Language Models are Zero-Shot Reasoners ⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Kojima et al. (University of Tokyo/Google)
- **Year**: 2022
- **Venue**: NeurIPS
- **Tags**: #paper #zero-shot #reasoning
- **PDF**: https://arxiv.org/abs/2205.11916
- **Why Read**: "Let's think step by step" prompting
- **Notes**: [[Zero-Shot Reasoning - Notes]]
- **Date Started**: 
- **Date Completed**: 

---

# PHASE 4: BENGALI NLP SPECIALIZATION 🇧🇩
**Duration**: Months 8-9 | **Papers**: 10 | **Focus**: Your Competitive Advantage

> Deep dive into low-resource, multilingual, and Bengali-specific NLP

## Bengali Language Models

### P4.1 | BanglaBERT Papers - Search Latest ⭐⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Tags**: #paper #bengali-nlp #must-read #foundation
- **Priority**: CRITICAL - Your research builds on this
- **Action**: 
  - [ ] Search "BanglaBERT" on Google Scholar
  - [ ] Search "Bangla BERT" on ACL Anthology
  - [ ] Find latest Bengali pretrained models
- **Papers to Find**:
  - Original BanglaBERT paper
  - BanglaBERT-Base and Large
  - IndicBERT (includes Bengali)
  - Any domain-specific Bengali BERT
- **Experiments to Run**:
  - [ ] Download and evaluate BanglaBERT
  - [ ] Compare with mBERT and XLM-R on Bengali tasks
  - [ ] Fine-tune for news classification
  - [ ] Test on Drishtikon's bias detection
- **Research Angles**:
  - "BanglaBERT v2: Improved pretraining"
  - "Domain-adapted BanglaBERT for news"
  - "BanglaBERT for bias detection"
- **Notes**: [[BanglaBERT - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P4.2 | IndicNLP - Resources and Benchmarks ⭐⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Tags**: #paper #indic #bengali-nlp #resources #must-read
- **Priority**: CRITICAL
- **Search**: "IndicNLP" on arXiv, AI4Bharat website
- **Why Critical**:
  - Largest Indic NLP resource
  - Bengali datasets and models
  - Benchmarks for comparison
- **Action Items**:
  - [ ] Download IndicNLP datasets
  - [ ] Evaluate IndicBERT on Bengali
  - [ ] Compare with your results
- **Research Use**: Baseline and datasets for Bengali experiments
- **Notes**: [[IndicNLP - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P4.3 | Bengali Language Models Survey ⭐⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Tags**: #survey #bengali-nlp #must-read
- **Priority**: CRITICAL
- **Action**: Search latest Bengali NLP surveys
- **Keywords**: "Bengali language models", "Bangla NLP survey", "low-resource Bengali"
- **Goal**: 
  - Understand current state of Bengali NLP
  - Identify research gaps
  - Find datasets and benchmarks
- **Notes**: [[Bengali NLP Survey - Notes]]
- **Date Started**: 
- **Date Completed**: 

## Low-Resource & Multilingual NLP

### P4.4 | XTREME - Multilingual Benchmark ⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Hu et al. (Google/CMU)
- **Year**: 2020
- **Venue**: arXiv
- **Tags**: #paper #benchmark #multilingual
- **PDF**: https://arxiv.org/abs/2003.11080
- **Why Read**: Benchmark for cross-lingual understanding
- **Bengali Application**: Evaluate models on Bengali XTREME tasks
- **Notes**: [[XTREME - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P4.5 | Unsupervised Cross-lingual Representation Learning ⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Lample, Conneau (Facebook AI)
- **Year**: 2019
- **Venue**: ACL
- **Tags**: #paper #cross-lingual #bengali-nlp
- **PDF**: https://arxiv.org/abs/1911.02116
- **Why Read**: Transfer from high to low-resource languages
- **Research Angle**: "English→Bengali transfer learning"
- **Notes**: [[Cross-lingual Transfer - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P4.6 | MAD-X - Adapter-Based Cross-lingual Transfer ⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Pfeiffer et al.
- **Year**: 2020
- **Venue**: EMNLP
- **Tags**: #paper #adapters #cross-lingual #quick-win
- **PDF**: https://arxiv.org/abs/2005.00052
- **Why Critical for You**:
  - Efficient cross-lingual transfer
  - Language adapters + task adapters
  - Works well for low-resource languages
- **Research Angle**: "Bengali language adapters"
- **Experiments**:
  - [ ] Train Bengali language adapter
  - [ ] Test on Bengali classification
- **Notes**: [[MAD-X - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P4.7 | Data Augmentation for Low-Resource NLP ⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Various - search latest
- **Tags**: #paper #data-augmentation #low-resource #bengali-nlp
- **Action**: Find 2-3 recent data augmentation papers
- **Keywords**: "data augmentation low-resource", "back-translation", "text augmentation Bengali"
- **Why Critical**: Bengali has limited training data
- **Research Angle**: "Data augmentation for Bengali classification"
- **Techniques to Explore**:
  - Back-translation
  - Paraphrasing
  - Adversarial examples
  - Mixup for text
- **Notes**: [[Data Augmentation - Notes]]
- **Date Started**: 
- **Date Completed**: 

## Named Entity Recognition & Information Extraction

### P4.8 | Bengali NER Papers ⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Tags**: #paper #ner #bengali-nlp #quick-win
- **Action**: Search "Bengali Named Entity Recognition"
- **Why Relevant**: NER for Bengali news (Drishtikon use case!)
- **Research Angle**: "NER for Bengali news entities"
- **Experiments**:
  - [ ] Evaluate existing Bengali NER models
  - [ ] Fine-tune BERT for Bengali NER
  - [ ] Create news-specific entity types
- **Application**: Extract entities from Drishtikon's news articles
- **Notes**: [[Bengali NER - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P4.9 | Sentiment Analysis for Bengali ⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Tags**: #paper #sentiment #bengali-nlp #quick-win
- **Action**: Search "Bengali sentiment analysis"
- **Why Relevant**: News bias detection (Drishtikon!)
- **Research Angle**: 
  - "Sentiment analysis for Bengali news"
  - "Multi-perspective sentiment in Bengali journalism"
- **Datasets to Find**:
  - Bengali sentiment datasets
  - News sentiment annotations
- **Experiments**:
  - [ ] Benchmark sentiment models on Bengali news
  - [ ] Fine-tune for bias detection
- **Notes**: [[Bengali Sentiment - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P4.10 | Bangla Text Classification Papers ⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Tags**: #paper #classification #bengali-nlp
- **Action**: Search "Bangla text classification", "Bengali document classification"
- **Why Relevant**: Core task for news categorization
- **Research Angle**: "News category classification for Bengali"
- **Application**: Automatic categorization in Drishtikon
- **Notes**: [[Bengali Classification - Notes]]
- **Date Started**: 
- **Date Completed**: 

---

# PHASE 5: CUTTING EDGE & RESEARCH 🚀
**Duration**: Months 10-12 | **Papers**: 16 | **Focus**: Latest Research + Your Publications

> Latest developments + identifying research gaps for your papers

## Efficient Fine-tuning & Adaptation

### P5.1 | LoRA - Low-Rank Adaptation ⭐⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Hu et al. (Microsoft)
- **Year**: 2022
- **Venue**: ICLR
- **Tags**: #paper #lora #efficient #must-read #quick-win
- **Priority**: CRITICAL - Will use in your research
- **PDF**: https://arxiv.org/abs/2106.09685
- **Why Critical**:
  - Fine-tune large models with few parameters
  - Perfect for resource-constrained research
  - SOTA for Bengali fine-tuning
- **Implementation Goal**:
  - [ ] Fine-tune LLaMA with LoRA for Bengali
  - [ ] Compare with full fine-tuning
  - [ ] Measure efficiency gains
- **Research Angle**: "LoRA for Bengali LLM adaptation"
- **Key Concepts**: [[Low-Rank Adaptation]], [[Parameter-Efficient Fine-tuning]]
- **Notes**: [[LoRA - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P5.2 | QLoRA - Quantized LoRA ⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Dettmers et al.
- **Year**: 2023
- **Venue**: arXiv
- **Tags**: #paper #qlora #efficient #quantization
- **PDF**: https://arxiv.org/abs/2305.14314
- **Why Read**: Fine-tune 65B models on single GPU
- **Research Use**: Train large Bengali models on limited hardware
- **Notes**: [[QLoRA - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P5.3 | Prefix Tuning ⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Li, Liang (Stanford)
- **Year**: 2021
- **Venue**: ACL
- **Tags**: #paper #prefix-tuning #efficient
- **PDF**: https://arxiv.org/abs/2101.00190
- **Why Read**: Alternative to full fine-tuning
- **Notes**: [[Prefix Tuning - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P5.4 | Adapters - Parameter-Efficient Transfer Learning ⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Houlsby et al. (Google)
- **Year**: 2019
- **Venue**: ICML
- **Tags**: #paper #adapters #efficient
- **PDF**: https://arxiv.org/abs/1902.00751
- **Why Read**: Add small trainable modules to frozen models
- **Bengali Application**: Bengali task adapters
- **Notes**: [[Adapters - Notes]]
- **Date Started**: 
- **Date Completed**: 

## Retrieval-Augmented Generation

### P5.5 | RAG - Retrieval-Augmented Generation ⭐⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Lewis et al. (Facebook AI)
- **Year**: 2020
- **Venue**: NeurIPS
- **Tags**: #paper #rag #retrieval #must-read #transfer-apps
- **Priority**: HIGH
- **PDF**: https://arxiv.org/abs/2005.11401
- **Why Critical**:
  - Combine retrieval with generation
  - Reduce hallucination
  - Update knowledge without retraining
- **Research Angle**: "RAG for Bengali question answering"
- **Drishtikon Application**: 
  - Retrieve relevant news articles
  - Generate multi-perspective summaries
- **Implementation Goal**:
  - [ ] Build Bengali RAG system
  - [ ] Use Drishtikon's 200+ source corpus
  - [ ] Evaluate on Bengali QA
- **Key Concepts**: [[RAG]], [[Dense Retrieval]], [[DPR]]
- **Notes**: [[RAG - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P5.6 | Dense Passage Retrieval (DPR) ⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Karpukhin et al. (Facebook AI)
- **Year**: 2020
- **Venue**: EMNLP
- **Tags**: #paper #retrieval #dpr
- **PDF**: https://arxiv.org/abs/2004.04906
- **Why Read**: Dense retrieval for RAG
- **Bengali Application**: Bengali document retrieval
- **Notes**: [[DPR - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P5.7 | REALM - Retrieval-Augmented Language Model Pretraining ⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Guu et al. (Google)
- **Year**: 2020
- **Venue**: ICML
- **Tags**: #paper #realm #retrieval
- **PDF**: https://arxiv.org/abs/2002.08909
- **Why Read**: Pretraining with retrieval
- **Notes**: [[REALM - Notes]]
- **Date Started**: 
- **Date Completed**: 

## Evaluation & Analysis

### P5.8 | Beyond Accuracy - Behavioral Testing ⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Ribeiro et al. (Microsoft)
- **Year**: 2020
- **Venue**: ACL
- **Tags**: #paper #evaluation #testing
- **PDF**: https://arxiv.org/abs/2005.04118
- **Why Read**: Proper model evaluation
- **Bengali Application**: Test Bengali model robustness
- **Notes**: [[Behavioral Testing - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P5.9 | BERTScore - Evaluating Text Generation ⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Zhang et al.
- **Year**: 2020
- **Venue**: ICLR
- **Tags**: #paper #evaluation #metrics
- **PDF**: https://arxiv.org/abs/1904.09675
- **Why Read**: Better than BLEU for generation
- **Bengali Use**: Evaluate Bengali text generation
- **Notes**: [[BERTScore - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P5.10 | A Primer in BERTology ⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Rogers et al.
- **Year**: 2020
- **Venue**: TACL
- **Tags**: #paper #analysis #bert #survey
- **PDF**: https://arxiv.org/abs/2002.12327
- **Why Read**: Survey of BERT analysis methods
- **Research Use**: Analyze BanglaBERT internals
- **Notes**: [[BERTology - Notes]]
- **Date Started**: 
- **Date Completed**: 

## Latest Developments (2023-2025)

### P5.11 | GPT-4 Technical Report ⭐⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: OpenAI
- **Year**: 2023
- **Venue**: arXiv
- **Tags**: #paper #gpt4 #multimodal #transfer-apps
- **Priority**: HIGH
- **PDF**: https://arxiv.org/abs/2303.08774
- **Why Read**: Current SOTA, multimodal capabilities
- **Notes**: [[GPT-4 - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P5.12 | Llama 3.1 Technical Report ⭐⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Meta
- **Year**: 2024
- **Tags**: #paper #llama3 #open-source #cutting-edge
- **Action**: Search for Llama 3 technical report
- **Why Critical**: Latest open-source SOTA
- **Research Use**: Base model for Bengali experiments
- **Notes**: [[Llama 3 - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P5.13 | Latest ACL/NAACL/EMNLP 2024-2025 Papers ⭐⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Tags**: #cutting-edge #conference #must-read
- **Priority**: CRITICAL - These are your competition
- **Action**: 
  - [ ] Browse ACL 2024 proceedings
  - [ ] Browse NAACL 2024 proceedings
  - [ ] Browse EMNLP 2024 proceedings
  - [ ] Filter by "low-resource", "multilingual", "Bengali"
- **Goal**: 
  - Understand current research trends
  - Identify gaps in Bengali NLP
  - Find potential collaborators
- **Papers to Focus**:
  - Low-resource NLP
  - Multilingual models
  - Any Bengali-related papers
  - Efficient training/inference
- **Notes**: [[Latest ACL Papers - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P5.14 | Mixture of Experts Papers ⭐⭐⭐
- **Status**: [ ] Not Started
- **Tags**: #moe #efficient #cutting-edge
- **Action**: Search "Mixture of Experts language models"
- **Why Read**: Efficient scaling technique
- **Papers to Find**:
  - Switch Transformers
  - GLaM
  - Latest MoE architectures
- **Notes**: [[MoE - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P5.15 | Direct Preference Optimization (DPO) ⭐⭐⭐⭐
- **Status**: [ ] Not Started
- **Authors**: Rafailov et al. (Stanford)
- **Year**: 2023
- **Venue**: arXiv
- **Tags**: #paper #dpo #alignment #cutting-edge
- **PDF**: https://arxiv.org/abs/2305.18290
- **Why Read**: Alternative to RLHF, simpler alignment
- **Research Angle**: "DPO for Bengali preference alignment"
- **Notes**: [[DPO - Notes]]
- **Date Started**: 
- **Date Completed**: 

### P5.16 | Latest arXiv - Weekly Monitoring ⭐⭐⭐⭐⭐
- **Status**: [ ] Ongoing
- **Tags**: #cutting-edge #arxiv #monitoring
- **Priority**: CRITICAL - Stay current
- **Action**: 
  - [ ] Subscribe to arXiv daily emails: cs.CL, cs.LG
  - [ ] Follow researchers on Twitter/X
  - [ ] Check Papers with Code weekly
  - [ ] Monitor ACL Anthology
- **Keywords to Track**:
  - "Bengali", "Bangla", "low-resource"
  - "multilingual", "cross-lingual"
  - "efficient training", "LoRA", "adapters"
  - "instruction tuning", "RLHF"
- **Goal**: Read 2-3 latest papers per week
- **Notes**: [[arXiv Monitoring - Notes]]

---

# BONUS: FOUNDATIONAL CS PAPERS 💻
**Optional but Recommended for Strong CS Background**

## Algorithms & Theory

### B1 | Turing's On Computable Numbers
- **Status**: [ ] Not Started
- **Year**: 1936
- **Tags**: #paper #theory #foundation #optional
- **Why Read**: Foundation of computer science
- **Notes**: [[Turing - Notes]]

### B2 | Shannon's Information Theory
- **Status**: [ ] Not Started
- **Year**: 1948
- **Tags**: #paper #information-theory #foundation
- **Why Read**: Entropy, compression, communication
- **Notes**: [[Shannon - Notes]]

### B3 | Quicksort Algorithm
- **Status**: [ ] Not Started
- **Author**: C.A.R. Hoare
- **Year**: 1962
- **Tags**: #paper #algorithms #sorting
- **Notes**: [[Quicksort - Notes]]

---

# RESEARCH IDEAS GENERATED 💡
**Track ideas from paper reading**

## Ideas from Phase 0
1. [ ] 

## Ideas from Phase 1
1. [ ] 

## Ideas from Bengali Papers
1. [ ] BanglaBERT v2 with improved pretraining
2. [ ] Domain-adapted BERT for Bengali news (Drishtikon use case)
3. [ ] Cross-lingual transfer English→Bengali for low-resource tasks
4. [ ] Self-Instruct for Bengali instruction dataset creation
5. [ ] RAG system for multi-perspective Bengali news analysis
6. [ ] LoRA-based Bengali LLM fine-tuning
7. [ ] Bengali bias detection using attention analysis
8. [ ] 

---

# IMPLEMENTATION PROJECTS 🔨
**Code implementations required**

## Must Implement (Core Skills)
- [ ] Transformer from scratch (PyTorch) - [[Implementation - Transformer]]
- [ ] BERT fine-tuning on Bengali - [[Implementation - BERT Bengali]]
- [ ] Word2Vec on Bengali Wikipedia - [[Implementation - Word2Vec Bengali]]
- [ ] LSTM from scratch (NumPy) - [[Implementation - LSTM]]
- [ ] Attention mechanism visualization - [[Implementation - Attention Viz]]

## Advanced Implementations
- [ ] LoRA fine-tuning of LLaMA for Bengali - [[Implementation - LoRA Bengali]]
- [ ] RAG system with Bengali news corpus - [[Implementation - RAG Bengali]]
- [ ] Bengali NER with BERT - [[Implementation - NER]]
- [ ] Self-Instruct data generation for Bengali - [[Implementation - Self-Instruct]]
- [ ] Multi-perspective news analysis (Drishtikon integration) - [[Implementation - Drishtikon]]

---

# DATASETS TO COLLECT 📊
**Bengali NLP resources**

## Must Have
- [ ] Bengali Wikipedia dump
- [ ] Bengali news corpus (Drishtikon + others)
- [ ] Bengali sentiment dataset
- [ ] Bengali NER dataset
- [ ] Bengali question answering dataset

## To Create
- [ ] Bengali instruction dataset (via Self-Instruct)
- [ ] Bengali news bias annotations
- [ ] Bengali multi-perspective summaries
- [ ] Bengali word analogy dataset

---

# CONFERENCES & VENUES TO MONITOR 📅

## Primary Targets (Your Publication Goals)
- **ACL** (Association for Computational Linguistics) - July annually
- **NAACL** (North American ACL) - June annually  
- **EMNLP** (Empirical Methods in NLP) - December annually
- **EACL** (European ACL) - April/May

## ML Conferences (Secondary Targets)
- **NeurIPS** - December
- **ICML** - July
- **ICLR** - April/May

## Workshops (Quick Wins!)
- ACL/EMNLP workshops on low-resource NLP
- Workshops on multilingual NLP
- South Asian NLP workshop
- Student Research Workshop (SRW)

---

# WEEKLY REVIEW TEMPLATE 📝

## Week of: [Date]

### Papers Read This Week
1. 
2. 
3. 

### Key Insights
- 
- 

### Implementation Progress
- 

### Research Ideas Generated
- 

### Questions/Blockers
- 

### Next Week Goals
- 

---

# MONTHLY REVIEW TEMPLATE 📊

## Month: [Month Year]

### Papers Completed: X/Target
### Implementations Done: X/Target
### Research Ideas: X

### Major Achievements
- 

### Challenges Faced
- 

### Key Learnings
- 

### Next Month Focus
- 

### Research Progress
- Paper ideas:
- Experiments run:
- Results:

---

# PAPER WRITING TRACKER 📄

## Paper 1: [Title]
- **Status**: Planning / Writing / Submitted / Under Review / Accepted
- **Target Venue**: ACL 2025 / NAACL 2025 / etc.
- **Deadline**: 
- **Research Question**: 
- **Experiments**: 
- **Writing Progress**: 0%
- **Notes**: [[Paper 1 Notes]]

## Paper 2: [Title]
- **Status**: 
- **Target Venue**: 
- **Notes**: [[Paper 2 Notes]]

---

# COLLABORATION TRACKER 🤝

## Potential Collaborators
- [ ] Email Prof. X about Bengali NLP
- [ ] Reach out to BanglaBERT authors
- [ ] Join Bengali NLP community
- [ ] Connect with IndicNLP team

## Mentorship
- [ ] Find PhD mentor in NLP
- [ ] Connect with ACL reviewers
- [ ] Join research reading groups

---

# RESOURCES & LINKS 🔗

## Paper Search
- arXiv CS.CL: https://arxiv.org/list/cs.CL/recent
- ACL Anthology: https://aclanthology.org/
- Semantic Scholar: https://www.semanticscholar.org/
- Papers with Code: https://paperswithcode.com/

## Implementation Resources
- Annotated Transformer: http://nlp.seas.harvard.edu/annotated-transformer/
- HuggingFace Transformers: https://huggingface.co/docs/transformers/
- PyTorch Tutorials: https://pytorch.org/tutorials/

## Bengali NLP Resources
- AI4Bharat: https://ai4bharat.org/
- IndicNLP: https://github.com/AI4Bharat/indic-nlp-library
- Bengali Wikipedia: https://bn.wikipedia.org/

## Communities
- r/LanguageTechnology
- NLP Discord servers
- Bengali NLP researchers on Twitter/X

---

# NOTES
- Update this list weekly
- Mark papers complete only after full notes + implementation (if required)
- Generate research ideas continuously
- Focus on Bengali NLP for competitive advantage
- Quality > Quantity in reading

**Last Updated**: 2025-02-10
**Next Review**: Weekly every Sunday
