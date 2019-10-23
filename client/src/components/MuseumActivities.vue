<template>
  <div class="hello">
    <h1>{{ title }}</h1>
    <h3>
      Please enter a fun activity you have completed (or attempted!) at a museum
    </h3>
    <br />
    <form class="activity-submission" @submit.prevent="handleSubmit">
      <p>
        <label for="museum-name">Which museum did you go to?</label>
        <select id="museum-name" v-model="museumId" name="Select a museum">
          <option value="0">The Metropolitan Museum of Art, NYC</option>
          <option value="1">Museum of Fine Arts, Boston</option>
          <option value="2">Art Institute of Chicago</option>
          <option value="3">National Gallery of Art, Wash DC</option>
          <option value="4">Denver Art Museum</option>
        </select>
      </p>
      <p>
        <label for="activity-name">What fun activity did you do?</label>
        <input id="activity-name" v-model="activityName" />
      </p>
      <p>
        <label for="activity-description"
          >What did you bring with you for the children to do?</label
        >
        <textarea
          id="activity-description"
          v-model="activityDescription"
        ></textarea>
      </p>
      <p>
        <label for="number-of-kids">How many kids did you bring?</label>
        <select id="number-of-kids" v-model.number="numberOfKids">
          <option>0</option>
          <option>1</option>
          <option>2</option>
          <option>3</option>
          <option>4</option>
        </select>
      </p>
      <p>
        <label for="low-age-range"
          >Youngest child's age (Please select 0 if child is under 1):</label
        >
        <select id="low-age-range" v-model.number="lowAgeRange">
          <option>0</option>
          <option>1</option>
          <option>2</option>
          <option>3</option>
          <option>4</option>
          <option>5</option>
          <option>6</option>
          <option>7</option>
          <option>8</option>
          <option>9</option>
          <option>10</option>
          <option>11</option>
          <option>12</option>
        </select>
      </p>
      <p>
        <label for="high-age-range">Oldest child's age:</label>
        <select id="high-age-range" v-model.number="highAgeRange">
          <option>1</option>
          <option>2</option>
          <option>3</option>
          <option>4</option>
          <option>5</option>
          <option>6</option>
          <option>7</option>
          <option>8</option>
          <option>9</option>
          <option>10</option>
          <option>11</option>
          <option>12</option>
        </select>
      </p>
      <p>
        <input type="submit" value="Tell us about it!" />
      </p>
      <div class="submitted-message" v-if="confirmationSubmit">
        {{ confirmationSubmit }}
      </div>
    </form>
    <section class="display-user-input">
      <p>Some user suggested activities are here:</p>
    </section>
  </div>
</template>

<script>
import axios from "axios";
import MuseumHome from "./MuseumHome.vue";

export default {
  name: "MuseumActivities",
  props: ["title"],
  components: {
    MuseumHome
  },
  data() {
    return {
      activities: [],
      museumId: "",
      activityName: "",
      activityDescription: "",
      numberOfKids: "",
      lowAgeRange: "",
      highAgeRange: "",
      confirmationSubmit: ""
      //can activities be on a child component page to display?  good idea.
    };
  },
  methods: {
    onSubmit() {},
    handleSubmit() {
      axios
        .post("/add-activity", {
          museum_id: this.museumId,
          activity_name: this.activityName,
          activity_descrip: this.activityDescription,
          number_of_kids_taken: this.numberOfKids,
          low_age_range_of_child_taken: this.lowAgeRange,
          high_age_range_of_child_taken: this.highAgeRange
        })
        .then(response => {
          console.log(response);
          this.activities = response.config.data;
          console.log(response);
          //need to get this to display in some place!!!!!
        });
      this.museumName = ""; //clears out the fields for next use - ADD FIELDS
      this.confirmationSubmit = "Thanks for your response"; // revert to previos structure wuth error and response printing. argh!
    },
    viewAllActivities() {
      axios.get("/home").then(res => (this.activities = res.data.activities));
      // the data exists in config.data (json) so how can it display on page
    }
  },
  mounted() {
    this.viewAllActivities();
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
