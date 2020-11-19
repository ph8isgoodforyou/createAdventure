<template>
<div>
    <Header />
    <CreateTripComp />
    <Footer />
</div>
</template>

<script>
import Header from '../components/Header'
import Footer from '../components/Footer'
import CreateTripComp from '../components/CreateTripComp'
export default {
    name: 'CreateTrip',
    components: {
        Header,
        Footer,
        CreateTripComp
    }
}
</script>

<style>

</style>
