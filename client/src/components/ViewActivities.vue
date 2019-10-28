<template>
  <div class="delete-activity-container">
    <button @click="deleteActivity">Delete this activity</button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ViewActivities",
  props: ["activities", "activity"],
  methods: {
    deleteActivity() {
      axios
        .delete("/activity/" + this.activity.id)
        .then(() => this.viewAllActivities());
    }
  }
};
</script>
<style scoped>
.delete-activity-container {
  font: red;
}
</style>
