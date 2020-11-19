<template>
<div>
    <Header />
    <TripViewComp />
    <Footer />
</div>
</template>

<script>
import Header from '../components/Header'
import Footer from '../components/Footer'
import TripViewComp from '../components/TripViewComp'
export default {
    name: 'TripView',
    components: {
        Header,
        Footer,
        TripViewComp
    }
}
</script>

<style>

</style>
