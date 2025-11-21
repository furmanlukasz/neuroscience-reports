# Neuroscience Reports Site - Project Handoff Document

## Project Overview

This is a personal research portfolio website for showcasing neuroscience reports and analysis. The site displays technical research reports on topics including EEG analysis, mild cognitive impairment (MCI), schizophrenia, machine learning applications, and various signal processing techniques.

**Current Site**: https://furmanlukasz.github.io/neuroscience-reports/
**Repository**: https://github.com/furmanlukasz/neuroscience-reports

## Current State

### What Exists
- **14 research reports** in HTML format (converted from Jupyter notebooks, R Markdown, etc.)
- **3D brain visualization** using Three.js (brain model with nodes and connections)
- **Daily quotes** from `proverbs.json` file
- **Images and figures** for each report in `/images/` directory
- **Static HTML site** using HTML5 UP template
- Basic navigation and responsive layout

### Content Files
- `web-*.html` - Individual research reports (e.g., `web-EEGAutoencoder-01.html`)
- `classification.html`, `transition-probability-matrix.html`, `correlation-matrices.html`, etc.
- `images/` - All report figures and visualizations
- `proverbs.json` - Collection of daily quotes/proverbs
- `about.html` - About page
- `brain_lh_low.obj` - 3D brain model file
- `rois4.obj` - Regions of interest for brain visualization
- `con_epochs_matrix.csv` - Connection matrix data for brain viz

## Vision & Goals

### What I Want

A modern, visually impressive research portfolio that:

1. **Showcases interdisciplinary thinking** - The site should visually represent how different research topics connect (RQA → MCI, Microstates → Schizophrenia, etc.)

2. **Easy to maintain** - I want to drop markdown files or add entries to a simple config file and have the site update automatically

3. **Tag-based discovery** - Visitors should be able to filter and explore research by topics/methods

4. **Beautiful, modern design** - Think Anthropic's website aesthetic (earthy, warm tones, not harsh dark/light theme), elegant typography, smooth interactions

5. **Interactive 3D brain** - Keep the brain visualization but make it responsive (currently breaks on window resize) and possibly use it as a separate interactive page

6. **GitHub Pages compatible** - Must deploy as static site, no backend required

### Design Preferences

**Visual Style**:
- Earthy, warm color palette (inspired by Anthropic/Claude website)
- Not purely dark or light - somewhere in between with earthy tones
- Clean, modern typography
- Generous whitespace
- Subtle but expressive - not overpowering

**Layout**:
- Clean, uncluttered homepage
- Easy navigation
- Reports displayed as cards/grid
- Tag filtering that feels natural
- Quotes displayed elegantly (currently from `proverbs.json`)

**Interactions**:
- Smooth animations
- Responsive on all devices
- Fast loading
- Accessible

## Research Topics & Tags

The reports cover these main areas (potential tags):

**Methods/Techniques**:
- Recurrence Quantitative Analysis (RQA)
- Transition Probability Matrix (TPM)
- Markov Chains
- System Dynamics
- Machine Learning
- Classification
- Autoencoders
- Deep Learning
- Microstates
- Network Analysis
- Source Localization
- Empirical Mode Decomposition (EMD)
- Phase-Amplitude Coupling (PAC)
- Preprocessing
- Signal Processing
- Spectral Analysis
- UMAP
- Clustering

**Clinical Applications**:
- Mild Cognitive Impairment (MCI)
- Alzheimer's Disease
- Schizophrenia
- EEG Analysis

**Content Types**:
- Research Reports (technical, detailed)
- Blog Posts / Thoughts (shorter reflections, cognitive models, connecting neuroscience to everyday observations)

## Existing Reports (Examples)

1. **"Highlighting Temporal Patterns in Resting-State EEG"** (Sept 2024)
   - Topics: Autoencoders, Deep Learning, RQA, EEG Analysis, MCI
   - File: `web-EEGAutoencoder-01.html`
   - Image: `images/eeg-autoencoder/model.png`

2. **"Recurrence Quantitative Analysis of EEG Data in MCI"** (June 2024)
   - Topics: RQA, EEG Analysis, MCI, Network Analysis, EMD
   - File: `web-RQA-STC-HC_vs_MCI.html`
   - Image: `images/rqa_stc_hht/Pipeline.png`

3. **"Transition Probability Matrix in Schizophrenia"** (Dec 2023)
   - Topics: TPM, Schizophrenia, Markov Chains, System Dynamics
   - File: `transition-probability-matrix.html`
   - Image: `images/transition/transition_probabilities_no_self.png`

*(Full list of 14 reports exists in repository)*

## Technical Requirements

### Must Have
- ✅ **Static site generation** - Works on GitHub Pages
- ✅ **Markdown support** - Should be able to add new reports as `.md` files with YAML front matter
- ✅ **Tag filtering** - Filter reports by research topics/methods
- ✅ **Responsive design** - Mobile, tablet, desktop
- ✅ **3D visualization** - Responsive Three.js brain (currently exists but needs resize fix)
- ✅ **Content from config** - Use YAML or JSON to manage report metadata

### Nice to Have
- 🎯 Interactive knowledge graph showing research topic connections
- 🎯 Timeline view of research
- 🎯 Search functionality
- 🎯 Related reports suggestions
- 🎯 Separate blog/thoughts section
- 🎯 Dark/light mode toggle

### Constraints
- No backend/server
- Must deploy on GitHub Pages
- Should reuse existing HTML reports and images
- Keep current 3D brain model and data files

## Content Structure

### Proposed Metadata Format

Each report should have metadata (YAML front matter or JSON):

```yaml
title: "Report Title"
date: 2024-09-23
description: "Brief description of the report"
image: "images/folder/preview.png"
type: "report" # or "blog"
tags:
  - EEG Analysis
  - Machine Learning
  - MCI
file: "web-report-name.html" # or .md
```

### File Organization

```
neuroscience-reports/
├── reports/               # All research reports
│   ├── *.html            # Existing HTML reports
│   ├── *.md              # Future markdown reports
├── images/               # All images organized by report
├── data/
│   ├── posts.yaml        # Metadata for all reports
│   ├── proverbs.json     # Daily quotes
│   ├── brain_lh_low.obj  # 3D brain model
│   └── con_epochs_matrix.csv
├── about.html            # About page
└── index.html            # Main page (to be generated)
```

## User Workflows

### Adding a New Report

1. Create report as `.html` or `.md` file
2. Add images to `/images/report-name/`
3. Add metadata entry to `posts.yaml` (or similar config)
4. Build/deploy (should be automatic via GitHub Actions or simple command)

### For Visitors

1. Land on homepage → see latest reports and/or knowledge graph
2. Browse by tags → filter to specific topics
3. Click report → read full analysis
4. Discover related research
5. Optionally explore 3D brain visualization

## Assets Provided

- ✅ 14 existing HTML reports with all content
- ✅ All images and figures in `/images/`
- ✅ 3D brain model files (`.obj`)
- ✅ Connection data (`.csv`)
- ✅ Quotes collection (`proverbs.json`)
- ✅ Current site template (HTML5 UP)

## Design Inspiration

**Visual References** (for style, not to copy):
- Anthropic website (claude.ai) - Earthy tones, warm aesthetic
- Observable (observablehq.com) - Interactive notebooks
- Distill.pub - Research presentation
- Brain-map.org - 3D brain visualizations

**Key Design Principles**:
- Restraint over flashiness
- Warmth through color and spacing
- Typography-driven hierarchy
- Purposeful, meaningful animations
- Academic credibility with modern polish

## Success Criteria

The site is successful if:
1. ✅ Visually impressive - showcases the interdisciplinary work beautifully
2. ✅ Easy to maintain - I can add reports with minimal effort
3. ✅ Fast and responsive - loads quickly, works on all devices
4. ✅ Discoverable - tags/filters help visitors explore the research
5. ✅ Professional - reflects the quality of the technical work
6. ✅ Functional - 3D brain works properly (no resize bugs)

## What I Don't Want

❌ Overly corporate/business-like design
❌ Pure black/white harsh contrast
❌ Flashy animations that distract from content
❌ Complex CMS or backend requirements
❌ Heavy frameworks that slow down the site
❌ Loss of existing reports/content

## Notes

- I took a gap in creating reports but I'm returning to it
- Reports are publication-format (exploratory) rather than formal papers
- Some reports are very technical, others are more reflective/cognitive models
- The site should reflect how I think - connecting different methodologies and domains
- I value both scientific rigor and accessible communication

## Repository Access

**GitHub**: https://github.com/furmanlukasz/neuroscience-reports
**Current Live Site**: https://furmanlukasz.github.io/neuroscience-reports/

All existing content, images, and 3D models are in the repository.

---

**Contact**: If you need clarification on research topics, existing reports, or design direction, please ask. I'm happy to provide more context about the neuroscience work or design preferences.
