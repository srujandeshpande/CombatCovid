var hamburger = document.querySelector(".hamburger");
var navlinks = document.querySelector(".nav-links");
var links = document.querySelectorAll(".nav-links li");

hamburger.addEventListener("click", () => {
  navlinks.classList.toggle("open");

  links.forEach(link => {
    link.classList.toggle("fade");
  });
});

// ! functions to change opacity of hamburger when hovering

var lines = document.querySelectorAll(".line");

hamburger.addEventListener("mouseover", () => {
  lines.forEach((x, i) => {
    lines[i].style.opacity = 0.5;
  });
});

hamburger.addEventListener("mouseout", () => {
  lines.forEach((x, i) => {
    lines[i].style.opacity = 1;
  });
});
