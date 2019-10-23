<template>
  <div class="art-generator">
    <!-- how to make this button only appear when on this page? -->
    <button>Generate Some Interesting Artwork!</button>
    <br />
    <br />
    <!-- could the external api call be another component? -->

    <div class="museum-activities-container">
      <br />
      <button @click="deleteActivity">Delete this entry</button>
      <!-- add the api to generate random art and then we can use that route to museums -->
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "MuseumHome",
  props: ["activities", "viewAllActivities"],
  methods: {
    deleteActivity() {
      axios
        .delete("/add-activity/" + this.new_activity.id)
        .then(() => this.viewAllActivities);
      // write route with PATCH method in MusAPI.py.  see Phil's patch
    }
  }
};
</script>

<style scoped>
.museum-activities-container {
  display: flex;
}
</style>
