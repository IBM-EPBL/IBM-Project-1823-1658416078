<template>
  <div class="greetings">
  <h1>Darkphish</h1>
</div>
</template>

<script>
export default {
  name: 'HelloWorld',
}
</script>

<style scoped>
*{
font-family: 'Courier New', Courier, monospace;
}
h1 {
font-weight: 500;
font-size: 2.6rem;
top: -10px;
}

h2 {
font-size: 1.2rem;
font-weight: bold;

}

.greetings h1,
.greetings h2 {
text-align: center;
}

@media (min-width: 1024px) {
.greetings h1,
.greetings h3 {
  text-align: left;
}
}
</style>