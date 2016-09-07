$(document).ready(function () {
  $('.about').attr('id', 'about');
  $('.speakers').attr('id', 'speakers');
  $('.sponsors').attr('id', 'sponsors');
  $('.past').attr('id', 'past');
  $('.tickets').attr('id', 'tickets');
  $('.section-header').attr('id', 'go-top');

  if ($(document).scrollTop() == 0) {
    $('.go-top').fadeOut(200);
  }
});

$('.go-top').click(function () {
  $('html, body').animate({
    scrollTop: 0
  }, 500);
});
$('.menu-item').click(function (event) {
  event.preventDefault();

  $('body, html').animate({
    scrollTop: $($.attr(this, 'href')).offset().top
  }, 500);
});

$(window).scroll(function (e) {
  var arrow = $('.go-top');
  var duration = 200;
  if ($(document).scrollTop() > 0) {
    arrow.fadeIn(duration)
  } else {
    arrow.fadeOut(duration)
  }

});
