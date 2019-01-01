const path = require("path");

module.exports = {
  entry: "./frontend/src",
  output: {
    path: path.resolve(__dirname, "./frontend/static/frontend"),
    filename: "bundle.js"
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: "babel-loader"
      }
    ]
  }
};
