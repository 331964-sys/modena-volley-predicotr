console.log("Modena Volley predictor loaded.");
document.addEventListener("DOMContentLoaded", () => {
  const courtWrapper = document.querySelector(".court-wrapper");
  if (!courtWrapper) return;

  const currentBZone = courtWrapper.getAttribute("data-current-bzone");
  if (!currentBZone) return; // niente selezione se non c'è ancora predizione

  const cells = document.querySelectorAll(".court-cell");
  cells.forEach(cell => {
    if (cell.getAttribute("data-zone") === currentBZone) {
      cell.classList.add("active");
    }
  });
});
