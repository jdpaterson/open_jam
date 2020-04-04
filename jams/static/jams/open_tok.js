var session;
var connectionCount = 0;
function handleError(error) {
  if (error) {
    alert(error.message);
  }
}
function printJam(){
  console.log(jam);
}
function printCurrentUser(){
  console.log(currentUser);
}
function connect(){
  session = OT.initSession(apiKey, sessionId);
  session.on({
    connectionCreated: function (event) {
      connectionCount++;
      console.log(connectionCount + ' connections.');
    },
    connectionDestroyed: function (event) {
      connectionCount--;
      console.log(connectionCount + ' connections.');
    },
    sessionDisconnected: function(event) {
      if (event.reason === 'networkDisconnected') {
        console.log('You lost your internet connection.'
          + 'Please check your connection and try connecting again.');
      }
    },
    streamCreated: function (event) {
      console.log("New stream in the session: " + event.stream.streamId);
      session.subscribe(event.stream);
    }
  });
  session.connect(token, function(error) {
    if (error) {
      handleError(error);
    }else{
      console.log("Connected to session")
      // session.subscribe()
    }
  })
}

function printCapabilities(){
  if (session.capabilities.publish == 1) {
    // The client can publish. See the next section.
  } else {
    // The client cannot publish.
    // You may want to notify the user.
  }
}

function subscribeToStream(){
  session.on("streamCreated", function (event) {
    console.log("New stream in the session: " + event.stream.streamId);
    session.subscribe(event.stream);
  });
}

var publisher;
function initPublisher(){
  publisher = OT.initPublisher(
    'publisher',
    {
      name: currentUser.fields.username
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

function disconnect(){
  session.disconnect();
}

// function initializeSession() {
//   var session = OT.initSession(apiKey, sessionId);
//   // Subscribe to a newly created stream
//   session.on('streamCreated', function(event) {
//     session.subscribe(event.stream, 'subscriber', {
//       insertMode: 'append',
//       width: '100%',
//       height: '100%'
//     }, handleError);
//   });

//   // Create a publisher
//   var publisher = OT.initPublisher('publisher', {
//     insertMode: 'append',
//     width: '100%',
//     height: '100%'
//   }, handleError);

//   // Connect to the session
//   session.connect(token, function(error) {
//     // If the connection is successful, initialize a publisher and publish to the session
//     if (error) {
//       handleError(error);
//     } else {
//       session.publish(publisher, handleError);
//     }
//   });
// }

// Publisher Code
// var session;
// var publisher;

// // Replace with the replacement element ID:
// publisher = OT.initPublisher(replacementElementId);
// publisher.on({
//   streamCreated: function (event) {
//     console.log("Publisher started streaming.");
//   },
//   streamDestroyed: function (event) {
//     console.log("Publisher stopped streaming. Reason: "
//       + event.reason);
//   }
// });

// // Replace apiKey and sessionID with your own values:
// session = OT.initSession(apiKey, sessionID);
// // Replace token with your own value:
// session.connect(token, function (error) {
//   if (session.capabilities.publish == 1) {
//     session.publish(publisher);
//   } else {
//     console.log("You cannot publish an audio-video stream.");
//   }
// });