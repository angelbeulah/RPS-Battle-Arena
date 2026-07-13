document.addEventListener("DOMContentLoaded", function () {

    const buttons = document.querySelectorAll(".choice-btn");

    buttons.forEach(button => {

        button.addEventListener("click", function () {

            this.style.transform = "scale(0.95)";

            setTimeout(() => {
                this.style.transform = "";
            }, 150);

        });

    });

    const statCards = document.querySelectorAll(".stat-card");

    statCards.forEach(card => {

        card.addEventListener("mouseenter", function () {
            this.style.boxShadow = "0 0 20px rgba(56,189,248,0.8)";
        });

        card.addEventListener("mouseleave", function () {
            this.style.boxShadow = "";
        });

    });

});