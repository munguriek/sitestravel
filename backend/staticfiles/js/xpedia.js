// on ready function
jQuery(document).ready(function($) {
  'use strict';

  // Preloader
  $('#status').fadeOut();
  $('#preloader')
    .delay(350)
    .fadeOut('slow');

  /**** select2 js ****/

  $('.myselect').select2();

  /*--------------------------
	nice Select active
	---------------------------- */

  $('select').niceSelect();

  //-----------Search box jquery------------//

  $('.searchd').on('click', function() {
    $('.searchbox').addClass('open', 1000);
  });

  $('.close').on('click', function() {
    $('.searchbox').removeClass('open', 1000);
  });

  // Menu js for Position fixed
  $(window).scroll(function() {
    var window_top = $(window).scrollTop() + 1;
    if (window_top > 160) {
      $('.hs_navigation_header_wrapper').addClass(
        'menu_fixed animated fadeInDown'
      );
    } else {
      $('.hs_navigation_header_wrapper').removeClass(
        'menu_fixed animated fadeInDown'
      );
    }
  });

  // ===== Scroll to Top ====
  $(window).scroll(function() {
    if ($(this).scrollTop() >= 100) {
      $('#return-to-top').fadeIn(200);
    } else {
      $('#return-to-top').fadeOut(200);
    }
  });
  $('#return-to-top').on('click', function() {
    $('body,html').animate(
      {
        scrollTop: 0,
      },
      500
    );
  });

  // Main Slider Animation

  (function($) {
    //Function to animate slider captions
    function doAnimations(elems) {
      //Cache the animationend event in a variable
      var animEndEv = 'webkitAnimationEnd animationend';

      elems.each(function() {
        var $this = $(this),
          $animationType = $this.data('animation');
        $this.addClass($animationType).one(animEndEv, function() {
          $this.removeClass($animationType);
        });
      });
    }

    //Variables on page load
    var $myCarousel = $('#carousel-example-generic'),
      $firstAnimatingElems = $myCarousel
        .find('.carousel-item:first')
        .find("[data-animation ^= 'animated']");

    //Initialize carousel
    $myCarousel.carousel();

    //Animate captions in first slide on page load
    doAnimations($firstAnimatingElems);

    //Pause carousel
    $myCarousel.carousel('pause');

    //Other slides to be animated on carousel slide event
    $myCarousel.on('click slide.bs.carousel', function(e) {
      var $animatingElems = $(e.relatedTarget).find(
        "[data-animation ^= 'animated']"
      );
      doAnimations($animatingElems);
    });
  })(jQuery);

  /*----------------------------------------------------------------------------------*/
  /* 		Date and Tiem Picker
/*-----------------------------------------------------------------------------------*/
  $('.datepicker').datepicker({ dateFormat: 'D dd M yy' });
  $('.horizontal-datepicker').datepicker({ dateFormat: 'dd M yy' });

  $(document).ready(function() {
    $('.btc_team_slider_wrapper .owl-carousel').owlCarousel({
      loop: true,
      margin: 10,
      autoplay: true,
      responsiveClass: true,
      smartSpeed: 1200,
      navText: [
        '<i class="flaticon-left-arrow" aria-hidden="true"></i>',
        '<i class="flaticon-right-arrow" aria-hidden="true"></i>',
      ],
      responsive: {
        0: {
          items: 1,
          nav: true,
        },
        600: {
          items: 2,
          nav: true,
        },
        1000: {
          items: 3,
          nav: true,
          loop: true,
          margin: 20,
        },
      },
    });
  });

  $(document).ready(function() {
    $('.btc_ln_slider_wrapper .owl-carousel').owlCarousel({
      loop: true,
      margin: 10,
      autoplay: false,
      responsiveClass: true,
      smartSpeed: 1200,
      navText: [
        '<i class="flaticon-left-arrow" aria-hidden="true"></i>',
        '<i class="flaticon-right-arrow" aria-hidden="true"></i>',
      ],
      responsive: {
        0: {
          items: 1,
          nav: true,
        },
        600: {
          items: 2,
          nav: true,
        },
        1000: {
          items: 3,
          nav: true,
          loop: true,
          margin: 20,
        },
      },
    });
  });

  $(document).ready(function() {
    $('.prs_pn_slider_wraper .owl-carousel').owlCarousel({
      loop: true,
      margin: 10,
      autoplay: true,
      responsiveClass: true,
      smartSpeed: 1200,
      navText: [
        '<i class="flaticon-play-button"></i>',
        '<i class="flaticon-play-button"></i>',
      ],
      responsive: {
        0: {
          items: 1,
          nav: true,
        },
        500: {
          items: 3,
          nav: true,
        },
        700: {
          items: 4,
          nav: true,
        },
        1000: {
          items: 6,
          nav: true,
          loop: true,
          margin: 20,
        },
      },
    });
  });

  // testimonial-slider js here
  $('#testimonial-slider').owlCarousel({
    navigationText: [
      "<i class='flaticon-angle-pointing-to-left'></i>",
      "<i class='flaticon-angle-arrow-pointing-to-right'></i>",
    ],
    items: 3,
    itemsDesktop: [1199, 3],
    itemsDesktopSmall: [980, 1],
    itemsTablet: [768, 1],
    itemsMobile: [479, 1],
    slideSpeed: 1500,
    paginationSpeed: 1500,
    navigation: true,
    pagination: false,
    afterAction: function(el) {
      //remove class active
      this.$owlItems.removeClass('active');

      //add class active
      this.$owlItems //owl internal $ object containing items
        .eq(this.currentItem + 1)
        .addClass('active');
    },
  });

  //-------------------------------------------------------
  // counter-section
  //-------------------------------------------------------
  $('.counter-section').on('inview', function(
    event,
    visible,
    visiblePartX,
    visiblePartY
  ) {
    if (visible) {
      $(this)
        .find('.timer')
        .each(function() {
          var $this = $(this);
          $({ Counter: 0 }).animate(
            { Counter: $this.text() },
            {
              duration: 2000,
              easing: 'swing',
              step: function() {
                $this.text(Math.ceil(this.Counter));
              },
            }
          );
        });
      $(this).off('inview');
    }
  });

  $('.album-slider').bxSlider({
    minSlides: 1,
    maxSlides: 10,
    slideWidth: 150,
    slideMargin: 17,
    ticker: true,
    tickerHover: true,
    speed: 20000,
    useCSS: false,
    infiniteLoop: false,
  });

  var wind = $(window);
  $('.loading').fadeOut(500);

  wind.on('scroll', function() {
    $('.skills-progress span').each(function() {
      var bottom_of_object = $(this).offset().top + $(this).outerHeight();
      var bottom_of_window = $(window).scrollTop() + $(window).height();
      var myVal = $(this).attr('data-value');
      if (bottom_of_window > bottom_of_object) {
        $(this).css({
          width: myVal,
        });
      }
    });
  });

  var $loop = $('.screen');
  if ($loop.length > 0) {
    $loop.owlCarousel({
      center: true,
      loop: true,
      nav: false,
      autoplay: false,
      autoplayTimeout: 2000,
      margin: 0,
      responsive: {
        320: {
          items: 1,
          margin: 10,
        },
        481: {
          items: 1,
          margin: 0,
        },
        767: {
          items: 2,
          margin: 0,
        },
        991: {
          items: 3,
        },
      },
    });
  }

  $(document).ready(function() {
    $('.lr_bc_slider_first_wrapper .owl-carousel').owlCarousel({
      loop: true,
      margin: 10,
      autoplay: true,
      responsiveClass: true,
      smartSpeed: 1200,
      navText: [
        '<i class="flaticon-left-arrow"></i>',
        '<i class="flaticon-right-arrow"></i>',
      ],
      responsive: {
        0: {
          items: 1,
          nav: true,
        },
        500: {
          items: 1,
          nav: true,
        },
        700: {
          items: 1,
          nav: true,
        },
        1000: {
          items: 1,
          nav: true,
          loop: true,
          margin: 20,
        },
      },
    });
  });

  // Magnific popup-video

  $('.test-popup-link').magnificPopup({
    type: 'iframe',
    iframe: {
      markup:
        '<div class="mfp-iframe-scaler">' +
        '<div class="mfp-close"></div>' +
        '<iframe class="mfp-iframe" frameborder="0" allowfullscreen></iframe>' +
        '<div class="mfp-title">Some caption</div>' +
        '</div>',
      patterns: {
        youtube: {
          index: 'youtube.com/',
          id: 'v=',
          src: 'https://www.youtube.com/embed/ryzOXAO0Ss0',
        },
      },
    },
    // other options
  });
});











// stepwise form

//jQuery time
var current_fs, next_fs, previous_fs; //fieldsets
var left, opacity, scale; //fieldset properties which we will animate
var animating; //flag to prevent quick multi-click glitches

$(".next").click(function(){
	if(animating) return false;
	animating = true;
	
	current_fs = $(this).parent();
	next_fs = $(this).parent().next();
	
	//activate next step on progressbar using the index of next_fs
	$("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");
	
	//show the next fieldset
	next_fs.show(); 
	//hide the current fieldset with style
	current_fs.animate({opacity: 0}, {
		step: function(now, mx) {
			//as the opacity of current_fs reduces to 0 - stored in "now"
			//1. scale current_fs down to 80%
			scale = 1 - (1 - now) * 0.2;
			//2. bring next_fs from the right(50%)
			left = (now * 50)+"%";
			//3. increase opacity of next_fs to 1 as it moves in
			opacity = 1 - now;
			current_fs.css({
        'transform': 'scale('+scale+')',
        'position': 'absolute'
      });
			next_fs.css({'left': left, 'opacity': opacity});
		}, 
		duration: 800, 
		complete: function(){
			current_fs.hide();
			animating = false;
		}, 
		//this comes from the custom easing plugin
		easing: 'easeInOutBack'
	});
});

$(".previous").click(function(){
	if(animating) return false;
	animating = true;
	
	current_fs = $(this).parent();
	previous_fs = $(this).parent().prev();
	
	//de-activate current step on progressbar
	$("#progressbar li").eq($("fieldset").index(current_fs)).removeClass("active");
	
	//show the previous fieldset
	previous_fs.show(); 
	//hide the current fieldset with style
	current_fs.animate({opacity: 0}, {
		step: function(now, mx) {
			//as the opacity of current_fs reduces to 0 - stored in "now"
			//1. scale previous_fs from 80% to 100%
			scale = 0.8 + (1 - now) * 0.2;
			//2. take current_fs to the right(50%) - from 0%
			left = ((1-now) * 50)+"%";
			//3. increase opacity of previous_fs to 1 as it moves in
			opacity = 1 - now;
			current_fs.css({'left': left});
			previous_fs.css({'transform': 'scale('+scale+')', 'opacity': opacity});
		}, 
		duration: 800, 
		complete: function(){
			current_fs.hide();
			animating = false;
		}, 
		//this comes from the custom easing plugin
		easing: 'easeInOutBack'
	});
});

// $(".submit").click(function(){
// 	return false;
// })