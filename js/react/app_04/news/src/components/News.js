import React from 'react';
import PropTypes from 'prop-types';
import  Article  from './Article';    

class News extends React.Component {
  render = () => {
    const { data } = this.props;
    let newsTemplate = null;

    if (data.length) {
      newsTemplate = data.map(function(item) {
        return <Article key={item.id} data={item} />;
      });
    } else {
      newsTemplate = <p>Дел пока нет</p>;
    }

    return newsTemplate;
  };
  render() {
    const { data } = this.props;

    return (
      <div className="news">
        {this.renderNews()}
        {data.length ? (
          <strong className={"news__count"}>
            Всего дел в TODO: {data.length}
          </strong>
        ) : null}
      </div>
    );
  }
}

News.propTypes = {
  data: PropTypes.array.isRequired
};


export default News;