<template>
    <div class="column is-3">
        <div class="box">
            <h3 class="is-size-4">{{ specialist.slug }}</h3>
        </div>
    </div>
</template>

<script>

export default {
    name: 'SpecialistBox',
    props: {
        specialist: Object
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