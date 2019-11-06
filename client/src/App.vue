<template>
  <div id="app">
    <img
      v-if="!showMuseumHome"
      alt="mona-lisa-cartoon"
      src="./assets/cartoon-mona-lisa.jpg"
    />
    <div class="navigation-buttons">
      <button @click="handleNav">{{ buttonText }}</button>
      <button @click="navButton2">{{ button2Text }}</button>
      <component v-bind:is="component" />
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
import MuseumInfo from "./components/MuseumInfo.vue";

export default {
  name: "app",
  components: {
    MuseumActivities,
    MuseumHome,
    MuseumInfo
  },
  data() {
    return {
      component: "",
      showMuseumHome: false,
      showMuseumInfo: false,
      buttonText: "Click here for a pre-museum activity!",
      button2Text: "Get Information about museums"
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
    },
    navButton2() {
      if (this.component === "") {
        this.component = MuseumInfo;
        this.button2Text = "Hide Museum Information";
      } else {
        this.component = "";
        this.button2Text = "Get Information about museums";
      }
    }
  }
};
</script>

<style></style>
