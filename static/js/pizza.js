var btn_cart = document.querySelector('.btn_cart');

btn_cart.addEventListener("click",  function(event) {
    // event - делегат события    
    event.preventDefault();

    let pizzaID = event.target.attributes['data-pizza-id'].value
    else {
        let pizza=event.target.closest('.box-pizza');
        let items = 
            {
              
                "name": pizza.querySelector('.booktitle'),
                "count": 1
            };
         

        localStorage.setItem("items", obj)

        let bookSection = document.querySelector('.pizza-section-' + bookID)

        bookSection.innerHTML += `
            <a href="#" class="remove_from_cart">Убрать из корзины</a>
        `
    }
})
