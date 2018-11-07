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
      from: "dummy_address",
      gas: 7900000
    }
  }
};
