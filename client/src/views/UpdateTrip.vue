<template>
<div>
    <Header />
    <UpdateTripComp />
    <Footer />
</div>
</template>

<script>
import Header from '../components/Header'
import Footer from '../components/Footer'
import UpdateTripComp from '../components/UpdateTripComp'
export default {
    name: 'UpdateTrip',
    components: {
        Header,
        Footer,
        UpdateTripComp
    }
}
</script>

<style>

</style>
