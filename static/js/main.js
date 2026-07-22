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
