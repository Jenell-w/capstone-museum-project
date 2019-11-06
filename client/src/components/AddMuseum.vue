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
      </ul>
      <input type="submit" value="Add a Museum you visited" />
    </form>
    {{ message }}
    <!-- add the api to generate random art and then we can use that route to museums -->
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
  background: #fafafa;
  padding: 10px;
  margin: 50px auto;
  box-shadow: 1px 1px 25px rgba(0, 0, 0, 0.35);
  border-radius: 10px;
  border: 6px solid #305a72;
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
</style>
