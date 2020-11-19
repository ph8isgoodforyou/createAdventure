<template>
<div>
    <Header />
    <CreatePointOfInterestComp />
    <Footer />
</div>
</template>

<script>
import Header from '../components/Header'
import Footer from '../components/Footer'
import CreatePointOfInterestComp from '../components/CreatePointOfInterestComp'
export default {
    name: 'CreatePointOfInterest',
    components: {
        Header,
        Footer,
        CreatePointOfInterestComp
    }
}
</script>

<style>

</style>
