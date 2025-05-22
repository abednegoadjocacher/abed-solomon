
    // Navigation fade-in
    gsap.from(".nav-bar", {
        duration: 1,
        y: -100,
        opacity: 0,
        ease: "power4.out"
    });

    // Hero section car images
    gsap.from(".hero-content .car-img", {
        duration: 1,
        opacity: 0,
        scale: 0.8,
        stagger: 0.2,
        ease: "back.out(1.7)"
    });

    // Hero buttons
    gsap.from(".car-buttons input", {
        duration: 1,
        y: 50,
        opacity: 0,
        delay: 1,
        stagger: 0.2,
        ease: "power2.out"
    });

    // Shop cards on scroll
    gsap.from(".card", {
        scrollTrigger: {
            trigger: "#shop",
            start: "top 80%",
        },
        duration: 1,
        y: 50,
        opacity: 0,
        stagger: 0.3,
        ease: "power2.out"
    });

    // Slide logos animation
    gsap.from(".slide-container .item", {
        scrollTrigger: {
            trigger: ".slide",
            start: "top 80%"
        },
        duration: 1,
        scale: 0.5,
        opacity: 0,
        stagger: 0.2,
        ease: "elastic.out(1, 0.75)"
    });

    // Contact section fade-in
    gsap.from(".footer-container", {
        scrollTrigger: {
            trigger: "#contact",
            start: "top 90%"
        },
        duration: 1,
        y: 100,
        opacity: 0,
        ease: "power4.out"
    });
