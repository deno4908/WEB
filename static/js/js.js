document.addEventListener('DOMContentLoaded', () => {
    let currentIndex = 0;
    const slides = document.querySelectorAll('.slideshow');
    const dots = document.querySelectorAll('.dot');
    const prevButton = document.querySelector('.prev');
    const nextButton = document.querySelector('.next');
    const slideshowList = document.querySelector('.slideshow-list');

   
    slides.forEach((slide, index) => {
        slide.style.display = 'block'; 
        slide.style.position = 'absolute'; 
        slide.style.width = '100%'; 
        slide.style.left = `${index * 100}%`; 
        slide.style.transition = 'opacity 0.5s ease-in-out'; 
        slide.style.opacity = index === 0 ? '1' : '0'; 
    });

    function showSlide(index) {
        if (index >= slides.length) {
            currentIndex = 0;
        } else if (index < 0) {
            currentIndex = slides.length - 1;
        } else {
            currentIndex = index;
        }

       
        slideshowList.style.transform = `translateX(-${currentIndex * 100}%)`;
        
       
        slides.forEach((slide, i) => {
            slide.style.opacity = i === currentIndex ? '1' : '0';
        });

       
        dots.forEach(dot => dot.classList.remove('active'));
        dots[currentIndex].classList.add('active');
    }


    prevButton.addEventListener('click', () => {
        showSlide(currentIndex - 1);
    });

    nextButton.addEventListener('click', () => {
        showSlide(currentIndex + 1);
    });


    dots.forEach((dot, index) => {
        dot.addEventListener('click', () => {
            showSlide(index);
        });
    });

    showSlide(currentIndex);

    // Tự động chạy (tùy chọn)
    setInterval(() => {
        showSlide(currentIndex + 1);
    }, 5000); // Chuyển slide mỗi 5 giây
});

document.addEventListener("DOMContentLoaded", function () {
    const buttons = document.querySelectorAll(".button button"); // Chọn đúng <button>
    const mainImage = document.getElementById("mainImage");

    buttons.forEach((button) => {
        button.addEventListener("click", function () {
            document.querySelectorAll(".button").forEach((item) => item.classList.remove("active"));
            this.parentElement.classList.add("active"); 
            const newImage = this.getAttribute("data-image");

            mainImage.style.opacity = "0"; 
            setTimeout(() => {
                mainImage.src = newImage;
                mainImage.style.opacity = "1"; // Hiển thị lại sau khi đổi
            }, 300);
            
        });
    });
});
