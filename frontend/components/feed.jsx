import { useState } from 'react';
import styles from '../styles/Home.module.css'

export default function Feed(...Props) {

  return (
    <div className={styles.feeddiv}>
      <div className={styles.feedtitle}>
        <h2>
          Public Feed
        </h2>
      </div>
      <div className={styles.feedwrapper}>
        <div className={styles.feedbox}></div>
        <div className={styles.feedbox}></div>
        <div className={styles.feedbox}></div>
      </div>
    </div>
  );
}