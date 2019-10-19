<template>
  <div id="app">
    <div class="navigation-button">
      <button @click="handleNav">{{ buttonText }}</button>
    </div>
    <img
      v-if="!showMuseumHome"
      &#x3C;img
      alt="Vue logo"
      src="./assets/cartoon-mona-lisa.jpg"
    />
    />
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
      buttonText: "Go to Activity Page"
    };
  },
  methods: {
    handleNav() {
      this.showMuseumHome = !this.showMuseumHome;
      if (this.buttonText === "Go to Activity Page") {
        this.buttonText = "Go to Family Viewseums Home";
      } else {
        this.buttonText = "Go to Activity Page";
      }
    }
  }
};
</script>

<style></style>
