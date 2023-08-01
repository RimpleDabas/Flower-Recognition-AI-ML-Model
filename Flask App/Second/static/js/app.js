

const showResultsBtn = document.getElementById('btn-Correct');
const showResultsBtn1 = document.getElementById('btn-Wrong');
const popupContainer = document.getElementById('popupContainer');

showResultsBtn.addEventListener('click', () => {
  
  const results = "<h2> Yay! Let's try another one</h2>";
  
  // Set the content of the pop-up container
  popupContainer.innerHTML = results;

  // Display the pop-up
  popupContainer.style.display = 'block';
});

showResultsBtn1.addEventListener('click', () => {
  
  const results1 = "<h2>Sorry I am not trained enough!</h2><p>Let's give another one a shot</p>";
  
  // Set the content of the pop-up container
  popupContainer.innerHTML = results1;

  // Display the pop-up
  popupContainer.style.display = 'block';
});
