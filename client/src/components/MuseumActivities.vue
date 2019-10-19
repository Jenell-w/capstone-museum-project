<template>
  <div class="hello">
    <h1>{{ title }}</h1>
    <p>Brought to you by Jenell with assistance from Code Forward</p>
    <br />
    <form class="activity-submission" @submit.prevent="handleSubmit">
      <p>
        <label for="museum-name">Which museum did you go to?</label>
        <input
          id="museum-name"
          v-model="museumName"
          placeholder="Name of museum"
        />
        <!-- change museum input for a drop down with museum names already there -->
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
      <br />
      <p>
        <!-- <MuseumHome
          v-for="activity in activities"
          v-bind:key="activity.museum_id"
          :activity="activity"
          :viewAllActivities="viewAllActivities"
        />-->
      </p>
      <!-- above: child component to display the entered activities -->
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
      museumName: "",
      activityName: "",
      activityDescription: "",
      numberOfKids: "",
      lowAgeRange: "",
      highAgeRange: "",
      confirmationSubmit: false
      //can activities be on a child component page to display?  good idea.
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
    handleSubmit() {
      axios
        .post("/add-activity", {
          museum_name: this.museumName,
          activity_name: this.activityName,
          activity_description: this.activityDescription,
          number_of_kids_taken: this.numberOfKids,
          low_age_range_of_child_taken: this.lowAgeRange,
          high_age_range_of_child_taken: this.highAgeRange
        })
        .then(
          response => {
            console.log(response);
          },
          error => {
            console.log(error);
          }
        );
      this.museumName = ""; //clears out the field for next use
      this.confirmationSubmit = true;
    },
    viewAllActivities() {
      axios
        .get("/home")
        .then(res => (this.activities = res.data.activities))
        .catch(error => {
          console.log(error.response + " is this an error?");
        });
      /*this.activities is not correct? or data.activity.?
       */
    },
    confirmSubmit() {}
  },
  mounted() {
    this.viewAllActivities();
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
