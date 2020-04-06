<template>
    <div>
        <p>Data:</p>
        <p>{{currentUser}}</p>
        <p>{{jam}}</p>
        <p>{{opentokApiKey}}</p>
        <p>{{opentokSessionId}}</p>
        <p>{{opentokToken}}</p>

    </div>
</template>

<script>
export default {
  data(){
    return {
      currentUser: {},
      jam: {},
      opentokApiKey: "",
      opentokSessionId: "",
      opentokToken: "",
    }
  },
  mounted(){
    this.currentUser = currentUser;
    this.jam = jam;
    this.opentokApiKey = opentokApiKey;
    this.opentokSessionId = opentokSessionId;
    this.opentokToken = opentokToken;
  },
  props: ['apiKey']
}
</script>

<style>
</style>