// Ensure the script executes after the DOM is fully loaded
document.addEventListener("DOMContentLoaded", () => {
    const productsContainer = document.getElementById("products-container");
  
    // Example: Adding dynamic behavior or fetching additional data (optional)
    console.log("Products page loaded successfully!");
  
    // Future functionality can include dynamically fetching products using an API.
  });
     
   // products.js

// Initialize cart count from session or local storage
let cartCount = localStorage.getItem('cartCount') || 0;
document.getElementById('cart-count').innerText = cartCount;

// Add to cart functionality
document.querySelectorAll('.add-to-cart-btn').forEach(button => {
  button.addEventListener('click', function() {
    // Get product details from data attributes
    const productId = this.getAttribute('data-product-id');
    const productName = this.getAttribute('data-product-name');
    const productPrice = this.getAttribute('data-product-price');

    // Add product to cart (we will store cart items in localStorage here)
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    cart.push({
      productId,
      productName,
      productPrice
    });
    localStorage.setItem('cart', JSON.stringify(cart));
  });
});

// Optionally, you could add an event listener to redirect to the cart page
document.getElementById('cart-icon-container').addEventListener('click', function() {
  window.location.href = '/cart';  // Redirect to the cart page
});