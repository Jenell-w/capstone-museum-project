<template>
  <div class="art-generator">
    <button>Generate Some Interesting Artwork!</button>
    <br />
    <br />
    <!-- could the external api call be another component? -->

    <div class="museum-activities-container">
      <p v-bind="activity">{{ activity.museum_id }}</p>
      <br />
      <p>{{ activity.activity_name }}</p>
      <br />
      <p>{{ activity.activity_name }}</p>
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
        .delete("/add-activity/" + this.activity.museum_id)
        .then(() => this.viewAllActivities);
    }
  }
};
</script>

<style scoped>
.museum-activities-container {
  display: flex;
}
</style>
