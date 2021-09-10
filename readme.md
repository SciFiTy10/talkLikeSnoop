<!-- PROJECT SHIELDS -->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/SciFiTy10/talkLikeSnoop">
    <img src="skill_image.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Talk Like Snoop</h3>

  <p align="center">
    Alexa now talks to you just like Snoop Dogg!
    <br />
    <a href="https://github.com/SciFiTy10/talkLikeSnoop"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://www.amazon.com/SciFiTy-Talk-Like-Snoop/dp/B07K1SHLJ8">Install Skill</a>
    ·
    <a href="https://github.com/SciFiTy10/talkLikeSnoop/issues">Report Bug</a>
    ·
    <a href="https://github.com/SciFiTy10/talkLikeSnoop/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
        <li><a href="#cicd-and-hosting">CI/CD and Hosting</a></li>
        <li><a href="#state-management">State Management</a></li>
        <li><a href="#testing">Testing</a></li>
        <li><a href="#project-folder-structure">Project Folder Structure</a></li>
        <li><a href="#things-i-learned-and-things-i-wouldve-done-differently">Things I Learned and Things I Would've Done Differently</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#running-project">Running Project</a></li>
        <li><a href="#running-tests">Running Tests</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

<!--add link to main page -->
<img src="skill_image.png" alt="main_page" >

Welcome to the Talk Like Snoop Alexa Skill!

This is arguably the most fun I've ever had programming.

In 2018, Amazon was running a promotion where if you published a new skill before Halloween, you would receive a free Echo Dot (3rd generation).

I have such great memories of audibly cackling at my computer when I got this to work for the first time.

---

### Built With

- [Python 3.6](https://www.python.org/downloads/release/python-370/)

---

### CI/CD and Hosting

- [AWS Lambda](https://aws.amazon.com/lambda/) - application code is hosted and executed as a Lambda function
  - I also created a beta lambda for new changes I planned to make.
- [Alexa Skills Store](https://www.amazon.com/SciFiTy-Talk-Like-Snoop/dp/B07K1SHLJ8) - distributed through the Alexa skill store

---

### State Management

The phrases asked and translated for the user are not persisted. The skill loops and lets the user ask for as many translations as they want before quitting.

---

### Testing

For testing application logic:

- [AWS Lambda Test Events](https://aws.amazon.com/lambda/) - Lambda has native support for configuring and running test events which take input and log output

For testing skill response:

- [Alexa Developer Console](https://developer.amazon.com/alexa/console/ask) - for running tests of the "front end" which would be the verbal input and verbal response.

---

### Project Folder Structure

This project is organized into separate modules which each perform one job.

- There is a main module which acts as the primary entry point to the application from the Alexa Skills Kit (front end).

- This is followed by a routing methods module which handles the intent of the user. There is an onLaunch intent to greet them, and an intent router which maps to the remaining options: stop, cancel, or talkLikeSnoop, which performs the main logic of translating speech.

- Beyond that, there are modules like utility_methods.py, which handle the different cases of each word the skill is churning through.

- Because there are Amazon Echos with a screen and users may access the skill through a mobile app, Alexa Skills need to return a card to display, so there are modules to handle that logic as well.

- And last but not least, there are methods for messages the user is sent, stop words to skip over, and a module for vowels.

---

### Things I Learned and Things I Would've Done Differently

- Alexa skill development is both simple in principle and complicated in practice

<i>How complicated can it be to have a device that does all the heavy lifting of providing you with text the user said and gives you programmatic hooks to leverage a response?</i>

The answer is subtle: it's a different experience designing for voice vs. a visual UI. And once you figure out how you're going to approach voice, you still have to handle the case of visual cards being returned.

- The english language is insanely complicated

The first version I built of this worked well, but for some words I wanted them to be translated differently.

So I came up with a solution for the follow up, but for literally every test case I could think of (basically where are vowels in relation to consonants?) there was a breaking case with a terrible sounding response.

English is an absolute minefield for how things are pronounced vs. how they are spelled and my application logic relies heavily on alphabetical placement.

The lesson learned here is that this can only work so well. For this app to be perfect, I would have to write out rules for dozens if not hundreds of edge cases.

<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

Make sure you have an Amazon echo device (any generation) which has Alexa built in.

---

### Installation

[Enable the Talk Like Snoop Skill](https://www.amazon.com/SciFiTy-Talk-Like-Snoop/dp/B07K1SHLJ8)

Or alternatively, say to your Amazon Echo:

`"Alexa, install Talk Like Snoop"`

---

### Running Project

Say to Alexa:

`"Alexa, talk like snoop"`

---

<!-- USAGE EXAMPLES -->

## Usage

Open the skill:

`"Alexa, talk like snoop"`

(the welcome response will play)

Speak To Alexa:

`"Say, on the contrary, this chicken is fire."`

She will reply:

`"On the contrarizzle, this chickizzle is fizzire."`

<!-- ROADMAP -->

## Roadmap

See the [open issues](https://github.com/SciFiTy10/talkLikeSnoop/issues) for a list of proposed features (and known issues).

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->

## Contact

Tyler Ridings - [LinkedIn](https://www.linkedin.com/in/tyler-ridings-24804585/)

Personal Portfolio - [https://www.tylerridings.dev](https://www.tylerridings.dev)

Project Link - [https://www.amazon.com/SciFiTy-Talk-Like-Snoop/dp/B07K1SHLJ8](https://www.amazon.com/SciFiTy-Talk-Like-Snoop/dp/B07K1SHLJ8p)

<!-- ACKNOWLEDGEMENTS -->

## Acknowledgements

- [Snoop Dogg](https://en.wikipedia.org/wiki/Snoop_Dogg)
- [Snoop Explaining For Shizzle](https://www.youtube.com/watch?v=PiAvfcfIzac)

<!-- MARKDOWN LINKS & IMAGES -->

[contributors-shield]: https://img.shields.io/github/contributors/SciFiTy10/talkLikeSnoop.svg?style=for-the-badge
[contributors-url]: https://github.com/SciFiTy10/talkLikeSnoop/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/SciFiTy10/talkLikeSnoop.svg?style=for-the-badge
[forks-url]: https://github.com/SciFiTy10/talkLikeSnoop/network/members
[stars-shield]: https://img.shields.io/github/stars/SciFiTy10/talkLikeSnoop.svg?style=for-the-badge
[stars-url]: https://github.com/SciFiTy10/talkLikeSnoop/stargazers
[issues-shield]: https://img.shields.io/github/issues/SciFiTy10/talkLikeSnoop.svg?style=for-the-badge
[issues-url]: https://github.com/SciFiTy10/talkLikeSnoop/issues
[license-shield]: https://img.shields.io/github/license/SciFiTy10/talkLikeSnoop.svg?style=for-the-badge
[license-url]: https://github.com/SciFiTy10/talkLikeSnoop/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/tyler-ridings-24804585/
