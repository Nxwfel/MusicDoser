$(document).ready(function(){
    $('.menu-btn').click(function(){
        $('.menu').addClass('active');
        $('.menu-btn').css('visibility', 'hidden');
        $('.socials').css('visibility', 'hidden');
    });

    $('.close-btn').click(function(){
        $('.menu').removeClass('active');
        $('.menu-btn').css('visibility','visible');
        $('.socials').css('visibility', 'visible');
    });
    $('.right-arrow').click(function(){
        $(this).next('.Dropdownmenu').slideToggle();
        $(this).find('.right-arrow').toggleClass(rotate);
    });
})