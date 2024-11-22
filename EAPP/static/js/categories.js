// categories.js

// Function to increase font size on hover and decrease when mouse leaves
const categoryNames = document.querySelectorAll('.category-name');

// Add hover effect for category names
categoryNames.forEach(category => {
  category.addEventListener('mouseover', () => {
    category.style.fontSize = '1.7em'; // Increase font size
  });
  
  category.addEventListener('mouseout', () => {
    category.style.fontSize = '1.5em'; // Reset to original size
  });
});

// Function to navigate to category products page when clicked
function navigateToCategory(category) {
  // Here, you'll use the category name (passed to the function) to navigate to the products page
  // You can customize the URL based on how your Flask backend is structured
  window.location.href = `/products/${category}`;
}