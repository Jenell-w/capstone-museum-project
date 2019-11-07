<template>
  <div class="hello">
    <h1>{{ title }}</h1>
    <div class="museum-buttons">
      <button class="museum-info-button" @click="navButton">
        {{ buttonText }}
      </button>
      <component v-bind:is="component" />
    </div>

    <MuseumHome />
    <h1>DURING Your Visit</h1>
    <br />
    <button class="activity-button" @click="isHidden = !isHidden">
      Browse Our Family Activities!
    </button>
    <section v-show="isHidden" class="display-user-input">
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
    <h1>AFTER Your Visit</h1>
    <h3>
      Share a fun activity you have completed (or attempted!) at a museum with
      your children!
    </h3>
    <br />
    <div class="container">
      <form class="activity-submission" @submit="handleSubmit">
        <ul class="flex-outer">
          <li>
            <label for="museum-name">
              Select the museum you visited: (or, add a new museum below!)
            </label>

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
            <label for="low-age-range">
              Youngest child's age (Please select 0 if child is under 1):
            </label>
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
            <button type="submit">Share with the World!</button>
          </li>
        </ul>
      </form>
    </div>

    <div class="submitted-message" v-if="confirmationSubmit">
      <p>
        <i>{{ confirmationSubmit }}</i>
      </p>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import AddMuseum from "./AddMuseum.vue";
import MuseumHome from "./MuseumHome.vue";
import MuseumInfo from "./MuseumInfo.vue";
export default {
  name: "MuseumActivities",
  props: ["title"],
  components: {
    AddMuseum,
    MuseumHome,
    MuseumInfo
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
      showAddMuseum: false,
      isHidden: false,
      component: "",
      buttonText: "Get Information about museums"
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
    },
    navButton() {
      if (this.component === "") {
        this.component = MuseumInfo;
        this.buttonText = "Hide Museum Information";
      } else {
        this.component = "";
        this.buttonText = "Get Information about museums";
      }
    }
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
.container {
  width: 80%;
  max-width: 1200px;
  margin: 0 auto;
}
.container * {
  box-sizing: border-box;
  font: normal 14px/1.5 "Fira Sans", "Helvetica Neue", sans-serif;
}
.flex-outer {
  list-style-type: none;
  padding: 0;
  max-width: 800px;
  margin: 0 auto;
}
.flex-outer li {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  margin: 0 5px;
}
.flex-outer > li:not(:last-child) {
  margin-bottom: 20px;
}
.flex-outer li label,
.flex-outer li p {
  padding: 8px;
  font-weight: 300;
  letter-spacing: 0.09em;
  text-transform: uppercase;
}
.flex-outer > li > label,
.flex-outer li p {
  flex: 1 0 120px;
  max-width: 220px;
  margin: 0 5px;
}
.flex-outer li button,
.activity-button,
.museum-info-button {
  margin-left: auto;
  margin: 10px;
  padding: 8px 16px;
  border: white;
  background: #333;
  color: #f2f2f2;
  text-transform: uppercase;
  letter-spacing: 0.09em;
  border-radius: 2px;
}
.activity-submission {
  font: normal 14px/1.5 "Fira Sans", "Helvetica Neue", sans-serif;
  background: grey;
  color: #fff;
  border-radius: 5px;
  padding: 20px;
}
</style>
