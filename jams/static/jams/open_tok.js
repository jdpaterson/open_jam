var publisher;
function initPublisher(){
  publisher = OT.initPublisher(
    'publisher',
    {
      name: currentUser.fields.username,
      style: {
        buttonDisplayMode: 'off'
      }
    },
    function(error) {
      if (error) {
        // The client cannot publish.
        // You may want to notify the user.
      } else {
        console.log('Publisher initialized.');
      }
    }
  );
}

function publish(){
  session.publish(publisher, function(error) {
    if (error) {
      console.log(error);
    } else {
      console.log('Publishing a stream.');
    }
  });
  publisher.on('streamCreated', function (event) {
    console.log('The publisher started streaming.');
  });
}