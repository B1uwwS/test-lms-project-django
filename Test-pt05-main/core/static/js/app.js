// Проверка подключения в консоли (нажмите F12 в браузере)
console.log("✅ JS файл успешно загружен и работает!");

document.addEventListener('DOMContentLoaded', function() {
    const aboutBox = document.querySelector('.about');
    const title = document.querySelector('h1');

    if (aboutBox) {
        // --- 1. Плавное появление блока при загрузке ---
        aboutBox.style.opacity = "0";
        aboutBox.style.transform = "translateY(50px)";
        aboutBox.style.transition = "all 1s ease-out";

        setTimeout(() => {
            aboutBox.style.opacity = "1";
            aboutBox.style.transform = "translateY(0)";
        }, 100);

        // --- 2. Интерактив: слежение за мышью (наклон) ---
        document.addEventListener('mousemove', (e) => {
            let xAxis = (window.innerWidth / 2 - e.pageX) / 25;
            let yAxis = (window.innerHeight / 2 - e.pageY) / 25;
            aboutBox.style.transform = `rotateY(${xAxis}deg) rotateX(${yAxis}deg)`;
        });

        // Сброс наклона, когда мышь уходит
        document.addEventListener('mouseleave', () => {
            aboutBox.style.transform = `rotateY(0deg) rotateX(0deg)`;
        });
    }

    if (title) {
        // --- 3. Постоянная анимация заголовка (Пульсация) ---
        let scale = 1;
        let growing = true;

        setInterval(() => {
            if (growing) {
                scale += 0.01;
                if (scale >= 1.1) growing = false;
            } else {
                scale -= 0.01;
                if (scale <= 1) growing = true;
            }
            title.style.transform = `scale(${scale})`;
            title.style.color = `hsl(${scale * 100}, 70%, 50%)`; // Меняет цвет при пульсации
        }, 30);
    }
});