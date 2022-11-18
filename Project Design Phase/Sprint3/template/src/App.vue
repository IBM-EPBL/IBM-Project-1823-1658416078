<template>
  <v-app>
    <div id = "bg">
    <br/>
    <header style = "padding-left: 10px;">
        <img alt="dark" class="logo" src="./assets/dark.png" width="100" height="100" />
        <div class="wrapper">
          <HelloWorld/>
        </div>
  </header>
  <main>
    <SearchBar />
  </main>
</div>

  </v-app>
</template>

<script>
import HelloWorld from './components/HelloWorld';
import SearchBar from './components/SearchBar.vue'

export default {
  name: 'App',

  components: {
    HelloWorld,
    SearchBar
  },

  data: () => ({
    //
  }),
};
</script>

<style scoped>

#bg{
  background-image: url("../src/assets/bg.jpeg"); /* The image used */
  background-position: center; /* Center the image */
  background-size: cover; /* Resize the background image to cover the entire container */
  width: 100%;
  max-width: 3840px;
  height: 960px;
}

header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
