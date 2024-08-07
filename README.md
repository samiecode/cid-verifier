# CID Verifier

## About
<p>
    CID Verifier is decentralized application (dapp) powered by <a href="https://docs.cartesi.io/cartesi-rollups/1.3/">cartesi</a> rollups technology.
</p>
<p> 
    A Content Identifier (CID) is a unique identifier used to reference a piece of content in a decentralized storage system. Unlike traditional URLs or file paths that specify the location of data, a CID references the data itself, regardless of where it is stored. This is a key feature of content-addressed storage systems.
</p>

## Getting Started

Below you'll find instructions on how setting up this dapp locally.

### Prerequisites

Here are some packages you need to have installed on your PC:

* [nodejs](https://nodejs.org/en), [npm](https://docs.npmjs.com/cli/v10/configuring-npm/install), [yarn](https://classic.yarnpkg.com/lang/en/docs/install/#debian-stable) 

* [docker](https://docs.docker.com/get-docker/)

* [cartesi-cli](https://docs.cartesi.io/cartesi-rollups/1.3/development/migration/#install-cartesi-cli)
  ```sh
  npm install -g @cartesi/cli
  ```

### Installation

1. Clone this repo
   ```sh
   git clone https://github.com/OsmanRodrigues/bshelf-dapp.git
   ```
2. Build and run the dapp via `cartesi-cli`
   ```sh
   cartesi build 
   ```
   and
   ```sh
   cartesi run 
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage

### Some CID token to use in the app

Send this cid as input
```text
bafkreiehl6mzaluyllznhbslr5wpkeenfzmsn2m5gyoygyevhtny3g4ade
```

```text
bafkreihqguf7kknhc7gjpsfdxueapm77w3xsao34so7yvet46akbmx6tdq
```

```text
bafkreidcdgt4sj2arr2n46g2gh4xeulqqcs3qcxa2z43ntzqizihjymo7e
```

```text
bafybeid3xnwcxm443fkwry37hdfoycawctkvlf7kmeew55gxjqhiiwi5je
```

```text
bafkreihj3k5czfp3b6r3rjomb5zznqw7tw2apqfxxecxr7z4zof4nbwojm
```

Here you can access the examples of dapp communication and resources consume.

### Advance handlers
* #### verify cid
    "bafkreihj3k5czfp3b6r3rjomb5zznqw7tw2apqfxxecxr7z4zof4nbwojm"

### Inspect handlers 
* #### Cid Verify Successfully
  ```
  interact
    - access the cartesi inspect endpoint on your browser
  ```sh 
  http://localhost:8080/inspect/cidVerify
  ```

* #### Total Verification
  interact
    - access the cartesi inspect endpoint on your browser
  ```sh 
  http://localhost:8080/inspect/totalVerification
  ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contributing
We welcome contributions from the community! If you'd like to contribute to Bshelf, please follow these steps:

- Fork the repository.
- Create a new branch for your feature or bug fix.
- Make your changes and commit them with descriptive commit messages.
- Push your changes to your forked repository.
- Submit a pull request to the main repository.
- Please ensure that your code adheres to the project's coding standards and includes appropriate tests.