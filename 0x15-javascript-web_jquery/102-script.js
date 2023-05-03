$(function () {
  const hello = $('DIV#hello');
  $('INPUT#btn_translate').on('click', function () {
    let lang = $('INPUT#language_code').val();
    $.get("https://fourtonfish.com/hellosalut/hello/", { lang: `${lang}` },
    function(res) { hello.text(res.hello); });
  });
});
