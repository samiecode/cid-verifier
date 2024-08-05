import {createApp} from "@deroll/app";
import {CID} from "multiformats/cid";
import {hexToString, stringToHex, getAddress} from "viem";

// create app
const app = createApp({
	url: process.env.ROLLUP_HTTP_SERVER_URL || "http://127.0.0.1:5004",
});

let cidVerify : any = []; // all cid that was successfully verified;
let totalVerification = 0;

app.addAdvanceHandler(async ({metadata, payload}) => {
	console.log("Input: ", metadata, payload);

	const sender = getAddress(metadata.msg_sender);

	try {
		const jsonPayload = JSON.stringify(hexToString(payload));

		const cid = CID.parse(jsonPayload);

		await app.createNotice({
			payload: stringToHex(`CID is valid: ${cid}`),
		});

		cidVerify.push({sender: sender, cid: cid});
		totalVerification += 1;

		return "accept";
	} catch (err: any) {
		app.createReport({
			payload: stringToHex(`Invalid CID: ${err?.message}`),
		});

		return "reject";
	}
});

app.addInspectHandler(async ({ payload }) => {
    console.log("Inspect Handler: ", {payload})

    const route = hexToString(payload)

    let response;
    switch (route) {
        case "cidVerify":
            response = JSON.stringify({cidVerify})
            break;
        case "totalVerification":
            response = JSON.stringify({totalVerification})
            break;
        default:
            response = "Invalid route: "
	}
	
	app.createReport({ payload: stringToHex(response) })
});

// start app
app.start().catch((e) => process.exit(1));
