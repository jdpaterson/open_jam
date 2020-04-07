<template>
  <div>
    <h2>Moderator</h2>
    {{ jamName }}
    <button v-on:click="showStart">Start the Show!</button>
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
    showStart: function() {
      console.log(this.jamName);
    },
    publish: function() {
      this.opentokSession.publish(this.publisher, function(error) {
        if (error) {
          console.log(error);
        } else {
          console.log("Publishing a stream.");
        }
      });
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
    publisherSet: function() {
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
  props: ["jamName", "opentokSession", "currentUser"]
};
</script>

<style>
</style>
