$(function () {
  const hello = $('DIV#hello');
  $('INPUT#btn_translate').on('click', translate);
  $("INPUT#language_code").on("keypress", function(eve) {
      if (eve.which === 13) translate();
  });
});
function translate() {
  let lang = $('INPUT#language_code').val();
  $.get("https://fourtonfish.com/hellosalut/hello/", { lang: `${lang}` },
  function(res) { hello.text(res.hello); });
}