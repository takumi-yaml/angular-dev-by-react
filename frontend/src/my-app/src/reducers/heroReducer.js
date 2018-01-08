export const heroReducer = (state=[], action) => {
    switch (action.type) {
        case 'CHANGE_NAME':
            return (
                Object.assign({}, state, {
                        hero: {
                            id: 0,
                            name: action.name
                        }
                    })
            );
        default:
            return state
    }
};


