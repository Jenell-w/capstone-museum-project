<template>
  <div class="hello">
    <h1>{{ title }}</h1>
    <h2>
      Visting an art museum can be kid-friendly: let us show you how!
      <br />Here is something you can do at the museum with your children.
    </h2>

    <h3>
      Please enter a fun activity you have completed (or attempted!) at a museum
    </h3>
    <br />
    <div class="container">
      <form class="activity-submission" @submit="handleSubmit">
        <div class="row">
          <div class="col-25">
            <label for="museum-name"
              >Select the museum you visited: (add a new museum below!)</label
            >
          </div>

          <!-- select drop down reads from museum_info table in db -->
          <div class="col-75">
            <select id="museum-name" v-model="museum" name="Select a museum">
              <option
                v-for="museum in museums"
                :key="museum.id"
                :value="museum.id"
                >{{ museum.museum_name }}</option
              >
            </select>
          </div>
          <div class="show-add-museum">
            <!-- <button @click="showAddMuseumComponent">
          Add a Museum if not in list
        </button>
            <need a function to make an @ click SHOW componenet!!-->
            <AddMuseum />
          </div>
          <div class="row">
            <div class="col-25">
              <label for="activity-name">What fun activity did you do?</label>
            </div>
            <div class="col-75">
              <input id="activity-name" v-model="activityName" />
            </div>
            <div class="col-25">
              <label for="activity-description"
                >Describe what you did and/or what you brought with you?</label
              >
            </div>
            <div class="col-75">
              <textarea
                id="activity-description"
                v-model="activityDescription"
              ></textarea>
            </div>
          </div>
          <div class="col=25">
            <label for="number-of-kids">How many kids did you bring?</label>
          </div>
          <div class="col-75">
            <select id="number-of-kids" v-model.number="numberOfKids">
              <option>0</option>
              <option>1</option>
              <option>2</option>
              <option>3</option>
              <option>4</option>
            </select>
          </div>
          <div class="col-25">
            <label for="low-age-range"
              >Youngest child's age (Please select 0 if child is under
              1):</label
            >
          </div>
          <div class="col-75">
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
          </div>
          <div class="col-25">
            <label for="high-age-range">Oldest child's age:</label>
          </div>
          <div class="col-75">
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
          </div>
        </div>
        <div class="row">
          <input type="submit" value="Tell us about it!" />
        </div>
      </form>
    </div>

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
        <p>Museum visited: {{ activity.museum_id }}</p>
        <p>Name of Activity: {{ activity.activity_name }}</p>
        <p>Description of activity: {{ activity.activity_descrip }}</p>
        <p>Oldest child:{{ activity.high_age_range }}</p>
        <p>Youngest child:{{ activity.low_age_range }}</p>
        <p>Number of children taken:{{ activity.num_kids_taken }}</p>

        <button @click="deleteActivity" :key="activity.id">
          Delete this activity
        </button>
      </div>

      <!-- how to delete item, need to tie the 
      activity id to the museum id- why is button showing up again?-->
    </section>
  </div>
</template>

<script>
import axios from "axios";
// import ViewActivities from "./ViewActivities.vue";
import AddMuseum from "./AddMuseum.vue";

export default {
  name: "MuseumActivities",
  props: ["title"],
  components: {
    AddMuseum
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
          museum_id: this.museum, // coming up blank, not getting the ID from museumInfo table
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
      });
    },
    deleteActivity() {
      let lookup = {};
      for (let i = 0, len = this.activities.length; i < len; i++) {
        lookup[this.activities[i].id] = this.activities[i];
      }
      axios
        .delete("/activity/" + this.activities.lookup[id]) //not deleting right activity
        .then(() => this.viewAllActivities());
    },
    showAddMuseumComponent() {
      showAddMuseum == true;
      // return componentName; try to render AddMuseum on click!
    }
  },
  watch: {
    museum() {
      console.log("museum id is", this.museum);
    },
    activities() {
      console.log("activity id is", this.activities[0].id);
    },
    activityIdTest() {
      console.log("activity lookup ID is", this.activities.find(id));
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
  padding: 2em;
  width: 100%;
  box-shadow: 0 3px 6px rgba(0, 0, 0, 0.16), 0 3px 6px rgba(0, 0, 0, 0.23);
}
* {
  box-sizing: border-box;
}

input[type="text"],
select,
textarea {
  width: 100%;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
  resize: vertical;
}

label {
  padding: 12px 12px 12px 0;
  display: inline-block;
}

input[type="submit"] {
  background-color: #4caf50;
  color: white;
  padding: 12px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  float: right;
}

input[type="submit"]:hover {
  background-color: #45a049;
}

.container {
  border-radius: 5px;
  background-color: #f2f2f2;
  padding: 20px;
}

.col-25 {
  float: left;
  width: 25%;
  margin-top: 6px;
}

.col-75 {
  float: left;
  width: 75%;
  margin-top: 6px;
}

/* Clear floats after the columns */
.row:after {
  content: "";
  display: table;
  clear: both;
}
</style>
