$(document).ready(function(){




    function adjustModalMaxHeightAndPosition(){
          $('.modal').each(function(){
            if($(this).hasClass('in') === false){
              $(this).show();
            }
            var contentHeight = $(window).height() - 60;
            var headerHeight = $(this).find('.modal-header').outerHeight() || 2;
            var footerHeight = $(this).find('.modal-footer').outerHeight() || 2;

            $(this).find('.modal-dialog').addClass('modal-dialog-center').css({

              'margin-top': function () {
                var mH = $(this).outerHeight();
                var wH = $(window).height();
                return (mH < wH ) ? -( mH * 0.6): -( wH * 0.5) + 12;
              },
              'margin-left': function () {
                return -($(this).outerWidth() / 2);
              }
            });
            if($(this).hasClass('in') === false){
              $(this).hide();
            }
          });
        }

    if ($(window).height() >= 320){
        $(window).resize(adjustModalMaxHeightAndPosition).trigger("resize");
    }

    $.fn.serializeObject = function(){
        var o = {};
        var a = this.serializeArray();
        $.each(a, function() {
            if (o[this.name] !== undefined) {
                if (!o[this.name].push) {
                    o[this.name] = [o[this.name]];
                }
                o[this.name].push(this.value || '');
            } else {
                o[this.name] = this.value || '';
            }
        });
        return o;
    };

}) ;