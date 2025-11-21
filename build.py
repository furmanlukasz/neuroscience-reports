#!/usr/bin/env python3
"""
Neuroscience Reports Site Builder
Generates static site from markdown files with YAML front matter
"""

import os
import re
import yaml
import markdown
from datetime import datetime
from pathlib import Path
import json

# Configuration
CONTENT_DIR = Path("content")
OUTPUT_DIR = Path(".")
TEMPLATE_DIR = Path("templates")
ASSETS_DIR = Path("assets")

# Tag definitions with colors
TAGS = {
    "RQA": {"name": "Recurrence Quantitative Analysis", "color": "#E2B4BD"},
    "TPM": {"name": "Transition Probability Matrix", "color": "#FFB69"},
    "Markov Chains": {"name": "Markov Chains", "color": "#F2B880"},
    "System Dynamics": {"name": "System Dynamics", "color": "#CBAC88"},
    "EEG Analysis": {"name": "EEG Analysis", "color": "#E2B4BD"},
    "Machine Learning": {"name": "Machine Learning", "color": "#FFB69"},
    "Classification": {"name": "Classification", "color": "#F2B880"},
    "MCI": {"name": "Mild Cognitive Impairment", "color": "#CBAC88"},
    "Alzheimer's": {"name": "Alzheimer's Disease", "color": "#E2B4BD"},
    "Schizophrenia": {"name": "Schizophrenia", "color": "#FFB69"},
    "Autoencoders": {"name": "Autoencoders", "color": "#F2B880"},
    "Deep Learning": {"name": "Deep Learning", "color": "#CBAC88"},
    "Microstates": {"name": "Microstates", "color": "#E2B4BD"},
    "Network Analysis": {"name": "Network Analysis", "color": "#FFB69"},
    "Source Localization": {"name": "Source Localization", "color": "#F2B880"},
    "EMD": {"name": "Empirical Mode Decomposition", "color": "#CBAC88"},
    "Cognitive Models": {"name": "Cognitive Models", "color": "#E2B4BD"},
    "PAC": {"name": "Phase-Amplitude Coupling", "color": "#FFB69"},
    "Preprocessing": {"name": "Preprocessing", "color": "#F2B880"},
    "Signal Processing": {"name": "Signal Processing", "color": "#CBAC88"},
    "Spectral Analysis": {"name": "Spectral Analysis", "color": "#E2B4BD"},
    "UMAP": {"name": "UMAP", "color": "#FFB69"},
    "Clustering": {"name": "Clustering", "color": "#F2B880"},
}


class Post:
    """Represents a blog post or report"""

    def __init__(self, filepath):
        self.filepath = Path(filepath)
        self.metadata = {}
        self.content = ""
        self.html_content = ""
        self.parse_file()

    def parse_file(self):
        """Parse markdown file with YAML front matter"""
        with open(self.filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract YAML front matter
        pattern = r'^---\s*\n(.*?)\n---\s*\n(.*)$'
        match = re.match(pattern, content, re.DOTALL)

        if match:
            yaml_content = match.group(1)
            markdown_content = match.group(2)
            self.metadata = yaml.safe_load(yaml_content) or {}
            self.content = markdown_content
        else:
            # No front matter, use entire content
            self.content = content

        # Convert markdown to HTML
        md = markdown.Markdown(extensions=['extra', 'codehilite', 'toc'])
        self.html_content = md.convert(self.content)

    @property
    def title(self):
        return self.metadata.get('title', 'Untitled')

    @property
    def date(self):
        return self.metadata.get('date', datetime.now())

    @property
    def description(self):
        return self.metadata.get('description', '')

    @property
    def tags(self):
        return self.metadata.get('tags', [])

    @property
    def image(self):
        return self.metadata.get('image', 'images/default.png')

    @property
    def post_type(self):
        return self.metadata.get('type', 'report')  # report or blog

    @property
    def slug(self):
        """Generate URL-friendly slug from filename"""
        return self.filepath.stem

    @property
    def output_path(self):
        """Get output HTML path"""
        return OUTPUT_DIR / f"{self.slug}.html"


def load_posts_from_yaml():
    """Load posts from posts.yaml configuration file"""
    posts = []

    yaml_file = Path("posts.yaml")
    if not yaml_file.exists():
        print("Warning: posts.yaml not found")
        return posts

    with open(yaml_file, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)

    if not config or 'posts' not in config:
        return posts

    for post_data in config['posts']:
        # Create a simple post object from YAML data
        post = type('Post', (), {})()
        post.slug = post_data.get('slug', '')
        post.title = post_data.get('title', 'Untitled')
        post.description = post_data.get('description', '')
        post.date = post_data.get('date', datetime.now())
        post.image = post_data.get('image', 'images/default.png')
        post.tags = post_data.get('tags', [])
        post.post_type = post_data.get('type', 'report')
        posts.append(post)

    # Sort by date (newest first)
    posts.sort(key=lambda p: p.date, reverse=True)

    return posts


def load_posts():
    """Load all posts - first try posts.yaml, then fall back to markdown files"""
    # Try loading from YAML first (preferred method)
    posts = load_posts_from_yaml()

    if posts:
        return posts

    # Fallback: scan for markdown files
    posts = []
    for md_file in Path(".").glob("*.md"):
        # Skip certain files
        if md_file.name in ['README.md', 'summary.md']:
            continue
        # Only include if it looks like a report
        if md_file.name.startswith(('web-', 'classification', 'transition',
                                     'correlation', 'motifs', 'state-', 'medium_')):
            posts.append(Post(md_file))

    # Sort by date (newest first)
    posts.sort(key=lambda p: p.date, reverse=True)

    return posts


def generate_post_html(post):
    """Generate HTML file for a single post"""
    # Read template
    template_path = Path("templates/post_template.html") if (Path("templates/post_template.html")).exists() else None

    if template_path:
        with open(template_path, 'r', encoding='utf-8') as f:
            template = f.read()
    else:
        # Use a simple template
        template = f"""<!DOCTYPE HTML>
<html>
<head>
    <title>{{{{ title }}}} - Datalab108</title>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
    <link rel="stylesheet" href="assets/css/main.css" />
    <noscript><link rel="stylesheet" href="assets/css/noscript.css" /></noscript>
</head>
<body class="is-preload">
    <div id="wrapper">
        <nav id="nav">
            <ul class="links">
                <li><a href="index.html">Science Reports</a></li>
                <li><a href="about.html">About</a></li>
            </ul>
        </nav>
        <div id="main">
            <article class="post featured">
                <header class="major">
                    <span class="date">{{{{ date }}}}</span>
                    <h2>{{{{ title }}}}</h2>
                    <p>{{{{ description }}}}</p>
                    <div class="tags">
                        {{{{ tags }}}}
                    </div>
                </header>
                <div class="content">
                    {{{{ content }}}}
                </div>
            </article>
        </div>
    </div>
    <script src="assets/js/jquery.min.js"></script>
    <script src="assets/js/browser.min.js"></script>
    <script src="assets/js/breakpoints.min.js"></script>
    <script src="assets/js/util.js"></script>
    <script src="assets/js/main.js"></script>
</body>
</html>"""

    # Format tags HTML
    tags_html = " ".join([f'<span class="tag" style="background-color: {TAGS.get(tag, {}).get("color", "#ccc")}">{tag}</span>'
                          for tag in post.tags])

    # Replace placeholders
    html = template.replace('{{{{ title }}}}', post.title)
    html = html.replace('{{{{ date }}}}', post.date.strftime('%B %d, %Y') if isinstance(post.date, datetime) else str(post.date))
    html = html.replace('{{{{ description }}}}', post.description)
    html = html.replace('{{{{ tags }}}}', tags_html)
    html = html.replace('{{{{ content }}}}', post.html_content)

    return html


def generate_index_html(posts):
    """Generate main index.html with all posts and tag filtering"""

    # Separate reports and blogs
    reports = [p for p in posts if p.post_type == 'report']
    blogs = [p for p in posts if p.post_type == 'blog']

    # Read the current index.html to preserve the header and 3D visualization
    with open('index.html', 'r', encoding='utf-8') as f:
        current_index = f.read()

    # Extract the header section (everything before <!-- Main -->)
    header_match = re.search(r'(.*?)<!-- Main -->', current_index, re.DOTALL)
    header_section = header_match.group(1) if header_match else ""

    # Extract footer section (everything after </div> following main)
    footer_match = re.search(r'(<!-- Footer -->.*?</html>)', current_index, re.DOTALL)
    footer_section = footer_match.group(1) if footer_match else ""

    # Generate posts HTML
    posts_html = ""

    # Featured post (most recent)
    if reports:
        featured = reports[0]
        posts_html += f"""
            <!-- Featured Post -->
            <article class="post featured">
                <header class="major">
                    <span class="date">{featured.date.strftime('%B %d, %Y') if isinstance(featured.date, datetime) else str(featured.date)}</span>
                    <h2><a href="{featured.slug}.html">{featured.title}</a></h2>
                    <p>{featured.description}</p>
                    <div class="post-tags">
                        {" ".join([f'<span class="tag" data-tag="{tag}">{tag}</span>' for tag in featured.tags])}
                    </div>
                </header>
                <a href="{featured.slug}.html" class="image main"><img src="{featured.image}" alt="" /></a>
                <ul class="actions special">
                    <li><a href="{featured.slug}.html" class="button small">Full Story</a></li>
                </ul>
            </article>
        """

    # Rest of posts
    posts_html += '\n            <!-- Posts -->\n            <section class="posts">\n'

    for post in reports[1:]:
        posts_html += f"""
            <article class="post-item" data-tags='{json.dumps(post.tags)}'>
                <header class="major">
                    <span class="date">{post.date.strftime('%B %d, %Y') if isinstance(post.date, datetime) else str(post.date)}</span>
                    <h2><a href="{post.slug}.html">{post.title}</a></h2>
                    <p>{post.description}</p>
                    <div class="post-tags">
                        {" ".join([f'<span class="tag" data-tag="{tag}">{tag}</span>' for tag in post.tags])}
                    </div>
                </header>
                <a href="{post.slug}.html" class="image main"><img src="{post.image}" alt="" /></a>
                <ul class="actions special">
                    <li><a href="{post.slug}.html" class="button small">Full Story</a></li>
                </ul>
            </article>
        """

    posts_html += "\n            </section>\n"

    # Generate tag filter HTML
    all_tags = set()
    for post in posts:
        all_tags.update(post.tags)

    tag_filter_html = """
        <div id="tag-filter" class="tag-filter">
            <h3>Filter by Tags:</h3>
            <div class="tags-container">
                <button class="tag-button active" data-tag="all">All</button>
    """

    for tag in sorted(all_tags):
        tag_color = TAGS.get(tag, {}).get("color", "#ccc")
        tag_filter_html += f'                <button class="tag-button" data-tag="{tag}" style="border-color: {tag_color}">{tag}</button>\n'

    tag_filter_html += """
            </div>
        </div>
    """

    # Build complete HTML
    complete_html = header_section
    complete_html += """
        <!-- Main -->
        <div id="main">
    """
    complete_html += tag_filter_html
    complete_html += posts_html
    complete_html += """
        </div>
    """
    complete_html += footer_section

    # Add tag filtering JavaScript before closing body tag
    tag_script = """
    <script>
    // Tag filtering functionality
    document.addEventListener('DOMContentLoaded', function() {
        const tagButtons = document.querySelectorAll('.tag-button');
        const posts = document.querySelectorAll('.post-item');

        tagButtons.forEach(button => {
            button.addEventListener('click', function() {
                const selectedTag = this.getAttribute('data-tag');

                // Update active button
                tagButtons.forEach(btn => btn.classList.remove('active'));
                this.classList.add('active');

                // Filter posts
                posts.forEach(post => {
                    const postTags = JSON.parse(post.getAttribute('data-tags'));

                    if (selectedTag === 'all' || postTags.includes(selectedTag)) {
                        post.style.display = '';
                    } else {
                        post.style.display = 'none';
                    }
                });
            });
        });

        // Tag click in post
        document.querySelectorAll('.tag').forEach(tag => {
            tag.style.cursor = 'pointer';
            tag.addEventListener('click', function() {
                const tagName = this.getAttribute('data-tag');
                const tagButton = document.querySelector(`.tag-button[data-tag="${tagName}"]`);
                if (tagButton) {
                    tagButton.click();
                    // Scroll to filter
                    document.getElementById('tag-filter').scrollIntoView({ behavior: 'smooth' });
                }
            });
        });
    });
    </script>
    """

    # Insert script before </body>
    complete_html = complete_html.replace('</body>', tag_script + '\n</body>')

    return complete_html


def build_site():
    """Main build function"""
    print("Building Neuroscience Reports site...")

    # Load all posts
    posts = load_posts()
    print(f"Found {len(posts)} posts")

    # Generate HTML files for each post (optional, if you want to regenerate)
    # for post in posts:
    #     html = generate_post_html(post)
    #     with open(post.output_path, 'w', encoding='utf-8') as f:
    #         f.write(html)
    #     print(f"Generated {post.output_path}")

    # Generate index.html
    index_html = generate_index_html(posts)
    with open(OUTPUT_DIR / 'index.html', 'w', encoding='utf-8') as f:
        f.write(index_html)
    print("Generated index.html")

    # Generate tags.json for JavaScript
    tags_data = {tag: TAGS[tag] for tag in TAGS}
    with open(OUTPUT_DIR / 'tags.json', 'w', encoding='utf-8') as f:
        json.dump(tags_data, f, indent=2)
    print("Generated tags.json")

    print("Build complete!")


if __name__ == "__main__":
    build_site()
