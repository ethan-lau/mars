import React from 'react';
import {List, ListItem} from 'material-ui/List';


export default class Content extends React.Component {
  render() {
    var listItems = [];
    this.props.data.forEach(function(content, index) {
      console.log(index.title);
      listItems.push(<ListItem key={index} primaryText={content.title} secondaryText={content.author} secondaryTextLines={1} />);
    });

    return (
      <div>
        <List style={{width: 600,display: 'block', marginTop: 20, marginRight: 'auto', marginBottom: 20, marginLeft: 'auto'}}>
          {listItems}
        </List>
      </div>
    );
  }
}
