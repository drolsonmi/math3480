<head>
<script>
MathJax = {
  tex: {
    inlineMath: [['$', '$'], ['\\(', '\\)']],
    displayMath: [['$$', '$$'], ['\\[', '\\]']]
  }
};
</script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>

# Entropy
Reading
* Geron, Chapter 6

__Additional Resources__
* [YouTube: Shannon Entropy and Information Gain](https://www.youtube.com/watch?v=9r7FIXEAGvs) by Serrano Academy
* [YouTube: Entropy (for data science) Clearly Explained!!!](https://www.youtube.com/watch?v=7VeUPuFGJHk&t=143s) by StatQuest

## Recall
Expected value:

$$E[x] = \sum x\cdot P(x)$$

## Introduction Scenario
* Choose 4 balls out of a bucket of red balls
  * How surprised are you if you get RRRR? Not
* Choose 4 balls out of a bucket of 75% red 25% blue balls
  * How surprised are you if you get RRRR? Moderately
* Choose 4 balls out of a bucket of 50% red 50% blue balls
  * How surprised are you if you get RRRR? High

## Surprise
Surprise and likelihood (probability) are inversely proportional. So, it's tempting to say, $Surprise = \frac{1}{P(x)}$. But it's deceptive, because following this, $P(x)=1$ happens when you have the most surprise.

Try a logarithm. Then $P(x)=0$ will give the most surprise. (Show this on Desmos)

$$\log_2\left(\frac{1}{P(x)}\right) = -\log_2P(x)$$

* Why $\log_2$? When we have 2 possibile outcomes, we have a binary situation
* The number of possible outcomes for drawing 4 balls is $2*2*2*2=2^4$
* The number of possible outcomes for drawing $k$ balls is $2*2*2*2=2^k$

Because of this, we are going to use $\log_2$. The base may change if there are a different number of outcomes, but in a decision tree, we only have two outcomes.

__What is the surprise when drawing 2 red and 2 blue balls when the bin is 75% red and 25% blue?__ The probability of this happening is,

$$P(x) = 0.75*0.75*0.25*0.25 = 0.0351$$

Fairly low probability. The surprise is then,

$$Surprise = -\log_2 (0.75*0.75*0.25*0.25) = -\log_2 0.75 + -\log_2 0.75 + -\log_2 0.25 + -\log_2 0.25 = 4.8301$$

This is just the sum of the surprise of each event!

## Entropy
__Entropy__ is a measure of disorder or uncertainty and the goal of machine learning models and Data Scientists in general is to reduce uncertainty
* Entropy is the Expected Value of the Surprise

To find the entropy, compare surprise to probability
* Find the product for each outcome
$$-P(x)\log_2 P(x)$$
* Add them together, and we get entropy!
$$E(surprise) = Entropy = \sum -(\log_2 P(x))P(x)$$

Note that this is just the equation for the expected value: $E(x)=\sum x\cdot P(x)$.

### Another example
Now, 8 letters, A-D. Find the entropy of each:
1. AAAAAAAA

    $$Entropy = -\left[\log_2\left(\frac{8}{8}\right)\frac{8}{8}\right] = -(0)(1) = 0$$

2. AABBCCDD

    $$Entropy = -\left[\log_2\left(\frac{2}{8}\right)\frac{2}{8} + \log_2\left(\frac{2}{8}\right)\frac{2}{8} + \log_2\left(\frac{2}{8}\right)\frac{2}{8} + \log_2\left(\frac{2}{8}\right)\frac{2}{8}\right]$$
    $$ = -\left[(-2)\frac{1}{4} + (-2)\frac{1}{4} + (-2)\frac{1}{4} + (-2)\frac{1}{4}\right] = 2$$

3. AAAABBCD

    $$Entropy = -\left[\log_2\left(\frac{4}{8}\right)\frac{4}{8} + \log_2\left(\frac{2}{8}\right)\frac{2}{8} + \log_2\left(\frac{1}{8}\right)\frac{1}{8} + \log_2\left(\frac{1}{8}\right)\frac{1}{8}\right]$$
    $$-\left[(-1)\frac{1}{2} + (-2)\frac{1}{4} + (-3)\frac{1}{8} + (-3)\frac{1}{8}\right] = 1.75$$

## Another look at Entropy
Another way to define Entropy:
* Entropy is the average number of questions we need to ask to get a certain result

### First example: $AAAAAAAA$
* How many questions do you need to ask to know which letter you drew?
* Since $P(A) = 1$, we don't have to ask any
  * Questions asked = 0 = Entropy

### Take the second example: $AABBCCDD$
* How many questions do you need to ask to know which letter you drew?
  * We could ask 
    * Is it A?
    * Is it B?
    * Is it C?
    * At this point, we know it's not A, B, or C, so we don't have to ask D. So, we asked 3 questions.

[![](https://mermaid.ink/img/pako:eNpVkEsKgzAQQK8yzLpewEWLv5ZC6aJdlSSLYMYaMEZiXBT17o2goLMaHu_BMCOWVhHG-HWyq-Hx4i2EScZ7D9pDcplXAFF0hulD_QQpS8SBPu0E2VqkW5Htipyl4kCXoliLbCuKXXFlmTjQpbixXOAJDTkjtQpHj4vC0ddkiGMcVkWVHBrPkbdzUIdOSU-F0t46jCvZ9HRCOXj7_rUlxt4NtEm5luEHZrXmP2eBVRM)](https://mermaid-js.github.io/mermaid-live-editor/edit/#pako:eNpVkEsKgzAQQK8yzLpewEWLv5ZC6aJdlSSLYMYaMEZiXBT17o2goLMaHu_BMCOWVhHG-HWyq-Hx4i2EScZ7D9pDcplXAFF0hulD_QQpS8SBPu0E2VqkW5Htipyl4kCXoliLbCuKXXFlmTjQpbixXOAJDTkjtQpHj4vC0ddkiGMcVkWVHBrPkbdzUIdOSU-F0t46jCvZ9HRCOXj7_rUlxt4NtEm5luEHZrXmP2eBVRM)


* We can look at this a different way. Ask instead,
  * Is it A or B?
  * Consider the diagram:

[![](https://mermaid.ink/img/pako:eNpdkMEKgzAMhl8l5Kwv4GFDqxuDscN2GtZDsXEW1EptD0N991XmQJdT-L8vkGTEUkvCCF9G9DVc77wDX_F4GUBZIGVrMhCDNpAc5xVCGB5getIwQbKK8R-86QnYytiPJZvBLI8L2MXLSJonxTdkG_eUs326qOc8LTDAlkwrlPQXjIvC0S_cEsfIt5Iq4RrLkXezV10vhaVMKqsNRpVoBgpQOKsf767EyBpHPylVwj-kXa35AzbKWTA)](https://mermaid-js.github.io/mermaid-live-editor/edit/#pako:eNpdkMEKgzAMhl8l5Kwv4GFDqxuDscN2GtZDsXEW1EptD0N991XmQJdT-L8vkGTEUkvCCF9G9DVc77wDX_F4GUBZIGVrMhCDNpAc5xVCGB5getIwQbKK8R-86QnYytiPJZvBLI8L2MXLSJonxTdkG_eUs326qOc8LTDAlkwrlPQXjIvC0S_cEsfIt5Iq4RrLkXezV10vhaVMKqsNRpVoBgpQOKsf767EyBpHPylVwj-kXa35AzbKWTA)

In each case, it took 2 questions. Questions asked = $\sum n\cdot P(x) = n_AP(A) + n_BP(B) + n_CP(C) + n_DP(D) = 2*\frac{1}{4} + 2*\frac{1}{4} + 2*\frac{1}{4} + 2*\frac{1}{4} = 2 = Entropy$

So, a second approach to calculating Entropy is,

$$Entropy = E[# of questions] = \sum n\cdot P(n)$$

where $n$ is the number of question needed to reach a category and $P(n) = P(x)$ is the probability of needing to ask those questions (that is, the probability of being in that category).

#### How do we know the second diagram is better?
If we follow this method with the first tree diagram, we'll get an entropy of 2.25

$$Entropy = 1\cdot\frac{1}{4} + 2\cdot\frac{1}{4} + 3\cdot\frac{1}{4} + 3\cdot\frac{1}{4} = \frac{9}{4} = 2.25$$

So, the more efficient model is the one with less

### Take the third example: $AAAABBCD$
How many questions do you need to ask to know which letter you drew?

We could follow the same process, but we'd get the same result (2 questions)

$$Entropy = 2\cdot\frac{1}{2} + 2\cdot\frac{1}{4} + 2\cdot\frac{1}{8} + 2\cdot\frac{1}{8}$$

However, notice that half of them are an A. What if we cut to the chase and ask that right off the bat?
* Is it A?
* Is it B?
* Is it C?

[![](https://mermaid.ink/img/pako:eNpVkEsKgzAQQK8yzLpewEWLv5ZC6aJdlSSLYMYaMEZiXBT17o2goLMaHu_BMCOWVhHG-HWyq-Hx4i2EScZ7D9pDcplXAFF0hulD_QQpS8SBPu0E2VqkW5Htipyl4kCXoliLbCuKXXFlmTjQpbixXOAJDTkjtQpHj4vC0ddkiGMcVkWVHBrPkbdzUIdOSU-F0t46jCvZ9HRCOXj7_rUlxt4NtEm5luEHZrXmP2eBVRM)](https://mermaid-js.github.io/mermaid-live-editor/edit/#pako:eNpVkEsKgzAQQK8yzLpewEWLv5ZC6aJdlSSLYMYaMEZiXBT17o2goLMaHu_BMCOWVhHG-HWyq-Hx4i2EScZ7D9pDcplXAFF0hulD_QQpS8SBPu0E2VqkW5Htipyl4kCXoliLbCuKXXFlmTjQpbixXOAJDTkjtQpHj4vC0ddkiGMcVkWVHBrPkbdzUIdOSU-F0t46jCvZ9HRCOXj7_rUlxt4NtEm5luEHZrXmP2eBVRM)

$Entropy = \sum n\cdot P(x) = n_AP(A) + n_BP(B) + n_CP(C) + n_DP(D) = 1*\frac{1}{2} + 2*\frac{1}{4} + 3*\frac{1}{8} + 3*\frac{1}{8} = 1.75$

So, this model is the better model in this case.