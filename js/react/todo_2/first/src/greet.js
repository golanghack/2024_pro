import React, { Component } from "react";

class Greet extends Component {
    render() {
        return <h1>Welcome, {this.props.name} </h1>;   
    }
}

export default Greet;