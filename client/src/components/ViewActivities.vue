<template>
  <div class="activity-list">
    <!-- <p>{{ activities.activity_descrip }}</p> -->
  </div>
</template>

<script>
import axios from "axios";
import ViewActivities from "./ViewActivities.vue";

export default {
  name: "ViewActivities",
  props: {
    activities: String
    // coming up as undefined - all info exists in the activities data in MuseumActivities
  },
  components: {
    ViewActivities
  },
  methods: {
    viewAllActivities() {
      axios.get("/home").then(res => (this.activities = res.config.data));
      console.log(this.activities);
      console.log("did this work?");
      // the data exists in config.data (json) so how can it display on page
    }
  },
  mounted() {
    this.viewAllActivities();
  }
};
</script>
