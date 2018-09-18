module.exports = {
  rpc: {
    host:"localhost",
    port:8545
  },
  networks: {
    development: {
      host: "localhost",
      port: 8545,
      network_id: "*",
      from: "0xc15e6bfacbb2d9073e573518100963b9c6d805dd",
      gas: 18000000
    }
  }
};
