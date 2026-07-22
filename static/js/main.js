document.addEventListener("DOMContentLoaded", function () {
  const sortBtn = document.getElementById("sort-rooms-btn");
  const container = document.getElementById("rooms-list-container");
  if (!sortBtn || !container) return;

  let isAscending = true;

  sortBtn.addEventListener("click", function () {
    const items = Array.from(container.getElementsByClassName("room-card-item"));
    if (items.length === 0) return;

    items.sort((a, b) => {
      const nameA = a.getAttribute("data-room-name") || "";
      const nameB = b.getAttribute("data-room-name") || "";
      return isAscending ? nameA.localeCompare(nameB) : nameB.localeCompare(nameA);
    });

    const icon = document.getElementById("sort-icon-symbol");
    icon.innerHTML = isAscending ? '<i data-lucide="arrow-down-a-z"></i>' : '<i data-lucide="arrow-up-a-z"></i>';

    lucide.createIcons();

    document.getElementById("sort-direction-label").textContent = isAscending ? "Sort: A → Z" : "Sort: Z → A";
    lucide.createIcons();

    items.forEach((item) => container.appendChild(item));

    isAscending = !isAscending;
  });
});






// Localstorage username retrieval and display
const usernameElement = document.getElementById("username");

if (usernameElement) {
  let username = localStorage.getItem("username");

  if (!username) {
    username = usernameElement.dataset.username;

    if (username) {
      localStorage.setItem("username", username);
    }
  }

  if (username) {
    usernameElement.textContent = username;
  }
}
const logoutButton = document.getElementById("logout-button");
if (logoutButton) {
  logoutButton.addEventListener("click", function () {
    localStorage.removeItem("username");
    location.reload();
  });
}
