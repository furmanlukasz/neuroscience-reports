# Neuroscience Reports - Modernization Plan

## Vision

Transform the current static site into a modern, interactive neuroscience research portfolio that **visually represents interdisciplinary thinking** through connected knowledge graphs, interactive timelines, and responsive 3D visualizations.

## Core Design Philosophy

**"Neural Networks Meet Network Science"**

The site itself should mirror how you think - showing connections between:
- Research topics (RQA → Machine Learning → MCI)
- Methodologies (Signal Processing → Deep Learning)
- Clinical applications (Schizophrenia ← Microstates ← System Dynamics)
- Temporal evolution (how your research themes evolved)

## Key Problems to Solve

1. ✅ **Maintenance**: Keep YAML-based content management
2. 🔧 **3D Visualization**: Fix resizing, make it truly responsive
3. 🆕 **Visual Interdisciplinarity**: Show connections between research areas
4. 🆕 **Modern UX**: React-based, smooth animations, interactive
5. 🆕 **Discoverability**: Help visitors explore your work meaningfully

## Tech Stack

### Core
- **React 18** + **TypeScript** - Modern, type-safe UI
- **Vite** - Lightning-fast dev environment and build
- **Three.js / React Three Fiber** - 3D visualizations (responsive!)
- **Framer Motion** - Smooth animations
- **D3.js / Cytoscape.js** - Network graphs and data viz

### Styling
- **Tailwind CSS** - Utility-first, modern styling
- **Shadcn/ui** - Beautiful, accessible components
- Custom neural network-inspired design system

### Content
- **Gray-matter** - YAML front matter parsing
- **Marked** or **React-Markdown** - Markdown rendering
- **Prism.js** - Code highlighting

### Deployment
- **Vite Static Build** → GitHub Pages
- No SSR needed, fully static

## Site Architecture

```
neuroscience-reports/
├── src/
│   ├── components/
│   │   ├── Brain3D/              # Responsive 3D brain
│   │   ├── KnowledgeGraph/       # Interactive network of topics
│   │   ├── Timeline/             # Research timeline
│   │   ├── ReportCard/           # Beautiful report cards
│   │   ├── TagCloud/             # Interactive tag visualization
│   │   └── Navigation/           # Modern nav
│   ├── pages/
│   │   ├── Home.tsx              # Landing with knowledge graph
│   │   ├── Research.tsx          # All reports with filtering
│   │   ├── Timeline.tsx          # Temporal view
│   │   ├── About.tsx             # About you
│   │   └── Report.tsx            # Individual report viewer
│   ├── data/
│   │   ├── posts.yaml            # Same structure, reused!
│   │   └── connections.yaml      # Research topic connections
│   ├── utils/
│   │   ├── markdown.ts           # Markdown processing
│   │   └── graph.ts              # Graph algorithms
│   └── App.tsx
├── public/
│   ├── reports/                  # Your existing HTML/MD files
│   └── images/                   # Existing images
└── vite.config.ts
```

## Key Features

### 1. Interactive Knowledge Graph (Hero Section)

**Concept**: A 3D network graph where nodes are research topics, edges show connections

```
       [EEG Analysis]────────[Signal Processing]
            │                      │
            │                      │
       [Microstates]          [Spectral Analysis]
            │                      │
            └──────[Schizophrenia]─┘
                       │
                   [System Dynamics]
                       │
                   [Markov Chains]───[TPM]───[Classification]
```

**Interactions**:
- Hover node → Highlight connected research
- Click node → Filter reports by topic
- Rotate/zoom the graph
- Nodes size = number of reports
- Edge thickness = number of shared reports

**Tech**: React Three Fiber + Force-directed graph

### 2. Responsive 3D Brain Visualization

**Fix Current Issues**:
- Use `useEffect` with resize listener
- Responsive canvas sizing
- Position brain relative to viewport
- Smooth opacity transitions

**Enhancements**:
- Click brain regions → Show relevant reports
- Pulse animation on node activations
- Parallax effect on scroll
- Can be background OR feature

### 3. Research Timeline

**Horizontal scrolling timeline**:
```
2023 ────●────●────●───── 2024 ────●────●─────
         │    │    │            │    │
         │    │    │            │    └─ RQA + Autoencoders
         │    │    │            └────── PAC Analysis
         │    │    └─────────────────── State Distributions
         │    └──────────────────────── TPM Classification
         └───────────────────────────── Microstates Dynamics
```

**Features**:
- Group by year/topic
- Filter timeline by tags
- Click to expand report preview
- Smooth horizontal scroll
- Show research evolution

### 4. Modern Report Cards

**Grid layout** with beautiful cards:
- Hover: Lift + glow effect
- Preview image with gradient overlay
- Tags as colored pills (clickable)
- Read time estimate
- Related reports suggestions

### 5. Smart Tag System

**Network visualization of tags**:
- Tags as nodes, co-occurrence as edges
- Click tag → Highlights connected tags + filters reports
- Visual clustering of related topics
- "Explore related research" suggestions

### 6. Split View: Reports & Blog

**Two sections**:
- **Research Reports**: Technical, grid view
- **Thoughts & Models**: Blog-style, list view

Easy toggle between views.

## Design System

### Color Palette (Neural-Inspired)

```css
/* Primary: Brain-inspired pinks/purples */
--neural-pink: #E2B4BD
--neural-orange: #FFB869
--neural-gold: #F2B880
--neural-beige: #CBAC88

/* Dark mode (default) */
--bg-primary: #0a0a0f
--bg-secondary: #16161d
--bg-tertiary: #1f1f2e

/* Accent: Synaptic connections */
--accent-cyan: #00d4ff
--accent-purple: #b794f4
--accent-green: #48bb78

/* Text */
--text-primary: #f7fafc
--text-secondary: #cbd5e0
--text-muted: #718096
```

### Typography

- **Headings**: Inter or Space Grotesk (modern, geometric)
- **Body**: Inter or System UI
- **Code**: JetBrains Mono

### Visual Motifs

- **Neural connections** as decorative elements
- **Signal waves** as dividers
- **Network patterns** in backgrounds
- **Pulse animations** for active elements

## User Flows

### Discovery Flow
```
1. Land on homepage
   ↓
2. See knowledge graph + latest report
   ↓
3. Click interesting topic node
   ↓
4. View filtered reports
   ↓
5. Click report → Full view
   ↓
6. See "Related Research" suggestions
```

### Exploration Flow
```
1. Browse timeline
   ↓
2. Notice research evolution
   ↓
3. Click tag to see all related
   ↓
4. Discover connections between MCI → Alzheimer's → PAC
```

## Implementation Phases

### Phase 1: Foundation (Day 1)
- [x] Create design plan
- [ ] Set up Vite + React + TypeScript
- [ ] Port existing YAML data structure
- [ ] Basic routing and layout
- [ ] Dark theme implementation

### Phase 2: Core Features (Day 1-2)
- [ ] Markdown parser and report renderer
- [ ] Modern report cards with grid layout
- [ ] Tag filtering system
- [ ] Responsive navigation

### Phase 3: Visualizations (Day 2-3)
- [ ] Responsive 3D brain (fix resizing!)
- [ ] Knowledge graph visualization
- [ ] Timeline component
- [ ] Tag network visualization

### Phase 4: Interactions (Day 3)
- [ ] Smooth animations with Framer Motion
- [ ] Tag filtering with graph highlighting
- [ ] Report suggestions
- [ ] Search functionality

### Phase 5: Polish & Deploy (Day 3-4)
- [ ] Performance optimization
- [ ] Mobile responsiveness
- [ ] Build for GitHub Pages
- [ ] Testing and deployment

## Content Migration

**Keep**:
- ✅ `posts.yaml` structure
- ✅ Existing HTML/MD reports
- ✅ All images
- ✅ Tag system

**Add**:
- 🆕 `connections.yaml` - Define topic relationships
- 🆕 Report excerpts/previews
- 🆕 Related reports metadata

## Example: connections.yaml

```yaml
connections:
  - from: "RQA"
    to: "System Dynamics"
    strength: high

  - from: "Microstates"
    to: "Markov Chains"
    strength: high

  - from: "MCI"
    to: "Alzheimer's"
    strength: medium
    relation: "progression"

  - from: "Autoencoders"
    to: "Deep Learning"
    strength: high

  - from: "PAC"
    to: "Network Analysis"
    strength: medium

# This creates the knowledge graph edges
```

## Success Metrics

**Technical**:
- ⚡ Lighthouse score > 95
- 📱 Fully responsive (mobile-first)
- ♿ WCAG AA accessibility
- 🚀 Fast load time < 2s

**UX**:
- 🎯 Easy topic discovery
- 🔗 Clear research connections
- 📖 Readable reports
- 🎨 Visually impressive

**Maintenance**:
- ⏱️ Add new report in < 5 minutes
- 📝 YAML-based content
- 🔄 One-command rebuild
- 📦 GitHub Pages deployment

## Inspiration

**Sites to reference**:
- [brain-map.org](https://atlas.brain-map.org/) - 3D brain vis
- [Observable](https://observablehq.com/) - Interactive notebooks
- [Distill.pub](https://distill.pub/) - Research presentation
- [Kinopio](https://kinopio.club/) - Knowledge graphs
- [Linear](https://linear.app/) - Modern, smooth UI

## Next Steps

1. **Get approval** on this plan
2. **Set up project** structure
3. **Build iteratively** with you reviewing each phase
4. **Deploy preview** for testing
5. **Launch** the new site

## Questions for You

Before I start building:

1. **Color scheme**: Like the neural-inspired palette above, or prefer something else?
2. **Knowledge graph**: Want it as the hero element, or more subtle?
3. **3D brain**: Background element or interactive feature?
4. **Priority**: What's most important - visual impact, easy maintenance, or discoverability?
5. **Timeline**: Need this ASAP or okay to build it right over a few days?

---

**This is a significant upgrade**. It will take your research portfolio from "good static site" to "impressive, modern, interactive showcase of interdisciplinary thinking."

Ready to build this?
