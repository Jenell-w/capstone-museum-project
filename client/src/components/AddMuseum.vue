<template>
  <div class="add">
    <div class="add-museum-container">
      <br />
      <button @click="addNewMuseum">Add a New Museum You visited!</button>
      <!-- add the api to generate random art and then we can use that route to museums -->
    </div>
  </div>
</template>

<script>
//import axios from "axios";

export default {
  name: "AddMuseum",
  props: [],
  data() {
    return {
      museum_name: ""
    };
  },
  methods: {
    addNewMuseum() {}
  }
};
</script>

<style scoped></style>
