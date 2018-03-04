$(document).ready(function(){

    function SetActiveNavLink() {
        $('.navbar-nav .nav-link').removeClass('active');

        var href = $('div.nav-identifier:first').data('href');

        var element = $('ul.navbar-nav .nav-link').filter(function (index) {
            return $(this).attr('href') == href;
        });

        element.addClass('active');
    }

    SetActiveNavLink();
});