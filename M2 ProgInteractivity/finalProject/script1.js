let titles = document.querySelectorAll("h1");
let paragraphs = document.querySelectorAll("p");
let header2s = document.querySelectorAll("h2");
let header3s = document.querySelectorAll("h3");
let imgs = document.querySelectorAll(".s1derp1, .s1derp2, .s5derp1");
let sectionie = document.querySelectorAll("section");
let logo1 = document.querySelector(".headerimg");

for (let i = 0; i < paragraphs.length; i++) {
  let title = titles[i];
  let paragraph = paragraphs[i];
  let header2 = header2s[i];
  let header3 = header3s[i];
  let imgie = imgs[i];
  

  let timeline = gsap.timeline({
    scrollTrigger: title,
    start: "top top"
  });
  timeline.from(title, {
    opacity: 0,
    x: 200,
    duration: 0.7
  });
  timeline.from(logo1, {
    opacity: 0,
    x: 0,
    duration: 0.4
  });
  timeline.from(header3, {
    opacity: 0,
    y: 100,
    duration: 0.6
  });
  timeline.from(paragraph, {
    opacity: 0,
    y: 100,
    duration: 0.6
  });
  timeline.from(header2, {
    opacity: 0,
    x: -100,
    duration: 0.7
  });
  timeline.from(imgie, {
    opacity: 0,
    y: -200,
    duration: 0.4
  });
}
