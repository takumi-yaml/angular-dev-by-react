import { connect } from 'react-redux';
import { changeName } from '../actions';
import Hero from '../components/Hero'

const mapStateToProps = (state) => {
    return {
        hero: state.hero
    }
};

const mapDispatchToProps = (dispatch) => {
    return {
        onKeyUp: (name) =>{
            dispatch(changeName(name))
        }
    }
};

const connecter = connect(
    mapStateToProps,
    mapDispatchToProps
);

export default connecter(Hero);
