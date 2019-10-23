<template>
  <div class="activity-list">
    <ul></ul>
    <div class="museum-activities-container">
      <br />
      <button @click="deleteActivity">Delete this entry</button>
    </div>
  </div>
</template>

<script>
// should the viewALLActivities function go here to display here or will it
// be imported from another function.
//import axios from "axios";

export default {
  name: "MuseumHome",
  props: ["activities", "viewAllActivities"]
};
</script>
