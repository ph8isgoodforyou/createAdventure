<template>
<div class="container">
    <div class="inner-container">
        <div class="text">
            <h1>No <span>adventures</span> planed at the moment</h1>
            <h3>Start living your life now!</h3>
            <a v-on:click="$router.push({ path: `/create/trip/` })">Create Trip</a>
        </div>
        <div class="video">
            <video id="videoBG" poster="poster.JPG" autoplay muted loop>
                <source src="../assets/videos/noTrips.mp4" type="video/mp4">
            </video>
        </div>
    </div>
</div>
</template>

<script>
export default {
    name: 'NoTrips'
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
}

.container {
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    font-family: 'Poppins', sans-serif;
}

.inner-container {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-gap: 30px;
    justify-content: center;
    align-items: center;
    width: 80%;
}

.container .inner-container .text {
    padding: 30px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.container .inner-container .text h1 {
    font-size: 5vh;
    font-weight: 400;
    padding: 10px;
    margin-bottom: 20px;
    text-transform: uppercase;
}

.container .inner-container .text h1 span {
    color: rgb(41, 105, 187);
}

.container .inner-container .text h3 {
    font-size: 3vh;
    font-weight: 100;
}

.container .inner-container .video {
    padding: 30px;
    display: flex;
    justify-content: center;
    align-items: center;
}

.container .inner-container .video video {
    background-size: cover;
    height: 600px;
    width: 400px;
    object-fit: cover;
}

.container .inner-container .text a {
    display: flex;
    justify-content: center;
    align-items: center;
    text-decoration: none;
    text-align: center;
    background: rgb(41, 105, 187);
    color: white;
    border: 3px solid;
    border-radius: 12px;
    margin-top: 20px;
    height: 50px;
    width: 200px;
}

.container .inner-container .text a:hover {
    background-color: rgb(146, 114, 9);
}

@media (max-width: 1024px) {
    .inner-container {
        display: block;
    }
}

@media (max-width: 280px) {
    .container .inner-container .video {
        padding: 0px;
        padding-bottom: 10px;
    }

    .container .inner-container .video video {
        width: 100%;

    }
}
</style>
