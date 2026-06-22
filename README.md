# The Erosion of Truth: A Human-AI Collaborative Analysis

An empirical and narrative synthesis tracing the structural, psychological, and existential cascade triggered by the rapid, forced integration of generative AI into institutional and personal workflows.

---

## 📊 Narrative Cascade (The 5 Dominoes)

The project explores how corporate technological mandates trigger a chain reaction that compromises human agency and reality:

```
[1. Boardroom Hype] -> [2. Coping Shortcuts] -> [3. Crisis of Agency] -> [4. Existential Escapism] -> [5. Collapse of Truth]
```

1.  **The Performative Boardroom (Hype):** Organizations adopt "AI-First" branding to satisfy external stakeholder expectations of innovation, creating a "Narrative-Practice Gap."
2.  **The Silent Compromise (Shortcut):** Employees/students bridge the performance gap by utilizing shortcuts ("AI-giarism") along a moral intensity spectrum.
3.  **The Author Identity Crisis (Crisis):** Offloading cognitive labor interrupts the feedback loop of self-efficacy, reducing psychological ownership and inducing Academic Impostor Syndrome (AIS) via the "Sleeper Effect."
4.  **The Digital Necropolis (Escape):** Retreating from workplace alienation, individuals accept digital reanimation of the deceased ("AI Resurrection"), governed by strict posthumous consent boundary conditions.
5.  **The Glass Shatters (Collapse):** Absolute trust in models leads to cognitive collapse when the AI lies, resulting in a trust rating crash from 3.9 stars to 1.8 stars and a plummet in user sentiment to a VADER score of -0.65.

---

## 📂 Project Directory Map

### 🗺️ Roadmaps & Blueprints
*   [presentation_roadmap.md](https://github.com/RootedOne/TEOT/blob/main/roadmaps/presentation_roadmap.md): The structural roadmap, slide visual specs, and speaker scripts for the presentation.
*   [article_roadmap.md](https://github.com/RootedOne/TEOT/blob/main/roadmaps/article_roadmap.md): The master index mapping the scientific synthesis sections to raw data sources, sample sizes, and methods.

### 📝 Written Deliverables
*   [the_erosion_of_truth_article.md](https://github.com/RootedOne/TEOT/blob/main/the_erosion_of_truth_article.md): The comprehensive, 0-100 scientific synthesis essay compiling all five research studies.

### 🖥️ Presentation Slides
*   [part_1_slide.md](https://github.com/RootedOne/TEOT/blob/main/slides/part_1_slide.md): Slide 1 - Boardroom Hype / Performative Rationality script and specs.
*   [part_2_slide.md](https://github.com/RootedOne/TEOT/blob/main/slides/part_2_slide.md): Slide 2 - AI-Giarism spectrum script and specs.
*   [part_3_slide.md](https://github.com/RootedOne/TEOT/blob/main/slides/part_3_slide.md): Slide 3 - Imposter feelings & task design script and specs.
*   [part_4_slide.md](https://github.com/RootedOne/TEOT/blob/main/slides/part_4_slide.md): Slide 4 - AI Resurrection and consent script and specs.
*   [part_5_slide.md](https://github.com/RootedOne/TEOT/blob/main/slides/part_5_slide.md): Slide 5 - Hallucination user-derived taxonomy, VADER stats, and Co-Pilot resolution.

### 📓 Research & Systematic Notes
*   [The_Illusion_of_AI-First_notes.txt](https://github.com/RootedOne/TEOT/blob/main/research/notes/The_Illusion_of_AI-First_notes.txt): Analysis of Branda (2026).
*   [Chatbot_or_cheatbot_notes.txt](https://github.com/RootedOne/TEOT/blob/main/research/notes/Chatbot_or_cheatbot_notes.txt): Analysis of Xu et al. (2026).
*   [Does_AI_Foster_imposter_feelings_notes.txt](https://github.com/RootedOne/TEOT/blob/main/research/notes/Does_AI_Foster_imposter_feelings_notes.txt): Analysis of Batista-Toledo & Gavilan (2026).
*   [s40359-026-04496-4_resurrection_notes.txt](https://github.com/RootedOne/TEOT/blob/main/research/notes/s40359-026-04496-4_resurrection_notes.txt): Analysis of Cheng et al. (2026).
*   [s41598-025-15416-8_lying_ai_notes.txt](https://github.com/RootedOne/TEOT/blob/main/research/notes/s41598-025-15416-8_lying_ai_notes.txt): Analysis of Massenon et al. (2025).

### 🛠️ Python Extraction Utility
*   [extract.py](https://github.com/RootedOne/TEOT/blob/main/extract.py): Python extraction script written to bypass Springer/Nature layout blockers and cleanly extract raw academic texts using `pypdf`.
*   [memories.txt](https://github.com/RootedOne/TEOT/blob/main/memories.txt): Shared collaboration progress journal.

---

## 🛠️ Setup & Usage

### Text Extraction Utility
To extract text from new reference PDFs downloaded into the project directory:

1.  Ensure Python 3 is installed.
2.  Install dependencies:
    ```bash
    pip install pypdf --user
    ```
3.  Run the extractor:
    ```bash
    python3 extract.py
    ```

---

## 📚 Academic References
*   **Hype:** Branda, F. (2026). The Illusion of “AI-First”: Organizational Rationality and the Performative Translation of AI Hype. *Philosophy & Technology*, 39, 66.
*   **Shortcut:** Xu, Y., Guo, J., Zhou, D., & Li, M. (2026). Chatbot or cheatbot? Moral judgments of AI usage in academic writing. *Education and Information Technologies*.
*   **Crisis:** Batista-Toledo, S., & Gavilan, D. (2026). Does AI Foster imposter feelings? The impact of task design on students’ use of AI. *Education and Information Technologies*, 31(8), 2123–2143.
*   **Escape:** Cheng, N., Huang, W., & Sun, M. (2026). Explore factors affecting students’ acceptance of AI resurrection and ethical dilemmas in AI resurrection technology among Chinese college students: a cross-sectional study. *BMC Psychology*, 14:794.
*   **Collapse:** Massenon, R., Gambo, I., Khan, J. A., Agbonkhese, C., & Alwadain, A. (2025). “My AI is Lying to Me”: User-reported LLM hallucinations in AI mobile apps reviews. *Scientific Reports*, 15:30397.
