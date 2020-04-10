<template>
  <div id="root">
    <slot
      :jam="dJam"
      :opentok-session="dOpentokSession"
      :user-lists="dUserLists"
      :current-user="dCurrentUser"
    />
  </div>
</template>

<script>
import { Moderator } from "./moderator";
export default {
  created() {
    this.dOpentokSession = OT.initSession(
      this.apiKey,
      this.dJam.fields.opentok_session_id
    );
    this.sessionConnect();
  },
  components: {
    Moderator,
  },
  data() {
    return {
      dCurrentUser: JSON.parse(this.currentUser)[0],
      dJam: JSON.parse(this.jam)[0],
      dOpentokSession: {},
      dUserLists: {
        moderators: [],
        publishers: [],
        subscribers: [],
      },
    };
  },
  methods: {
    sessionConnect: function() {
      this.dOpentokSession.connect(this.opentokToken);
    },
    sessionDisconnect: function() {
      this.dOpentokSession.disconnect();
    },
    sessionInit: function() {
      this.dOpentokSession.on({
        connectionCreated: (event) => {
          console.log("Connection Created", JSON.parse(event.connection.data));
          if (JSON.parse(event.connection.data).role == "publisher") {
            this.dUserLists.publishers.push(event.connection);
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
        streamCreated: (event) => {
          console.log("New stream in the session: ", event);
          const connectionData = JSON.parse(event.stream.connection.data);
          console.log("NAME: ", connectionData.name);
          this.dOpentokSession.subscribe(event.stream, "main-event");
        },
      });
    },
  },
  mounted() {
    this.sessionInit();
  },
  props: ["api-key", "currentUser", "jam", "opentokToken"],
};
</script>

<style></style>
