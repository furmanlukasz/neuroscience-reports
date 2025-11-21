# Neuroscience Reports - Site Maintenance Guide

This guide explains how to maintain and add content to your neuroscience reports website.

## Overview

The site uses a simple build system that generates the main index page from a configuration file (`posts.yaml`). This allows you to:

- **Easily add new reports or blog posts** by editing a single YAML file
- **Tag-based filtering** so visitors can filter by topic
- **3D brain visualization** as an interactive background
- **GitHub Pages compatible** - no backend required

## Tags System

The following tags are available:

| Tag | Description |
|-----|-------------|
| **RQA** | Recurrence Quantitative Analysis |
| **TPM** | Transition Probability Matrix |
| **Markov Chains** | Markov chain analysis |
| **System Dynamics** | System dynamics studies |
| **EEG Analysis** | EEG signal analysis |
| **Machine Learning** | Machine learning methods |
| **Classification** | Classification tasks |
| **MCI** | Mild Cognitive Impairment |
| **Alzheimer's** | Alzheimer's Disease research |
| **Schizophrenia** | Schizophrenia studies |
| **Autoencoders** | Autoencoder methods |
| **Deep Learning** | Deep learning approaches |
| **Microstates** | EEG microstate analysis |
| **Network Analysis** | Brain network analysis |
| **Source Localization** | Source localization methods |
| **EMD** | Empirical Mode Decomposition |
| **Cognitive Models** | Cognitive modeling |
| **PAC** | Phase-Amplitude Coupling |
| **Preprocessing** | Data preprocessing |
| **Signal Processing** | Signal processing methods |
| **Spectral Analysis** | Spectral analysis |
| **UMAP** | UMAP dimensionality reduction |
| **Clustering** | Clustering methods |

## Adding a New Report or Blog Post

### Step 1: Create Your HTML Report

Create your report as an HTML file (e.g., `web-myreport.html`) or markdown file. Place it in the root directory.

### Step 2: Add Metadata to posts.yaml

Edit `posts.yaml` and add a new entry:

```yaml
  - slug: web-myreport  # Filename without .html
    title: "Your Report Title"
    description: "A brief description of your report"
    date: 2024-11-21  # YYYY-MM-DD format
    image: "images/myreport/main.png"  # Path to preview image
    type: report  # or 'blog' for blog posts
    tags:
      - EEG Analysis
      - Machine Learning
      - MCI
```

### Step 3: Rebuild the Site

Run the build script:

```bash
python3 build.py
```

This will regenerate `index.html` with your new post included and all tags updated.

### Step 4: Commit and Push

```bash
git add .
git commit -m "Add new report: Your Report Title"
git push origin main
```

Your site will automatically update on GitHub Pages!

## Directory Structure

```
neuroscience-reports/
├── build.py              # Build script
├── posts.yaml            # Post metadata configuration
├── index.html            # Generated main page
├── assets/
│   └── css/
│       ├── main.css      # Main stylesheet
│       └── tags.css      # Tag system styles
├── images/               # Images for reports
└── web-*.html            # Individual report pages
```

## Content Types

### Research Reports (`type: report`)

Technical neuroscience research reports with:
- Scientific methodology
- Data analysis
- Results and conclusions
- Technical figures and visualizations

### Blog Posts (`type: blog`)

Shorter, more accessible posts including:
- Thoughts on neuroscience topics
- Cognitive models
- Movie/media analysis connecting to neuroscience
- Personal insights and reflections

## Customization

### Adding New Tags

Edit `build.py` and add to the `TAGS` dictionary:

```python
TAGS = {
    "Your Tag": {"name": "Your Tag Full Name", "color": "#HEX COLOR"},
    # ... existing tags
}
```

Then run `python3 build.py` to rebuild.

### Adjusting 3D Visualization

Edit `assets/css/tags.css` to adjust:

```css
#renderMain {
    opacity: 0.4;  /* Adjust visibility (0.0 - 1.0) */
}
```

### Changing Color Scheme

Edit the color values in:
- `assets/css/tags.css` for tag colors
- `assets/css/main.css` for overall theme

## Tips

1. **Image Optimization**: Keep images under 500KB for fast loading
2. **Consistent Naming**: Use `web-` prefix for report HTML files
3. **Date Format**: Always use YYYY-MM-DD format
4. **Tag Selection**: Choose 3-7 relevant tags per post
5. **Preview Images**: Use images that represent the key findings

## Workflow Example

```bash
# 1. Create new analysis and export as HTML
# (Use your Jupyter notebook, R Markdown, etc.)

# 2. Save as web-my-new-analysis.html

# 3. Edit posts.yaml
nano posts.yaml

# 4. Add entry for new report

# 5. Rebuild site
python3 build.py

# 6. Preview locally (optional)
# Open index.html in browser

# 7. Commit changes
git add .
git commit -m "Add analysis of X"
git push

# Done! Site updates automatically
```

## Troubleshooting

**Tags not showing?**
- Make sure tags in `posts.yaml` match exactly with `TAGS` in `build.py`
- Run `python3 build.py` to rebuild

**3D visualization not appearing?**
- Check browser console for JavaScript errors
- Ensure all required scripts are loaded

**Images not loading?**
- Verify image path is correct in `posts.yaml`
- Check that image exists in `images/` directory

**Build script fails?**
- Install dependencies: `pip3 install pyyaml markdown`
- Check YAML syntax in `posts.yaml`

## Advanced: Markdown to HTML

For markdown-based reports, you can:

1. Create a `.md` file with YAML front matter:

```markdown
---
title: "My Report"
date: 2024-11-21
tags:
  - EEG Analysis
  - MCI
type: report
---

# Your Report Content Here
```

2. The build script can convert this to HTML automatically

3. Or use tools like Pandoc:

```bash
pandoc input.md -o web-output.html --standalone --mathjax
```

## Questions?

For issues or questions:
- Check this guide
- Review existing reports in `posts.yaml`
- Check `build.py` for configuration details

---

**Last updated:** November 2024
