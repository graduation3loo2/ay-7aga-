/*global console, $, alert*/
function resizeIframe(){
  var iFrame = document.getElementById('myframe'),
      cont = iFrame.contentDocument,
      contHeight = cont.body.offsetHeight;

  iFrame.height = contHeight;
};

$(function () {

  'use strict';
  //////////////////////////////////////////////////////////////////////////////
  /*
    set the height of the background of header = the height of the window
    '.header' => for all the headers of the website except the home page
    '.home-header' => just the header of the home page only
  */
  $('.header').height($(window).height() - 225);
  $('.home-header').height($(window).height());
  //////////////////////////////////////////////////////////////////////////////
  /*
    centering the div('.head-title') vertical and horizontal
  */
  $('.header .head-title').css({
    marginTop: (($('.header').height() - $('.header .head-title').height()) / 2.5)
  });

  $('.header .head-title').css({
    marginLeft: (($('.header').width() - $('.header .head-title').width()) / 2)
  });
  //////////////////////////////////////////////////////////////////////////////
  /*
    set the height of the background of header = the height of the window in resize() function
    '.header' => for all the headers of the website except the home page
    '.home-header' => just the header of the home page only
  */
  $(window).resize(function () {

    $('.header').height($(window).height() - 200);
    $('.home-header').height($(window).height());

    $('.header .head-title').css({
      marginTop: (($('.header').height() - $('.header .head-title').height()) / 2.5)
    });

    $('.header .head-title').css({
      marginLeft: (($('.header').width() - $('.header .head-title').width()) / 2)
    });

  });
  //////////////////////////////////////////////////////////////////////////////
  // /*
  //   sliding up and down on clicking advanced search button
  // */
  // $('.adv-trigger').on('click', function () {
  //   $('.adv-search').slideToggle(800);
  //
  //   $('html, body').animate({
  //     scrollTop: (($('.head-title').offset().top) - 20)
  //   }, 800);
  // });
  //////////////////////////////////////////////////////////////////////////////
  /*
    changing the type of the input field from date to text when focuesd
    and reverse it when blured
  */
  $('.departure').focus(function () {
    $(this).attr('type', 'date');
  });

  $('.departure').blur(function () {
    $(this).attr('type', 'text');
  });
  //////////////////////////////////////////////////////////////////////////////
  /*
    switching follow button color with click in home page
  */
  if ($('.agency-card button').hasClass('followed')) {
    $(this).text('unfollow');
  } else if ($('.agency-card button').hasClass('')) {
    $(this).text('follow');
  }

  $('.agency-card button').on('click', function () {
    $(this).toggleClass('followed');

    if ($(this).hasClass('followed')) {
      $(this).text('unfollow');
    } else if ($(this).hasClass('')) {
      $(this).text('follow');
    }
  });
  /* this one for the button in the user-agency page */
  if ($('.tabs-panel .prof-intro button').hasClass('followed')) {
    $(this).text('unfollow');
  } else if ($('.tabs-panel .prof-intro button').hasClass('')) {
    $(this).text('follow');
  }

  $('.tabs-panel .prof-intro button').on('click', function () {
    $(this).toggleClass('followed');

    if ($(this).hasClass('followed')) {
      $(this).text('unfollow');
    } else if ($(this).hasClass('')) {
      $(this).text('follow');
    }
  });
  /* this one for the save button in the trip page */
  if ($('.trip-details .trip-actions #save-trip').hasClass('saved')) {
    $(this).text('unsave');
  } else if ($('.trip-details .trip-actions #save-trip').hasClass('')) {
    $(this).text('saved');
  }

  $('.trip-details .trip-actions #save-trip').on('click', function () {
    $(this).toggleClass('saved');

    if ($(this).hasClass('saved')) {
      $(this).text('unsave');
    } else if ($(this).hasClass('')) {
      $(this).text('saved');
    }
  });
  /* this one for the save button in the vote page */
  $('.trip-details .trip-actions button').on('click', function () {
    $(this).siblings().removeClass('voted');
    $(this).toggleClass('voted');
  });
  //////////////////////////////////////////////////////////////////////////////
  /*
    linking each tab with it's page in profile page
  */
  $('.prof-tabs button').on('click', function () {
    $(this).siblings().removeClass('active');
    $(this).addClass('active');

    $('#' + $(this).data('id')).siblings().fadeOut(500).removeClass('active');
    $('#' + $(this).data('id')).fadeIn(500).addClass('active');
  });
  //////////////////////////////////////////////////////////////////////////////
  /*
    linking each tab(history, saved) with it's page in my trips page
  */
  // $('.my-trips-tabs button').on('click', function () {
  //   $(this).siblings().removeClass('active');
  //   $(this).addClass('active');
  //
  //   $('#' + $(this).data('id')).siblings().fadeOut(500).removeClass('active');
  //   $('#' + $(this).data('id')).fadeIn(500).addClass('active');
  // });
  //////////////////////////////////////////////////////////////////////////////
  /*
    linking each tab with it's page in trip page
  */
  $('.trip-tabs div').on('click', function () {
    $(this).siblings().removeClass('active');
    $(this).addClass('active');

    $('#' + $(this).data('id')).siblings().fadeOut(500).removeClass('active');
    $('#' + $(this).data('id')).fadeIn(500).addClass('active');
  });
  //////////////////////////////////////////////////////////////////////////////
  /*
    Scroll To Top Button
  */
  $(window).on('scroll', function () {
    if ($(window).scrollTop() > 500) {
      $('.scroll-top').fadeIn(250);
    } else {
      $('.scroll-top').fadeOut(250);
    }
  });

  $('.scroll-top').click(function () {
    $('html, body').animate({
      scrollTop: 0
    }, 1000);
  });

  $('.scroll-top').hover(function () {
    $('.scroll-top span').animate({
      left: '8px',
      opacity: 1
    }, 250);
  }, function () {
    $('.scroll-top span').animate({
      left: '50%',
      opacity: 0
    }, 250);
  });
  //////////////////////////////////////////////////////////////////////////////
  /*
    the trigger of skitter (slider)
  */
  $('.skitter-large').skitter({
    interval: 3000,
    navigation: true,
    label: false,
    numbers: true,
    numbers_align: "right",
    dots: false,
    preview: true,
    thumbs: false,
    focus: true,
    controls: true
  });
  //////////////////////////////////////////////////////////////////////////////
  /*
    the trigger of niceScroll
  */
  $(function () {
    $("html").niceScroll({
      cursorcolor: '#0BB',
      cursorwidth: '8px',
      cursorborderradius: "3px"
    });
  });

});
