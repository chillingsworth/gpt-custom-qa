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

            Settlement Daddy

        </h1>
        <p className={styles.description}>

            Structured Settlement and Annuity Experts

        </p>
      </main>
    </div>
  )
}