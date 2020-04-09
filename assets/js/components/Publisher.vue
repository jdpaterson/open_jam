<template>
  <div>
    <p>Publisher</p>
  </div>
</template>

<script>
export default {
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
  props: ["jam", "opentokSession", "currentUser"]
};
</script>

<style>
</style>