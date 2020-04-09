<template>
  <div id="root">
    <p>Root Jam: {{ jam.fields.name }}</p>
    <slot
      :jam="jam"
      :opentok-session="opentokSession"
      :user-lists="userLists"
      :current-user="currentUser"
    />
  </div>
</template>

<script>
import { Moderator } from "./moderator";
export default {
  components: {
    Moderator
  },
  data() {
    return {
      currentUser: { fields: {} },
      jam: { fields: {} },
      opentokSession: {},
      opentokToken: "",
      userLists: {
        moderators: [],
        publishers: [{ username: "1" }, { username: "3" }],
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
        connectionCreated: event => {
          console.log("Connection Created", JSON.parse(event.connection.data));
          if (JSON.parse(event.connection.data).role == "publisher") {
            this.userLists.publishers.push(JSON.parse(event.connection.data));
          }
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
    this.sessionConnect();
  }
};
</script>

<style>
</style>