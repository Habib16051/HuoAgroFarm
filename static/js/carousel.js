// Select the carousel elements
const carousel = document.querySelector('.carousel');
const carouselInner = carousel.querySelector('.carousel-inner');
const carouselItems = carousel.querySelectorAll('.carousel-item');
const prevButton = carousel.querySelector('.prev');
const nextButton = carousel.querySelector('.next');

// Set initial slide index
let slideIndex = 0;

// Function to show the current slide
function showSlide(index) {
    carouselItems.forEach((item, i) => {
        if (i === index) {
            item.classList.add('visible');
        } else {
            item.classList.remove('visible');
        }
    });
}

// Event listeners for Previous and Next buttons
prevButton.addEventListener('click', () => {
    slideIndex = (slideIndex - 1 + carouselItems.length) % carouselItems.length;
    showSlide(slideIndex);
});

nextButton.addEventListener('click', () => {
    slideIndex = (slideIndex + 1) % carouselItems.length;
    showSlide(slideIndex);
});

// Initial slide
showSlide(slideIndex);
