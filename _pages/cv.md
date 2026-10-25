---
layout: single
title: "Resume"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
  - /resume/
---

[Download resume (PDF)]({{ '/files/Lakshman_Resume_2026.pdf' | relative_url }}){: .btn .btn--primary}

## Professional summary

AI/ML Engineer experienced in developing LLM-powered applications, agentic workflows, RAG systems, and machine learning solutions across cybersecurity, GRC, and healthcare. Proficient in Python, PyTorch, LangChain, LangGraph, NLP, and deep learning, with hands-on experience in API integration, intelligent automation, and AI application development.

## Technical skills

{% include resume/skills.md %}

## Experience

{% capture experience %}{% include resume/experience.md %}{% endcapture %}
{{ experience | replace: "## ", "### " }}

## Projects & Publications

{% for publication in site.publications reversed %}
### {{ publication.title }}

{{ publication.content }}
{% endfor %}

## Education

{% include resume/education.md %}

## Contact

[slakshman2004@gmail.com](mailto:slakshman2004@gmail.com) Â· [LinkedIn](https://www.linkedin.com/in/lakshman-shanmugam-00bb42267/) Â· [GitHub](https://github.com/LakshmanS27)
