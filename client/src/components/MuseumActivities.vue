<template>
  <div class="hello">
    <h1>{{ title }}</h1>
    <h2>
      Visting an art museum can be kid-friendly: let us show you how!
      <br />Here is something you can do at the museum with your children before
      you visit.
    </h2>
    <MuseumHome />
    <h3>
      Please enter a fun activity you have completed (or attempted!) at a museum
      with your children!
    </h3>
    <br />
    <!-- <div class="container"> -->
    <form class="activity-submission" @submit="handleSubmit">
      <ul class="flex-outer">
        <li>
          <label for="museum-name"
            >Select the museum you visited: (or, add a new museum below!)</label
          >

          <!-- select drop down reads from museum_info table in db -->
          <select id="museum-name" v-model="museum" name="Select a museum">
            <option
              v-for="museum in museums"
              :key="museum.id"
              :value="museum.id"
              >{{ museum.museum_name }}</option
            >
          </select>
        </li>
        <div class="show-add-museum">
          <!-- 
          would be nice to load this component on click of button!!-->
          <AddMuseum />
        </div>
        <li>
          <label for="activity-name">What fun activity did you do?</label>
          <input id="activity-name" v-model="activityName" />
        </li>
        <li>
          <label for="activity-description">Describe the activity:</label>
          <textarea
            rows="6"
            placeholder="What did you bring? What did you do?"
            id="activity-description"
            v-model="activityDescription"
          ></textarea>
        </li>
        <li>
          <label for="number-of-kids">How many kids did you bring?</label>
          <select id="number-of-kids" v-model.number="numberOfKids">
            <option>0</option>
            <option>1</option>
            <option>2</option>
            <option>3</option>
            <option>4</option>
          </select>
        </li>
        <li>
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
        </li>
        <li>
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
        </li>
        <li>
          <input type="submit" value="Tell us about it!" />
        </li>
      </ul>
    </form>

    <div class="submitted-message" v-if="confirmationSubmit">
      <p>
        <i>{{ confirmationSubmit }}</i>
      </p>
    </div>

    <hr />
    <section class="display-user-input">
      <p>Some user suggested activities:</p>
      <hr />
      <div
        class="museum-activity"
        v-for="activity in activities"
        :key="activity.id"
        :viewAllActivities="viewAllActivities"
      >
        <p>
          Museum visited:
          {{ museums.find(m => m.id === activity.museum_id).museum_name }}
        </p>
        <p>Name of Activity: {{ activity.activity_name }}</p>
        <p>Description of activity: {{ activity.activity_descrip }}</p>
        <p>Oldest child:{{ activity.high_age_range }}</p>
        <p>Youngest child:{{ activity.low_age_range }}</p>
        <p>Number of children taken:{{ activity.num_kids_taken }}</p>

        <button class="delete-activity" @click="deleteActivity(activity.id)">
          Delete this activity
        </button>
      </div>
    </section>
  </div>
</template>

<script>
import axios from "axios";
import AddMuseum from "./AddMuseum.vue";
import MuseumHome from "./MuseumHome.vue";
export default {
  name: "MuseumActivities",
  props: ["title"],
  components: {
    AddMuseum,
    MuseumHome
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
      confirmationSubmit: "",
      showAddMuseum: false
      //can activities be on a child component page to display?  good idea.
    };
  },
  methods: {
    handleSubmit() {
      axios
        .post("/add-activity", {
          museum_id: this.museum,
          activity_name: this.activityName,
          activity_descrip: this.activityDescription,
          number_of_kids_taken: this.numberOfKids,
          low_age_range_of_child_taken: this.lowAgeRange,
          high_age_range_of_child_taken: this.highAgeRange
        })
        .then(() => this.viewAllActivities());
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
        this.viewAllActivities();
      });
    },
    deleteActivity(id) {
      axios
        .delete("/activity/" + id) //not deleting right activity
        .then(() => this.viewAllActivities());
    }
    // showAddMuseumComponent() {
    //   showAddMuseum == true;
    //   // return componentName; try to render AddMuseum on click!
    // }
  },
  watch: {
    museum() {
      console.log("museum id is", this.museum);
    },
    activities() {
      console.log("activity id is", this.activities[0].id);
    }
  },
  mounted() {
    this.museumList();

    //the most recently entered activity will display at bottom.
  }
};
</script>

<style scoped>
.museum-activity {
  padding: 2em;
  width: 100%;
  box-shadow: 0 3px 6px rgba(0, 0, 0, 0.16), 0 3px 6px rgba(0, 0, 0, 0.23);
}
* {
  box-sizing: border-box;
}
.flex-outer li {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  margin: 0 5px;
}
.flex-outer > li > label,
.flex-outer li p {
  flex: 1 0 120px;
  max-width: 220px;
  margin: 0 5px;
}
.flex-outer li button {
  margin-left: auto;
  padding: 8px 16px;
  border: none;
  background: #333;
  color: #f2f2f2;
  text-transform: uppercase;
  letter-spacing: 0.09em;
  border-radius: 2px;
}
.activity-submission {
  border-radius: 5px;
  background-color: rgb(243, 235, 220);
  padding: 35px;
}
</style>
