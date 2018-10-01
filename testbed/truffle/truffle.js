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
      from: "0x738f9c800fc80459f8f01c0e685ac2030b4fad2f",
      gas: 18000000
    }
  }
};
