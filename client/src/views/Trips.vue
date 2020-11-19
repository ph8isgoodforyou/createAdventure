<template>
<div>
    <div class="container">
        <Header />
        <div class="list">
            <TripsList/>
        </div>
        <Footer />
    </div>
</div>
</template>

<script>
import Header from '../components/Header'
import TripsList from '../components/TripsList'
import Footer from '../components/Footer'


export default {
    name: 'Trips',
    components: {
        TripsList,
        Footer,
        Header,
    },
}
</script>

<style>
.container {
    background: rgb(238, 231, 231);
}

.list {
    margin: 20px;
}
</style>
