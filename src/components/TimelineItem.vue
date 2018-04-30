<template>
  <md-card class="md-layout-item md-medium-size-20">
    <md-card-header>
      {{ titleS }}
    </md-card-header>
    <md-card-content>
      {{ctnt}}
    </md-card-content>

  </md-card>
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

</style>
