window.timber = window.timber || {};

timber.cache = {
    // General
    $html: $('html'),
    $body: $('body'),
    // Navigation
    $navigation: $('#accessibleNav'),

    // Mobile Slide Out Navigation
    mobileSideNav: {
        $container: $('.container'),
        $toggle: $('#sideNavToggle'),
        $nav: $( '#mobileSideNav' )
    }

};

timber.init = function () {

    // // Run on load
    // timber.accessibleNav();
    // timber.productImageSwitch();
    // timber.carouselInit();
    // timber.loginFormInit();
    // timber.celebrityGallery();
    timber.mobileSideNav();
    timber.infiniteScroll();
    // timber.mobileProductInfoBlock();
    // timber.productDescriptionBlock();
    // timber.loader.init();
    // // initialize smooth scroll
    smoothScroll.init();
};

timber.mobileSideNav = function(){

    var $container = timber.cache.mobileSideNav.$container,
        $toggle = timber.cache.mobileSideNav.$toggle,
        $nav = timber.cache.mobileSideNav.$nav;

    $toggle.click(function(e) {
        e.preventDefault();
        e.stopPropagation();

        if ( $container.hasClass('menu-open') ){
            timber.mobileSideNav.close();
        } else {
            timber.mobileSideNav.open();
        }
    });
    $container.click(function(e){
        if ( $container.hasClass('menu-open') ){
            timber.mobileSideNav.close();
        }
    });

    this.mobileSideNav.open = function(){
        $container.addClass( 'menu-open' );
        $nav.addClass( 'open' );
    };

    this.mobileSideNav.close = function(){
        $container.removeClass( 'menu-open' );
        $nav.removeClass( 'open' );
    };
};


timber.infiniteScroll = function() {
  // add a way point to the last item currently shown on the page.
  $('.last-item').last().waypoint(function() {
    var waypoint = this;
    // you're at the end of the page, stop assigning waypoints.
    if (typeof $('#last-page')[0] != 'undefined') {
      console.log('found last item');
      waypoint.disable();
      return;
    }

    var loadingImage;
    pInfScrNode = $('.more').last();
    pInfScrURL = $('.more a').last().attr("href");
    console.log(pInfScrNode);
    console.log(pInfScrURL);

    $.ajax({
        type: 'GET',
        url: pInfScrURL,
        beforeSend: function() {
          loadingImage = pInfScrNode.clone().empty().append('<img src=\"http://cdn.shopify.com/s/files/1/0068/2162/assets/loading.gif?105791\" />');
          loadingImage.insertAfter(pInfScrNode);
          pInfScrNode.hide();
        },
        success: function(data) {
          // remove loading
          console.log('got it');
          pInfScrNode.next().remove();
          var filteredData = $(data).find(".celebrities-list-block");
          console.log(filteredData);
          filteredData.insertBefore( $("#list-foot") );
          loadingImage.remove();
          waypoint.disable();
          // recursively call yourself to attach another waypoint to the last item we just received

          // leave this commented out until it works...
          timber.infiniteScroll();
        },
        dataType: "html"
      });

        console.log('You have scrolled to my waypoint.');
    }, {
    offset: 'bottom-in-view'
  });
};

// Initialize Timber's JS on docready
$(function() {
    window.timber.init();
});
