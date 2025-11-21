/**
 * Enhanced interactions for Neuroscience Reports
 * Fixes 3D brain resizing and adds smooth animations
 */

// Fix 3D Brain Resize Issue
(function() {
    let renderer, camera, scene;
    let brainContainer;

    function init3DBrain() {
        brainContainer = document.getElementById('renderMain');
        if (!brainContainer) return;

        // Wait for Three.js scene to be initialized
        const checkInterval = setInterval(() => {
            // Find the canvas inside renderMain
            const canvas = brainContainer.querySelector('canvas');
            if (canvas && window.innerWidth) {
                clearInterval(checkInterval);
                setup3DResize();
            }
        }, 100);
    }

    function setup3DResize() {
        // Handle window resize for 3D brain
        let resizeTimeout;
        window.addEventListener('resize', () => {
            clearTimeout(resizeTimeout);
            resizeTimeout = setTimeout(() => {
                const canvas = brainContainer.querySelector('canvas');
                if (canvas) {
                    // Update canvas size
                    canvas.style.width = '100vw';
                    canvas.style.height = '100vh';

                    // Trigger Three.js resize if available
                    if (window.THREE && renderer && camera) {
                        const width = window.innerWidth;
                        const height = window.innerHeight;

                        renderer.setSize(width, height);
                        camera.aspect = width / height;
                        camera.updateProjectionMatrix();
                    }
                }
            }, 250);
        });
    }

    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init3DBrain);
    } else {
        init3DBrain();
    }
})();

// Smooth Tag Filtering with Stagger Animation
(function() {
    function enhanceTagFiltering() {
        const tagButtons = document.querySelectorAll('.tag-button');
        const posts = document.querySelectorAll('.post-item');

        if (!tagButtons.length || !posts.length) return;

        tagButtons.forEach(button => {
            button.addEventListener('click', function() {
                const selectedTag = this.getAttribute('data-tag');

                // Update active button with smooth transition
                tagButtons.forEach(btn => {
                    btn.classList.remove('active');
                    btn.style.transform = 'scale(1)';
                });
                this.classList.add('active');
                this.style.transform = 'scale(1.05)';
                setTimeout(() => {
                    this.style.transform = 'scale(1)';
                }, 200);

                // Filter posts with staggered animation
                let visibleIndex = 0;
                posts.forEach((post, index) => {
                    const postTags = JSON.parse(post.getAttribute('data-tags') || '[]');
                    const shouldShow = selectedTag === 'all' || postTags.includes(selectedTag);

                    if (shouldShow) {
                        // Fade in with delay
                        post.style.opacity = '0';
                        post.style.transform = 'translateY(20px)';
                        post.style.display = '';

                        setTimeout(() => {
                            post.style.transition = 'all 0.4s cubic-bezier(0.4, 0, 0.2, 1)';
                            post.style.opacity = '1';
                            post.style.transform = 'translateY(0)';
                        }, visibleIndex * 60);

                        visibleIndex++;
                    } else {
                        // Fade out
                        post.style.transition = 'all 0.3s ease';
                        post.style.opacity = '0';
                        post.style.transform = 'translateY(-10px)';

                        setTimeout(() => {
                            post.style.display = 'none';
                        }, 300);
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
                    // Smooth scroll to filter
                    document.getElementById('tag-filter')?.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });
    }

    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', enhanceTagFiltering);
    } else {
        enhanceTagFiltering();
    }
})();

// Parallax Effect on Scroll
(function() {
    function addParallax() {
        const intro = document.getElementById('intro');
        if (!intro) return;

        let ticking = false;

        window.addEventListener('scroll', () => {
            if (!ticking) {
                window.requestAnimationFrame(() => {
                    const scrolled = window.pageYOffset;
                    const rate = scrolled * 0.5;

                    if (intro) {
                        intro.style.transform = `translateY(${rate}px)`;
                    }

                    ticking = false;
                });
                ticking = true;
            }
        });
    }

    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', addParallax);
    } else {
        addParallax();
    }
})();

// Lazy Load Images for Performance
(function() {
    function lazyLoadImages() {
        const images = document.querySelectorAll('img[data-src]');

        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.removeAttribute('data-src');
                    observer.unobserve(img);
                }
            });
        });

        images.forEach(img => imageObserver.observe(img));
    }

    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', lazyLoadImages);
    } else {
        lazyLoadImages();
    }
})();

// Smooth Reveal on Scroll
(function() {
    function revealOnScroll() {
        const reveals = document.querySelectorAll('.post-item, .post.featured');

        const revealObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        }, {
            threshold: 0.1
        });

        reveals.forEach(el => {
            el.style.opacity = '0';
            el.style.transform = 'translateY(30px)';
            el.style.transition = 'all 0.6s cubic-bezier(0.4, 0, 0.2, 1)';
            revealObserver.observe(el);
        });
    }

    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', revealOnScroll);
    } else {
        revealOnScroll();
    }
})();

// Add subtle cursor trail effect (surprise element)
(function() {
    let coords = { x: 0, y: 0 };
    let circles = [];

    const colors = [
        'rgba(196, 165, 123, 0.3)',  // accent
        'rgba(212, 165, 165, 0.3)',  // neural-pink
        'rgba(229, 184, 150, 0.3)'   // neural-orange
    ];

    function addCursorTrail() {
        // Create cursor trail circles
        for (let i = 0; i < 8; i++) {
            const circle = document.createElement('div');
            circle.className = 'cursor-trail';
            circle.style.cssText = `
                position: fixed;
                width: 8px;
                height: 8px;
                border-radius: 50%;
                pointer-events: none;
                z-index: 9999;
                background: ${colors[i % colors.length]};
                transition: all 0.3s ease;
                opacity: 0;
            `;
            document.body.appendChild(circle);
            circles.push(circle);
        }

        // Track mouse movement
        window.addEventListener('mousemove', (e) => {
            coords.x = e.clientX;
            coords.y = e.clientY;
        });

        // Animate circles
        function animateCircles() {
            let x = coords.x;
            let y = coords.y;

            circles.forEach((circle, index) => {
                circle.style.left = x - 4 + 'px';
                circle.style.top = y - 4 + 'px';
                circle.style.opacity = (8 - index) / 16;

                const nextCircle = circles[index + 1] || circles[0];
                x += (parseInt(nextCircle.style.left) || x) / 12;
                y += (parseInt(nextCircle.style.top) || y) / 12;
            });

            requestAnimationFrame(animateCircles);
        }

        animateCircles();
    }

    // Only on desktop
    if (window.innerWidth > 980) {
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', addCursorTrail);
        } else {
            addCursorTrail();
        }
    }
})();

console.log('%c🧠 Neuroscience Reports - Enhanced', 'font-size: 16px; color: #c4a57b; font-weight: bold;');
console.log('%cEarthy design with neural insights', 'font-size: 12px; color: #8a7f73;');
