document.addEventListener('DOMContentLoaded', () => {
    var closeBtn = document.querySelector('#closeBtn');
    var sidebar = document.querySelector('#sidebar');
    var buttonContent = document.querySelectorAll('.button_content')
    var mainButtons = document.querySelectorAll('.button')

    console.log(buttonContent);
    closeBtn.addEventListener('click' , function (){
        closeBtn.classList.toggle('fa-times');
        sidebar.classList.toggle('de-active')
        buttonContent.forEach(function(item) {
            item.classList.toggle('de-active');
        });

        mainButtons.forEach(function(item) {
            item.classList.toggle('de-active');
        });
    });

});
