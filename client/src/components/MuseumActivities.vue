<template>
  <div class="hello">
    <h1>{{ title }}</h1>
    <p>Brought to you by Jenell with assistance from Code Forward</p>
    <br />
    <form class="activity-submission" @submit.prevent="onSubmit">
      <p>
        <label for="museum-name">Which museum did you go to?</label>
        <input
          id="museum-name"
          v-model="museumName"
          placeholder="Name of museum"
        />
      </p>
      <p>
        <label for="activity-description">
          What fun activity did you do? What did you bring with you for the
          children to do?
        </label>
        <textarea
          id="activity-description"
          v-model="activityDescription"
        ></textarea>
      </p>
      <p>
        <label for="low-age-range">Youngest child's age:</label>
        <select id="low-age-range" v-model.number="lowAgeRange">
          <option>0</option>
          <option>1</option>
          <option>2</option>
        </select>
      </p>
      <p>
        <label for="high-age-range">Oldest child's age:</label>
        <select id="high-age-range" v-model.number="highAgeRange">
          <option>8</option>
          <option>9</option>
          <option>10</option>
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
      <br />
      <p v-for="activity in activities" v-bind:key="activity.id">
        {{ activity }}
      </p>
      <br />
      <p></p>
      <br />
      <p></p>
      <br />
    </section>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "MuseumActivities",
  props: ["title"],
  data() {
    return {
      activities: [],
      museumName: null,
      activityDescription: null,
      lowAgeRange: null,
      highAgeRange: null,
      confirmationSubmit: "We have recorded your response"
      //need to determine how many inputs i will get? to add to db?
    };
  },
  methods: {
    onSubmit() {
      let museumActivity = {
        museumName: this.museumName,
        activityDescription: this.activityDescription,
        lowAgeRange: this.lowAgeRange,
        highAgeRange: this.highAgeRange
      };
      this.$emit("information-submitted", museumActivity);
      this.museumName = null;
      this.activityDescription = null;
      this.lowAgeRange = null;
      this.highAgeRange = null;
    },
    viewAllActivities() {
      axios
        .get("/home")
        .then(res => (this.activities = res.data.activities))
        .catch(error => {
          console.log(error.response + "did we do it?");
        }); //this call is failing, getting a 404 not found!
      /*this.activities is not correct? or data.activity.?
       */
    },
    confirmSubmit() {
      let confirmationSubmit = true; //to display 'thank you for submitting' message.
    }
  },
  mounted() {
    this.viewAllActivities();
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
