import React, { Component } from 'react';
import { capitalize } from "../lib";

class Hero extends Component {
    send(e) {
        console.log(this.props)
        this.props.onKeyUp(this.refs.heroName.value);
    }

    render(){
        return (
            <div>
                <h2>{capitalize(this.props.hero.name)} Details</h2>
                <div>
                    <span>id: </span> {this.props.hero.id}
                </div>
                <div>
                    <label>name:
                        <input type={'text'}
                               value={capitalize(this.props.hero.name)}
                               onChange={this.send.bind(this)}
                               ref='heroName'
                        />
                    </label>
                </div>
            </div>
        );
    }
}


export default Hero;
