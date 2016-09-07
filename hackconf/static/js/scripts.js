'use strict';

(function () {
  $(document).foundation();

  // Google map
  google.maps.event.addDomListener(window, 'load', init);

  var map;
  var brooklyn = new google.maps.LatLng(42.6847251, 23.3189384);
  var MY_MAPTYPE_ID = 'custom_style';
  function init() {
    var featureOpts = [{
      stylers: [{ saturation: -20 }, { lightness: 40 }, { visibility: 'simplified' }, { gamma: 0.8 }, { weight: 0.4 }]
    }, {
        elementType: 'labels',
        stylers: [{ visibility: 'on' }]
      }, {
        featureType: 'water',
        stylers: [{ color: '#dee8ff' }]
      }];
    var mapOptions = {
      zoom: 16,
      scrollwheel: false,
      panControl: false,
      mapTypeControl: false,
      streetViewControl: false,
      center: new google.maps.LatLng(42.6847251, 23.3189384),
      mapTypeControlOptions: {
        mapTypeIds: [google.maps.MapTypeId.ROADMAP, MY_MAPTYPE_ID]
      },
      mapTypeId: MY_MAPTYPE_ID
    };
    map = new google.maps.Map(document.getElementById('map'), mapOptions);
    var image = '/static/images/pmarker.png';
    var myLatLng = new google.maps.LatLng(42.6847251, 23.3189384);
    var beachMarker = new google.maps.Marker({
      position: myLatLng,
      map: map,
      icon: image
    });
    var styledMapOptions = {
      name: 'Custom Style'
    };
    var customMapType = new google.maps.StyledMapType(featureOpts, styledMapOptions);
    map.mapTypes.set(MY_MAPTYPE_ID, customMapType);
  }
})();
//# sourceMappingURL=scripts.js.map
