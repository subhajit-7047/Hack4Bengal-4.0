// Replace all existing JavaScript with this updated version
document.addEventListener('DOMContentLoaded', function () {
    const sidebarToggle = document.querySelector('.sidebar-toggle');
    const sideNav = document.querySelector('.side-nav');
    const mainContent = document.querySelector('.main-content');
    const icon = sidebarToggle.querySelector('i');

    // Toggle sidebar
    sidebarToggle.addEventListener('click', (e) => {
        e.stopPropagation();
        sideNav.classList.toggle('active');
        mainContent.classList.toggle('shifted');

        // Toggle icon
        if (sideNav.classList.contains('active')) {
            icon.classList.remove('fa-bars');
            icon.classList.add('fa-times');
            sidebarToggle.style.left = '300px';
        } else {
            icon.classList.remove('fa-times');
            icon.classList.add('fa-bars');
            sidebarToggle.style.left = '20px';
        }
    });

    // Close sidebar when clicking outside
    document.addEventListener('click', (e) => {
        if (!sideNav.contains(e.target) && !sidebarToggle.contains(e.target)) {
            sideNav.classList.remove('active');
            mainContent.classList.remove('shifted');
            icon.classList.remove('fa-times');
            icon.classList.add('fa-bars');
            sidebarToggle.style.left = '20px';
        }
    });

    // Prevent sidebar closing when clicking inside it
    sideNav.addEventListener('click', (e) => {
        e.stopPropagation();
    });

    // Handle window resize
    window.addEventListener('resize', () => {
        if (window.innerWidth > 992 && sideNav.classList.contains('active')) {
            sideNav.classList.remove('active');
            mainContent.classList.remove('shifted');
            icon.classList.remove('fa-times');
            icon.classList.add('fa-bars');
            sidebarToggle.style.left = '20px';
        }
    });

    // Add scroll progress indicator
    const scrollProgress = document.createElement('div');
    scrollProgress.className = 'scroll-progress';
    document.body.appendChild(scrollProgress);

    window.addEventListener('scroll', () => {
        const windowHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const scrolled = (window.scrollY / windowHeight);
        scrollProgress.style.transform = `scaleX(${scrolled})`;
    });

    // Add ripple effect to buttons
    document.querySelectorAll('.btn-start, .btn-consult, .nav-link').forEach(button => {
        button.classList.add('ripple');
    });

    // Button click handlers
    document.querySelectorAll('.btn-start').forEach(button => {
        button.addEventListener('click', function (e) {
            const testTitle = this.closest('.assessment-card').querySelector('.assessment-title').textContent;
            const testDescription = this.closest('.assessment-card').querySelector('.assessment-description').textContent;

            // You can replace this with actual test functionality
            Swal.fire({
                title: `Starting ${testTitle}`,
                text: 'Preparing your assessment...',
                icon: 'info',
                showCancelButton: true,
                confirmButtonText: 'Begin Test',
                cancelButtonText: 'Cancel',
                background: '#fff',
                customClass: {
                    confirmButton: 'btn btn-purple',
                    cancelButton: 'btn btn-frost'
                }
            });
        });
    });

    // Consultation button
    document.querySelector('.btn-consult').addEventListener('click', function () {
        Swal.fire({
            title: 'Book Consultation',
            html: `
            <div class="consultation-form">
                <select class="form-select" id="consultationType">
                    <option value="">Select Consultation Type</option>
                    <option value="video">Video Call</option>
                    <option value="audio">Audio Call</option>
                    <option value="chat">Chat Session</option>
                </select>
                <input type="date" class="form-input" id="consultationDate" min="${new Date().toISOString().split('T')[0]}">
                <select class="form-select" id="consultationTime">
                    <option value="">Select Time Slot</option>
                    <option value="09:00">09:00 AM</option>
                    <option value="11:00">11:00 AM</option>
                    <option value="14:00">02:00 PM</option>
                    <option value="16:00">04:00 PM</option>
                </select>
            </div>
        `,
            showCancelButton: true,
            confirmButtonText: 'Book Now',
            customClass: {
                confirmButton: 'btn btn-success',
                cancelButton: 'btn btn-frost'
            }
        });
    });

    // View All buttons
    document.querySelectorAll('.btn-view-all').forEach(button => {
        button.addEventListener('click', function () {
            const sectionTitle = this.closest('.section-header').querySelector('.section-title').textContent;
            // Replace with actual view all functionality
            window.location.href = `#${sectionTitle.toLowerCase().replace(/\s+/g, '-')}`;
        });
    });

    // Quick Links and Navigation
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            const href = this.getAttribute('href');

            // Add active class
            document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
            this.classList.add('active');

            if (href.startsWith('#')) {
                // It's an anchor link, scroll to section
                const targetSection = document.querySelector(href);
                if (targetSection) {
                    targetSection.scrollIntoView({ behavior: 'smooth' });
                }
            } else {
                // It's a page link, navigate to the page
                window.location.href = href;
            }
        });
    });

    // Auth buttons
    document.querySelector('.btn-login').addEventListener('click', function () {
        window.location.href = 'login.html';
    });

    document.querySelector('.btn-signup').addEventListener('click', function () {
        window.location.href = 'signup.html';
    });

    // Enhanced Counter Animation with Reset and Reload functionality
    function resetAndAnimateCounter(counter) {
        const target = parseInt(counter.getAttribute('data-target'));
        const duration = 2000;
        const steps = 60;
        const stepDuration = duration / steps;
        let current = 0;

        // Always reset to 0 first
        counter.textContent = '0';

        const increment = target / steps;

        function animate() {
            current += increment;
            if (current > target) {
                current = target;
            }
            counter.textContent = Math.round(current).toLocaleString();

            if (current < target) {
                setTimeout(animate, stepDuration);
            }
        }

        animate();
    }

    // Function to handle all counters
    function initializeCounters() {
        const counters = document.querySelectorAll('.counter');
        counters.forEach(counter => resetAndAnimateCounter(counter));
    }

    // Run on initial page load
    initializeCounters();

    // Run on page refresh/reload
    window.addEventListener('beforeunload', () => {
        const counters = document.querySelectorAll('.counter');
        counters.forEach(counter => counter.textContent = '0');
    });

    // Run when page becomes visible again
    document.addEventListener('visibilitychange', () => {
        if (!document.hidden) {
            initializeCounters();
        }
    });

    // Run after page is fully loaded
    window.addEventListener('load', initializeCounters);

    // Run when navigating back to page
    window.addEventListener('pageshow', (event) => {
        if (event.persisted) {
            initializeCounters();
        }
    });

    // Add loading states to buttons
    function addLoadingState(button) {
        button.disabled = true;
        const originalText = button.innerHTML;
        button.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Loading...';
        return () => {
            button.disabled = false;
            button.innerHTML = originalText;
        };
    }

    // Loading Screen Handler
    window.addEventListener('load', function () {
        const loadingScreen = document.querySelector('.loading-screen');

        // Simulate loading time (you can remove this setTimeout in production)
        setTimeout(() => {
            loadingScreen.classList.add('fade-out');

            // Remove from DOM after animation
            setTimeout(() => {
                loadingScreen.style.display = 'none';
            }, 500);
        }, 1500);

        // Initialize scroll-based animations
        const observerOptions = {
            root: null,
            rootMargin: '0px',
            threshold: 0.1
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                }
            });
        }, observerOptions);

        // Observe all elements with fade-in-up class
        document.querySelectorAll('.fade-in-up').forEach(element => {
            observer.observe(element);
        });
    });

    const viewAllAssessmentsBtn = document.querySelector('.btn-view-all');
    const assessmentCardsContainer = document.querySelector('.assessment-cards');

    const initialAssessments = [
        {
            title: "Depression Screening",
            description: "Evaluate symptoms of depression with our clinically validated questionnaire and AI analysis.",
            image: "static/image/img1.jpg",
            tag: "Powered"
        },
        {
            title: "Anxiety Assessment",
            description: "Measure your anxiety levels and get personalized recommendations based on ML analysis.",
            image: "https://images.unsplash.com/photo-1527613426441-4da17471b66d?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80",
            tag: "Powered"
        },
        {
            title: "Stress Level Test",
            description: "Understand your stress patterns and learn coping mechanisms with our smart analysis.",
            image: "https://images.unsplash.com/photo-1493612276216-ee3925520721?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80",
            tag: "New"
        },
        {
            title: "Bipolar Screening",
            description: "Early detection questionnaire for bipolar disorder symptoms with ML-based evaluation.",
            image: "https://images.unsplash.com/photo-1450101499163-c8848c66ca85?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80",
            tag: "Powered"
        }
    ];

    const additionalConditions = [
        {
            title: "OCD",
            description: "Obsessions and compulsions",
            image: "https://images.unsplash.com/photo-1551836022-d5d88e9218df?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80",
            tag: "Powered"
        },
        {
            title: "PTSD",
            description: "Post-traumatic stress",
            image: "https://images.unsplash.com/photo-1517602302552-471fe67acf66?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80",
            tag: "Powered"
        },
        {
            title: "Insomnia",
            description: "Chronic sleep difficulties",
            image: "https://images.unsplash.com/photo-1512758017271-d7b84c2113f1?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80",
            tag: "Powered"
        },
        {
            title: "ADHD",
            description: "Attention and hyperactivity",
            image: "static/image/img2.jpg", // Updated image
            tag: "Powered"
        },
        {
            title: "Autism",
            description: "Social communication challenges",
            image: "static/image/img3.jpg", // Updated image
            tag: "Powered"
        }
    ];

    let showingAll = false;

    function renderAssessments(assessments) {
        assessmentCardsContainer.innerHTML = "";
        assessments.forEach(assessment => {
            const card = document.createElement('div');
            card.className = 'assessment-card';
            card.innerHTML = `
                <div class="assessment-image">
                    <img src="${assessment.image}" alt="${assessment.title}">
                    <span class="assessment-tag">${assessment.tag}</span>
                </div>
                <div class="assessment-content">
                    <h3 class="assessment-title">${assessment.title}</h3>
                    <p class="assessment-description">${assessment.description}</p>
                    <button class="btn-start" onclick="startTest('${assessment.title.toLowerCase().replace(/\s+/g, '-')}')">
                        Start Test <i class="fas fa-arrow-right"></i>
                    </button>
                </div>
            `;
            assessmentCardsContainer.appendChild(card);
        });
    }

    viewAllAssessmentsBtn.addEventListener('click', function () {
        if (showingAll) {
            renderAssessments(initialAssessments);
            viewAllAssessmentsBtn.innerHTML = 'View All <i class="fas fa-chevron-right"></i>';
        } else {
            renderAssessments([...initialAssessments, ...additionalConditions]);
            viewAllAssessmentsBtn.innerHTML = 'Show Less <i class="fas fa-chevron-up"></i>';
        }
        showingAll = !showingAll;
    });

    // Initial render
    renderAssessments(initialAssessments);

    // Smooth scrolling for top navigation links
    document.querySelectorAll('.top-nav-links a').forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);

            if (targetId) {
                const targetSection = document.getElementById(targetId);
                if (targetSection) {
                    targetSection.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });

                    // Update active state
                    document.querySelectorAll('.top-nav-links a').forEach(a => a.classList.remove('active'));
                    this.classList.add('active');
                }
            }
        });
    });

    // Scroll spy to update active state based on scroll position
    window.addEventListener('scroll', () => {
        const sections = ['assessments', 'blog', 'resources'];
        let currentSection = '';

        sections.forEach(section => {
            const element = document.getElementById(section);
            if (element) {
                const rect = element.getBoundingClientRect();
                if (rect.top <= 100) {
                    currentSection = section;
                }
            }
        });

        document.querySelectorAll('.top-nav-links a').forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${currentSection}`) {
                link.classList.add('active');
            }
        });
    });

    // Add this after the scroll spy code
    document.querySelectorAll('.top-nav-links a').forEach(link => {
        // Check if current page matches the link
        if (window.location.pathname.includes(link.getAttribute('href'))) {
            link.classList.add('active');
        }

        link.addEventListener('click', function (e) {
            // Remove active class from all links
            document.querySelectorAll('.top-nav-links a').forEach(a => {
                a.classList.remove('active');
            });
            // Add active class to clicked link
            this.classList.add('active');
        });
    });

    // Update page title when navigation links are clicked
    function updatePageTitle(title) {
        document.getElementById('currentPageTitle').textContent = title;
    }

    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', function () {
            const title = this.textContent.trim();
            updatePageTitle(title);
        });
    });

    // Blog Slider functionality
    const blogSlider = {
        currentSlide: 0,
        sliding: false,
        autoSlideTimer: null,

        init() {
            this.container = document.querySelector('.blog-cards');
            this.cards = document.querySelectorAll('.blog-card');
            this.dots = document.querySelectorAll('.dot');
            this.slideCount = this.cards.length;

            // Navigation buttons
            document.getElementById('prevSlide')?.addEventListener('click', () => this.slide('prev'));
            document.getElementById('nextSlide')?.addEventListener('click', () => this.slide('next'));

            // Dot navigation
            this.dots.forEach((dot, index) => {
                dot.addEventListener('click', () => {
                    this.pauseAutoSlide();
                    this.goToSlide(index);
                    this.startAutoSlide();
                });
            });

            // Touch support
            let touchStartX = 0;
            this.container.addEventListener('touchstart', (e) => {
                touchStartX = e.changedTouches[0].screenX;
                this.pauseAutoSlide();
            });

            this.container.addEventListener('touchend', (e) => {
                const touchEndX = e.changedTouches[0].screenX;
                const diff = touchStartX - touchEndX;

                if (Math.abs(diff) > 50) {
                    this.slide(diff > 0 ? 'next' : 'prev');
                }
                this.startAutoSlide();
            });

            // Pause on hover
            this.container.addEventListener('mouseenter', () => this.pauseAutoSlide());
            this.container.addEventListener('mouseleave', () => this.startAutoSlide());

            // Start auto sliding
            this.startAutoSlide();
            this.updateActiveStates();
        },

        startAutoSlide() {
            this.pauseAutoSlide();
            this.autoSlideTimer = setInterval(() => this.slide('next'), 5000);
        },

        pauseAutoSlide() {
            if (this.autoSlideTimer) {
                clearInterval(this.autoSlideTimer);
                this.autoSlideTimer = null;
            }
        },

        goToSlide(index) {
            if (index === this.currentSlide || this.sliding) return;
            this.currentSlide = index;
            this.updateSlidePosition();
        },

        slide(direction) {
            if (this.sliding) return;
            this.sliding = true;

            if (direction === 'next') {
                this.currentSlide = (this.currentSlide + 1) % this.slideCount;
            } else {
                this.currentSlide = (this.currentSlide - 1 + this.slideCount) % this.slideCount;
            }

            this.updateSlidePosition();
        },

        updateSlidePosition() {
            const cardWidth = this.cards[0].offsetWidth + 32; // Including gap
            const newTransform = -(this.currentSlide * cardWidth);

            this.container.style.transform = `translateX(${newTransform}px)`;
            this.updateActiveStates();

            setTimeout(() => {
                this.sliding = false;
            }, 600);
        },

        updateActiveStates() {
            this.cards.forEach((card, index) => {
                if (index === this.currentSlide) {
                    card.classList.add('active');
                } else {
                    card.classList.remove('active');
                }
            });

            this.dots.forEach((dot, index) => {
                if (index === this.currentSlide) {
                    dot.classList.add('active');
                } else {
                    dot.classList.remove('active');
                }
            });
        }
    };

    // Initialize the slider
    blogSlider.init();
});

function startTest(condition) {
    window.location.href = `test.html?condition=${condition}`;
}

// FAQ Functionality
document.addEventListener('DOMContentLoaded', function () {
    const faqItems = document.querySelectorAll('.faq-item');

    faqItems.forEach(item => {
        item.addEventListener('click', function (e) {
            // Create ripple effect
            const ripple = document.createElement('span');
            ripple.classList.add('ripple');

            const rect = item.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            ripple.style.left = x + 'px';
            ripple.style.top = y + 'px';

            item.appendChild(ripple);

            setTimeout(() => ripple.remove(), 600);

            // Toggle active state
            const wasActive = item.classList.contains('active');

            // Close all other items
            faqItems.forEach(otherItem => {
                otherItem.classList.remove('active');
            });

            // Toggle current item if it wasn't active
            if (!wasActive) {
                item.classList.add('active');
            }
        });
    });
});

// Fix for navigation buttons
document.querySelectorAll('.top-nav-links a').forEach(link => {
    link.addEventListener('click', function (e) {
        const href = this.getAttribute('href');

        // Only handle anchor links on the same page
        if (href.startsWith('#')) {
            e.preventDefault();
            const targetSection = document.querySelector(href);
            if (targetSection) {
                targetSection.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }

            // Update active state
            document.querySelectorAll('.top-nav-links a').forEach(a => a.classList.remove('active'));
            this.classList.add('active');
        }
        // Allow default behavior for external links
    });
});
document.querySelectorAll('.top-nav-links a').forEach(link => {
    link.addEventListener('click', function (e) {
        const href = this.getAttribute('href');

        // Only handle anchor links on the same page
        if (href.startsWith('#')) {
            e.preventDefault();
            const targetSection = document.querySelector(href);
            if (targetSection) {
                targetSection.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }

            // Update active state
            document.querySelectorAll('.top-nav-links a').forEach(a => a.classList.remove('active'));
            this.classList.add('active');
        }
        // Allow default behavior for external links
    });
});