<template>
<div class="greeting-container">
    <div class="inner-greeting-container">
        <h2><span>Where</span> are you going today?</h2>
        <a v-on:click="$router.push({ path: `/trips/`})">View Your Trips</a>
    </div>
</div>
</template>

<script>
export default {
    name: 'GreetingUser'
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Lato:wght@300;400&family=Poppins:wght@200;400&display=swap');

/*
font-family: 'Lato', sans-serif;
font-family: 'Poppins', sans-serif;
*/
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Poppins', sans-serif;
}

.greeting-container {
    background-color: #111010;
    color: white;
    min-height: 90vh;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    background: url('../assets/img/greeting-photo.jpg');
    background-size: cover;
}

.inner-greeting-container {
    height: 80%;
    width: 80%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding-left: 5%;
    padding-right: 5%;
    background-color: rgba(37, 16, 16, 0.9);
    box-shadow: 0 0 15px 6px rgb(136, 134, 146);
}

.inner-greeting-container h2 {
    font-size: 40px;
    font-weight: 100;
}

.inner-greeting-container h2 span {
    color: #a07028;
}

.inner-greeting-container a {
    margin-top: 40px;
    margin-bottom: 15px;
    color: white;
    border: solid 4px;
    width: 200px;
    height: 60px;
    display: flex;
    justify-self: center;
    justify-content: center;
    align-items: center;
    font-weight: 100;
}

.inner-greeting-container a:hover {
    color: white;
    background: #a0801f;
}

@media (max-width: 370px) {
    .greeting-container {
        height: 40vh;
    }

    .inner-greeting-container {
        height: 100%;
        width: 90%;
    }

}

@media (max-width: 280px) {
    .greeting-container {
        height: 55vh;
    }
}
</style>
