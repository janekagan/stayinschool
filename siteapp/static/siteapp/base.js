$('document').ready(function() {

    /*$('#brand-div').click(function() {
        setTimeout(changeColor())
    });*/

    brandcolor = $('h1').css('color');
    console.log(brandcolor);
    $('#brand').css({'fill': brandcolor, "stroke": brandcolor});

});