$(document).ready(function () {
    session = new QiSession();

    /*$('#page_empty').show();
    $('#page_1').hide();
    $('#page_2').hide();
    $('#page_3').hide();
    $('#page_4').hide();
    $('#page_2_1').hide();
    $('#page_2_2').hide();
    $('#page_2_3').hide();
    */


    session.service("ALMemory").done(function(ALMemory) {

        ALMemory.subscriber("Example/Page0").done(function(subscriber) {

            subscriber.signal.connect(function() {
                $('#page_empty').hide();
                $('#page_1').show();
                $('#page_2').hide();
                $('#page_2_1').hide();
                $('#page_2_2').hide();
                $('#page_2_3').hide();
                $('#page_3').hide();
                $('#page_4').hide();
            });
        });


        ALMemory.subscriber("Example/Page1").done(function(subscriber) {

            subscriber.signal.connect(function() {
                $('#page_1').show();
                $('#page_empty').hide();
                $('#page_2').hide();
                $('#page_2_1').hide();
                $('#page_2_2').hide();
                $('#page_2_3').hide();
                $('#page_3').hide();
                $('#page_4').hide();

            });
        });

        ALMemory.subscriber("Example/Page2").done(function(subscriber) {

            subscriber.signal.connect(function() {
                $('#page_2').show();
                $('#page_empty').hide();
                $('#page_1').hide();
                $('#page_2_1').hide();
                $('#page_2_2').hide();
                $('#page_2_3').hide();
                $('#page_3').hide();
                $('#page_4').hide();
            });
        });

        ALMemory.subscriber("Example/Page21").done(function(subscriber) {

            subscriber.signal.connect(function() {
                $('#page_3').hide();
                $('#page_empty').hide();
                $('#page_1').hide();
                $('#page_2').hide();
                $('#page_2_1').show();
                $('#page_2_2').hide();
                $('#page_2_3').hide();
                $('#page_4').hide();

            });
        });

          ALMemory.subscriber("Example/Page22").done(function(subscriber) {

            subscriber.signal.connect(function() {
                $('#page_3').hide();
                $('#page_empty').hide();
                $('#page_1').hide();
                $('#page_2').hide();
                $('#page_2_1').hide();
                $('#page_2_2').show();
                $('#page_2_3').hide();
                $('#page_4').hide();

            });
        });

           ALMemory.subscriber("Example/Page23").done(function(subscriber) {

            subscriber.signal.connect(function() {
                $('#page_3').hide();
                $('#page_empty').hide();
                $('#page_1').hide();
                $('#page_2').hide();
                $('#page_2_1').hide();
                $('#page_2_2').hide();
                $('#page_2_3').show();
                $('#page_4').hide();

            });
        });

        ALMemory.subscriber("Example/Page3").done(function(subscriber) {

            subscriber.signal.connect(function() {
                $('#page_3').show();
                $('#page_empty').hide();
                $('#page_1').hide();
                $('#page_2').hide();
                $('#page_2_1').hide();
                $('#page_2_2').hide();
                $('#page_2_3').hide();
                $('#page_4').hide();

            });
        });

        ALMemory.subscriber("Example/Page4").done(function(subscriber) {

            subscriber.signal.connect(function() {
                $('#page_4').show();
                $('#page_empty').hide();
                $('#page_1').hide();
                $('#page_2').hide();
                $('#page_2_1').hide();
                $('#page_2_2').hide();
                $('#page_2_3').hide();
                $('#page_3').hide();

            });
        });

         
    });

    function raise(event, value) {
        session.service("ALMemory").done(function(ALMemory) {
            ALMemory.raiseEvent(event, value);
        });
    }


    $('#visiter').on('click', function() {
        console.log("click 1");
        raise('Example/Button1', 1)
    });

    $('#dormir').on('click', function() {
        console.log("click 2");
        raise('Example/Button2', 1)
    });

    $('#deplacer').on('click', function() {
        console.log("click 3");
        raise('Example/Button3', 1)
    });

    $('#red').on('click', function() {
        console.log("click red");
        raise('Example/Red', 1)
    });

    $('#blue').on('click', function() {
        console.log("click blue");
        raise('Example/Blue', 1)
    });

    $('#yellow').on('click', function() {
        console.log("click yellow");
        raise('Example/Yellow', 1)
    });


});

