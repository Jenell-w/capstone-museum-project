<template>
  <div id="app">
    <img
      v-if="!showMuseumHome"
      alt="Vue logo"
      src="./assets/cartoon-mona-lisa.jpg"
    />
    <div class="navigation-button">
      <button @click="handleNav">{{ buttonText }}</button>
    </div>
    <MuseumActivities
      v-if="!showMuseumHome"
      title="Welcome to Family ViewSeums!"
    />
    <MuseumHome v-if="!showMuseumHome" />
    <!-- <AddMuseum /> -->
  </div>
</template>

<script>
import MuseumActivities from "./components/MuseumActivities.vue";
import MuseumHome from "./components/MuseumHome.vue";
import AddMuseum from "./components/AddMuseum.vue";

export default {
  name: "app",
  components: {
    MuseumActivities,
    MuseumHome,
    AddMuseum
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
