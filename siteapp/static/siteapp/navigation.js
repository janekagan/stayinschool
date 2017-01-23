$('document').ready(function() {

    css = {
        'text-decoration': 'underline',
        'font-size': '1.55em'
        };

    if (window.location.href.includes('about')) {
        css['stroke'] = 'Crimson';
        css['fill'] = 'Crimson';
        $('#one a').css(css);
     }

    if (window.location.href.includes('music')) {
        css['stroke'] = 'SeaGreen';
        css['fill'] = 'SeaGreen';
        $('#two a').css(css);
        }

    if (window.location.href.includes('videos')) {
        css['stroke'] = 'RoyalBlue';
        css['fill'] = 'RoyalBlue';
        $('#three a').css(css);
        }

    if (window.location.href.includes('social')) {
        css['stroke'] = 'Tomato';
        css['fill'] = 'Tomato';
        $('#four a').css(css);
        }

    if (window.location.href.includes('contact')) {
        css['stroke'] = 'DarkOrchid';
        css['fill'] = 'DarkOrchid';
        $('#five a').css(css);
        }

    $('#brand-div').click(function() {
        console.log(window.location.href);
        $('#page').fadeOut();
        if (window.location.href.split('//')[1].split('/')[1].length != 0) {
            setTimeout(function() {
                window.location.href = '/';
            }, 300);
        }
    });

    $('tspan a').click(function(e) {
        e.preventDefault();
        url = $(this).attr('url');
        $('#page').fadeOut();
        setTimeout(function() {
            window.location.href = url;
        }, 300);
    });

});