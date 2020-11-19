<template>
<div></div>
</template>

<script>
export default {
    created() {
        this.$store.dispatch('userLogout')
            .then(() => {
                this.$router.push({
                    path: '/'
                })
            })
    }
}
</script>

<style>

</style>
