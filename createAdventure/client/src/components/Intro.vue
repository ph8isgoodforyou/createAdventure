<template>
  <div class="intro">
    <div class="intro-wrapper">
      <video id="videoBG" poster="poster.JPG" autoplay muted loop>
        <source src="../assets/videos/intro-video.mp4" type="video/mp4">
      </video>
      <h1 class="intro-logo1">
        Unleash
      </h1>
      <h1 class="intro-logo2">
        The
      </h1>
      <h1 class="intro-logo3">
        Adventurer
      </h1>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Intro'
}
</script>

<style scoped>
/*--------------------------------------Intro start------------*/
.intro-logo1,
.intro-logo2,
.intro-logo3{
    z-index: 3;
    position: absolute;
    text-align: center;
    font-size: 10vh;
    color: white;
}
.intro-logo1{
    opacity: 0.5;
    top: 20%;
    left: 20%;
    transform: translate(-50%, -50%);
}
.intro-logo2{
    opacity: 0.7;
    top: 30%;
    left: 30%;
    transform: translate(-50%, -50%);
}
.intro-logo3{
    opacity: 0.9;
    top: 40%;
    left: 40%;
    transform: translate(-50%, -50%);
}
@media(max-width: 1160px){
    .intro-logo2{
        top: 30%;
        left: 28%;
        transform: translate(-50%, -50%);
    }
}
@media(max-width: 992px){
    .intro-logo1,
    .intro-logo2,
    .intro-logo3{
        font-size: 8vh;
    }
    .intro-logo1{
        top: 20%;
        left: 30%;
        transform: translate(-50%, -50%);
    }
    .intro-logo2{
        top: 30%;
        left: 30%;
        transform: translate(-50%, -50%);
    }
    .intro-logo3{
        top: 40%;
        left: 43%;
        transform: translate(-50%, -50%);
    }
}
@media(max-width: 480px){
    .intro-logo3{
        top: 40%;
        left: 50%;
        transform: translate(-50%, -50%);
    }
}
@media(max-width: 440px){
    .intro-logo1{
        top: 20%;
        left: 40%;
        transform: translate(-50%, -50%);
    }
}
.intro{
    min-width: auto;
}

.intro-wrapper{
    position: absolute;
    left: 0;
    width: 100%;
    height: 100vh;
    overflow: hidden;
}
.intro-wrapper video{
    min-height: 100%;
    min-width: 100%;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}
.intro-wrapper img{
    min-height: 100%;
    min-width: 100%;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    object-fit: cover;
    pointer-events: none;
    z-index: initial;
}

/*--------------------------------------Intro end------------- */
</style>
