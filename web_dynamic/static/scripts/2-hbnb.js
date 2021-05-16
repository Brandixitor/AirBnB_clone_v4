// const host = 'localhost';
const host = '0.0.0.0';

const checkAmenities = function () {
  const checkedAmenities = {};
  let displayAmenities = [];
  $('.amenities .popover input').change(function () {
    if ($(this).prop('checked')) {
      checkedAmenities[$(this).attr('data-id')] = $(this).attr('data-name');
    } else if (!$(this).prop('checked')) {
      delete checkedAmenities[$(this).attr('data-id')];
    }
    displayAmenities = Object.values(checkedAmenities).sort();
    if (displayAmenities.length != 0)
      $('.amenities h4').text(displayAmenities.join(', '));
    else
      $('.amenities h4').html("&nbsp;");
  });
};

const checkApiStatus = function () {
  $.getJSON(`http://${host}:5001/api/v1/status`, (data) => {
    if (data.status === 'OK') {
      $('div#api_status').addClass('available');
    } else {
      $('div#api_status').removeClass('available');
    }
  });
};

$(() => {
  checkAmenities();
  checkApiStatus();
});
