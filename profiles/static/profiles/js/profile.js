$(function () {
    $(".item").slice(0, 3).show();
    $("#loadMore").on('click', function (e) {
        e.preventDefault();
        $(".item:hidden").slice(0, 3).slideDown();
        if ($(".item:hidden").length == 0) {
            $("#load").fadeOut('slow');
        }
        $('html,body').animate({
            scrollTop: $(this).offset().top
        }, 1500);
    });
});

$(function () {
    $(".item2").slice(0, 3).show();
    $("#loadMore2").on('click', function (e) {
        e.preventDefault();
        $(".item2:hidden").slice(0, 3).slideDown();
        if ($(".item2:hidden").length == 0) {
            $("#load").fadeOut('slow');
        }
        $('html,body').animate({
            scrollTop: $(this).offset().top
        }, 1500);
    });
});