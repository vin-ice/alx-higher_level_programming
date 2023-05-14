$(function () {
  $.ajax({
    url: "https://fourtonfish.com/hellosalut/?lang=fr",
    success: function(res) { $("DIV#hello").text(res.hello); }
  });
});
