<template>
<div>
    <Header />
    <ContactSection />
    <Footer />
</div>
</template>

<script>
import Header from '../components/Header'
import Footer from '../components/Footer'
import ContactSection from '../components/ContactSection'

export default {
    name: 'Contact',
    components: {
        ContactSection,
        Footer,
        Header,
    }
}
</script>

<style>

</style>
