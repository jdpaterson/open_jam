import Vue from "vue";
import Root from "./components/Root.vue";
import Moderator from "./components/moderator/Moderator.vue";
import Publisher from "./components/Publisher.vue";
import Subscriber from "./components/Subscriber.vue";

window.Vue = Vue;
const app = new Vue({
  el: "#app",
  components: {
    Root,
    Moderator,
    Publisher,
    Subscriber,
  },
  delimiters: ["[[", "]]"],
});
