// $(document).ready(function(){
//     var quantity = 1;
//
//     $('.quantity-right-plus').click(function(e){
//         e.preventDefault();
//         var quantity = parseInt($('#quantity').val());
//         $('#quantity').val(quantity + 1);
//     });
//
//     $('.quantity-left-minus').click(function(e){
//         e.preventDefault();
//         var quantity = parseInt($('#quantity').val());
//         if(quantity > 1){
//             $('#quantity').val(quantity - 1);
//         }
//     });
//
// });



//number input

(function() {

    window.inputNumber = function(el) {

        var min = el.attr('min') || false;
        var max = el.attr('max') || false;

        var els = {};

        els.dec = el.prev();
        els.inc = el.next();

        el.each(function() {
            init($(this));
        });

        function init(el) {

            els.dec.on('click', decrement);
            els.inc.on('click', increment);

            function decrement() {
                var value = el[0].value;
                value--;
                if(!min || value >= min) {
                    el[0].value = value;
                }
            }

            function increment() {
                var value = el[0].value;
                value++;
                if(!max || value <= max) {
                    el[0].value = value++;
                }
            }
        }
    }
})();

inputNumber($('.input-number'));

//end of number input




//hover images


// jQuery(document).ready(function($){
//
//     var $overlay = $('<div id="overlay"></div>')
//     var $image = $('<img>');
//
//     $overlay.append($image);
//
//     $('body').append($overlay);
//
//
//     //Hover and show in big image
//     $('.thumb img').hover(function(){
//             var $src = $(this).attr('src');
//             $('#main-img img').attr('src', $src);
//         },
//         $('.row').hover(function(){
//                 var $src = 'https://dummyimage.com/800x800/55595c/fff';
//                 $('#main-img img').attr('src', $src);
//             },
//
//
//         )
//     )
//
// });

//end of hover images