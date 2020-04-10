<template>
  <div>
    <h2>Moderator</h2>
    <h3>The Publisher Thing</h3>
    <div id="main-event">
      <h2>Publisher Div</h2>
    </div>
    <h2>Publisher List</h2>
    <div id="publisherList">
      <ul>
        <li v-for="(publisher, index) in userLists.publishers" :key="index">
          <!-- {{ publisher.data }} -->
          A Publisher
          <button v-on:click="signalPublisherStart(publisher)">
            Start as publisher
          </button>
        </li>
      </ul>
    </div>
    <div id="subscriberList">
      <!-- <li v-for="(subscriber, index) in userLists.subscribers" :key="index">{{ subscr.name }}</li> -->
    </div>
    <button v-on:click="publisherStart">Start the Show!</button>
    <button v-on:click="publisherEnd">Stop the Show!</button>
  </div>
</template>

<script>
export default {
  created() {
    this.dModerator = this.publisherInit();
  },
  data: function() {
    return {
      dModerator: {},
    };
  },
  methods: {
    publisherEnd: function() {
      this.publisher.destroy();
    },
    publisherInit: function() {
      return OT.initPublisher(
        "publisher",
        {
          name: this.currentUser.fields.username,
          showControls: true,
          style: {
            buttonDisplayMode: "on",
            nameDisplayMode: "on",
          },
        },
        function(error) {
          if (error) {
            // The client cannot publish.
            // You may want to notify the user.
          } else {
            console.log("Publisher initialized.");
          }
        }
      );
    },
    publisherStart: function() {
      this.opentokSession.publish(this.publisher, function(error) {
        if (error) {
          console.log(error);
        } else {
          console.log("Publishing a stream.");
        }
      });
    },
    signalPublisherStart: function(pubConnection) {
      this.opentokSession.signal(
        {
          to: pubConnection,
          data: JSON.parse(pubConnection.data).username,
          type: "PUBSTART",
        },
        function(error) {
          if (error) {
            console.log("signal error (" + error.name + "): " + error.message);
          } else {
            console.log("signal sent.");
          }
        }
      );
    },
  },
  props: ["jam", "opentokSession", "currentUser", "userLists"],
};
</script>

<style></style>
