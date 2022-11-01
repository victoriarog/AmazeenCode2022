let slideDeck = document.querySelector(".slidedeck");
let prevButton = document.querySelector(".prev");
let nextButton = document.querySelector(".next");
let slides = document.querySelectorAll(".slide");

console.log("slides", slides.length);

prevButton.addEventListener("click", onPrevButtonClick);
nextButton.addEventListener("click", onNextButtonClick);

let index = 0;
let previousIndex = 0;
const width = 800;

function onPrevButtonClick(e) {
  e.preventDefault();
  if (index > 0) {
    previousIndex = index;
    index = index - 1;
    switchSlide();
  }
}

function onNextButtonClick(e) {
  e.preventDefault();
  if (slides.length > index + 1) {
    previousIndex = index;
    index = index + 1;
    switchSlide();
  }
}

function switchSlide() {
  slides[previousIndex].classList.remove("active");
  slides[index].classList.add("active");

  slideDeck.style.transform = "translateX(-" + index * width + "px)";
}
