---
title: Transformer架构详解
description: 深入理解自注意力机制、多头注意力、位置编码等核心组件
---

# Transformer架构详解

<span class="difficulty-advanced">进阶</span> <span style="color: #999; font-size: 13px;">📖 20分钟阅读</span>

## 革命性突破

Transformer是2017年Google提出的架构，论文《Attention Is All You Need》彻底改变了NLP领域。

## 核心组件

### 1. 自注意力机制

计算词与词之间的关联程度。

**公式：**
$$
\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
$$

### 2. 多头注意力

从多个角度理解信息。

### 3. 位置编码

保留序列的位置信息。

### 4. 前馈网络

非线性变换增强表达能力。

## 为什么强大

- 并行计算
- 长距离依赖
- 可扩展性

## 下一步学习

- [模型训练与微调](/advanced/llm/training-fine-tuning)

---

::: info 参考资料
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
:::
