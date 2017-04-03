$(document).ready(function () {
  $('.about').attr('id', 'about');
  $('.call-for-speakers').attr('id', 'call-for-speakers');
  $('.program').attr('id', 'program');
  $('.lecturers').attr('id', 'lecturers');
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

$(".language-bar div").click(function(){
  var lang = $(this).attr("ref");
  var url = window.location.pathname.split(window.location.hostname);

  // remove the previous lang
  url.shift();

  var path = location.origin + "/" + lang + "/" + url.join("/");
  location.href = path;
});
