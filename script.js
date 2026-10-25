(function () {
  const yearEl = document.getElementById("year");
  if (yearEl) {
    yearEl.textContent = String(new Date().getFullYear());
  }

  const navToggle = document.querySelector(".nav-toggle");
  const navLinks = document.getElementById("primary-menu");

  if (navToggle && navLinks) {
    navToggle.addEventListener("click", function () {
      const isOpen = navLinks.classList.toggle("is-open");
      navToggle.setAttribute("aria-expanded", String(isOpen));
    });

    navLinks.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        navLinks.classList.remove("is-open");
        navToggle.setAttribute("aria-expanded", "false");
      });
    });
  }

  const themeToggle = document.querySelector(".theme-toggle");
  const storedTheme = localStorage.getItem("theme");

  function applyTheme(theme) {
    document.documentElement.setAttribute("data-theme", theme);
    localStorage.setItem("theme", theme);
    if (themeToggle) {
      themeToggle.textContent =
        theme === "dark" ? "Use light theme" : "Use dark theme";
    }
  }

  applyTheme(storedTheme === "dark" ? "dark" : "light");

  if (themeToggle) {
    themeToggle.addEventListener("click", function () {
      const next =
        document.documentElement.getAttribute("data-theme") === "dark"
          ? "light"
          : "dark";
      applyTheme(next);
    });
  }

  const sectionIds = ["about", "skills", "projects"];
  const sections = sectionIds
    .map(function (id) {
      return document.getElementById(id);
    })
    .filter(Boolean);
  const navAnchors = document.querySelectorAll('.nav-links a[href^="#"]');

  function setActiveLink() {
    const fromTop = window.scrollY + 120;
    let currentId = "about";

    sections.forEach(function (section) {
      if (section.offsetTop <= fromTop) {
        currentId = section.id;
      }
    });

    navAnchors.forEach(function (anchor) {
      const isActive = anchor.getAttribute("href") === "#" + currentId;
      anchor.classList.toggle("is-active", isActive);
    });
  }

  window.addEventListener("scroll", setActiveLink, { passive: true });
  setActiveLink();
})();

const projectSearch = document.getElementById("project-search");
const searchMessage = document.getElementById("search-message");
const projectItems = document.querySelectorAll(".projects-list li");

if (projectSearch) {
  projectSearch.addEventListener("input", function () {
    const searchText = projectSearch.value.toLowerCase().trim();
    let visibleCount = 0;

    projectItems.forEach(function (project) {
      const projectText = project.textContent.toLowerCase();
      const matches = projectText.includes(searchText);

      project.style.display = matches ? "" : "none";

      if (matches) visibleCount++;
    });

    searchMessage.textContent =
      visibleCount + " project(s) found.";
  });
}
