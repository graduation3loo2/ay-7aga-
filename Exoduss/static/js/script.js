/*global console, $*/

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
  $('.adv-trigger').on('click', function () {
    $('.adv-search').slideDown(800);

    $('html, body').animate({
        scrollTop: (($('.head-title').offset().top) - 20)
    }, 800);
  });
  //////////////////////////////////////////////////////////////////////////////
  /*
    changing the type of the input field from date to text when focuesd
    and reverse it when blured
  */
  $('.departure').focus(function () {
    $(this).attr('type', 'date')
  });

  $('.departure').blur(function () {
    $(this).attr('type', 'text')
  });
  //////////////////////////////////////////////////////////////////////////////
  /*
    linking each trip card with it's brief(extention)
  */
  $('.trip-card').on('click', function () {
    $(this).siblings().removeClass('active');
    $(this).addClass('active');

    $('#' + $(this).data('id')).siblings().fadeOut(500).removeClass('active');
    $('#' + $(this).data('id')).fadeIn(500).addClass('active');
  });
  //////////////////////////////////////////////////////////////////////////////
  /*
    linking each tab with it's page in profile page
  */
  $('.prof-tabs h3').on('click', function () {
    $(this).siblings().removeClass('active');
    $(this).addClass('active');

    $('#' + $(this).data('id')).siblings().fadeOut(500).removeClass('active');
    $('#' + $(this).data('id')).fadeIn(500).addClass('active');
  });
  //////////////////////////////////////////////////////////////////////////////
  /*
    linking each tab(history, saved) with it's page in my trips page
  */
  $('.my-trips-tabs button').on('click', function () {
    $(this).siblings().removeClass('active');
    $(this).addClass('active');

    $('#' + $(this).data('id')).siblings().fadeOut(500).removeClass('active');
    $('#' + $(this).data('id')).fadeIn(500).addClass('active');
  });
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
    edit the information of the account
  */
  $('.tab-details .user-info .fa-edit').one('click', function () {

    $('#' + $(this).data('id')).show(500).addClass('active').focus();
    $(this).siblings('h3').hide(500);
    $(this).attr('class', 'far fa-check-square');

    $('.tab-details .user-info .fa-check-square').one('click', function () {

      $(this).siblings('h3').text($('#' + $(this).data('id')).val());
      $('#' + $(this).data('id')).hide(500).removeClass('active');
      $(this).siblings('h3').show(500);

    });

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



});
