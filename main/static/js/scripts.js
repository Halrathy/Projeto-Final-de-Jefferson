console.log("funcionou");
let buttonElement = document.querySelector("#search-btn");
let formElement = document.querySelector("#search-form");
    $( function(){        
        $(buttonElement).on('click', function(){
            formElement.submit();
        })
    })