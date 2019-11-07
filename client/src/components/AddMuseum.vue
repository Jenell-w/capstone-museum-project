<template>
  <div class="add-museum-container">
    <br />
    <form class="museum-submission" @submit="addNewMuseum">
      <ul>
        <li>
          <label for="museum-name">Museum Name:</label>
          <input id="museum-name" v-model="museumName" />
        </li>
        <li>
          <label for="museum-city">Museum City:</label>
          <input id="museum-city" v-model="museumCity" />
        </li>
        <li>
          <button type="submit">Add a Museum you visited</button>
        </li>
      </ul>
    </form>
    {{ message }}
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "AddMuseum",
  props: ["museums", "museum"],
  data() {
    return {
      museumName: "",
      museumCity: "",
      message: ""
    };
  },
  methods: {
    addNewMuseum() {
      axios.post("/add-museum", {
        museum_name: this.museumName,
        museum_city: this.museumCity
      });
      this.message = "Thanks for adding a museum!";
    }
  }
};
</script>

<style scoped>
.museum-submission {
  max-width: 350px;
  background: darkgrey;
  padding: 10px;
  margin: 50px auto;
  box-shadow: 1px 1px 25px rgba(0, 0, 0, 0.35);
  border-radius: 10px;
  border: 6px solid #305a72;
  font: normal 18px/1.5 "Fira Sans", "Helvetica Neue", sans-serif;
  font-weight: 300;
  letter-spacing: 0.09em;
  text-transform: uppercase;
}
.museum-submission ul {
  padding: 0;
  margin: 0;
  list-style: none;
}
.museum-submission ul li {
  display: block;
  margin-bottom: 10px;
  min-height: 35px;
}
li button {
  margin-left: auto;
  padding: 8px 16px;
  border: none;
  background: #333;
  color: #f2f2f2;
  text-transform: uppercase;
  letter-spacing: 0.09em;
  border-radius: 2px;
}
</style>
