<<<<<<< HEAD
$(() => {
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

    // console.log(checkedAmenities);
=======
let amenitiesChecked = {};
$(() => {
  $('input[type=checkbox]').click(function () {
    if (this.checked) {
      amenitiesChecked[this.dataset.id] = this.dataset.name;
    } else {
      delete amenitiesChecked[this.dataset.id];
    }
    $('.amenities h4').text(Object.values(amenitiesChecked).join(', '));
>>>>>>> cc2915ad9bec3ef385068c59ea0b45c2299ae4ba
  });
});
