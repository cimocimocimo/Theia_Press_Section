window.timber = window.timber || {};

window.pageData = window.pageData || {};

window.shopData = window.shopData || {isLoaded: false};

timber.cache = {
    // General
    $window: $(window),
    $html: $('html'),
    $body: $('body'),

    // Navigation
    $navigation: $('#accessibleNav'),
    $customerMenu: $('.customer-menu'),

    $cartCount: $('#cartCount'),

    // Mobile Slide Out Navigation
    mobileSideNav: {
        $bodyContainer: $('#body-container'),
        $headerContainer: $('#header-container'),
        $bothContainers: $('#body-container, #header-container'),
        $toggle: $('#sideNavToggle'),
        $nav: $( '#mobileSideNav' ),
        $subMenuLinks: $('.main-menu-link.js-has-sub-menu'),
        $subMenus: $('.sub-menu-mobile')
    }
};

timber.init = function () {

    // Run on load
    timber.accessibleNav();
    timber.mobileSideNav();
    timber.headerSubNav();

    // initialize smooth scroll
    smoothScroll.init();

    timber.loader.init();

    // cart count link
    timber.initCartCount();

    timber.infiniteScrollInit();

    timber.loadShopifyData();

    // wire events
    $(window).on('shopDataLoaded', function(event){
        console.log(event);
        timber.setCustomerMenuData()
    });
};

timber.setCustomerMenuData = function(){
    var $menu = timber.cache.$customerMenu,
        $loginLink = $menu.find('.customer-login-link'),
        customer = shopData.customer;

// avatarImageAlt:
// avatarImageSrc:
// customerFullName:

    $loginLink.text(sprintf('%s %s', customer.firstName, customer.lastName));
    console.log(customer);
};

timber.loadShopifyData = function(){
    var allowedDomains = [
        'http://www.theiacouture.com',
        'http://theiacouture.com',
        'http://theia.myshopify.com',
        'http://theia2.myshopify.com',
    ];

    // when the iframe finishes loading send a message to trigger it to
    // send back the customer info.
    $('#data-iframe').on('load', function(){
        this.contentWindow.postMessage('', '*');
    });

    $(window).on('message', function(event){
        allowedDomainIndex = $.inArray(event.originalEvent.origin, allowedDomains);
        if (allowedDomainIndex !== -1){
            shopData = JSON.parse(event.originalEvent.data);
            shopData.isLoaded = true;
            $(window).trigger('shopDataLoaded');
        }
    });
};

timber.initCartCount = function(){
    var $cartCount = timber.cache.$cartCount,
        count = 0;

    updateCartCountElement();
    getCartCount();

    function getCartCount(){
        // http://stackoverflow.com/questions/10346201/how-to-show-shopify-cart-values-on-pages-on-website-outside-of-shopify-website
        $.ajax({
            url: "//theia.myshopify.com/cart.json",
            dataType: "jsonp",
            success: getCartCountCallback,
            error: function( jxhr, status, err ) {
                console.log("Error, status = " + status + ", err = " + err);
            }
        });
    }

    function getCartCountCallback(data){
        // store the cart count in a closure
        count = data.item_count;

        // update the cartCount element
        updateCartCountElement();
    }

    function updateCartCountElement(){
        $cartCount.text(count);
        if (count > 0){
            $cartCount.addClass('positive-count');
        } else {
            $cartCount.removeClass('positive-count');
        }
    }
};

timber.getUrlVars = function () {
    var result = {};
    var location = window.location.href.split('#');
    var parts = location[0].replace(/[?&]+([^=&]+)=([^&]*)/gi, function(m,key,value) {
        result [key] = value;
    });
    return result ;
};

timber.mobileSideNav = function(){
    var $body = timber.cache.$body,
        $bodyContainer = timber.cache.mobileSideNav.$bodyContainer,
        $headerContainer = timber.cache.mobileSideNav.$headerContainer,
        $bothContainers = timber.cache.mobileSideNav.$bothContainers,
        $toggle = timber.cache.mobileSideNav.$toggle,
        $nav = timber.cache.mobileSideNav.$nav,
        $subMenuLinks = timber.cache.mobileSideNav.$subMenuLinks,
        $subMenus = timber.cache.mobileSideNav.$subMenus,
        isOpen = false;

    $toggle.click(function(e) {
        e.preventDefault();
        e.stopPropagation();

        if (isOpen){
            timber.mobileSideNav.close();
        } else {
            timber.mobileSideNav.open();
        }
    });

    // close the side menu when user clicks on the body or the header when open.
    $bothContainers.click(function(e){
        if ( isOpen ){
            timber.mobileSideNav.close();
        }
    });

    this.mobileSideNav.open = function(){
        $bothContainers.addClass( 'menu-open' );
        $body.addClass('js-no-scroll');
        $nav.addClass( 'open' );
        isOpen = true;
    };

    this.mobileSideNav.close = function(){
        $bothContainers.removeClass( 'menu-open' );
        $body.removeClass('js-no-scroll');
        $nav.removeClass( 'open' );
        isOpen = false;
    };

    // side nav sub menus
    //

    return;

    // get the natural hight of the sub menus to allow for the transition animations to work.

    // open the submenus.
    openSubMenus();
    $subMenus.each(function(i){
        var $currMenu = $(this),
            height = $currMenu.height();

        $currMenu.attr('data-height', height);
    });
    closeSubMenus();

    $subMenuLinks.click(function(event){
        event.preventDefault();

        // get the target name, format the id, get the element
        var $this = $(this),
            target = $this.data('target'),
            targetIdSelector = '#sub-menu-mobile-' + target,
            $targetMenu = $(targetIdSelector);

        if (isSubMenuOpen($targetMenu)){
            // close the menu and any others
            closeSubMenus();
        } else {
            // close any menus and open the menu
            closeSubMenus();
            openSubMenu($this, $targetMenu);
        }
    });

    function isSubMenuOpen($menu){
        return $menu.hasClass('js-open');
    }

    function closeSubMenus(){
        $subMenuLinks.removeClass('active');
        $subMenus.removeClass('js-open');
        $subMenus.css('height', 0);
    }

    function openSubMenu($link, $subMenu){
        $subMenu.addClass('js-open');
        $subMenu.css('height', $subMenu.data('height'));
        $link.addClass('active');
    }

    function openSubMenus(){
        $subMenuLinks.addClass('active');
        $subMenus.addClass('js-open');
    }
};

timber.headerSubNav = function(){

    // debug
    return;

    // get elements
    var $subNavRow = timber.cache.headerSubNav.$row,
        $subMenus = timber.cache.headerSubNav.$subMenus,
        $availableOnlineSubMenu = $('#sub-menu-desktop-available-online'),
        $exclusiveSubMenu = $('#sub-menu-desktop-exclusive'),
        $mainMenu = timber.cache.headerSubNav.$mainMenu,
        $subMenuLinks = $mainMenu.find('#available-online-header-main-menu-link, #exclusive-header-main-menu-link'),
        $shopLink = $mainMenu.find('#available-online-header-main-menu-link'),
        $collectionsLink = $mainMenu.find('#exclusive-header-main-menu-link'),
        menuClosetimeoutId;

    // set the sub menu left offset to be the same as the link
    function setMenuHorizontalPositions(){
        var shopLinkLeftOffset = $shopLink.offset().left,
            collectionsLinkLeftOffset = $collectionsLink.offset().left;

        $availableOnlineSubMenu.css('left', shopLinkLeftOffset);
        $exclusiveSubMenu.css('left', collectionsLinkLeftOffset);
    }
    setMenuHorizontalPositions();

    // and set them anytime the window is resized.
    $(window).resize(function(event){
        setMenuHorizontalPositions();
    });

    // when the user mouses over a sub menu link
    $subMenuLinks.mouseenter(function(event){

        // get the target name, format the id, get the element
        var $this = $(this),
            target = $this.data('target'),
            targetIdSelector = '#sub-menu-desktop-' + target,
            $targetMenu = $(targetIdSelector);

        // if another menu is open
        if ($subMenus.hasClass('js-open') && !$targetMenu.hasClass('js-open')){
            $subMenus.removeClass('js-open');
            $subMenuLinks.removeClass('active');
            $targetMenu.addClass('js-open');
            $this.addClass('active');

        } else if (!$subMenus.hasClass('js-open')) {
            // no menus are open, so open the target
            $targetMenu.addClass('js-open');
            $this.addClass('active');
        }
    });

    // when the user mouses away from the main nav or the open sub nav menu start a timeout
    // when the time out finishes
    $mainMenu.mouseleave(function(event){
        menuClosetimeoutId = window.setTimeout(closeSubMenus, 600);
    });
    $subMenus.mouseleave(function(event){
        menuClosetimeoutId = window.setTimeout(closeSubMenus, 600);
    });
    $mainMenu.mouseenter(function(event){
        window.clearTimeout(menuClosetimeoutId);
    });
    $subMenus.mouseenter(function(event){
        window.clearTimeout(menuClosetimeoutId);
    });

    function closeSubMenus(){
        $subMenus.removeClass('js-open');
        $subMenuLinks.removeClass('active');
    }
};

timber.accessibleNav = function () {
    var $nav = timber.cache.$navigation,
        $allLinks = $nav.find('a'),
        $topLevel = $nav.children('li').find('a'),
        $parents = $nav.find('.site-nav--has-dropdown'),
        $subMenuLinks = $nav.find('.site-nav--dropdown').find('a'),
        activeClass = 'nav-hover',
        focusClass = 'nav-focus';

    // Mouseenter
    $parents.on('mouseenter touchstart', function(evt) {
        var $el = $(this);

        if (!$el.hasClass(activeClass)) {
            evt.preventDefault();
        }

        showDropdown($el);
    });

    // Mouseout
    $parents.on('mouseleave', function() {
        hideDropdown($(this));
    });

    $subMenuLinks.on('touchstart', function(evt) {
        // Prevent touchstart on body from firing instead of link
        evt.stopImmediatePropagation();
    });

    $allLinks.focus(function() {
        handleFocus($(this));
    });

    $allLinks.blur(function() {
        removeFocus($topLevel);
    });

    // accessibleNav private methods
    function handleFocus ($el) {
        var $subMenu = $el.next('ul');
        hasSubMenu = $subMenu.hasClass('sub-nav') ? true : false,
        isSubItem = $('.site-nav--dropdown').has($el).length,
        $newFocus = null;

        // Add focus class for top level items, or keep menu shown
        if ( !isSubItem ) {
            removeFocus($topLevel);
            addFocus($el);
        } else {
            $newFocus = $el.closest('.site-nav--has-dropdown').find('a');
            addFocus($newFocus);
        }
    }

    function showDropdown ($el) {
        $el.addClass(activeClass);

        setTimeout(function() {
            timber.cache.$body.on('touchstart', function() {
                hideDropdown($el);
            });
        }, 250);
    }

    function hideDropdown ($el) {
        $el.removeClass(activeClass);
        timber.cache.$body.off('touchstart');
    }

    function addFocus ($el) {
        $el.addClass(focusClass);
    }

    function removeFocus ($el) {
        $el.removeClass(focusClass);
    }
};

timber.infiniteScrollInit = function(){

    // we should only have one infinite scrolling block per page
    var $infiniteScrollBlock = $('[data-infinite-scroll]').first(),
        isRequestActive = false, // prevent repeated ajax calls
        hasNextPage = $infiniteScrollBlock.attr('data-has-next-page') === 'true',
        nextPageUrl = '',
        $paginationBlock = $('.pagination-block');

    if ($infiniteScrollBlock.length === 0){
        return;
    }

    $paginationBlock.addClass('js-hidden');

    if (hasNextPage){
        var waypointTrigger = new Waypoint({
            element: $infiniteScrollBlock[0],
            handler: waypointCallback,
            offset: 'bottom-in-view'
        });

        nextPageUrl = $infiniteScrollBlock.attr('data-next-page-url');

    } else {
        nextPageUrl = '';
    }

    function waypointCallback(direction){
        if (!isRequestActive && direction === 'down' && hasNextPage){
            getNextPage();
        }
    }

    function getNextPage(){
        isRequestActive = true;
        $.ajax({
            type: 'GET',
            url: nextPageUrl,
            dataType: 'html',
            beforeSend: showLoader,
            success: loadPage
        });
    }

    function loadPage(response){
        var $responseBlock = $(response).find('[data-infinite-scroll]'),
            pageHtml = $responseBlock.html();

        // add the page to the rest of the pages
        $infiniteScrollBlock.append(pageHtml);

        hasNextPage = $responseBlock.attr('data-has-next-page') === 'true';
        nextPageUrl = '';

        if (hasNextPage){
            // refresh the position of the waypoint
            waypointTrigger.context.refresh();
            nextPageUrl = $responseBlock.attr('data-next-page-url');
        } else {
            // no more pages, destroy the waypoint
            waypointTrigger.destroy();
        }

        hideLoader();
        isRequestActive = false;
    }

    function showLoader(){
        console.log('showing loader');

        timber.loader.show('.spinner-block');
    }

    function hideLoader(){
        console.log('hiding loader');

        timber.loader.hide('.spinner-block');
    }
};

// this is a callback for the google api loader on the event detail page.
timber.initEventMap = function() {
    var latLngArr = window.pageData.eventDetail.latLngArray,
        latLng = {
            lat: parseFloat(latLngArr[0]),
            lng: parseFloat(latLngArr[1])
        },
        map = new google.maps.Map(document.getElementById('location-map'), {
            zoom: 14,
            center: latLng,
            scrollwheel: false,
            draggable: false,
            disableDefaultUI: true
        }),
        marker = new google.maps.Marker({
            position: latLng,
            map: map,
            title: 'event location'
        });
}


timber.loader = {
    element: '',
    selector: '.spinner',

    init: function(){
        // get loader template
        timber.loader.element = $('#loaderAnimationTemplate').html();
    },

    show: function( target ){
        // append the loader element to the target element and show it

        if ( typeof target === 'undefined' ) {
            return;
        }

        var $target = $(target),
            $spinner = $target.find(timber.loader.selector);

        if ($spinner.length > 0){
            $spinner.removeClass('js-hidden');
        } else {
            $target.append( timber.loader.element );
        }
    },

    hide: function( target ){
        // hide the loader element in the target

        if ( typeof target === 'undefined' ) {
            return;
        }

        var $target = $(target),
            $spinner = $target.find(timber.loader.selector);

        $spinner.addClass('js-hidden');
    },

    destroy: function( target ){
        if( typeof target === 'undefined' ){
            // no target element, hide and destroy all loader animations
            return;
        }

        // hide and destroy the loader in the target element
        $( target ).remove();
    }
};

// Initialize Timber's JS on docready
$(function() {
    window.timber.init();
});
