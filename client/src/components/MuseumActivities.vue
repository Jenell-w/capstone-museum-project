<template>
  <div class="hello">
    <h1>{{ title }}</h1>
    <h3>
      Please enter a fun activity you have completed (or attempted!) at a museum
    </h3>
    <br />
    <form class="activity-submission" @submit="handleSubmit">
      <p>
        <label for="museum-name">Which museum did you go to?</label>
        <select id="museum-name" v-model="museum" name="Select a museum">
          <option
            v-for="museum in museums"
            :key="museum.id"
            :value="museum.id"
            >{{ museum.museum_name }}</option
          >
        </select>
        <!-- change this to read v-for directly from the database w db id not my values -->
      </p>
      <p>
        <label for="activity-name">What fun activity did you do?</label>
        <input id="activity-name" v-model="activityName" />
      </p>
      <br />
      <p>
        <label for="activity-description"
          >Describe what you did and/or what you brought with you?</label
        >
        <textarea
          id="activity-description"
          v-model="activityDescription"
        ></textarea>
      </p>
      <br />
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
      <br />
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
    <hr />
    <section class="display-user-input">
      <p>Some user suggested activities:</p>
      <br />
      <hr />
      <div
        class="museum-activity"
        v-for="activity in activities"
        :key="activity.id"
        :viewAllActivities="viewAllActivities"
      >
        <p>Name of Activity: {{ activity.activity_name }}</p>
        <p>Description of activity: {{ activity.activity_descrip }}</p>
        <p>Oldest child:{{ activity.high_age_range }}</p>
        <p>Youngest child:{{ activity.low_age_range }}</p>
        <p>Number of children taken:{{ activity.num_kids_taken }}</p>

        <button @click="deleteActivity">Delete this activity</button>
      </div>

      <!-- how to delete item, need to tie the 
      activity id to the museum id- why is button showing up again?-->
    </section>
  </div>
</template>

<script>
import axios from "axios";
import ViewActivities from "./ViewActivities.vue";

export default {
  name: "MuseumActivities",
  props: ["title"],
  components: {
    ViewActivities
  },
  data() {
    return {
      activities: [],
      museums: [],
      museum: "",
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
        .then(() => this.viewAllActivities());
      this.museumName = ""; //clears out the fields for next use - ADD FIELDS
      this.confirmationSubmit = "Thanks for your response!";
    },
    viewAllActivities() {
      axios.get("/home").then(res => (this.activities = res.data.activities));
      console.log(this.activities);
    },
    museumList() {
      axios.get("/museum").then(res => {
        this.museums = res.data.museums;
        this.museum = this.museums[0].id;
        console.log("our museums are ", this.museums);
      });
    },
    deleteActivity() {
      axios
        .delete("/activity/" + this.activities.id)
        .then(() => this.viewAllActivities());
    },
    viewId() {
      console.log(this.activities.id);
    }
  },
  watch: {
    museum() {
      console.log(this.museum);
    }
  },
  mounted() {
    this.viewAllActivities();
    this.museumList();
    //the most recently entered activity will display at bottom.
  }
};
</script>

<style scoped>
.museum-activity {
  display: flex;
  padding: 2em;
  width: 100%;
  box-shadow: 0 3px 6px rgba(0, 0, 0, 0.16), 0 3px 6px rgba(0, 0, 0, 0.23);
}
</style>
