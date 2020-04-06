<template>
  <div id="root">
    <p>Data:</p>
    <p>CurrentUser: {{currentUser}}</p>
    <p>Jam: {{jam}}</p>
    <p>Token: {{opentokToken}}</p>
    <button v-on:click="sessionConnect">Connect</button>
    <button v-on:click="sessionDisconnect">Disconnect</button>
    <!-- <button onClick="initPublisher()">Init Publisher</button>
    <button onClick="publish()">Publish</button>
    <button onClick="subscribeToStream()">Subscribe</button> -->
  </div>
</template>

<script>
export default {
  data(){
    return {
      currentUser: {},
      jam: {},
      opentokSession: {},
      opentokToken: "",
      moderators: [],
      publishers: [],
      subscribers: []
    }
  },
  methods: {
    sessionConnect: function(){
      this.opentokSession.connect(this.opentokToken);
    },
    sessionDisconnect: function(){
      this.opentokSession.disconnect();
    },
    sessionInit: function(){
      this.opentokSession.on({
        connectionCreated: function (event) {
          // TODO: Add the connection to the appropriate list (moderator/publisher/subscriber)
        },
        connectionDestroyed: function (event) {
          // TODO: Remove the connection from the appropriate list (moderator/publisher/subscriber)
        },
        sessionDisconnected: function(event) {
          if (event.reason === 'networkDisconnected') {
            console.log('You lost your internet connection.'
              + 'Please check your connection and try connecting again.');
          }
        },
        streamCreated: function (event) {
          console.log("New stream in the session: " + event.stream.streamId);
          // session.subscribe(event.stream);
        }
      });
    },
  },
  mounted(){
    this.currentUser = currentUser;
    this.jam = jam;
    this.opentokSession = opentokSession;
    this.opentokToken = opentokToken;
    this.sessionInit();
  }
}
</script>

<style>
</style>