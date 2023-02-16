import Head from 'next/head'
import styles from '../styles/Home.module.css'

export default function Home() {
  return (
    <div>
      <Head>
        <title>Create Next App</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      
      <main className={styles.main}>
        <h1 className={styles.title}>
          <div>
            Settlement Daddy
          </div>
        </h1>
        <p className={styles.description}>
          <div>
            Structured Settlement and Annuity Experts
          </div>
        </p>
      </main>
    </div>
  )
}