<template>
  <div id="app">
    <img
      v-if="!showMuseumHome"
      alt="Vue logo"
      src="./assets/cartoon-mona-lisa.jpg"
    />
    <div class="navigation-button">
      <button @click="handleNav">{{ buttonText }}</button>
      <br />
    </div>
    <MuseumActivities
      v-if="!showMuseumHome"
      title="Welcome to Family ViewSeums!"
    />
    <MuseumHome v-if="!showMuseumHome" />
    <!-- <div class="second-nav-button">
      <button @click="showAllActivities"> {{ }}
    </div>-->
    <!-- <AddMuseum /> -->
    <!-- <ViewActivities /> -->
  </div>
</template>

<script>
import MuseumActivities from "./components/MuseumActivities.vue";
import MuseumHome from "./components/MuseumHome.vue";
import AddMuseum from "./components/AddMuseum.vue";
import ViewActivities from "./components/ViewActivities.vue";

export default {
  name: "app",
  components: {
    MuseumActivities,
    MuseumHome,
    AddMuseum,
    ViewActivities
  },
  data() {
    return {
      showMuseumHome: false,
      buttonText: "View Family-Friendly Activities"
    };
  },
  methods: {
    handleNav() {
      this.showMuseumHome = !this.showMuseumHome;
      if (this.buttonText === "View Family-Friendly Activities") {
        this.buttonText = "Go to Family Viewseums Home";
      } else {
        this.buttonText = "View Family-Friendly Activities";
      }
    }
  }
};
</script>

<style></style>
