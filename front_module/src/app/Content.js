import React from 'react';
import {List, ListItem} from 'material-ui/List';


export default class Content extends React.Component {
  render() {
    var listItems = [];
    this.props.data.forEach(function(content, index) {
      listItems.push(<ListItem key={index} primaryText={<a target="_blank" href={content.url}>{content.title}</a>} secondaryText={content.author} 
        secondaryTextLines={1}></ListItem>);
    });

    return (
      <div>
        <List style={{display: 'block', marginTop: 0, marginRight: 'auto', marginBottom: 0, marginLeft: 'auto'}}>
          {listItems}
        </List>
      </div>
    );
  }
}
