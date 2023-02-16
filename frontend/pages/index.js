import Head from 'next/head'
import styles from '../styles/Home.module.css'
import Search from '../components/search'


export default function Home() {
  return (
    <div>
      <Head>
        <title>Create Next App</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main className={styles.main}>
        <p className={styles.description}>
            settlementdaddy.com
        </p>
        <div>
          <Search></Search>
        </div>
      </main>
    </div>
  )
}