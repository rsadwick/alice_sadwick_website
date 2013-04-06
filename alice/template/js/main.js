$(document).ready(function() {

    //ui:
    //color in nav
    var ui_container = $('nav');
    var current_area = window.location.pathname.split('/');
    switch(current_area[2])
    {
        case 'shower':
            ui_container.find('li a').eq(0).addClass("active");
            break;

        case 'birth':
            ui_container.find('li a').eq(1).addClass("active");
            break;

        case 'registry':
            ui_container.find('li a').eq(2).addClass("active");
            break;

        case 'gallery':
            var gallery = $('body').find(".image-gallery");
            ui_container.find('li a').eq(3).addClass("active");
            activate_insta_api();
            break;
    }

    ///rsvp system
    var is_coming = $("#id_coming");
    var form = $('#form');
    var yes_btn = $("#yes").bind('click touch', function(e){
        is_coming.val('yes');
        setRsvp();
    });

    var no_btn = $("#no").bind('click touch', function(e){
        is_coming.val('no');
        setRsvp();

    });

    function activate_insta_api()
    {
        if(gallery.length)
        {
            //ajax to get instagram:
            $.ajax({
                url: '/baby/services/instagram/',
                success: function(data)
                {
                    gallery.find('#ajax_load').remove();
                    //set default:
                    for(var current_img = 0; current_img < data.length; current_img++)
                    {
                        try{
                            caption_text = (data[current_img].caption.text != null) ? data[current_img].caption.text : "";
                        }
                        catch(e){}
                        gallery.append($('<img />', {
                            'class': 'pics',
                            'src': data[current_img].thumbnail.url,
                            'data-glisse-big' : data[current_img].standard.url,
                            'rel' : 'group1',
                            'title' : caption_text,
                            'width' : '174',
                            'height' : '174'

                        }))
                    }

                    $('.pics').glisse({
                        changeSpeed: 550,
                        speed: 500,
                        effect:'bounce',
                        fullscreen: false
                    });
                },
                error: function (request, status, error) {
                   // alert("An unexpected error occured.");
                }
            });
        }
    }


    function setRsvp()
    {
        $.ajax({
            url: "/baby/services/rsvp/",
            type: "post",
            data: form.serialize(),
            success: function(response) {
                switch(response)
                {
                    case 'True':
                        form.html("<div class='alert alert-success'>Thanks, we will see you soon!</div>");
                        break;
                    case 'False':
                        form.html("<div class='alert alert-success'>Sorry you can't make it, see you later!</div>");
                        break;
                    default:
                        $('.message').html('<div class="alert alert-error">Oh snap! An error happened, try again.</div>');

                }
            }
        })
    }


});
