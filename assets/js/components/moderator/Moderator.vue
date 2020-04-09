<template>
  <div>
    <h2>Moderator</h2>
    {{ jam.fields.name }}
    <!-- <h3>The Publisher Thing</h3> -->
    <div id="publisher">
      <h2>Publisher Div</h2>
    </div>
    <h2>Publisher List</h2>
    <div id="publisherList">
      <ul>
        <li v-for="(publisher, index) in userLists.publishers" :key="index">{{ publisher.username }}</li>
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
  data: function() {
    return {
      publisher: {}
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
          style: {
            buttonDisplayMode: "on"
          }
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
    }
  },
  mounted() {
    this.publisher = this.publisherInit();
  },
  props: ["jam", "opentokSession", "currentUser", "userLists"]
};
</script>

<style>
</style>
