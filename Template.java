import java.io.*;

class Template {

    private static int calculate(String input) {
        return 0;
    }

    public static void main(String args[]) {
        System.out.print(calculate(readStdin()));
    }

    private static String readStdin() {
        String inStr = "";
        try {
            BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
            while (true) {
                int c = in.read();
                if (c == -1) {
                    break;
                } else {
                    inStr += (char)c;
                }
            }
        } catch (Exception e) {
        }
        return inStr;
    }

}
