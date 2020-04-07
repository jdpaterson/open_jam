<template>
  <div id="root">
    <p>Root Jam: {{ jam.fields.name }}</p>
    <slot
      :jam-name="jam.fields.name"
      :opentok-session="opentokSession"
      :user-lists="userLists"
      :current-user="currentUser"
    />
    <!-- <button onClick="initPublisher()">Init Publisher</button>
    <button onClick="publish()">Publish</button>
    <button onClick="subscribeToStream()">Subscribe</button>-->
  </div>
</template>

<script>
import Moderator from "./Moderator.vue";
export default {
  components: {
    Moderator
  },
  data() {
    return {
      currentUser: {},
      jam: { fields: {} },
      opentokSession: {},
      opentokToken: "",
      userLists: {
        moderators: [],
        publishers: [],
        subscribers: []
      }
    };
  },
  methods: {
    sessionConnect: function() {
      this.opentokSession.connect(this.opentokToken);
    },
    sessionDisconnect: function() {
      this.opentokSession.disconnect();
    },
    sessionInit: function() {
      this.opentokSession.on({
        connectionCreated: function(event) {
          // TODO: Add the connection to the appropriate list (moderator/publisher/subscriber)
          console.log("Connection Created");
        },
        connectionDestroyed: function(event) {
          // TODO: Remove the connection from the appropriate list (moderator/publisher/subscriber)
          console.log("Connection Destroyed");
        },
        sessionDisconnected: function(event) {
          if (event.reason === "networkDisconnected") {
            console.log(
              "You lost your internet connection." +
                "Please check your connection and try connecting again."
            );
          }
        },
        streamCreated: function(event) {
          console.log("New stream in the session: " + event.stream.streamId);
          // session.subscribe(event.stream);
        }
      });
    }
  },
  mounted() {
    this.currentUser = currentUser;
    this.jam = jam;
    this.opentokSession = opentokSession;
    this.opentokToken = opentokToken;
    this.sessionInit();
  }
};
</script>

<style>
</style>