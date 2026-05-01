<head>
<title>Ethics and Responsible AI</title>
<script>
MathJax = {
  tex: {
    inlineMath: [['\\(', '\\)']],
    displayMath: [['$$', '$$'], ['\\[', '\\]']]
  }
};
</script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>

# Ethics and Responsible AI
These notes are copied from the [MATH 3080 Ethics lecture notes](https://github.com/drolsonmi/math3080/Notes/20_Ethics.md).

## Review of Statstical Learning
- Reminder about Modeling 

$$y = f(x) + \epsilon \qquad\qquad \hat{y} = \hat{f}(x) \approx f(x)$$

- Reducible and Irreducible Error
- Amplification of Error

Because of errors in models, it is easy to incorrectly use and to misinterpret models.

-----

## Ethics
Earlier in the semester, we discussed some of the Ethics of Graphing. But we never really defined ethics. What exactly do we mean when we talk about ethics?

In general terms, __ethics__ is an ongoing process of articulating values, and in turn, questioning and justifying decisions based on those values, usually in terms of rights, obligations, benefits to society, or specific virtues.

An __ethical dilemma__ is a situation where a difficult choice has to be made between different courses of action, each of which entails transgressing a moral principle.

What are some common ethical concerns?
- Transparency / Lack of Understanding / Lack of autonomy to make informed choices
- Unfair bias
- Security
- Privacy
- AI pseudoscience
- Accountability to people
- AI-driven unemployment and deskilling

Ethical dilemmas happen frequently in Data Science. But living up to ethical standards has always shown to be a benefit to organizations and to society. When dealing with ethical dilemmas, it is important to remember:
- Ethics requires an element of ingenuity to solve new moral challenges
- Ethics requires humility and a willingness to confront difficult questions and even change opinions
- Ethics should not be viewed as law or policy
    - Ethics reflect values and expectations we have of one another - most of which have not been written down or enforced by a formal system

-----

## Responsible AI
A number of studies have shown that Software Engineers who use AI tools are more likely to write bad code, introducing bugs and vulnerability points. These could be major security risks for you and your company. Because of this, many companies have sought to establish a set of guidelines to make effective use of AI.

At the beginning of the semester, we learned about CRISP-DM, guidelines for effective model development in Data Mining.
- Remember, this is not a requirement, but a commonly accepted standard we use for effective analysis and model development

But what are the standards for good AI development and usage? Is there something like CRISP-DM for AI on the whole?
- No universal standard, but standards are needed
- Companies generally create their own standards to describe good principles, practices, governance processes, and tools that match their organization's mission and goals

Since 2016, a number of guidelines and recommendations have been passed around the world. The European Union passed the [EU Artificial Intelligence Act](https://artificialintelligenceact.eu/) in 2024, the first official framework for AI development and usage was passed. Individual states have attempted to pass similar frameworks, but there is no comprehensive framework in the United States yet.

No company has the perfect set of standards. Nonetheless, it is important to have a *defined* and *repeatable* process for using AI responsibly.

Because there is potential to impact many areas of society, not to mention people's daily lives, it's important to develop AI technologies with __ethics__ in mind. 
- Every decision point requires *consideration* and *evaluation* to ensure that choices have been made *responsibly* from concept to deployment.

Since official frameworks haven't been passed yet, standards of __Responsible AI__ are not universal. However, as companies have developed their standards, there have been a set of common themes, principles, and ideas that keep appearing. These focus on,
1. Transparency
2. Fairness
3. Accountability
4. Privacy
5. Safety and Reliability (Robustness)
6. Social Benefit

(The first four are commonly addressed. It is also common to see 5 and 6, just not as commonly as 1-4.)

-----

## Benefits of Responsible AI
Responsible AI = Successful AI

List these 7 benefits. As a class, discuss what each might mean and how it can be a benefit to the organization. Subpoints are some major points that can be addressed.

1. Smart investment in product development
    - Not having clear AI standards puts the organization at risk for big challenges
        - Delaying product launches
        - Halting work
        - Pulling products off the market

2. Responsible AI trailblazers attract and retain top talent
    - Workers find more job satisfaction in organized and honest organizations
    - Workers have stronger loyalty to employers who tackle the issues that resonate with them, especially ethical issues

3. Safeguarding the promise of data
    - Cisco research reports that for every \\$1 invested in strengthening data privacy, \\(y = mx + b\\) the average company will see a return of \\$2.70

4. Preparing in advance of AI regulation
    - Organizations that already have policies in place will be able to easily adapt when official regulation is put in place
    - The challenge is to develop regulations in a way that is proportionately tailored to *mitigate risks* and promote *reliable* and *trustworty* AI applications while still *enabling innovation* and the promise of AI for *societal benefit*

5. Responsible AI can improve revenue growth
    - Evidence that 

6. Responsible AI is power up partnerships

7. Maintaining strong trust and branding

