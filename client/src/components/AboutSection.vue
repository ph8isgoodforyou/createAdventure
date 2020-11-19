<template>
<div class="content">
    <div id="About" class="about">
        <div class="section">
            <div class="about-content">
                <h1>About Us</h1>
                <span></span>
                <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Temporibus vitae iusto dolorum quam obcaecati
                    perspiciatis quae consequuntur labore, odit ad, tempora dolore.</p>
                <ul class="about-social-media">
                    <li><a href="#"><i class="fab fa-facebook"></i></a></li>
                    <li><a href="#"><i class="fab fa-instagram"></i></a></li>
                    <li><a href="#"><i class="fab fa-twitter"></i></a></li>
                    <li><a href="#"><i class="fab fa-youtube"></i></a></li>
                </ul>
            </div>
            <div class="about-img"></div>
        </div>
    </div>
</div>
</template>

<script>
export default {
    name: 'About'
}
</script>

<style scoped>
.content {
    text-align: center;
    background: #0c0b0c;
    width: 100%;
    z-index: 2;
}

/*--------------------------------------About start------------*/
.content .about {
    color: #f4f4f4;
    display: grid;
    align-content: center;
    min-height: 100vh;
}

.content .about .section {
    display: grid;
    grid-template-columns: 1fr 1fr;
    min-height: 90vh;
    width: 85vw;
    margin: 0 auto;
}

.about-img {
    background: url('../assets/img/intro-img.jpg') no-repeat center;
}

.about-content {
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
}

.about-content h1 {
    font-family: "montserrat", sans-serif;
    text-transform: uppercase;
    font-size: 36px;
    letter-spacing: 6px;
    opacity: 0.9;
}

.about-content span {
    height: 0.5px;
    width: 80px;
    background-color: #8d5603;
    margin: 30px 0;
}

.about-content p {
    font-family: 'Bitter', serif;
    padding-bottom: 15px;
    font-weight: 300;
    opacity: 0.7;
    width: 60%;
    text-align: center;
    margin: 0 auto;
    line-height: 1.7;
}

.about-social-media {
    display: flex;
    padding: 15px 0px;
}

.about-social-media li {
    display: block;
    padding: 5px;
    margin: 5px;
}

.about-social-media li a {
    font-size: 26px;
    opacity: 0.8;
    color: #a07028;
    border: 2px solid #a07028;
    border-radius: 12px;
    margin: 10px;
    padding: 10px;
}

.about-social-media li a:hover {
    border-color: turquoise;
    color: turquoise;
}

@media(max-width: 992px) {
    .content .about .section {
        grid-template-columns: 1fr;
        width: 100%;
    }

    .about-img {
        height: 100vh;
    }

    .about-content {
        height: 100vh;
    }

    .about-content h1 {
        font-size: 20px;
        margin-top: 50px;
    }

    .about-content span {
        margin: 20px 0;
    }

    .about-content p {
        font-size: 14px;
    }

    .about-social-media li {
        font-size: 15px;
    }

    .about-social-media li a {
        font-size: 15px;
        margin: 1px;
    }
}

/*--------------------------------------About end------------- */
</style>
