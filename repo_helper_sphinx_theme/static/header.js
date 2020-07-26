// Based on https://www.aleksandrhovhannisyan.com/blog/dev/responsive-navbar-without-bootstrap/

const topnav = document.getElementById("topnav");
const bodywrapper = document.querySelector(".bodywrapper");
const topnavToggle = topnav.querySelector(".menu-toggle");
const sphinxsidebar = document.querySelector(".sphinxsidebar");

function openMobileNavbar() {
  sphinxsidebar.classList.add("opened");
  topnavToggle.setAttribute("aria-label", "Close navigation menu.");
}

function closeMobileNavbar() {
  sphinxsidebar.classList.remove("opened");
  topnavToggle.setAttribute("aria-label", "Open navigation menu.");
}

topnavToggle.addEventListener("click", () => {
  if (sphinxsidebar.classList.contains("opened")) {
    closeMobileNavbar();
  } else {
    openMobileNavbar();
  }
});

bodywrapper.addEventListener("click", closeMobileNavbar);
