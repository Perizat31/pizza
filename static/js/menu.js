// var btn_cart = document.querySelector('.btn_cart');
// btn_cart.addEventListener('click',function(event){
//     if(event.target.hasAttribute('data-book-id')){
//         const card=event.target.closest('.box-book');
//         console.log(card)

//     }

// })

$(document).ready(function() {
    $(".btn_cart").click(function(event) {
        event.preventDefault();

        let pizzaID = event.target.attributes['data-pizza-id'].value
        let pizzaContainer = $(".pizza-section-" + pizzaID);
        let pizzaName = pizzaContainer.find(".pizzatitle").text()
        let pizzaImage = pizzaContainer.find(".pizzaimg").attr('src')
        let pizzaCost = pizzaContainer.find(".pizzacost").attr('data-cost')

        let cartItems = JSON.parse(localStorage.getItem("cartItems"))

        if (cartItems !== null){
            let pizzaInCartPredicate = pizza => pizza.id === pizzaID;

            let pizzaInCartExists = cartItems.some(pizzaInCartPredicate)

            if (pizzaInCartExists) {
                cartItems.forEach(element => {
                    if (element.id === pizzaID) {
                        element.quantity += 1
                    }
                });
            }
            else {
                cartItems.push(
                    {
                        "id": bookID,
                        "name": pizzaName,
                        "img": pizzaImage,
                        "price": pizzaCost,
                        "quantity": 1
                    }
                )
            }

            localStorage.setItem("cartItems", JSON.stringify(cartItems))
        }
        else {
            localStorage.setItem("cartItems", JSON.stringify([
                {
                    "id": pizzaID,
                    "name": pizzaName,
                    "img": pizzaImage,
                    "price": pizzaCost,
                    "quantity": 1
                }
            ]))
        }

    })
})