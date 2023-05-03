$(function () {
  const hello = $('DIV#hello');
  $.get("https://fourtonfish.com/hellosalut/?lang=fr", function(res) {
      hello.text(res.hello);
  });
});
