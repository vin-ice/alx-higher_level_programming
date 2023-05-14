$(function () {
  $('INPUT#btn_translate').on('click', translate);
  $("INPUT#language_code").on("keypress", function(eve) {
      if (eve.which === 13) translate();
  });
});
function translate() {
  let lang = $('INPUT#language_code').val().toLowerCase();
  $.get(`https://fourtonfish.com/hellosalut/hello/${lang}`,
  function(res) { $('DIV#hello').text(res.hello); });
}