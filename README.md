# Corebody
    <footer>
        <p>&copy; 2026 Corebody. Tutti i diritti riservati.</p>
    </footer>

    
// Parallax leggero sullo scroll
window.addEventListener('scroll', function() {
    const scrolled = window.pageYOffset;
    const heroImage = document.querySelector('immagine_iniziale > img');
    const heroTitle = document.querySelector('immagine_iniziale .titolo');
    
    if (heroImage && scrolled < window.innerHeight) {
        heroImage.style.transform = `scale(${1 + scrolled * 0.0003}) translateY(${scrolled * 0.3}px)`;
    }
    
    if (heroTitle && scrolled < window.innerHeight) {
        heroTitle.style.opacity = 1 - (scrolled * 0.002);
        heroTitle.style.transform = `translate(-50%, calc(-50% + ${scrolled * 0.4}px))`;
    }
    
    // Nascondi scroll indicator
    const scrollIndicator = document.querySelector('.scroll-indicator');
    if (scrollIndicator) {
        scrollIndicator.style.opacity = scrolled > 50 ? '0' : '1';
    }
});