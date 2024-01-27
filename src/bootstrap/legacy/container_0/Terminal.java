import java.io.*;
// time to find a sandbox to execute something like rm -rf /*.
// so get closer to the bloody truth.
public class Terminal {

    class ReaderConsole implements Runnable {
        private InputStream is;
	private String x;
        public ReaderConsole(InputStream is,String x) {
            this.is = is;
	    this.x=x;
        }

        public void run() {
            InputStreamReader isr = null;
	             try {
                isr = new InputStreamReader(is);
                // hey! how about a byte reader?
		// this does not allow input. consider a process instead.
            } catch (Exception e1) {
                e1.printStackTrace();
		}
            BufferedReader br = new BufferedReader(isr);
	    // the heck! must be able to write into the stream.
            int c = -1;
            try {
                while ((c = br.read()) != -1) {
                    System.out.println("WELCOME_Y: "+this.x);
                    System.out.print((byte) c);
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
    // always the same thing.
    // can we try that now?
    class WrittenConsole implements Runnable {
        private OutputStream os;
	private String x;
        public WrittenConsole(OutputStream os,String x) {
            this.os = os;
	    this.x=x;
        }

        public void run() {
            try {
                while (true) {
                    String line = this.getConsoleLine();
                    line += "\n";
                    System.out.println("WELCOME_X: "+this.x);
                    byte[] bts = line.getBytes();
                    os.write(bts);
                    System.out.println(bts);
                    os.flush();
		    Thread.sleep(1000);
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
        }

        private String getConsoleLine() throws IOException {
            String line = "whoami";
	    //            InputStreamReader input = new InputStreamReader(System.in);
            //BufferedReader br = new BufferedReader(input);
            //line = br.readLine();
            return line;
        }
    }

    // can you find the stderr?
    // whoami?
    public void execute() throws Exception {
	//        String[] cmds = { "su","-","test" };
	String[] cmds = {"sshpass","-p","test","mosh","test@localhost"};
	// same error????
        Process process = Runtime.getRuntime().exec(cmds);
        InputStream os = process.getInputStream();
        OutputStream is = process.getOutputStream();
        InputStream es = process.getErrorStream();// this one is correct.
	// somehow mistaken.
	// write to outputStream?
        Thread t1 = new Thread(new WrittenConsole(is,"input"));
        Thread t0 = new Thread(new ReaderConsole(es,"error"));
        Thread t2 = new Thread(new ReaderConsole(os,"output"));
        t1.start();
        t0.start();
        t2.start();
        // great then. whatever.
	// need to detach?
    }

    public static void main(String[] args) {
        System.out.println("WELCOME");
        // not as effective as I expected.
        Terminal t = new Terminal();
        try {
            System.out.println("AGAIN");
            t.execute();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
