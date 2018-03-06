var path = require("path")
var webpack = require('webpack')

const config = {
    context: __dirname,

    entry: './index',

    output: {
        path: path.resolve('./assets/bundles/'),
        filename: "bootstrap-webpack.js",
    },

    module: {
        rules: [
            {
                test: /\.css$/,
                use: ['style-loader', 'css-loader']
            }
        ]
    }
};

module.exports = config;
