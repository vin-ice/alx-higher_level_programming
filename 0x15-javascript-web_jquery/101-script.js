$(function() {
  const ls = $('UL.my_list');
  $('DIV#add_item').on('click', function() {
    ls.append('<li>Item</li>');
  });
  $('DIV#remove_item').on('click', function() {
    ls.find('li').last().remove();
  });
  $('DIV#clear_list').on('click', function() {
    ls.find('li').remove();
  });
});
