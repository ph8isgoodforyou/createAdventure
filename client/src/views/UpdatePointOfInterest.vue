<template>
<div>
    <Header />
    <UpdatePointOfInterestComp />
    <Footer />
</div>
</template>

<script>
import Header from '../components/Header'
import Footer from '../components/Footer'
import UpdatePointOfInterestComp from '../components/UpdatePointOfInterestComp'
export default {
    name: 'UpdatePointOfInterest',
    components: {
        Header,
        Footer,
        UpdatePointOfInterestComp
    }
}
</script>

<style>

</style>
