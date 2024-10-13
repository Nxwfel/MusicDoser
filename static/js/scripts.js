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
    })
    $('.bar1').click(function(){
        $('.bar1').css('background-color', '#fff');
        $('.bar3').css('background-color','transparent');
        $('.bar2').css('background-color', 'transparent');
    });
    $('.bar2').click(function(){
        $('.bar2').css('background-color', '#fff');
        $('.bar3').css('background-color','transparent');
        $('.bar1').css('background-color', 'transparent');
    });
    $('.bar3').click(function(){
        $('.bar3').css('background-color', '#fff');
        $('.bar2').css('background-color','transparent');
        $('.bar1').css('background-color', 'transparent');
    });
})