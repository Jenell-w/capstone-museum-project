<template>
  <div class="hello">
    <h1>{{ title }}</h1>
    <p>Brought to you by Jenell with assistance from Code Forward</p>
    <ul>
      <li v-for="activity in activities">{{ activity }}</li>
    </ul>
  </div>
</template>

<script>
//import axios from "axios";

export default {
  name: "MuseumActivities",
  props: ["title"],
  data() {
    return {
      activities: ["a", "b", "c"]
    };
  },
  mounted() {
    console.log("mounted vue comppnent!");
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
