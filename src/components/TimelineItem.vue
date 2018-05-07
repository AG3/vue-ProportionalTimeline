<template>
  <v-card class="event-card">
    <v-card-title>
      {{ titleS }}
    </v-card-title>
    <v-card-text>
      {{ctnt}}
    </v-card-text>

  </v-card>
</template>

<script>
export default {
  name: 'TimelineItem',
  props: {
    titleS: String,
    ctnt: String
  }
}
</script>

<style scoped>
.event-card {
  width: 150px;
}
</style>
