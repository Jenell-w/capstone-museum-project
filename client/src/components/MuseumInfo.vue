<template>
  <div class="display-museuminfo-container">
    <h2>{{ title }}</h2>
    <ul class="museum-list">
      <a href="https://goo.gl/maps/t1HP2EbBPVZL9jZc8">
        <li>The Metropolitan Museum of Art</li>
      </a>
      <a href="https://goo.gl/maps/DaVuJ8qKFJJuHWjU7">
        <li>The National Gallery of Art</li>
      </a>
      <a href="https://goo.gl/maps/MEzdREL9pYz9Yt6NA">
        <li>Museum of Fine Arts</li>
      </a>
      <a href="https://g.page/artinstitutechi?share">
        <li>The Art Institute of Chicago</li>
      </a>
      <a href="https://goo.gl/maps/eVRqzUpG7XDH3mf88">
        <li>Denver Art Museum</li>
      </a>
    </ul>
    <!-- Ideally, i would love to display an iframe embed code from googlemaps or wikipedia that 
    displays below each museum name, so the information remains on the page.-->
  </div>
</template>

<script>
export default {
  name: "MuseumInfo",
  props: ["title"],
  data() {
    return {
      metLink: ""
    };
  }
};
</script>
<style scoped></style>
