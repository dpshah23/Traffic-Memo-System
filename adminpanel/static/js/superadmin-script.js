// script.js
$(document).ready(function() {
    $('.sub-btn').click(function() {
        $(this).next('.sub-menu').slideToggle();
        $(this).find('.dropdown').toggleClass('rotate');
    });

    $('.menu-btn').click(function(){
        $('.side-bar').toggleClass('active');
        $('#sideBarContainer').toggleClass('col-3')

        if($('#mainContent').hasClass('col-12')) {
            $('#mainContent').removeClass('col-12');
            $('#mainContent').addClass('col-9 offset-3');
        } else {
            $('#mainContent').removeClass('col-9 offset-3');
            $('#mainContent').addClass('col-12');
        }
    })

    // $('.close-btn').click(function(){
    //     $('.side-bar').removeClass('active');
    //     // $('.menu-btn').css("visibility" , "visible");
    // })
});
