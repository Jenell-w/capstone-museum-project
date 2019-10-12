<template>
  <div class="home">
    <button>Generate Some Interesting Artwork!</button>
    <br />
    <br />
    <iframe
      src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d12084.832829126724!2d-73.963244!3d40.7794366!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x3b2fa4f4b6c6a1fa!2sThe%20Metropolitan%20Museum%20of%20Art!5e0!3m2!1sen!2sus!4v1570913132044!5m2!1sen!2sus"
      width="600"
      height="450"
      frameborder="0"
      style="border:0;"
      allowfullscreen
    ></iframe>
  </div>
</template>

<script>
export default {
  name: "MuseumHome",
  props: ["title"]
};
</script>

<style scoped></style>
