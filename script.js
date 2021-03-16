let shoppingCart = [];

// Linking HTML buttons to JS file
let cartButton = document.getElementById("#cart-button");
let checkoutButton = document.getElementById("#checkout-button");

// When buttons are clicked, open new pages.
function viewCart() {
	window.open("cart.html", "_blank");
};

function viewCheckout() {
	window.open("checkout.html", "_blank");
};

// Event listeners
//cartButton.addEventListener("click", viewCart());
//checkoutButton.addEventListener("click", viewCheckout());
