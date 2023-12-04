<template>
    <div class="column is-3">
        <div class="box">
            <h3 class="is-size-4">{{ direction.name }}</h3>
            <li v-for="direction_point in direction.directionpoints">
                {{ direction_point.description }}
            </li>
        </div>
    </div>
</template>

<script>
export default {
    name: 'DirectionBox',
    props: {
        direction: Object
    }
}
</script>

<style scoped>
  .image {
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
  }
</style>