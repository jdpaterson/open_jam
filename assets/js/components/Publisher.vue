<template>
  <div>
    <p>Publisher</p>
  </div>
</template>

<script>
export default {
  created() {},
  data: function() {
    return {
      dPublisher: this.publisherInit(),
    };
  },
  methods: {
    initPublisherSession: function() {
      this.opentokSession.on({
        signal: (event) => {
          console.log("Signal Event: ", event);
          const { data, type } = event;
          if (
            type == "signal:PUBSTART" &&
            data == this.currentUser.fields.username
          ) {
            this.publisherStart();
          }
        },
      });
    },
    publisherEnd: function() {
      this.publisher.destroy();
    },
    publisherInit: function() {
      return OT.initPublisher(
        "publisher",
        {
          name: this.currentUser.fields.username,
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
      this.opentokSession.publish(this.dPublisher, function(error) {
        if (error) {
          console.log(error);
        } else {
          console.log("Publishing a stream.");
        }
      });
    },
  },
  mounted() {
    this.initPublisherSession();
    // console.log("PUB:", this.currentUser);
    // this.initPublisherSession(this.openTokSession);
    // this.publisher = this.publisherInit();
  },
  props: ["jam", "opentokSession", "currentUser"],
};
</script>

<style></style>
