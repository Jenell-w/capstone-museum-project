<template>
  <div id="app">
    <img
      v-if="!showMuseumHome"
      alt="mona-lisa-cartoon"
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
    <MuseumHome v-if="showMuseumHome" />
  </div>
</template>

<script>
import MuseumActivities from "./components/MuseumActivities.vue";
import MuseumHome from "./components/MuseumHome.vue";

export default {
  name: "app",
  components: {
    MuseumActivities,
    MuseumHome
  },
  data() {
    return {
      showMuseumHome: false,
      buttonText: "Click here for a pre-museum activity!",
      activities: ""
    };
  },
  methods: {
    handleNav() {
      this.showMuseumHome = !this.showMuseumHome;
      if (this.buttonText === "Click here for a pre-museum activity!") {
        this.buttonText = "Go to Family Viewseums Home";
      } else {
        this.buttonText = "Click here for a pre-museum activity!";
      }
    }
  }
};
</script>

<style></style>
